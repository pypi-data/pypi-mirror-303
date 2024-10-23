"""Main module."""

# library modules
import asyncio
import random
import re
import sys
import traceback
import functools
from typing import Callable, List, Dict, Any, Union
from pprint import pformat
from pydantic import BaseModel

from agptools.helpers import build_uri, DATE, TO_NS, NOW
from agptools.containers import walk
from agptools.logs import logger
from agptools.progress import Progress
from agptools.crontab import Crontab

from syncmodels.crud import parse_duri
from syncmodels.storage import (
    Storage,
    WaveStorage,
    tf,
    REG_SPLIT_PATH,
    SurrealConnectionPool,
)
from syncmodels.definitions import (
    URI,
    JSON,
    UID,
    WAVE,
    ORG_KEY,
    ID_KEY,
    REG_SPLIT_ID,
    extract_wave,
    DATETIME_KEY,
    REG_PRIVATE_KEY,
)

# ---------------------------------------------------------
# local imports
# ---------------------------------------------------------
from ..definitions import MONOTONIC_KEY

# ---------------------------------------------------------
# models / mappers
# ---------------------------------------------------------
# from ..models.swarmtube import SwarmtubeApp
# from .. import mappers
# from ..models.enums import *
# from ..definitions import TAG_KEY

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

log = logger(__name__)


class Event(BaseModel):
    "TBD"
    wave: WAVE
    uid: UID
    payload: Any = None


class Broker:
    "Basic Broker capabilities"

    def __init__(self):
        self.subscriptions: Dict[UID, List[Callable]] = {}

    async def start(self):
        "any action related to start broker operations"

    async def stop(self):
        "any action related to stop broker operations"

    async def subscribe(self, uid: UID, callback: Callable):
        "TBD"
        inventory = self.subscriptions.setdefault(uid, [])
        if callback not in inventory:
            inventory.append(callback)

    async def unsubscribe(self, uid: UID, callback: Callable):
        "TBD"
        inventory = self.subscriptions.setdefault(uid, [])
        if callback in inventory:
            inventory.remove(callback)

    async def is_connected(self):
        return True


class iAgent:
    IDLE_SLEEP = 5

    def __init__(
        self,
        uid,
        broker: Broker,
        storage: Union[WaveStorage, Storage],
        meta=None,
        prefix="",
        *args,
        **kw,
    ):
        if not prefix:
            prefix = uid
        self.uid = uid
        self.broker = broker
        self.storage = storage

        self.state = ST_INIT
        self.meta = {} if meta is None else meta

        self.prefix = prefix
        _uri = parse_duri(prefix)
        if not _uri["_path"] and (
            m := re.match(r"/?(?P<prefix>.*?)/?$", prefix)
        ):
            d = m.groupdict()
            if d["prefix"]:
                self.prefix = "/{prefix}".format_map(d)

        # super().__init__(*args, **kw)

    async def main(self):
        "main loop"
        # await super().main()
        await self._start_live()
        while self.state < ST_STOPPED:
            await self._idle()
        await self._stop_live()

    async def _start_live(self):
        log.info("[%s] _start_live", self.uid)

    async def _stop_live(self):
        log.info("[%s] _stop_live", self.uid)

    async def _idle(self):
        # log.debug("[%s] alive", self.uid)
        await asyncio.sleep(self.IDLE_SLEEP)


class Tube(iAgent):
    """Represents the concept of a stream of events that
    can be located by a UID or searching metadata
    """

    uid: UID

    def __init__(
        self,
        uid: UID,
        sources: List[UID],
        broker: Broker,
        storage: Storage,
        meta=None,
        **kw,
    ):
        super().__init__(
            uid=uid, broker=broker, storage=storage, meta=meta, **kw
        )
        self.sources = sources
        assert isinstance(
            self.storage, WaveStorage
        ), "needed for subscriptions"


