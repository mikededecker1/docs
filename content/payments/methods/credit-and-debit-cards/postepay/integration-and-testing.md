---
title: "Integrating and testing Postepay"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Postepay - MultiSafepay Docs"
short_description: "Options for integrating Postepay and testing payments"
layout: 'child'
url: '/payment-methods/postepay/integration-testing/'
aliases:
    - /payments/methods/credit-and-debit-cards/postepay/integration-and-testing/
    - /postepay/integration-testing/
    - /postepay/integration-testing/
---
## Integration

| | |
|---|---|
| **API** | See API reference – [Co-branded credit cards](/api/#co-branded-credit-cards). {{< br >}} **Bundled credit cards** {{< br >}} You can also bundle multiple credit cards together on your MultiSafepay credit card payment page. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits. {{< br >}} To make Postepay available as a payment method on the MultiSafepay credit card payment page, set the [`locale`](/developer/api/using-locale-parameters) to `it_IT` (Italy) in transaction requests. {{< br >}} See API reference – [Credit cards](/api/#credit-cards). |
| **Ready-made integrations** | You can integrate using the Visa gateway (redirect) in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test a Postepay order

1. Make a [redirect](/api/#postepay) API request with the `locale` set to `it_IT`.
2. On the payment page:
    - In the **Numero carta** field, enter `4111111111111111`.
    - In the **Titolare carta** field, enter any name.
    - From the **Data di scadenza** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Conferma**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

**Note:** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.

### Test refunding an order

To test refunding an order:

1. Create an order using card number `4012001038443335`. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

### Test an API refund

To test refunding an order via the API:

1. Create an order using card number `4012001038443335`. 
2. Make a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Notes:**

- You can't test cancelling orders. 
- In the live environment, you can't accept refund orders. These are done automatically.

