## NOTE => This code use global timer
## NOTE => This code will run for one minute / 60 seconds (to avoid endless run)

from  multiprocessing import Process
from time import sleep, time


def threadRun(name, start_time):
    while True:
        print(f"{name} is running at { int(time() - start_time) }")
        sleep(5)

def main():
    # print("START")
    start_time = time()
    
    # create threads t1, t3
    t1 = Process(target=threadRun, args=("Thread 1", start_time))
    t3 = Process(target=threadRun, args=("Thread 3", start_time))

    # start thread t1, t3
    t1.start()
    t3.start()


    # after 20 seconds terminate t1 and start t2
    # wait 20 seconds
    sleep(20)

    # terminate t1
    t1.terminate()

    # create and start t2
    t2 = Process(target=threadRun, args=("Thread 2", start_time))
    t2.start()

    # again after 18 seconds, stop t3 and start t1
    # wait 18 seconds
    sleep(18)

    # recreate and start t1
    t1 = Process(target=threadRun, args=("Thread 1", start_time))
    t1.start()

    # terminate t3
    t3.terminate()


    # after a total of one minute/ 60 seconds I am terminating all process
    # to avoid endless running of threads
    sleep(22)
    t1.terminate()
    t2.terminate()

    # print("END")

if __name__ == "__main__":
    main()
