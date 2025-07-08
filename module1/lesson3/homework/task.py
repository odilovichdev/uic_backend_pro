# from threading import Thread
# import multiprocessing 
# import time
# import random 
# from queue import Queue

# main_queue = Queue()
# cpu_queue = Queue()
# i_o_queue = Queue()


# def task_func(delay):
#     time.sleep(delay)


# def create_task(queue: Queue):

#     task_type = ["cpu", "i/o"]
#     id_ = 1

#     while True:
#         task = {
#             "task_id": id_,
#             "task_type": task_type[random.randint(0,1)],
#             "task_function": (task_func, random.randint(1,3))
#         }
#         queue.put(task)
#         time.sleep(5)
#         print(f"Create {id_} task.")
#         id_ += 1
        

# def filter_task(main_queue: Queue, cpu_queue: Queue, i_o_queue: Queue):
#     while True:
#         task = main_queue.get()
#         print(task["task_type"])
#         if task["task_type"] == "cpu":
#             cpu_queue.put(task)
#         else:
#             i_o_queue.put(task)
#         print("Filterd task.")


# def i_o_task(i_o_queue: Queue):
#     while True:
#         task = i_o_queue.get()
#         func, arg = task["task_function"]
#         func(arg)
#         print("Complited i/o task.")


# def cpu_task(cpu_queue: Queue):
#     while True:
#         task = cpu_queue.get()
#         func, arg = task["task_function"]
#         func(arg)
#         print("Complited cpu task.")



# if __name__ == "__main__":
#     thread1 = Thread(target=create_task, args=(main_queue,))
#     thread2 = Thread(target=filter_task, args=(main_queue, cpu_queue, i_o_queue))
#     thread3 = Thread(target=i_o_task, args=(i_o_queue, ))
#     proccess = multiprocessing.Process(target=cpu_task, args=(cpu_queue,))


#     thread1.start()
#     thread2.start()
#     thread3.start()
#     proccess.start()


#     thread1.join()
#     thread2.join()
#     thread3.join()
#     proccess.join()



