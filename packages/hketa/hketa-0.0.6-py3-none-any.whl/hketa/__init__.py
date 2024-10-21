import importlib
import sys
from typing import Coroutine, Iterable

import aiohttp

from . import t


def routes(co: t.Transport,
           *,
           session: aiohttp.ClientSession = None) -> Coroutine[None, None, dict[str, t.Route]]:
    return importlib.import_module(f'.{co}', sys.modules[__name__].__package__)\
        .__dict__\
        .get('routes')(session=session)


def stops(co: t.Transport,
          route_id: str,
          *,
          session: aiohttp.ClientSession = None) -> Coroutine[None, None, Iterable[t.Stop]]:
    return importlib.import_module(f'.{co}', sys.modules[__name__].__package__)\
        .__dict__\
        .get('stops')(route_id, session=session)


def etas(co: t.Transport,
         route_id: str,
         stop_id: str,
         language: t.Language = 'tc',
         *,
         session: aiohttp.ClientSession = None) -> Coroutine[None, None, t.Etas]:
    return importlib.import_module(f'.{co}', sys.modules[__name__].__package__)\
        .__dict__\
        .get('etas')(route_id, stop_id, language, session=session)
