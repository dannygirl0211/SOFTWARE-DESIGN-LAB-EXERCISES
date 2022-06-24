
import random, time
from threading import Thread


class sleepy_thread(Thread):

    def __init__(self, number, sleep_max):
        Thread.__init__(self, name="Thread " + str(number))
        self._sleep_interval = random.randint(1, sleep_max)

    def run(self):
        print("%s, sleep interval: %d seconds" % \
              (self.getName(), self._sleep_interval))
        time.sleep(self._sleep_interval)
        print("%s waking up" % self.getName())

def main():
    num_threads = int(input("Enter the number of threads: "))
    sleep_max = int(input("Enter the maximum sleep time in seconds: "))
    thread_list = []
    for count in range(num_threads):
        thread_list.append(sleepy_thread(count + 1, sleep_max))
    for thread in thread_list:
        thread.start()


if __name__ == "__main__":
    main()