class App(iAgent):
    "TBD"
    TIME_TO_LIVE = sys.float_info.max

    def __init__(self, uid="app", *args, **kw):
        super().__init__(uid=uid, *args, **kw)
        self.tubes = {}
        self.tasks = {}
        self.loop = None
        self.t0 = 0

    async def _start_live(self):
        assert self.loop is None
        self.loop = asyncio.get_running_loop()
        self.t0 = self.loop.time()

        # start broker and storage
        await self.storage.start()
        await self.broker.start()

        # start tubes
        for uid, tube in self.tubes.items():
            log.info("- starting: [%s]", uid)
            self.tasks[uid] = self.loop.create_task(tube.main(), name=uid)

    async def _stop_live(self):
        # requests fibers to TERM
        for uid, tube in self.tubes.items():
            log.info("- term: [%s]", uid)
            tube.state = ST_STOPPED

        # wait and clear stopped for 5 secs
        t0 = self.loop.time()
        while self.tasks and self.loop.time() - t0 < 5:
            for uid, task in list(self.tasks.items()):
                if task.done():
                    self.tasks.pop(uid)
                    log.info("- end: [%s]", uid)
            await asyncio.sleep(0.5)

        # kill remaining
        for uid, task in self.tasks.items():
            log.info("- kill: [%s]", uid)
            task.cancel()

        # wait and clear stopped for 5 secs
        t0 = self.loop.time()
        while self.tasks and self.loop.time() - t0 < 5:
            for uid, task in list(self.tasks.items()):
                if task.done():
                    self.tasks.pop(uid)
                    log.info("- finished: [%s]", uid)
            await asyncio.sleep(0.5)

        # stop broker and storage
        await self.storage.stop()
        await self.broker.stop()

    def must_stop(self):
        return len(self.tubes) < 1

    def add(self, *tubes):
        for tube in tubes:
            self.tubes[tube.uid] = tube

    def run(self):
        asyncio.run(self.main())

    async def _idle(self):
        await super()._idle()
        if self.must_stop():
            self.state = ST_STOPPED
            log.info("[%s] want stop", self.uid)


ST_INIT = 0
ST_HISTORICAL = 1
ST_SWITCHING = 2
ST_LIVE = 3
ST_STOPPED = 4


class Clock(Tube):
    "A tube that emit a clock tick"
    counter: int

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.counter = 0

    async def _start_live(self):
        await super()._start_live()

    async def _stop_live(self):
        await super()._stop_live()

    async def _idle(self):
        await super()._idle()
        self.counter += 1
        edge = {
            # MONOTONIC_KEY: time.time(),  # TODO: let the storage set this value?
            #'uid': uid,
            "payload": self.counter,
        }
        await self.storage.put(self.uid, edge)


class SwarmTubeException(Exception):
    "base for all SwarmTube Exceptions"


class SkipWave(SwarmTubeException):
    """the item can't be processed but we
    need to advance the Wave to the next one
    """


class RetryWave(SwarmTubeException):
    """the item can't be processed but we
    need to retry later on, so the Wave
    doesn't jump to the next one
    """


