import requests

BASE_URL="http://127.0.0.1:8000"

def signup(data):
    return requests.post(f"{BASE_URL}/auth/signup",json=data)

def login(data):
    return requests.post(f"{BASE_URL}/auth/login",data={
            "username": data["email"],
            "password": data["password"]})

def get_applications(token):
    return requests.get(f"{BASE_URL}/application/all_applications",
                        headers={"Authorization":f"Bearer {token}"})

def add_application(token,data):
    return requests.post(f"{BASE_URL}/application/new_application",
                         json=data,
                         headers={"Authorization":f"Bearer {token}"})

def get_one_application(token,app_id):
    return requests.get(f"{BASE_URL}/applications/{app_id}",
                        headers={"Authorization":f"Bearer {token}"})

def update_application_status(token,app_id,status):
    return requests.patch(f"{BASE_URL}/applications/update/{app_id}",
                          json={"status":status},
                          headers={"Authorization":f"Bearer {token}"})

def delete_application(token,app_id):
    return requests.delete(f"{BASE_URL}/applications/delete/{app_id}",
                           headers={"Authorization":f"Bearer {token}"})
