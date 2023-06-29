""" 
Created on : 29/06/23 1:08 pm
@author : ds  
"""
import asyncio
import datetime


# async def main():
#     print("Hello.....")
#     await asyncio.sleep(1)
#     print(".....World!")
# asyncio.run(main())

def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()


loop = asyncio.new_event_loop()
end_time = loop.time() + 5

try:
    loop.run_forever()
finally:
    loop.close()


