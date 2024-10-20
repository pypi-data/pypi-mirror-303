import hashlib
import requests

class APIWink:
    def __init__(self):
        """
        Initializes an APIKeyManager instance to manage multiple SDK instances.
        Stores instances in a dictionary with their API keys as keys.
        """
        self.base_url = "https://apiwink-backend.onrender.com/"
        self.instances = {}
        self.config = None
    
    def activate_config(self, config_key):
        data = {
            "config_key": config_key
        }
        response = self.post_to_url(self.base_url+"activate_config", data)
        if not response:
            return False
        self.config = response.get("ack_key")
        return True

    def create_key(self, walletid: str, serviceid: str, requests: int) -> str:
        """
        Creates a new SDK instance and generates an API key.
        Stores the SDK instance in the instances dictionary.
        Returns the generated API key.
        """
        data = {
            "walletid": walletid,
            "serviceid": serviceid,
            "reqs": requests,
            "api_key": hashlib.sha256(f"{walletid}:{serviceid}".encode()).hexdigest()
        }
        response = self.post_to_url(self.base_url+"add_key", data)
        try:
            success, message = response.get("success"), response.get("message")
        except Exception as e:
            print("could not hit api")
            return None
        print(message)
        if not success:
            return None
        return data["api_key"]

    def validate_request(self, api_key: str) -> bool:
        """
        Validates an API key by checking if the corresponding SDK instance has requests left.
        Returns True if the request is valid, otherwise False.
        """
        data = {
            "api_key": api_key
        }
        response = self.post_to_url(self.base_url+"sub_request", data)
        try:
            success, message = response.get("success"), response.get("message")
        except:
            print("could not hit api")
            return False
        print(message)
        if not success:
            return False
        return True
    
    def fetch_details(self, api_key: str) -> bool:
        """
        Validates an API key by checking if the corresponding SDK instance has requests left.
        Returns True if the request is valid, otherwise False.
        """
        data = {
            "api_key": api_key
        }
        response = self.post_to_url(self.base_url+"fetch_data", data)
        try:
            success, message = response.get("success"), response.get("message")
        except:
            print("could not hit api")
            return None
        # print(message)
        if not success:
            return None
        return message
    
    def add_refills(self, api_key: str, add_requests: int) -> bool:
        """
        Adds refills to the SDK instance associated with the given API key.
        Returns True if the refills were successfully added, otherwise False.
        """

        data = {
            "api_key": api_key,
            "add_reqs": add_requests
        }
        response = self.post_to_url(self.base_url+"update_requests", data)
        try:
            success, message = response.get("success"), response.get("message")
        except:
            print("could not hit api")
            return False
        print(message)
        if not success:
            return False
        return True
    
    def post_to_url(self, url, data):
        try:
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.post(url=url, json=data, headers=headers)
            response.raise_for_status()
            
            print("Response status code:", response.status_code)
            print("Response content:", response.text)
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            return None
