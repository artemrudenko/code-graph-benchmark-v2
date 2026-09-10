import asyncio, time, json, sys
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    url = "http://127.0.0.1:8765/mcp"
    t_connect_start = time.time()
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            t_connect = time.time() - t_connect_start
            results = {}
            results['connect_time_s'] = t_connect

            # Q3: blast radius / find-all-usages of jsonable_encoder
            t0 = time.time()
            r3 = await session.call_tool("find_referencing_symbols", {"name_path": "jsonable_encoder", "relative_path": "encoders.py"})
            t3 = time.time() - t0
            results['Q3_find_referencing_symbols_jsonable_encoder'] = {
                'time_s': t3,
                'content': [c.text if hasattr(c, 'text') else str(c) for c in r3.content]
            }

            # Q6: test discovery - search for jsonable_encoder usage in tests dir via pattern search
            t0 = time.time()
            try:
                r6 = await session.call_tool("search_for_pattern", {
                    "substring_pattern": "jsonable_encoder",
                    "relative_path": "../../tests" if False else "tests",
                })
                t6 = time.time() - t0
                results['Q6_search_for_pattern_tests'] = {
                    'time_s': t6,
                    'content': [c.text if hasattr(c, 'text') else str(c) for c in r6.content]
                }
            except Exception as e:
                results['Q6_search_for_pattern_tests'] = {'error': str(e), 'time_s': time.time() - t0}

            # Q7: hallucination canary
            t0 = time.time()
            r7 = await session.call_tool("find_symbol", {"name_path": "resolve_response_model_overrides", "include_body": False})
            t7 = time.time() - t0
            results['Q7_find_symbol_canary'] = {
                'time_s': t7,
                'content': [c.text if hasattr(c, 'text') else str(c) for c in r7.content]
            }

            print(json.dumps(results, indent=2))

asyncio.run(main())
