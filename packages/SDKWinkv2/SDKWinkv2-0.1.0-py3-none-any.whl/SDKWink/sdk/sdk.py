import hashlib
import requests

class SDK:
    def __init__(self, walletid, serviceid, reqs) -> None:
        """
        Initializes the SDK instance with wallet ID, service ID, and request count.
        Generates an API key for the instance.
        """
        self.walletid = walletid
        self.serviceid = serviceid
        self.reqs = reqs
        self.api_key = self.generate_api_key()
    
    def generate_api_key(self) -> str:
        """
        Generates a unique API key using the wallet ID and service ID.
        Returns the SHA-256 hashed key as a hexadecimal string.
        """
        key_string = f"{self.walletid}:{self.serviceid}"
        return hashlib.sha256(key_string.encode()).hexdigest()

    def validate(self) -> bool:
        """
        Validates if the instance has remaining requests.
        Decreases request count if valid.
        Returns True if validation is successful, otherwise False.
        """
        if self.reqs > 0:
            self.reqs -= 1
            return True
        return False
    
    def refill(self, num_reqs: int) -> bool:
        """
        Refills the request count for the instance with a specified number.
        Returns True after refilling.
        """
        self.reqs = num_reqs
        return True


class APIKeyManager:
    def __init__(self):
        """
        Initializes an APIKeyManager instance to manage multiple SDK instances.
        Stores instances in a dictionary with their API keys as keys.
        """
        self.base_url = "https://apiwink-backend.onrender.com/"
        self.instances = {}

    def create_key(self, walletid: str, serviceid: str, reqs: int) -> str:
        """
        Creates a new SDK instance and generates an API key.
        Stores the SDK instance in the instances dictionary.
        Returns the generated API key.
        """
        data = {
            "walletid": walletid,
            "serviceid": serviceid,
            "reqs": reqs,
            "api_key": hashlib.sha256(f"{walletid}:{serviceid}".encode()).hexdigest()
        }
        response = self.post_to_url(self.base_url+"add_key", data)
        try:
            success, message = response.get("success"), response.get("message")
        except Exception as e:
            print("could not hit api")
            return False
        print(message)
        if not success:
            return False
        return True

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
    
    def add_refills(self, api_key: str, num_requests: int) -> bool:
        """
        Adds refills to the SDK instance associated with the given API key.
        Returns True if the refills were successfully added, otherwise False.
        """

        data = {
            "api_key": api_key,
            "add_reqs": num_requests
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
