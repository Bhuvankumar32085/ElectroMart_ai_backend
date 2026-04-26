import requests
import os

BASE_URL = os.getenv("NEXT_API_BASE")

session = requests.Session()

def get_user_orders(user_id):
    try:
        url = f"{BASE_URL}/api/ai/orders/{user_id}"

        res = session.get(url, timeout=5)
        print("User orders response:", res.json())  # Debugging line
        return res.json()
    except Exception as e:
        return {"error": str(e)}