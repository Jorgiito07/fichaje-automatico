import requests
import os
import sys

# Usuario y contraseña guardados como Secret en GitHub
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

# URLs de la API
LOGIN_URL = "https://vinci.dasstime.dorlet.com/api/auth"
CLOCK_URL = "https://vinci.dasstime.dorlet.com/api/portal/addclock"

# start → inicio, stop → fin
mode = sys.argv[1]  # "start" o "stop"

session = requests.Session()

# --- LOGIN ---
login_payload = {
    "UserName": USERNAME,
    "Password": PASSWORD,
    "RememberMe": True,
    "provider": "credentials"
}

login_response = session.post(LOGIN_URL, json=login_payload)

if login_response.status_code != 200:
    print("Error en login:", login_response.text)
    exit(1)

# --- FICHAJE ---
clock_payload = {
    "TTId": None,
    "IsStart": True if mode == "start" else False,
    "Offset": -60  # ajusta automáticamente UTC+1
}

clock_response = session.post(CLOCK_URL, json=clock_payload)

print(f"Fichaje {mode} resultado:", clock_response.status_code)
print(clock_response.text)
