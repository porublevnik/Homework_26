from typing import Iterable

def filter_query(value: str, data: Iterable[str]):
    return list(filter(lambda x: value in x, data))

def map_query(value: str, data: Iterable[str]):
    return list(map(lambda x: x.split(' ')[int(value)], data))

def unique_query(data: Iterable[str], *args, **kwargs):
    return list(set(data))

def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)

def limit_query(value: str, data: Iterable[str]):
    return list(data)[:int(value)]