class Particle(Tube):
    "TBD"
    MAX_EVENTS = 1024
    _live = Dict[UID, List[Event]] | None
    _historical = Dict[UID, List[Event]] | None

    RETRY_DELAY = 15
    LIVE_WAITING = 10

    def __init__(
        self,
        uid: UID,
        sources: List[UID],
        broker: Broker,
        storage: Storage,
        since=None,
        **kw,
    ):
        super().__init__(
            uid, sources=sources, broker=broker, storage=storage, **kw
        )
        self.since = since
        self._wave = {}
        self._live = {}
        self._historical = {}
        self._live_activity = asyncio.Queue()
        self._need_resync = False

        self._milk = set()
        self._wip_edge = {}
        self._wip_uncompleted = set()

        self.context = {}

        self.metrics = Progress()
        for uri in self.sources:
            # TODO: use faster dqueue?
            self._live[uri] = []
            self._historical[uri] = []

    async def main(self):
        "TBD"
        self._need_resync = True
        # self.metrics.start()
        while self._need_resync:
            self._need_resync = False
            await self._start_live()
            await self._start_historical()

        log.info("=" * 70)
        log.info("[%s] >> Idle", self.uid)
        log.info("=" * 70)

        context = self.context
        while self.state < ST_STOPPED:
            try:
                # live processing must be based on analyzing
                # the while buffer, not just reacting to a single event
                # (as if we're processing historical data) because
                # it's safer (race-conditions)
                event = await asyncio.wait_for(
                    self._live_activity.get(),
                    timeout=self.LIVE_WAITING,
                )
                edge = self.pop_edge(self._live, context)
                if edge:
                    await self.dispatch(edge)
                    # self._wave[_uid] = _wave
            except asyncio.TimeoutError:
                # we only can sent datetime event when live connection
                #  is active, in order not to move forward the crontab
                # cursors and have problems when connection comes back again
                if await self.broker.is_connected():
                    context[DATETIME_KEY] = NOW()
                    self._live_activity.put_nowait(True)
                    # self._milk.clear()
                pass  #  No live data has been received
            except Exception as why:
                log.error(why)
                log.error(
                    "".join(traceback.format_exception(*sys.exc_info()))
                )

            # self._live_activity.clear()

            self.metrics.update(n=0)

        await self._stop_live()

    async def _start_live(self):
        "TBD"
        log.info("[%s] ++ Requesting LIVE STREAMING", self.uid)

        for uid in self.sources:
            await self.broker.subscribe(uid, self.live)

    async def _stop_live(self):
        "TBD"
        for uid in self.sources:
            await self.broker.unsubscribe(uid, self.live)

    def _new_wip(self):
        self._wip_edge = {_: [] for _ in self.sources}
        self._wip_uncompleted = set(self.sources)

    async def _start_historical(self):
        "TBD"
        self.state = ST_HISTORICAL
        self._wave = await self.storage.last_waves(
            self.prefix, self.sources, self.uid
        )
        if self.since is not None:
            wave__ = TO_NS(self.since.timestamp())
            for key in list(self._wave):
                self._wave[key] = wave__

        assert isinstance(self._wave, Dict), "missing await?"

        # self._wave = {uid: _wave for uid in self.sources}

        log.info("-" * 80)
        log.info("[%s] -- Switching to HISTORICAL", self.uid)
        log.info("-" * 80)

        # init feeding variables
        buffer = self._historical
        self._milk.update(self.sources)

        # reset WIP edge variables
        self._new_wip()

        context = self.context

        while self.state < ST_LIVE:
            # for each input source, feed the historical with ALL
            # available data as we can't switch to LIVE streaming
            # until all historical data has been moved to 'live'
            # buffers when WIP edge can't be completed because
            # some sources are missing.

            # the number of data included from storage
            n = 0

            for uid in self._milk:
                stream = await self.storage.storage.since(
                    uid, self._wave[uid], max_results=self.MAX_EVENTS
                )
                if stream:  # is ordeder by MONOTONIC_KEY
                    buffer[uid].extend(stream)
                    n += len(stream)
                    self._wave[uid] = extract_wave(stream[-1])
            self._milk.clear()

            if n == 0:  # no more historical data
                # move live data to historical and try to continue until
                # we get a state with no more historical data and no more live data
                self.state = ST_SWITCHING
                # time.sleep(0.9)
                assert id(buffer) != id(self._live)
                for uid, _buff in self._live.items():
                    _hist = self._historical[uid]
                    while True:
                        try:
                            candidate = _buff.pop(0)
                            if candidate[MONOTONIC_KEY] > self._wave[uid]:
                                _hist.append(candidate)
                                n += 1
                            else:
                                # this live event has been captured by historical polling
                                # so is already processed
                                # print(f"*** already processed: --> {candidate}")
                                pass
                        except IndexError:
                            break
                if n == 0:
                    log.info("*" * 80)
                    log.info(
                        "[%s] ** Switching to LIVE STREAMING **", self.uid
                    )
                    log.info("*" * 80)
                    self.metrics.update(n=0, force=True)
                    self.state = ST_LIVE

            # try to process buffer
            while self.state < ST_LIVE:
                # TODO: HERE: if milked, cut_wave really necesary? <-------------
                edge = self.pop_edge(buffer, context)
                if edge:
                    await self.dispatch(edge)
                elif self.state == ST_SWITCHING:
                    break
                elif self._milk:
                    break  # continue loading more historical
                else:
                    # TODO: WHEN happens this situation?
                    foo = 1

            # check if we have an overflow while processing historical data
            if self._need_resync:
                log.info(
                    "[%s] *** ---> Request Stopping Streaming due OVERFLOW",
                    self.uid,
                )
                await self._stop_live()

    def live(self, _uri: UID, event: Dict):
        "TBD"
        uri = _uri["uri"]
        # TODO: REVIEW it looks like is handled at the end as well ...
        if len(self._live[uri]) >= self.MAX_EVENTS:
            self._need_resync = True
            return

        # wave_uri = parse_duri(event['id'])
        if MONOTONIC_KEY not in event:
            m = REG_SPLIT_PATH.match(event["id"])
            if m:
                event[MONOTONIC_KEY] = m.groupdict()["id"]

        self._live[uri].append(event)
        # self._live_activity.put_nowait(event)
        self._live_activity.put_nowait(False)

        if self.state == ST_LIVE:
            pass
        elif len(self._live[uri]) >= self.MAX_EVENTS:
            # request stop streaming and a new re-sync process
            # TODO: REVIEW it looks like is handled at the beginning as well ...
            self._need_resync = True

    def pop_edge(self, buffer, context):
        """Analyze buffer and return an edge if all data
        is available for processing the next step"""
        # TODO: implement a policy delegation criteria to know when edge is ready to be processed

        self._pop_policy(buffer, context)
        # check if we must send the WIP edge
        if self._wip_uncompleted:
            pass
        else:
            # WIP edge is completed, so return it back and
            # reset WIP place holders for the next edge
            edge = self._wip_edge  # get a reference
            self._new_wip()  # that will be lost here

            # avoid sending empty edges
            if all(edge.values()):
                if MONOTONIC_KEY not in edge:
                    # we need to provide a MONOTONIC_KEY to the edge
                    # try to get the minimal wave value from returned
                    # egde
                    waves = set()
                    for key, value in walk(edge):
                        if key and key[-1] in (MONOTONIC_KEY,):
                            waves.add(value)
                    if waves:
                        edge[MONOTONIC_KEY] = max(waves)
                    else:
                        # error
                        log.error(
                            "can't find any %s in the edge!", MONOTONIC_KEY
                        )
                        log.error("%s", edge)
                        foo = 1

                return edge

    def _pop_policy(self, buffer, context) -> Dict:
        """
        Extract the current `edge` if is ready for processing
        and move forward the stream for the next step
        dropping all values that are going to be used


        Default policy is to do the minimal step for computation.
        - get the minimal wave
        - drop the input related with the minimal wave
        - return a custom `edge` for computation
        """
        for uid, stream in buffer.items():
            if stream:
                data = stream.pop(0)
                self._wip_edge[uid].append(data)
                self._wip_uncompleted.remove(uid)
                if not self._wip_uncompleted:
                    ts = extract_wave(data) or data.get(MONOTONIC_KEY)
                    self._wip_edge[MONOTONIC_KEY] = TO_NS(ts)
                    break  # generate a edge
            else:
                # source stream is empty, we need to wait for completion
                self._milk.add(uid)

    def _cut_edge(self, buffer, cut_wave):
        # TODO: delete, not used
        edge = {}
        milked = []

        for uid, stream in buffer.items():
            item = stream[0]
            item_wave = extract_wave(item)
            if item_wave <= cut_wave:
                # extract from buffer
                stream.pop(0)
                milked.append(uid)
            edge[uid] = item

        return milked, edge

    async def dispatch(self, edge):
        "TBD"
        # build the data to be processed
        # split metadata (".*__" fields by now) and each
        # input stream
        # TODO: review the criteria for keywords filtering
        ikeys = set([k for k in edge if k.endswith("__")])
        ekeys = ikeys.symmetric_difference(edge)
        assert ekeys, "no payload in the edge?"

        # set found metadata
        data = {k: edge[k] for k in ikeys}
        while self.state < ST_STOPPED:
            log.info("[%s] -> dispatch", self.uid)
            log.info("%s", pformat(edge))
            try:
                # do the computation
                payload = await self._compute(edge, ekeys)
                if payload is None:
                    log.info("[%s] <- dispatch: SKIP due NO DATA", self.uid)
                else:
                    # check key consistency
                    # TODO: REVIEW: Wath's is this intended for?
                    # TODO: >>>
                    # payload_keys = set([tf(_) for _ in payload])
                    # if payload_keys.difference(payload):
                    #     raise RuntimeError(
                    #         f"Particle returns an object with not compatible key names: {payload}"
                    #     )
                    # TODO: <<<

                    # update
                    data.update(payload)
                    # store results
                    # and shift sync / waves info
                    await self.storage.put(self.uid, data)
                    N = sum([len(_) for _ in self._live.values()])
                    self.metrics.update(buffer=N)
                    log.info("[%s] <- dispatch:", self.uid)
                    log.info("%s", pformat(data))

                wave = data.get(MONOTONIC_KEY)  # Must exist!
                if wave:
                    await self.storage.update_sync_wave(
                        self.prefix,
                        self.sources,
                        self.uid,
                        wave,
                    )
                else:
                    log.error("data %s has no %s key", data, MONOTONIC_KEY)
                break  #  let continue with next wave
            except SkipWave as why:
                # some error is produced, but we want to jump to the next wave
                wave = data.get(MONOTONIC_KEY)  # Must exist!
                if wave:
                    log.info("Skip wave [%s], reason: %s", wave, why)

                    await self.storage.update_sync_wave(
                        self.prefix,
                        self.sources,
                        self.uid,
                        wave,
                    )
                else:
                    log.error("data %s has no %s key!", data, MONOTONIC_KEY)
                break  #  let continue with next wave
            except RetryWave as why:
                delay = self.RETRY_DELAY
                for msg in why.args:
                    log.info("Retry wave, reason: %s", msg)
                    if isinstance(msg, dict):
                        delay = msg.get("delay", self.RETRY_DELAY)
                log.warning(
                    "%s._compute() has failed but is needed a retry (%s secs)",
                    str(self),
                    delay,
                )
                await asyncio.sleep(delay)
            except Exception as why:
                log.error(why)
                log.error(
                    "".join(traceback.format_exception(*sys.exc_info()))
                )
                delay = self.RETRY_DELAY * 10
                log.warning(
                    "%s._compute() has failed for an UNEXPECTED reason. "
                    "Wave edge can't be moved forward, retry in (%s secs)",
                    str(self),
                    delay,
                )
                await asyncio.sleep(delay)

    async def _compute(self, edge, ekeys):
        """
        Return None if we don't want to store info
        """
        raise NotImplementedError()


