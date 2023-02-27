from typing import Iterable, Callable, Dict

class Request:

    def __init__(self, query_data: Iterable[str]):
        self.query_data = query_data
        self.CMD_TO_FUNCTIONS: Dict[str, Callable] = {
            'filter': self._filter_query,
            'unique': self._unique_query,
            'limit': self._limit_query,
            'map': self._map_query,
            'sort': self._sort_query
        }
        self.file_data = None
    
    def _file_data_set(self, data):
        self.file_data = data
        
    def _filter_query(self, value: str):
        self._file_data_set(list(filter(lambda x: value in x, self.file_data)))
        return self.file_data

    def _map_query(self, value: str):
        self._file_data_set(list(map(lambda x: x.split(' ')[int(value)], self.file_data)))
        return self.file_data

    def _unique_query(self, *args, **kwargs):
        self._file_data_set(list(set(self.file_data)))
        return self.file_data

    def _sort_query(self, value: str):
        reverse = value == 'desc'
        self._file_data_set(sorted(self.file_data, reverse=reverse))
        return self.file_data

    def _limit_query(self, value: str):
        self._file_data_set(list(self.file_data)[:int(value)])
        return self.file_data

    def _read_file(self):
        with open(self.query_data['file_name']) as file:
            for line in file:
                yield line

    def build_query(self, cmd, value):
        if self.file_data is None:
            self.file_data = self._read_file()


        func = self.CMD_TO_FUNCTIONS[cmd]
        return func(value=value)
