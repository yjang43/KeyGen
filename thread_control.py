"""The script manages multi threads.  Input and user interface happens in main_thread while
processing and reformulating post-keyword_vector map is reformulated in bg_thread.
"""

import threading
import time
import pickle
from datetime import datetime

from posts_render import align_posts

# Set global variables 'keywords' and 'data_container'
try:
    with open('keywords.pickle', 'rb') as f:
        keywords = pickle.load(f)
except FileNotFoundError:
    with open('keywords.pickle', 'wb') as f:
        pickle.dump([], f)
        keywords = []
try:
    with open('data_container.pickle', 'rb') as f:
        data_container = pickle.load(f)
except FileNotFoundError:
    with open('data_container.pickle', 'wb') as f:
        pickle.dump([], f)
        data_container = []


class MainThread(threading.Thread):
    """Class that instantiate thread that controls input."""

    def __init__(self, q):
        """Initialize instance with input queue.

        q: input queue that is an instance of queue.Queue
        """

        super().__init__()
        self.queue = q
        self.main_thread_log = "MAIN\n"

    def run(self):
        """Override super class run() method to take input and send it to queue
        when start() is called.
        """

        while True:
            keyword = input("ENTER KEYWORD ('quit' to end): ")
            if keyword == 'quit':
                self.queue.join()
                with open('data_container.pickle', 'wb') as f:
                    pickle.dump(data_container, f)
                with open('keywords.pickle', 'wb') as f:
                    pickle.dump(keywords, f)
                print("SUCCESSFULLY EXITING THE PROGRAM")
                break

            self.main_thread_log += f'LOG {datetime.now()}: "{keyword}" has been put into the queue\n'
            self.queue.put(keyword)


class BackgroundThread(threading.Thread):
    """The class instantiates a thread that processes reformulating post and keywords map of the data."""

    def __init__(self, q):
        """Instantiates with input queue.

        q: input queue with data type queue.Queue
        """

        super().__init__(daemon=True)
        self.queue = q
        self.background_thread_log = "BACKGROUND\n"

    def run(self):
        """Overrides super class's method to dequeue a keyword and reformulate the data."""

        while True:
            keyword = self.queue.get()
            if keyword in keywords:
                self.background_thread_log += f"LOG {datetime.now()}: {keyword} FOUND\n"
                align_posts(keyword, data_container)
            else:
                self.background_thread_log += f"LOG {datetime.now()}: PROCESSING {keyword}\n"
                keywords.append(keyword)
                time.sleep(3)       # Todo: temporarily put for representational reason
                self.reformulate(keyword)
                self.background_thread_log += f"LOG {datetime.now()}: PROCESSING {keyword} FINISHED\n"

                align_posts(keyword, data_container)

            self.queue.task_done()

    # noinspection PyMethodMayBeStatic
    def reformulate(self, keyword):
        """Reformulate and update keywords of each post.

        keyword: keyword that gets added to the keywords vector."""
        for data in data_container:
            frequency = data['post'].count(keyword)
            data['keywords'][keyword] = frequency