class XParticle(Particle):
    """Particle that compute rolling averages

    You may use in combination with other TimedParticle instances


    """

    EXCLUDE = f'id$|{REG_PRIVATE_KEY}'
    IDS_KEYS = set([ID_KEY, ORG_KEY])

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        super().__init__(uid, sources, broker, storage, since=None, **kw)
        specs = specs or {
            "__default__": 5,  # None means Default
        }
        self.specs = specs
        self.last = {}
        self._cached_M = {}

        self._duri = parse_duri(uid)

    def _find_M(self, key):
        for pattern, M in self.specs.items():
            if pattern:
                if re.match(pattern, key):
                    self._cached_M[key] = M
                    break
        else:
            # get default value (key = "")
            self._cached_M[key] = M = self.specs.get("__default__")

        return M

    def _calc(self, key, old_value, new_value):
        raise NotImplementedError()

    async def _compute(self, edge, ekeys):
        """
        Return None if we don't want to store info
        """
        # TODO: use different periods for each found key
        old = {}
        used = set()  # just double check, remove later on
        for uid, stream in edge.items():
            if re.match(self.EXCLUDE, uid):
                continue
            for data in stream:
                keys = [_ for _ in data if not re.match(self.EXCLUDE, _)]
                _oid = parse_duri(data[ORG_KEY])
                oid = _oid[ID_KEY]
                if oid not in self.last:
                    self.last[oid] = {key: data[key] for key in keys}

                old = self.last[oid]
                old_keys = set(old)
                keys = old_keys.intersection(data)
                for key in keys:
                    old_value = old[key]  # always exists
                    new_value = data[key]  # always exists
                    # TODO: cache int/float values?
                    if isinstance(new_value, (int, float)):
                        # M = self._cached_M.get(key) or self._find_M(key)
                        # value = old_value + (new_value - old_value) / M
                        value = self._calc(key, old_value, new_value)
                        old[key] = value
                        used.add(oid)

                # propagate other values or new ones that appears later on
                missing_keys = keys.symmetric_difference(data)

                regular_keys = self.IDS_KEYS.symmetric_difference(
                    missing_keys
                )
                for key in regular_keys:
                    old[key] = data[key]
                # ids
                for key in self.IDS_KEYS.intersection(data):
                    _duri = parse_duri(data[key])
                    self._duri[ID_KEY] = _duri[ID_KEY]
                    uri = build_uri(**self._duri)
                    old[key] = uri

                foo = 1

        # replace in result
        assert (
            len(used) == 1
        ), "can't mix more than one (:small) id in the same wave/edge"
        return old


