import json

"""
Here are the things clients can request:
- All items that have a defined name
- All items that don't have a defined name
- Temperature, humidity data, and door status
"""

def get_items_with_name():
    jsonObject = {
        "labeledItems": [
            {
                "name": "item1",
                "expiryDate": "2024-02-31"
            },
            {
                "name": "item2",
                "expiryDate": "2024-02-20"
            },
            {
                "name": "item3",
                "expiryDate": "2024-03-01"
            }
        ]
    }
    return jsonObject

def get_items_without_name():
    jsonObject = {
        "unlabeledItems": [
            {
                "expiryDate": "2024-02-31",
                "barcode": "1234567890"
            },
            {
                "expiryDate": "2024-02-20",
                "barcode": "1234567891"
            },
            {
                "expiryDate": "2024-03-01",
                "barcode": "1234567892"
            }
        ]
    }
    return jsonObject

def get_environment_data():
    jsonObject = {
        "temperature": 25,
        "humidity": 30,
        "doorClosed": True
    }
    return jsonObject

def handle_client_side_functionality(body):
    return_data = None
    if body["type"] == "GetItemsWithName":
        return_data = get_items_with_name()
    elif body["type"] == "GetItemsWithoutName":
        return_data = get_items_without_name()
    elif body["type"] == "GetEnvironmentData":
        return_data = get_environment_data()
    return return_data, 200

def handle_add_user(body):
    return None, 200

def handle_update_user(body):
    return None, 200

def generate_response(body, status):
    response = {
        'statusCode': status,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response

def lambda_handler(event, context):
    path = event["path"]
    body = json.loads(event["body"])
    path = path.split("/")
    status, data = None, None
    if path[-1] == "client_side_functionality":
        data, status = handle_client_side_functionality(body)
    elif path[-1] == "add_user":
        data, status = handle_add_user(body)
    elif path[-1] == "update_user":
        data, status = handle_update_user(body)
    else:
        data, status = "Invalid path", 404 

    response = generate_response(data, status)

    return response