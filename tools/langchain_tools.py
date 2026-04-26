from langchain_core.tools import Tool
from tools.product_tool import search_products
from tools.order_tool import get_user_orders
from tools.user_tool import get_user_details


# 🔥 product tool (same)
def product_tool_func(query: str):
    return str(search_products(query))


# 🔥 order tool (user_id input se lega)
def order_tool_func(user_id: str):
    if not user_id:
        return "User ID missing"
    return str(get_user_orders(user_id))


# 🔥 user tool (user_id input se lega)
def user_tool_func(user_id: str):
    if not user_id:
        return "User ID missing"
    return str(get_user_details(user_id))


product_tool = Tool(
    name="search_products",
    func=product_tool_func,
    description="Search products using query"
)

order_tool = Tool(
    name="get_user_orders",
    func=order_tool_func,
    description="Get user orders. Input should be user_id"
)

user_tool = Tool(
    name="get_user_details",
    func=user_tool_func,
    description="Get user details. Input should be user_id"
)