class XMAParticle(XParticle):
    def _calc(self, key, old_value, new_value):
        M = self._cached_M.get(key) or self._find_M(key)
        value = old_value + (new_value - old_value) / M
        return value


class MAXParticle(XParticle):
    """Particle that compute the max of some values

    You may use in combination with other TimedParticle instances

    # TODO: Create additional KPI for Stochastic, BB and MACD?
    """

    EXCLUDE = f'id$|{REG_PRIVATE_KEY}'
    IDS_KEYS = set([ID_KEY, ORG_KEY])

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        super().__init__(uid, sources, broker, storage, since=None, **kw)
        specs = specs or {
            None: 5,  # None means Default
        }
        self.specs = specs
        self.stats = {}

    def _calc(self, key, old_value, new_value):
        M = self._cached_M.get(key) or self._find_M(key)
        value = old_value + (new_value - old_value) / M
        return value


class TimedParticle(Particle):
    """Particle that compute data when at certains moments, similar to crontab

    2024-09-24 11:56:05.231292

    - take 1st date
    - if base mark doesn't exits, set to this value
    - as a base mark
    - iterate over *contab* alike expansion
    - date.replace() and check if

    """

    TIME_REGEXP = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}).*?(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})"

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        super().__init__(uid, sources, broker, storage, since=None, **kw)
        specs = specs or {
            'second': 0,
        }
        self.cron = {_: Crontab(**specs) for _ in sources}

    def _pop_policy(self, buffer, context):
        # we need to make the smaller step possible
        # as happends in live streaming
        for uid in list(self._wip_uncompleted):
            # we need to use a datetime from data, not wave
            # as the TimedParticle are based on data
            stream = buffer[uid]

            def check(dt):
                if dt:
                    dt = DATE(dt)
                    if ts := self.cron[uid].check(dt):
                        # this uid has reach the timed boundary
                        # so we can pause *milking* this source
                        # until the other ones reach the same boundary
                        # as well
                        self._wip_uncompleted.remove(uid)
                        self._wip_edge[MONOTONIC_KEY] = TO_NS(ts)
                        return ts

            while stream:
                data = stream[0]
                dt = data.get(DATETIME_KEY) or extract_wave(data)
                if check(dt):
                    break
                else:
                    # add to thw WIP edge and remove from buffers
                    self._wip_edge[uid].append(stream.pop(0))
            else:
                dt = context.get(DATETIME_KEY)
                if check(dt):
                    pass
                else:
                    # source stream is empty, we need to wait for completion
                    self._milk.add(uid)

    async def _compute(self, edge, ekeys):
        """
        Return None if we don't want to store info
        """
        foo = 1


