#!/usr/bin/env python3
"""
Module 0-simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page and page size.
    Returns a tuple of size two containing a start
    index and an end index corresponding to the range
    of indexed to return in a list for those particular
    pagination parameters.
    """
    if page <= 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index
