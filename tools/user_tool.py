import requests
import os

BASE_URL = os.getenv("NEXT_API_BASE")

session = requests.Session()

def get_user_details(user_id):
    try:
        
        url = f"{BASE_URL}/api/ai/user/{user_id}"

        res = session.get(url, timeout=5)

        data = res.json()

        print("User details response:", data)  # Debugging line
        # 🔥 IMPORTANT: clean data return karo (LLM friendly)
        return {
            "name": data.get("name"),
            "email": data.get("email"),
            "ordersCount": data.get("ordersCount"),
            "cartItems": data.get('cartItems'),
            "role": data.get("role")
        }

    except Exception as e:
        return {"error": str(e)}