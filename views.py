import os
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from request_model import RequestSchema, BatchRequestSchema
from request import Request

main_bp =Blueprint('main', __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
    data = request.json
    try:
        validated_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    query = Request(validated_data)

    query.build_query(
        cmd=query.query_data['cmd1'],
        value=query.query_data['value1']
    )
    query.build_query(
        cmd=query.query_data['cmd2'],
        value=query.query_data['value2']
    )

    return jsonify(query.file_data)


@main_bp.route("/perform_query_extended", methods=['POST'])
def perform_query_extended():
    """
    В тело запроса передается словарь вида
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
    """
    data = request.json
    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    query = Request(validated_data)

    result = None
    for command in query.query_data['commands']:
        query.build_query(
            cmd=command['cmd'],
            value=command['value']
        )

    return jsonify(query.file_data)