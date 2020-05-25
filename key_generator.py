"""The script acts as a driver that generates keyword from what user has inputted throughout time."""

import queue

from thread_control import MainThread, BackgroundThread

# start threads
_input_queue = queue.Queue()
main_thread = MainThread(_input_queue)
bg_thread = BackgroundThread(_input_queue)
main_thread.start()
bg_thread.start()


main_thread.join()
# save logs of each threads
with open('log.txt', 'w') as f:
    f.write(
        main_thread.main_thread_log
        + "\n\n\n"
        + bg_thread.background_thread_log
    )
