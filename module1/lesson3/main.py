# import threading
# import time
# import requests
# import multiprocessing

# def calc():
#     x = 0
#     for _ in range(10_000_000):
#         x+=1


# def fetch_url(url):
#     response = requests.get(url)
#     print(f"Fetching {url} with status code {response.status_code}")
    

# start_time = time.time()

# if __name__ == "__main__":
#     threads = []

#     for _ in range(8):
#         t = threading.Thread(target=calc)   
#         t.start()
#         threads.append(t)

#     for i in threads:
#         i.join()

#     # for _ in range(8):
#     #     calc()

#     print(f"Time taken: {time.time()-start_time}")


# for _ in range(8):
#     url = "https://google.com"
#     fetch_url(url)

# threads = []

# for _ in range(4):
#     url = "https://google.com"
#     t = threading.Thread(target=fetch_url, args=(url,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()


# print("Time taken: ", time.time() - start_time)


# start_time = time.time()

# def calc():
#     x = 0
#     for _ in range(10_000_000):
#         x += 1



# if __name__ == "__main__":
#     process = []
#     for _ in range(8):
#         p = multiprocessing.Process(target=calc)
#         p.start()
#         process.append(p)


#     for p in process:
#         p.join()

#     # for _ in range(8):
#     #     calc()

#     print(f"Time taken: ", time.time()-start_time)

# start_time = time.time()


# def fetch_url(url):
#     response = requests.get(url)
#     print(f"Fetched {url} with status code {response.status_code}")


# def calc():
#     x = 0
#     for _ in range(10_000_000):
#         x += 1


# for _ in range(8):
#     fetch_url("https://google.com")


# print(f"Time taken: {time.time()-start_time}")


# for _ in range(8):
#     increment_counter()

# threads = []
# for _ in range(8):
#     t = threading.Thread(target=increment_counter)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# if __name__ == "__main__":
#     processes = []

#     for _ in range(4):
#         p = multiprocessing.Process(target=increment_counter)
#         p.start()
#         processes.append(p)


#     for p in processes:
#         p.join()

#     print("Counter value after incrementing in main thread, ", shared_data['counter'])


# import threading
# import multiprocessing

# shared_data = {"counter": 0}


# def increment_counter(data, lock):
#     for _ in range(100):
#         with lock:
#             data["counter"]+=1
#     print(data['counter'])


# if __name__ == "__main__":
#     process = []

#     with multiprocessing.Manager() as manager:
#         shared_data = manager.dict()
#         lock = manager.Lock()
#         shared_data['counter'] = 0

#         for _ in range(8):
#             p = multiprocessing.Process(target=increment_counter, args=(shared_data, lock))
#             p.start()
#             process.append(p)
        
#         for p in process:
#             p.join()

#         print(shared_data['counter'])


# import threading
# import queue
# import time

# task_queue = queue.Queue()


# for i in range(20):
#     task_queue.put(f"task {i}")


# def worker(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(f"Processing {item}")
#         time.sleep(2)
#         q.task_done()


# threads = []

# for _ in range(4):
#     t = threading.Thread(target=worker, args=(task_queue, ))
#     t.start()
#     threads.append(t)

# task_queue.join()

# for _ in threads:
#     task_queue.put(None)


# print(f"All tasks added to the queue.")


# import time
# import requests

# start_time = time.time()

# def fetch_url(url):
#     response = requests.get(url)
#     print(f"Fetched {url} with status code {response.status_code}")


# for _ in range(4):
#     url = f"https://google.com"
#     fetch_url(url)

# print(time.time() - start_time)

import asyncio
import aiohttp
import time


async def async_sleep(name):
    print(f"Started {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")


def synchronous_sleep(name):
    print(f"Started {name}")
    time.sleep(2)
    print(f"Finished {name}")


async def sync_to_async(name):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, synchronous_sleep, name)


async def main():
    await asyncio.gather(
        async_sleep("task 1"),
        async_sleep("task 2"),
        async_sleep("task 3"),
        sync_to_async("task 4"),
        sync_to_async("task 5"),
        sync_to_async("task 6")
    )


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Time taken: {time.time()-start_time}")

















        
