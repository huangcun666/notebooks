import asyncio,time
import aiohttp,requests
URL="https://morvanzhou.github.io/"

async def job(session):
        r=await session.get(URL)
        return str(r.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks=[loop.create_task(job(session)),loop.create_task(job(session)),loop.create_task(job(session)),loop.create_task(job(session)),loop.create_task(job(session)),loop.create_task(job(session))]
        finished,unfinished=await asyncio.wait(tasks)
        all_results=[r.result() for r in finished]
        print(all_results)
t1=time.time()
loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Normal total time",time.time()-t1)