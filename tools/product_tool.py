import requests
import os

BASE_URL = os.getenv("NEXT_API_BASE")

session = requests.Session()

def search_products(query):
    try:
        url = f"{BASE_URL}/api/ai/products"
        params = {"query": query}

        res = session.get(url, params=params, timeout=10)
        print("Product search response:", res.json())  # Debugging line

        return res.json()
    except Exception as e:
        return {"error": str(e)}