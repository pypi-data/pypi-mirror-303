import asyncio
import sys

PY311 = sys.version_info[0:2] >= (3, 11)

if PY311:
    asyncio.coroutine = getattr(asyncio, "coroutine", lambda f: f)  # type: ignore[attr-defined]
