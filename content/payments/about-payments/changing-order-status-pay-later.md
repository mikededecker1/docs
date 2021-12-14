---
title: "Shipped status for pay later methods"
weight: 40
meta_title: "Shipped status for pay later methods - MultiSafepay Docs"
read_more: "."
url: '/about-payments/pay-later-shipped-status/'
---

For [pay later methods](/payments/methods/pay-later/), you must manually change the [order status](/payments/multisafepay-statuses/) from **Completed** to **Shipped**. This triggers the payment method to invoice the customer and transfer the funds to MultiSafepay. It also prevents the order from expiring. 

## In your MultiSafepay account

To change the order status in your MultiSafepay account, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

## In your backend

If you change the order status in your [backend](/getting-started/glossary/#backend), the following [ready-made integrations](/integrations/ready-made/) can pass the updated status to your MultiSafepay account automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, you can update the status via our API by making a `PATCH /orders` request. See API reference – [Update an order](/api/#update-an-order).

**Note:** Some third-party plugins may not support updating the status via our API. 
