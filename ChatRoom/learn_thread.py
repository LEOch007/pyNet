import threading


def action(max):
    for i in range(max):
        # get the name of current single thread
        print(threading.current_thread().getName() + " " + str(i))


for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        t1 = threading.Thread(target=action, args=(50,))
        t1.start()
        t2 = threading.Thread(target=action, args=(52,))
        t2.start()

print("Main thread has done.")