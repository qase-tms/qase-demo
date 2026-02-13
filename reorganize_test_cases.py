import json
import re

# Suite Hierarchy Breakdown provided in the problem description
suites_data = {
    "top_level": {
        "01 Authentication": 2,
        "02 Search & Browse": 1,
        "03 Cart & Promotions": 3,
        "04 Checkout": 6,
        "05 Orders": 4,
        "06 Returns & Refunds": 7,
        "07 Admin": 5,
    },
    "child_suites": {
        "Registration": {"id": 9, "parent_id": 2},
        "Login & Sessions": {"id": 11, "parent_id": 2},
        "Password Reset": {"id": 12, "parent_id": 2},
        "Filters & Facets": {"id": 8, "parent_id": 1},
        "Category Browse": {"id": 10, "parent_id": 1},
        "Search Results": {"id": 13, "parent_id": 1},
        "Product Detail (PDP)": {"id": 17, "parent_id": 1},
        "Promo Codes": {"id": 14, "parent_id": 3},
        "Cart Basics": {"id": 16, "parent_id": 3},
        "Cart Persistence & Merge": {"id": 18, "parent_id": 3},
        "Guest Checkout": {"id": 15, "parent_id": 6},
        "Address & Shipping": {"id": 19, "parent_id": 6},
        "Payment": {"id": 22, "parent_id": 6},
        "Confirmation": {"id": 23, "parent_id": 6},
        "Order History": {"id": 24, "parent_id": 4},
        "Cancellation": {"id": 25, "parent_id": 4},
        "Shipment Tracking": {"id": 27, "parent_id": 4},
        "Returns": {"id": 20, "parent_id": 7},
        "Refund Status": {"id": 26, "parent_id": 7},
        "Catalog Management": {"id": 21, "parent_id": 5},
        "Order Operations": {"id": 28, "parent_id": 5},
        "Roles & Permissions": {"id": 29, "parent_id": 5},
        "Promotions Management": {"id": 30, "parent_id": 5},
    },
}

suite_name_to_id = {
    "registration": 9,
    "login": 11,
    "sessions": 11,
    "password reset": 12,
    "filters": 8,
    "facets": 8,
    "category browse": 10,
    "search results": 13,
    "pdp": 17,
    "product detail": 17,
    "promo codes": 14,
    "cart basics": 16,
    "cart persistence": 18,
    "guest checkout": 15,
    "address": 19,
    "shipping": 19,
    "payment": 22,
    "confirmation": 23,
    "order history": 24,
    "cancellation": 25,
    "shipment tracking": 27,
    "returns": 20,
    "refund status": 26,
    "catalog management": 21,
    "order operations": 28,
    "roles": 29,
    "permissions": 29,
    "promotions management": 30,
}

# Add fuzzy matching for top-level suites to keywords for more flexibility
fuzzy_suite_mapping = {}
for suite_name, suite_id in suites_data["top_level"].items():
    key = suite_name.split(' ', 1)[1].lower().replace(" & ", " ").replace("-", " ")
    fuzzy_suite_mapping[key] = suite_id
for suite_name, suite_info in suites_data["child_suites"].items():
    key = suite_name.lower().replace(" & ", " ").replace("-", " ")
    fuzzy_suite_mapping[key] = suite_info["id"]

# Function to fetch test cases using the Qase API tool
def fetch_all_test_cases(project_code="QD", limit_per_call=50):
    all_cases = []
    offset = 0
    total_cases = 120  # Assuming 120 total cases from previous context

    while offset < total_cases:
        # This part will be replaced by a direct tool call in the agent's execution.
        # For the purpose of running this script standalone, we'll simulate it.
        # In a real scenario, this would involve a tool call.
        print(f"print(default_api.user_qase_list_cases(code='{project_code}', limit={limit_per_call}, offset={offset}))")
        
        # Simulate data return for testing the script's logic
        # In actual agent execution, the tool output would be captured here.
        # For now, we'll just break after one simulated call to avoid infinite loop.
        break 
        
    return all_cases

# Function to generate tool calls for updating test cases
def generate_update_tool_calls(project_code, case_id, new_suite_id):
    print(f"print(default_api.user_qase_update_case(code='{project_code}', id={case_id}, suite_id={new_suite_id}))")

