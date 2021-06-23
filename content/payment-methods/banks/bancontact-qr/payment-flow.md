---
title: "Bancontact QR payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Bancontact QR payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/bancontact.svg'
aliases: 
    - /payment-methods/bancontact/how-does-bancontact-qr-work/
---

The table below shows a successful Bancontact QR payment flow from start to finish.  

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer authenticates their account, and confirms to pay. | | |
| 4. | The transaction is successful. {{< br >}} It cannot be reversed by the customer and settlement is guaranteed. | Completed | Completed |
| 5. | Bancontact settles the funds with MultiSafepay.| | |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance.| | |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| Bancontact has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

## Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/banks/bancontact-qr/user-guide/processing-refunds/).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |