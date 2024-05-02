#!/usr/bin/env python3
'''
    Simple pagination hypermedia
'''
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
        The function should return a tuple of size two containing a
        start index and an end index corresponding to the
        range of indexes to return in a list for those
        particular pagination parameters.
    '''
    start_index = (page - 1) * page_size
    end_index = (start_index + page_size)

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            Get items by pagination
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)

        # Retrieve the rows from the csv file
        data = self.dataset()

        # Copy rows from start to ending index for pagination effect
        data = data[start_index:end_index]

        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            Hyper media return
        '''

        # Assert that both page and page_size are integers greater than 0
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        hyper_dict = {}

        # Round up pages like 2.3; You need another page to present remainer
        hyper_dict['total_pages'] = math.ceil(len(self.dataset()) / page_size)

        hyper_dict['data'] = self.get_page(page, page_size)
        hyper_dict['page_size'] = len(hyper_dict['data'])
        hyper_dict['page'] = page

        # Next page
        if hyper_dict['page'] >= hyper_dict['total_pages']:
            next_page = None
        else:
            next_page = hyper_dict['page'] + 1
        hyper_dict['next_page'] = next_page

        # Previous page
        if hyper_dict['page'] == 1:
            prev_page = None
        else:
            prev_page = hyper_dict['page'] - 1
        hyper_dict['prev_page'] = prev_page

        return hyper_dict
