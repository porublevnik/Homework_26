import re
from typing import Optional, Iterable, Callable, Dict

class Request:

    def __init__(self, query_data: Dict[str, str]):
        self.query_data: Dict[str, str] = query_data
        self.CMD_TO_FUNCTIONS: Dict[str, Callable] = {
            'filter': self._filter_query,
            'unique': self._unique_query,
            'limit': self._limit_query,
            'map': self._map_query,
            'sort': self._sort_query,
            'regex': self._regex
        }
        self.file_data: Iterable[str] = self._read_file()
    
    def _file_data_set(self, data: Iterable[str]):
        self.file_data = data
        
    def _filter_query(self, value: str) -> Optional[Iterable[str]]:
        self._file_data_set(list(filter(lambda x: value in x, self.file_data)))
        return self.file_data

    def _map_query(self, value: str) -> Optional[Iterable[str]]:
        self._file_data_set(list(map(lambda x: x.split(' ')[int(value)], self.file_data)))
        return self.file_data

    def _unique_query(self, *args, **kwargs) -> Optional[Iterable[str]]:
        self._file_data_set(list(set(self.file_data)))
        return self.file_data

    def _sort_query(self, value: str) -> Optional[Iterable[str]]:
        reverse: bool = value == 'desc'
        self._file_data_set(sorted(self.file_data, reverse=reverse))
        return self.file_data

    def _limit_query(self, value: str) -> Optional[Iterable[str]]:
        self._file_data_set(list(self.file_data)[:int(value)])
        return self.file_data

    def _regex(self, value:str) -> Optional[Iterable[str]]:
        regex = re.compile(value)
        self._file_data_set(list(filter(lambda x: re.search(regex, x), self.file_data)))
        return self.file_data

    def _read_file(self) -> Iterable[str]:
        with open(self.query_data['file_name']) as file:
            for line in file:
                yield line

    def build_query(self, cmd: str, value: str) -> Callable:
        func = self.CMD_TO_FUNCTIONS[cmd]
        return func(value=value)
