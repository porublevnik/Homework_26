# lesson23
По адресу /perform_query_extended в тело запроса передается словарь вида
{
    "commands": [
        {
            "cmd": "unique",
            "value": ""
        },
        {
            "cmd": "filter",
            "value": "GET"
        },
        {
            "cmd": "sort",
            "value": "desc"
        }
    ],
    "file_name": "data/apache_logs.txt"
}
количество словарей с командами не ограничено

