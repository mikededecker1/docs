---
title: "CBC/KBC payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "CBC/KBC payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/cbc.svg'
url: '/payments/methods/banks/cbc-kbc/payment-flow/'
aliases: 
    - /payment-methods/cbc/how-does-cbc-work/
    - /payments/methods/banks/cbc/payment-flow/
    - /payments/methods/banks/kbc/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects CBC/KBC at checkout and is redirected to a MultiSafepay payment page. | Initialized | Initialized |
| 2. | The customer authenticates their account and completes the payment. {{< br >}} **Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**. We import our bank statements daily and all incoming payments are then finalized. | | |
| 3. | We collect the funds and settle them in your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 5-day period. | Expired | Expired |

## Refund statuses

 Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |




