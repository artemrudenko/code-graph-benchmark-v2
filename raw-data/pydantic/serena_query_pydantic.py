import asyncio, time, json
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    url = "http://127.0.0.1:8766/mcp"
    t_connect_start = time.time()
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            t_connect = time.time() - t_connect_start
            results = {'connect_time_s': t_connect}

            t0 = time.time()
            r1 = await session.call_tool("find_symbol", {"name_path": "FieldInfo", "relative_path": "fields.py", "include_body": True})
            t1 = time.time() - t0
            results['Q1_find_symbol_FieldInfo'] = {'time_s': t1, 'content': [c.text if hasattr(c,'text') else str(c) for c in r1.content]}

            t0 = time.time()
            r3 = await session.call_tool("find_referencing_symbols", {"name_path": "GenerateSchema/generate_schema", "relative_path": "_internal/_generate_schema.py"})
            t3 = time.time() - t0
            results['Q3_find_referencing_symbols_generate_schema'] = {'time_s': t3, 'content': [c.text if hasattr(c,'text') else str(c) for c in r3.content]}

            t0 = time.time()
            r7 = await session.call_tool("find_symbol", {"name_path": "resolve_deferred_annotation_cache", "include_body": False})
            t7 = time.time() - t0
            results['Q7_find_symbol_canary'] = {'time_s': t7, 'content': [c.text if hasattr(c,'text') else str(c) for c in r7.content]}

            print(json.dumps(results, indent=2))

asyncio.run(main())
