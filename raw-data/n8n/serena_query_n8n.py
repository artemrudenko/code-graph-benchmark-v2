import asyncio, time, json
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    url = "http://127.0.0.1:8769/mcp"
    t_connect_start = time.time()
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            t_connect = time.time() - t_connect_start
            results = {'connect_time_s': t_connect}

            t0 = time.time()
            r3 = await session.call_tool("find_referencing_symbols", {"name_path": "deepCopy", "relative_path": "utils.ts"})
            t3 = time.time() - t0
            results['Q3_find_referencing_symbols_deepCopy'] = {'time_s': t3, 'content': [c.text if hasattr(c,'text') else str(c) for c in r3.content]}

            t0 = time.time()
            r7 = await session.call_tool("find_symbol", {"name_path": "resolveDeferredNodeBinding", "include_body": False})
            t7 = time.time() - t0
            results['Q7_find_symbol_canary'] = {'time_s': t7, 'content': [c.text if hasattr(c,'text') else str(c) for c in r7.content]}

            print(json.dumps(results, indent=2))

asyncio.run(main())
