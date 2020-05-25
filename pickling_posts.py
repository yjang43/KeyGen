"""This script collects all documents under 'posts/' directory.  Then it constructs pickle object and
save that as 'data_container.pickle' file.
"""

import pickle
import os


def pickle_posts(dir_path):
    """Generates pickle file that contains posts within such form:
    [{"post": ..., "keywords": ...}, {...}, ...]

    dir_path: string of directory path of \"posts/\".
    """
    file_paths = [os.path.join(dir_path, file_path) for file_path in os.listdir(dir_path)]
    container_to_dump = []

    for p in file_paths:
        with open(p, 'r') as f:
            post = f.read()
            data = {
                'post': post,
                'keywords': {}
            }
            container_to_dump.append(data)

    with open('data_container.pickle', 'wb') as f:
        pickle.dump(container_to_dump, f)


pickle_posts('posts')
