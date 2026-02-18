# Shared Step: Complete checkout with default payment

**Purpose**: Reusable sequence for completing the checkout process using predefined shipping, billing, and payment details.

**Steps**:
1. **Action**: Navigate to cart and proceed to checkout
   **Expected Result**: Checkout flow initiated
2. **Action**: Fill in required shipping and billing details
   **Data**: `Shipping address: {shipping_address}, Billing address: {billing_address}`
   **Expected Result**: Order summary is displayed with correct totals
3. **Action**: Click 'Place Order'
   **Expected Result**: Order confirmation page is displayed