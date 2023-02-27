# from typing import Callable, Dict
# from commands import *
#
# # CMD_TO_FUNCTIONS: Dict[str, Callable] = {
# #     'filter': filter,
# #     'unique': unique,
# #     'limit': limit,
# #     'map': map,
# #     'sort': sort
# # }
#
# CMD_TO_FUNCTIONS: Dict[str, Callable] = {
#     'filter': filter_query,
#     'unique': unique_query,
#     'limit': limit_query,
#     'map': map_query,
#     'sort': sort_query
# }
#
# def read_file(file_name: str):
#     with open(file_name) as file:
#         for line in file:
#             yield line
#
# def build_query(cmd, value, file_name, data):
#     if data is None:
#         source_data = read_file(file_name)
#     else:
#         source_data = data
#
#     func = CMD_TO_FUNCTIONS[cmd]
#     func_result = func(value=value, data=source_data)
#
#     return func_result