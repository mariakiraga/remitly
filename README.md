# Remitly excercise
This repository contains a Python script that provides a method to verify JSON input data and unit tests to verify the method's validity.

## Method Description

The `verify_json` method provided in the Python script takes JSON input data and returns `False` if `Resource` field contains a single asterisk (`*`), otherwise it returns `True`. The method can be used with JSON data provided as a string or loaded from a file.

## Files

- `verify_json.py`: Python script containing the `verify_json` method as well as unit test with edge cases.
- `test.json`: Sample JSON file for testing purposes.
- `test.txt`: Sample text file for testing purposes.

## Usage

To use the `verify_json` method, simply import it into your Python script and call it with JSON input data. Below is an example:

```python
from verify_json import verify_json

# Example usage with JSON input data provided as a string
json_input = '''
            {
                "PolicyName": "root",
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "IamListAccess",
                            "Effect": "Allow",
                            "Action": [
                                "iam:ListRoles",
                                "iam:ListUsers"
                            ],
                            "Resource": "*"
                        }
                    ]
                }
            }
            '''
print(verify_json(json_input=json_input))  # Output: False

# Example usage with JSON input data loaded from a file
print(verify_json(file_path = 'path/to/json/file.json'))
```
