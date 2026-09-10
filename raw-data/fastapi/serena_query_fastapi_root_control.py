import asyncio, time, json, sys
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    url = "http://127.0.0.1:8766/mcp"
    t_connect_start = time.time()
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            t_connect = time.time() - t_connect_start

            results = {}

            t0 = time.time()
            r1 = await session.call_tool("find_symbol", {"name_path": "solve_dependencies", "relative_path": "fastapi/dependencies/utils.py", "include_body": False})
            t1 = time.time() - t0
            results['find_symbol'] = {'time_s': t1, 'content': [c.text if hasattr(c,'text') else str(c) for c in r1.content]}

            t0 = time.time()
            r2 = await session.call_tool("find_referencing_symbols", {"name_path": "solve_dependencies", "relative_path": "fastapi/dependencies/utils.py"})
            t2 = time.time() - t0
            results['find_referencing_symbols'] = {'time_s': t2, 'content': [c.text if hasattr(c,'text') else str(c) for c in r2.content]}

            results['connect_time_s'] = t_connect
            print(json.dumps(results, indent=2))

asyncio.run(main())
