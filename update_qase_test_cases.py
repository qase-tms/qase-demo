import os
import qase.api_client_v1
from qase.api_client_v1.api.cases_api import CasesApi
from qase.api_client_v1.models.test_case_update import TestCaseUpdate
import json
import logging

# Configure logging
logging.basicConfig(filename='qase_updates.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Script started.")

# Your Qase API Token and Project Code
QASE_API_TOKEN = os.getenv("QASE_API_TOKEN")
QASE_PROJECT_CODE = "QD"  # Replace with your actual project code

if not QASE_API_TOKEN:
    logging.error("QASE_API_TOKEN environment variable not set.")
    raise ValueError("QASE_API_TOKEN environment variable not set.")
else:
    logging.info(f"QASE_API_TOKEN loaded (first 5 chars): {QASE_API_TOKEN[:5]}...")

configuration = qase.api_client_v1.Configuration(host="https://api.qase.io/v1")
configuration.api_key["TokenAuth"] = QASE_API_TOKEN

api_client = qase.api_client_v1.ApiClient(configuration)
cases_api = CasesApi(api_client)

updates_to_perform_json = """
[
    {
        "case_id": 1,
        "new_title": "Auth: Negative: Register new user and verify account via email (3DS required, Discount eligible)",
        "suite_id": 29
    },
    {
        "case_id": 2,
        "new_title": "Auth: Sign in then sign out clears the session (3DS required)",
        "suite_id": 30
    },
    {
        "case_id": 3,
        "new_title": "Auth: Request password reset from login (EU address, US address)",
        "suite_id": 11
    },
    {
        "case_id": 4,
        "new_title": "Browse: Browse category, open product, return to category with state preserved (Discount eligible, US address)",
        "suite_id": 19
    },
    {
        "case_id": 5,
        "new_title": "Search: Search and sort results (Discount eligible)",
        "suite_id": 28
    },
    {
        "case_id": 6,
        "new_title": "Search: Negative: Apply multiple facets updates search results (EU address)",
        "suite_id": 8
    },
    {
        "case_id": 7,
        "new_title": "PDP: Negative: Add variant to cart and confirm selected variant is retained (Discount eligible)",
        "suite_id": 17
    },
    {
        "case_id": 8,
        "new_title": "Cart: Negative: Update cart quantity and remove item empties cart (EU address, Out-of-stock)",
        "suite_id": 19
    },
    {
        "case_id": 9,
        "new_title": "Cart: Merge guest cart into user cart on login (Discount eligible)",
        "suite_id": 11
    },
    {
        "case_id": 10,
        "new_title": "Cart: Apply promo code updates discount and totals (Out-of-stock)",
        "suite_id": 22
    },
    {
        "case_id": 11,
        "new_title": "Checkout: Guest checkout enters email and proceeds (EU address)",
        "suite_id": 19
    },
    {
        "case_id": 12,
        "new_title": "Checkout: Select address and shipping method during checkout (US address, 3DS required)",
        "suite_id": 21
    },
    {
        "case_id": 13,
        "new_title": "Checkout: Pay by card at checkout (Out-of-stock)",
        "suite_id": 20
    },
    {
        "case_id": 14,
        "new_title": "Checkout: Capture order number on confirmation (Discount eligible, 3DS required)",
        "suite_id": 12
    },
    {
        "case_id": 15,
        "new_title": "Orders: Open latest order and verify items and totals (Out-of-stock)",
        "suite_id": 13
    },
    {
        "case_id": 16,
        "new_title": "Orders: Request cancellation for an unshipped order (Out-of-stock)",
        "suite_id": 12
    },
    {
        "case_id": 17,
        "new_title": "Orders: Open shipment tracking details and verify tracking link (US address, Discount eligible)",
        "suite_id": 28
    },
    {
        "case_id": 18,
        "new_title": "Returns: Start a return request for an eligible order (Out-of-stock)",
        "suite_id": 25
    },
    {
        "case_id": 19,
        "new_title": "Orders: View refund-in-progress status updates (Out-of-stock, 3DS required)",
        "suite_id": 25
    },
    {
        "case_id": 20,
        "new_title": "Admin: Perform admin action and verify changes persist (3DS required, Discount eligible)",
        "suite_id": 29
    },
    {
        "case_id": 21,
        "new_title": "Admin: Sign in to admin and navigate to an admin section (Discount eligible)",
        "suite_id": 28
    },
    {
        "case_id": 22,
        "new_title": "Cart: Apply promo code updates discount and totals (3DS required)",
        "suite_id": 11
    },
    {
        "case_id": 23,
        "new_title": "Admin: Sign in to admin and navigate to an admin section (EU address, Discount eligible)",
        "suite_id": 25
    },
    {
        "case_id": 24,
        "new_title": "Auth: Start registration with new email and password (Discount eligible)",
        "suite_id": 16
    },
    {
        "case_id": 25,
        "new_title": "Auth: Sign in and land on authenticated area (3DS required)",
        "suite_id": 14
    },
    {
        "case_id": 26,
        "new_title": "Auth: Complete password reset via email and sign in with new password (US address)",
        "suite_id": 23
    },
    {
        "case_id": 27,
        "new_title": "Browse: Browse category listing (load more) and open a product (Out-of-stock, 3DS required)",
        "suite_id": 10
    },
    {
        "case_id": 28,
        "new_title": "Search: Negative: Search, sort results, and open a product (Discount eligible, Out-of-stock)",
        "suite_id": 13
    },
    {
        "case_id": 29,
        "new_title": "Search: Apply a filter facet updates search results (US address, Out-of-stock)",
        "suite_id": 10
    },
    {
        "case_id": 30,
        "new_title": "PDP: Select variant and add product to cart (Discount eligible)",
        "suite_id": 13
    },
    {
        "case_id": 31,
        "new_title": "Cart: Update cart quantity and remove item empties cart (Out-of-stock)",
        "suite_id": 15
    },
    {
        "case_id": 32,
        "new_title": "Cart: Negative: Merge guest cart into user cart on login (Discount eligible, 3DS required)",
        "suite_id": 10
    },
    {
        "case_id": 33,
        "new_title": "Cart: Negative: Apply then remove promo code updates totals (Out-of-stock, EU address)",
        "suite_id": 16
    },
    {
        "case_id": 34,
        "new_title": "Checkout: Guest checkout end-to-end (address, shipping, payment, place order) (US address)",
        "suite_id": 11
    },
    {
        "case_id": 35,
        "new_title": "Checkout: Select or add delivery address during checkout (US address, EU address)",
        "suite_id": 27
    },
    {
        "case_id": 36,
        "new_title": "Checkout: Pay by card at checkout (Discount eligible, 3DS required)",
        "suite_id": 29
    },
    {
        "case_id": 37,
        "new_title": "Orders: Capture order number and verify it appears in order history (EU address)",
        "suite_id": 29
    },
    {
        "case_id": 38,
        "new_title": "Orders: Open latest order from order history (Discount eligible)",
        "suite_id": 8
    },
    {
        "case_id": 39,
        "new_title": "Orders: Request cancellation for an unshipped order (Out-of-stock, Discount eligible)",
        "suite_id": 14
    },
    {
        "case_id": 40,
        "new_title": "Orders: Open shipment tracking details and verify tracking link (US address)",
        "suite_id": 27
    },
    {
        "case_id": 41,
        "new_title": "Returns: Start a return request for an eligible order (EU address)",
        "suite_id": 20
    },
    {
        "case_id": 42,
        "new_title": "Orders: View refund-in-progress status updates (Out-of-stock)",
        "suite_id": 27
    },
    {
        "case_id": 43,
        "new_title": "Admin: Sign in to admin and navigate to an admin section (US address, Discount eligible)",
        "suite_id": 11
    },
    {
        "case_id": 44,
        "new_title": "Admin: Perform admin action and verify changes persist (EU address)",
        "suite_id": 24
    },
    {
        "case_id": 45,
        "new_title": "Cart: Apply then remove promo code updates totals (3DS required, Discount eligible)",
        "suite_id": 30
    },
    {
        "case_id": 46,
        "new_title": "Admin: Perform admin action and verify changes persist (EU address)",
        "suite_id": 22
    },
    {
        "case_id": 47,
        "new_title": "Auth: Register new user and verify account via email (US address)",
        "suite_id": 13
    },
    {
        "case_id": 48,
        "new_title": "Auth: Negative: Sign in and land on authenticated area (3DS required)",
        "suite_id": 14
    },
    {
        "case_id": 49,
        "new_title": "Auth: Complete password reset via email and sign in with new password (Discount eligible)",
        "suite_id": 10
    },
    {
        "case_id": 50,
        "new_title": "Browse: Browse category listing (load more) and open a product (US address)",
        "suite_id": 14
    },
    {
        "case_id": 51,
        "new_title": "Search: Search and sort results (EU address, 3DS required)",
        "suite_id": 16
    },
    {
        "case_id": 52,
        "new_title": "Search: Apply facets then clear filters restores default results (US address, 3DS required)",
        "suite_id": 21
    },
    {
        "case_id": 53,
        "new_title": "PDP: Negative: Add variant to cart and confirm selected variant is retained (US address, 3DS required)",
        "suite_id": 18
    },
    {
        "case_id": 54,
        "new_title": "Cart: Update cart items (qty, remove, add different) recalculates totals (Discount eligible)",
        "suite_id": 24
    },
    {
        "case_id": 55,
        "new_title": "Cart: Negative: Guest cart persists after login (Out-of-stock)",
        "suite_id": 19
    },
    {
        "case_id": 56,
        "new_title": "Cart: Negative: Apply promo code updates discount and totals (Out-of-stock, Discount eligible)",
        "suite_id": 20
    },
    {
        "case_id": 57,
        "new_title": "Checkout: Negative: Guest checkout enters email and proceeds (Out-of-stock)",
        "suite_id": 20
    },
    {
        "case_id": 58,
        "new_title": "Checkout: Select or add delivery address during checkout (Discount eligible)",
        "suite_id": 28
    },
    {
        "case_id": 59,
        "new_title": "Checkout: Pay by card at checkout (EU address, 3DS required)",
        "suite_id": 22
    },
    {
        "case_id": 60,
        "new_title": "Checkout: Capture order number on confirmation (US address)",
        "suite_id": 12
    },
    {
        "case_id": 61,
        "new_title": "Orders: Open latest order and verify items and totals (US address, Out-of-stock)",
        "suite_id": 11
    },
    {
        "case_id": 62,
        "new_title": "Orders: Negative: Request cancellation for an unshipped order (3DS required)",
        "suite_id": 18
    },
    {
        "case_id": 63,
        "new_title": "Orders: Negative: Open shipment tracking details and verify tracking link (3DS required)",
        "suite_id": 8
    },
    {
        "case_id": 64,
        "new_title": "Returns: Create return request with reason and verify label availability (Discount eligible, EU address)",
        "suite_id": 30
    },
    {
        "case_id": 65,
        "new_title": "Orders: View refund-in-progress status updates (US address)",
        "suite_id": 25
    },
    {
        "case_id": 66,
        "new_title": "Admin: Sign in to admin and navigate to an admin section (Discount eligible)",
        "suite_id": 17
    },
    {
        "case_id": 67,
        "new_title": "Admin: Perform admin action and verify changes persist (Discount eligible, US address)",
        "suite_id": 26
    },
    {
        "case_id": 68,
        "new_title": "Cart: Apply promo code updates discount and totals (3DS required)",
        "suite_id": 27
    },
    {
        "case_id\": 69,\n        \"new_title\": \"Admin: Perform admin action and verify changes persist (3DS required)\",\n        \"suite_id\": 15\n    },\n    {\n        \"case_id\": 70,\n        \"new_title\": \"Auth: Negative: Register new user and verify account via email (Discount eligible)\",\n        \"suite_id\": 17\n    },\n    {\n        \"case_id\": 71,\n        \"new_title\": \"Auth: Negative: Sign in and land on authenticated area (EU address, Out-of-stock)\",\n        \"suite_id\": 8\n    },\n    {\n        \"case_id\": 72,\n        \"new_title\": \"Auth: Complete password reset via email and sign in with new password (Out-of-stock)\",\n        \"suite_id\": 30\n    },\n    {\n        \"case_id\": 73,\n        \"new_title\": \"Browse: Negative: Browse category listing (load more) and open a product (US address, EU address)\",\n        \"suite_id\": 9\n    },\n    {\n        \"case_id\": 74,\n        \"new_title\": \"Search: Search, sort results, and open a product (Out-of-stock, Discount eligible)\",\n        \"suite_id\": 26\n    },\n    {\n        \"case_id\": 75,\n        \"new_title\": \"Search: Apply a filter facet updates search results (3DS required, US address)\",\n        \"suite_id\": 13\n    },\n    {\n        \"case_id\": 76,\n        \"new_title\": \"PDP: Negative: Select variant and add product to cart (US address, Out-of-stock)\",\n        \"suite_id\": 14\n    },\n    {\n        \"case_id\": 77,\n        \"new_title\": \"Cart: Update cart quantity and remove item empties cart (US address)\",\n        \"suite_id\": 18\n    },\n    {\n        \"case_id\": 78,\n        \"new_title\": \"Cart: Guest cart persists after login (Out-of-stock)\",\n        \"suite_id\": 23\n    },\n    {\n        \"case_id\": 79,\n        \"new_title\": \"Cart: Apply then remove promo code updates totals (Discount eligible)\",\n        \"suite_id\": 22\n    },\n    {\n        \"case_id\": 80,\n        \"new_title\": \"Checkout: Negative: Guest checkout enters email and proceeds (EU address)\",\n        \"suite_id\": 13\n    },\n    {\n        \"case_id\": 81,\n        \"new_title\": \"Checkout: Select address and shipping method during checkout (EU address)\",\n        \"suite_id\": 25\n    },\n    {\n        \"case_id\": 82,\n        \"new_title\": \"Checkout: Negative: Pay by card with 3DS authentication (US address, EU address)\",\n        \"suite_id\": 18\n    },\n    {\n        \"case_id\": 83,\n        \"new_title\": \"Checkout: Capture order number on confirmation (Out-of-stock)\",\n        \"suite_id\": 17\n    },\n    {\n        \"case_id\": 84,\n        \"new_title\": \"Orders: Open latest order and verify items and totals (US address)\",\n        \"suite_id\": 9\n    },\n    {\n        \"case_id\": 85,\n        \"new_title\": \"Orders: Request cancellation for an unshipped order (3DS required, Out-of-stock)\",\n        \"suite_id\": 15\n    },\n    {\n        \"case_id\": 86,\n        \"new_title\": \"Orders: Open shipment tracking details and verify tracking link (3DS required)\",\n        \"suite_id\": 21\n    },\n    {\n        \"case_id\": 87,\n        \"new_title\": \"Returns: Start a return request for an eligible order (US address, Out-of-stock)\",\n        \"suite_id\": 10\n    },\n    {\n        \"case_id\": 88,\n        \"new_title\": \"Orders: View refund-in-progress status updates (3DS required)\",\n        \"suite_id\": 11\n    },\n    {\n        \"case_id\": 89,\n        \"new_title\": \"Admin: Perform admin action and verify changes persist (Out-of-stock)\",\n        \"suite_id\": 26\n    },\n    {\n        \"case_id\": 90,\n        \"new_title\": \"Admin: Perform admin action and verify changes persist (3DS required)\",\n        \"suite_id\": 23\n    },\n    {\n        \"case_id\": 91,\n        \"new_title\": \"Cart: Negative: Apply then remove promo code updates totals (US address, Out-of-stock)\",\n        \"suite_id\": 11\n    },\n    {\n        \"case_id\": 92,\n        \"new_title\": \"Admin: Perform admin action and verify changes persist (US address)\",\n        \"suite_id\": 20\n    },\n    {\n        \"case_id\": 93,\n        \"new_title\": \"Auth: Start registration with new email and password (EU address, 3DS required)\",\n        \"suite_id\": 28\n    },\n    {\n        \"case_id\": 94,\n        \"new_title\": \"Auth: Sign in then sign out clears the session (US address, EU address)\",\n        \"suite_id\": 26\n    },\n    {\n        \"case_id\": 95,\n        \"new_title\": \"Auth: Complete password reset via email and sign in with new password (EU address, US address)\",\n        \"suite_id\": 16\n    },\n    {\n        \"case_id\": 96,\n        \"new_title\": \"Browse: Browse category, open product, return to category with state preserved (US address)\",\n        \"suite_id\": 19\n    },\n    {\n        \"case_id\": 97,\n        \"new_title\": \"Search: Search, sort results, and open a product (3DS required)\",\n        \"suite_id\": 30\n    },\n    {\n        \"case_id\": 98,\n        \"new_title\": \"Search: Apply multiple facets updates search results (Out-of-stock)\",\n        \"suite_id\": 17\n    },\n    {\n        \"case_id\": 99,\n        \"new_title\": \"PDP: Add variant to cart and confirm selected variant is retained (US address)\",\n        \"suite_id\": 21\n    },\n    {\n        \"case_id\": 100,\n        \"new_title\": \"Cart: Update cart quantity updates totals (3DS required)\",\n        \"suite_id\": 29\n    },\n    {\n        \"case_id\": 101,\n        \"new_title\": \"Cart: Negative: Guest cart persists after login (EU address, 3DS required)\",\n        \"suite_id\": 12\n    },\n    {\n        \"case_id\": 102,\n        \"new_title\": \"Cart: Negative: Apply then remove promo code updates totals (Discount eligible)\",\n        \"suite_id\": 24\n    },\n    {\n        \"case_id\": 103,\n        \"new_title\": \"Checkout: Guest checkout enters email and proceeds (Out-of-stock, 3DS required)\",\n        \"suite_id\": 22\n    },\n    {\n        \"case_id\": 104,\n        \"new_title\": \"Checkout: Select or add delivery address during checkout (US address, Discount eligible)\",\n        \"suite_id\": 18\n    },\n    {\n        \"case_id\": 105,\n        \"new_title\": \"Checkout: Pay by card at checkout (Out-of-stock, Discount eligible)\",\n        \"suite_id\": 23\n    },\n    {\n        \"case_id\": 106,\n        \"new_title\": \"Orders: Negative: Capture order number and verify it appears in order history (US address)\",\n        \"suite_id\": 21\n    },\n    {\n        \"case_id\": 107,\n        \"new_title\": \"Orders: Open latest order and verify items and totals (Out-of-stock)\",\n        \"suite_id\": 9\n    },\n    {\n        \"case_id\": 108,\n        \"new_title\": \"Orders: Cancel unshipped order and verify status updates (Out-of-stock)\",\n        \"suite_id\": 19\n    },\n    {\n        \"case_id\": 109,\n        \"new_title\": \"Orders: Open shipment tracking details and verify tracking link (Discount eligible, 3DS required)\",\n        \"suite_id\": 24\n    },\n    {\n        \"case_id\": 110,\n        \"new_title\": \"Returns: Create return request with reason and verify label availability (US address, 3DS required)\",\n        \"suite_id\": 10\n    },\n    {\n        \"case_id\": 111,\n        \"new_title\": \"Orders: View refund-in-progress status updates (EU address, Discount eligible)\",\n        \"suite_id\": 9\n    },\n    {\n        \"case_id\": 112,\n        \"new_title\": \"Admin: Perform admin action and verify changes persist (EU address, Out-of-stock)\",\n        \"suite_id\": 17\n    },\n    {\n        \"case_id\": 113,\n        \"new_title\": \"Admin: Sign in to admin and navigate to an admin section (Discount eligible)\",\n        \"suite_id\": 19\n    },\n    {\n        \"case_id\": 114,\n        \"new_title\": \"Cart: Negative: Apply promo code updates discount and totals (US address)\",\n        \"suite_id\": 8\n    },\n    {\n        \"case_id\": 115,\n        \"new_title\": \"Admin: Negative: Sign in to admin and navigate to an admin section (EU address)\",\n        \"suite_id\": 23\n    },\n    {\n        \"case_id\": 116,\n        \"new_title\": \"Auth: Register new user and verify account via email (EU address, 3DS required)\",\n        \"suite_id\": 12\n    },\n    {\n        \"case_id\": 117,\n        \"new_title\": \"Auth: Sign in and land on authenticated area (Discount eligible)\",\n        \"suite_id\": 24\n    },\n    {\n        \"case_id\": 118,\n        \"new_title\": \"Auth: Complete password reset via email and sign in with new password (EU address)\",\n        \"suite_id\": 22\n    },\n    {\n        \"case_id\": 119,\n        \"new_title\": \"Browse: Negative: Browse category, open product, return to category with state preserved (US address, EU address)\",\n        \"suite_id\": 22\n    },\n    {\n        "case_id": 120,
        "new_title": "Search: Refine search query and verify results update (US address)",
        "suite_id": 12
    }
]
"""
updates_to_perform = json.loads(updates_to_perform_json)

for update in updates_to_perform:
    case_id = update["case_id"]
    new_title = update["new_title"]
    suite_id = update["suite_id"]

    try:
        logging.info(f"Attempting to update case {case_id} with new title: '{new_title}' and suite_id: {suite_id}")
        test_case_update_body = TestCaseUpdate(title=new_title, suite_id=suite_id)
        response = cases_api.update_case(QASE_PROJECT_CODE, case_id, test_case_update_body)
        logging.info(f"Successfully updated case {case_id}: {response.result.id}")
    except Exception as e:
        logging.error(f"Error updating case {case_id}: {e}")

logging.info("All updates attempted.")