class EODParticle(TimedParticle):
    """Particle that compute data at the end of the day"""

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        specs = specs or {
            'second': 0,
            'minute': 0,
            'hour': 0,
        }
        super().__init__(
            uid, sources, broker, storage, since=None, specs=specs, **kw
        )


class HourParticle(TimedParticle):
    """Particle that extract data from stream to compute result every 1 hour"""

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        specs = specs or {
            'second': 0,
            'minute': 0,
        }
        super().__init__(
            uid, sources, broker, storage, since=None, specs=specs, **kw
        )


class MinuteParticle(TimedParticle):
    """Particle that extract data from stream to compute result every 1min"""

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        specs = specs or {
            'second': 0,
        }
        super().__init__(
            uid, sources, broker, storage, since=None, specs=specs, **kw
        )


class Minute5Particle(TimedParticle):
    """Particle that extract data from stream to compute result every 5min"""

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        specs = specs or {
            'second': 0,
            'minute': '|'.join([str(_) for _ in range(0, 60, 5)]),
        }
        super().__init__(
            uid, sources, broker, storage, since=None, specs=specs, **kw
        )


class Minute15Particle(TimedParticle):
    """Particle that extract data from stream to compute result every 15min"""

    def __init__(
        self, uid, sources, broker, storage, since=None, specs=None, **kw
    ):
        specs = specs or {
            'second': 0,
            'minute': '|'.join([str(_) for _ in range(0, 60, 15)]),
        }
        super().__init__(
            uid, sources, broker, storage, since=None, specs=specs, **kw
        )


