"""The script includes functions that is responsible for rendering query."""

import math

import numpy as np


def align_posts(keyword, data_container):
    """Renders(writing result into \"render.txt\" for now) most related posts into GUI.

    keyword: keyword to query with which posts will be measured its relevance.
    data_container: container that holds data about posts.
                    It is in the shape of [{"posts": ..., "keywords": ...}, {...}, ...]
    """

    render_text = ""

    compare_container = [data for data in data_container if data['keywords'][keyword] != 0]
    render_text += f"YOU HAVE SEARCHED \"{keyword}\"\n"
    render_text += f"THERE ARE {len(compare_container)} POSTS\n\n"

    compare_table = [data['keywords'][keyword] for data in data_container if data['keywords'][keyword] != 0]
    compare_table = np.array(compare_table)
    priority_list = -np.argsort(compare_table)

    for priority in priority_list:
        data = compare_container[priority]
        render_text += data['post'] + "\n\n"

    with open('render.txt', 'w') as f:

        f.write(render_text)


def normalize_keywords(keywords):
    """Normalizes keyword vector

    keywords: keyword vector to normalize.
    """
    total_frequency = 0
    for keyword in keywords:
        total_frequency += keywords[keyword]**2

    normalized_keywords = {}
    for keyword in keywords:
        normalized_keywords[keyword] = math.sqrt(keywords[keyword]**2 / total_frequency)

    return normalized_keywords
