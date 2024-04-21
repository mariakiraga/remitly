import json
import unittest

def verify_json(file_path=None, json_input=None):
    """Verifies input JSON data from file or string.
    When both file path and string are given the method verifies input from file.

    Parameters
    ----------
    file_path : str, optional
        Location of JSON file which contains the data
    json_input : str, optional
        JSON data passed as string

    Returns
    -------
    bool
        False if an input JSON Resource field contains a single asterisk
        True in any other case
    """

    json_file=''
    if (file_path and json_input) or (file_path and json_input==None):
        print('Verifying input from file')
        try:
            json_file = open(file_path, 'r').read()
        except OSError:
            print('Invalid file path')
            return
    elif json_input:
        print('Verifying input from string')
        json_file = json_input

    try:
        json_object = json.loads(json_file)
        try:
            # print('closing file')
            json_file.close()
        except AttributeError:
            pass 
        try:
            value = json_object['PolicyDocument']['Statement'][0]['Resource']
        except (KeyError, AttributeError):
            print('JSON file contents of other format than expected.')
            return
        
        if value == '*':
            return False
    
    except json.JSONDecodeError as jde:
        print('Syntax error in JSON file:', jde)
        return
    except ValueError as ve:
        print('JSON file contains incorrect value data type.', ve)
        return
    except TypeError as te:
        print(te)
        return
    return True

class TestVerifyJson(unittest.TestCase):
    path = 'test.json'
    path2 = 'test.txt'
    string = '''
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
    string2 = '''
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
                            "Resource": "A"
                        }
                    ]
                }
            }
            '''
    def test_case_a(self):
        self.assertTrue(verify_json(json_input=self.string2))
    def test_case_b(self):
        self.assertIsNone(verify_json(json_input="{'1':2}"))
    def test_case_c(self):
        self.assertIsNone(verify_json(json_input='{"1":2}'))
    def test_case_d(self):
        self.assertIsNone(verify_json())
    def test_case_e(self):
        self.assertIsNone(verify_json(self.path2))
    def test_case_f(self):
        self.assertIsNone(verify_json(self.string, self.path))
    def test_case_g(self):
        self.assertIsNone(verify_json(self.string))
    def test_case_h(self):
        self.assertFalse(verify_json(self.path))
    def test_case_i(self):
        self.assertFalse(verify_json(self.path, self.string))
    def test_case_j(self):
        self.assertFalse(verify_json(file_path = self.path))
    def test_case_k(self):
        self.assertFalse(verify_json(json_input=self.string))

if __name__ == '__main__':
    unittest.main()