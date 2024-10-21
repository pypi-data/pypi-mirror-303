import json

def process_json(input_json):
    """Processes the input JSON and returns a modified JSON."""
    # Parse the input JSON
    data = json.loads(input_json)

    # Example calculation: sum all values in the input JSON
    total = sum(data.values())

    # Prepare output JSON
    output_data = {
        "total": total,
        "original_data": data
    }

    # Convert output to JSON
    output_json = json.dumps(output_data)
    return output_json