# Main logic to process test cases
def main():
    # Simulate fetching all test cases - in actual agent execution, this would be
    # replaced by direct tool calls and parsing of their outputs.
    # For now, we'll use a dummy list to test the matching logic.
    # In a real run, the previous tool outputs would be used.
    
    # For demonstration, I am using a simplified structure matching the expected JSON output.
    # In a real execution, the agent would parse the full JSON output from the
    # user_qase_list_cases tool calls.
    
    # Since I cannot directly call the Qase API within this script executed by default_api.Shell,
    # I will rely on the agent to feed me the data or execute the update calls.
    # For this script to be runnable, I will simulate the all_test_cases data
    # based on the small example provided in the problem description.
    
    # The actual full data parsing would involve reading the large file outputs.
    # Given the constraint of not being able to read large files directly in the script,
    # I will present the strategy for the agent to execute.
    
    # The agent's next action should be to:
    # 1. Fetch all test cases using `user_qase_list_cases` with pagination.
    # 2. Accumulate the 'entities' from each call.
    # 3. Pass this accumulated list to a function that performs the matching and generates update calls.
    
    # For now, I will demonstrate the matching logic with a hardcoded sample.
    # This part should ideally receive `all_test_cases` from the agent after it fetches them.
    
    # This list represents a small sample of test cases,
    # mirroring the structure seen in the read_file output.
    all_test_cases_sample = [
        {
            "id": 1,
            "title": "Auth: Negative: Register new user and verify account via email (3DS required, Discount eligible)",
            "description": "Validates Web UI behavior for new user scenarios.",
            "suite_id": 2, # Currently a top-level suite
        },
        {
            "id": 2,
            "title": "Auth: Sign in then sign out clears the session (3DS required)",
            "description": "Validates Web UI behavior for returning user scenarios.",
            "suite_id": 2, # Currently a top-level suite
        },
        {
            "id": 3,
            "title": "Auth: Request password reset from login (EU address, US address)",
            "description": "Validates Backend API behavior for admin scenarios.",
            "suite_id": 2, # Currently a top-level suite
        },
        {
            "id": 4,
            "title": "Browse: Browse category, open product, return to category with state preserved (Discount eligible, US address)",
            "description": "Validates Web UI behavior for admin scenarios.",
            "suite_id": 1, # Currently a top-level suite
        },
        {
            "id": 5,
            "title": "Search: Search and sort results (Discount eligible)",
            "description": "Validates Web UI behavior for new user scenarios.",
            "suite_id": 1, # Currently a top-level suite
        },
        {
            "id": 6,
            "title": "Search: Negative: Apply multiple facets updates search results (EU address)",
            "description": "Validates Payments behavior for guest scenarios.",
            "suite_id": 1, # Currently a top-level suite
        },
        {
            "id": 7,
            "title": "PDP: Negative: Add variant to cart and confirm selected variant is retained (Discount eligible)",
            "description": "Validates Payments behavior for new user scenarios.",
            "suite_id": 3, # Currently a top-level suite
        },
        {
            "id": 8,
            "title": "Cart: Negative: Update cart quantity and remove item empties cart (EU address, Out-of-stock)",
            "description": "Validates Search behavior for returning user scenarios.",
            "suite_id": 3, # Currently a top-level suite
        },
        {
            "id": 9,
            "title": "Cart: Merge guest cart into user cart on login (Discount eligible)",
            "description": "Validates Admin behavior for admin scenarios.",
            "suite_id": 3, # Currently a top-level suite
        },
        {
            "id": 10,
            "title": "Cart: Apply promo code updates discount and totals (Out-of-stock)",
            "description": "Validates Payments behavior for new user scenarios.",
            "suite_id": 3, # Currently a top-level suite
        },
        {
            "id": 101,
            "title": "Cart: Negative: Guest cart persists after login (EU address, 3DS required)",
            "description": "Validates Admin behavior for returning user scenarios.",
            "suite_id": 12, # This one is already in a child suite
        },
        {
            "id": 102,
            "title": "Cart: Negative: Apply then remove promo code updates totals (Discount eligible)",
            "description": "Validates Search behavior for guest scenarios.",
            "suite_id": 24, # This one is already in a child suite
        }
    ]
    
    updated_count = 0
    for case in all_test_cases_sample: # Use the sample for script testing
        case_id = case["id"]
        current_suite_id = case["suite_id"]
        title = case["title"].lower()
        description = case.get("description", "").lower()

        new_suite_id = None

        # Check for child suite keywords first
        for suite_name, suite_id in suite_name_to_id.items():
            if suite_name in title or suite_name in description:
                new_suite_id = suite_id
                break
        
        # If a child suite is found, and the current suite is a top-level suite or None, update.
        if new_suite_id is not None and new_suite_id != current_suite_id:
            is_current_suite_top_level = False
            for top_suite_name, top_suite_id in suites_data["top_level"].items():
                if current_suite_id == top_suite_id:
                    is_current_suite_top_level = True
                    break
            
            if is_current_suite_top_level:
                generate_update_tool_calls("QD", case_id, new_suite_id)
                updated_count += 1
                
    print(f"Script identified {updated_count} cases for potential update.")
    print("Please execute the printed tool calls to apply the changes.")

if __name__ == "__main__":
    main()
