import json
import pytest
from task import process_json

def test_process_json():
    input_data = '{"a": 10, "b": 20, "c": 30}'
    expected_output = json.dumps({
        "total": 60,
        "original_data": {"a":10, "b": 20, "c": 30}
    })

    assert process_json(input_data) == expected_output