# ---------------------------------------------------------
# Surreal Implementation
# ---------------------------------------------------------
from surrealist import Surreal


class Subscription(BaseModel):
    "live queries callbacks to be fired"
    lq_uid: UID
    callbacks: List[Callable]


class SurrealBroker(Broker):
    "pub / sub broker based on surreal"

    def __init__(self, url):
        super().__init__()
        self.url = url
        # TODO: missing surreal credentials
        self.connection_pool = SurrealConnectionPool(url)
        self._live_queries = {}
        log.info("broker will use [%s]", self.url)

    async def subscribe(self, uri: URI, callback: Callable):
        "TBD"
        await super().subscribe(uri, callback)

        _uri = parse_duri(uri)
        _sub_uri = dict(_uri)
        _sub_uri["path"] = f"/{_sub_uri['_path']}"
        # sub_uri = build_uri(**_sub_uri)

        table = tf(_sub_uri["_path"])
        if not (lq := self._live_queries.get(table)):
            # TODO: table or uri (fquid)?
            handler = functools.partial(self.dispatch, table)

            key = (_uri["fscheme"], _uri["host"])
            pool = self.connection_pool
            connection = pool.connections.get(key) or await pool._connect(
                *key
            )
            assert connection, "surreal connection has failed"

            # TODO: I think this is unnecessary
            info = connection.session_info().result
            namespace, database = _uri["fscheme"], _uri["host"]
            if info["ns"] != namespace or info["db"] != database:
                connection.use(namespace, database)

            res = connection.live(table, callback=handler)
            lq_uid = res.result

            lq = self._live_queries[table] = Subscription(
                lq_uid=lq_uid, callbacks=[]
            )

        lq.callbacks.append((callback, _uri))

    async def unsubscribe(self, uri: URI, callback: Callable):
        "TBD"
        await super().unsubscribe(uri, callback)

        _uri = parse_duri(uri)
        _sub_uri = dict(_uri)
        _sub_uri["path"] = f"/{_sub_uri['_path']}"
        # sub_uri = build_uri(**_sub_uri)

        table = tf(_sub_uri["_path"])
        if lq := self._live_queries.get(table):
            lq.callbacks.remove((callback, _uri))
            if not lq.callbacks:

                key = (_uri["fscheme"], _uri["host"])
                pool = self.connection_pool
                connection = pool.connections.get(
                    key
                ) or await pool._connect(*key)
                assert connection, "surreal connection has failed"

                # TODO: I think this is unnecessary
                info = connection.session_info().result
                namespace, database = _uri["fscheme"], _uri["host"]
                if info["ns"] != namespace or info["db"] != database:
                    connection.use(namespace, database)

                connection.kill(lq.lq_uid)
                self._live_queries.pop(table)
        else:
            pass

    def dispatch(self, uid: str, res):
        "process an event from broker"
        result = res["result"]
        assert result["action"] in (
            "CREATE",
            "UPDATE",
        )
        # event = Event(uid=uid, **result['result'])
        event = result["result"]
        for callback, _uri in self._live_queries[uid].callbacks:
            if _uri.get("id") in (event.get(ORG_KEY), None):
                callback(_uri, event)

    async def is_connected(self):
        connections = [
            con.is_connected()
            for con in self.connection_pool.connections.values()
        ]
        return all(connections)


# ---------------------------------------------------------
# Example of a Particle Implementation
# ---------------------------------------------------------
class PlusOne(Particle):
    "Example of a Particle Implementation that adds 1 to the payload"

    async def _compute(self, edge, ekeys):
        s = 0
        for k in ekeys:
            s += edge[k]["payload"]

        s /= len(ekeys)
        s += random.random()
        data = {
            self.uid: s,
        }
        return data


class TempDiff(Particle):
    """Example of a Particle Implementation that computes
    the difference between the first and the last value"""

    async def _compute(self, edge, ekeys):
        X = [edge[k]["payload"] for k in ekeys]
        y = X[0] - X[-1]
        return y


# ---------------------------------------------------------
class TubeSync(Particle):
    """Do nothing special, but synchronize data"""
