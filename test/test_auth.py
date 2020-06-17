import mopinion.client as APIClient
import unittest
import json

class AuthTest(unittest.TestCase):

    def test_signature_token(self):
        with open("creds.json") as file:
            creds = json.load(file)
            public_key, private_key = creds["public-key"], creds["private-key"]

        client = APIClient.Client(public_key, private_key)
        token = client.get_signature_token(public_key, private_key)
        print(token)

if __name__ == '__main__':
    unittest.main()
