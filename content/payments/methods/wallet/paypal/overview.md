---
title: 'PayPal overview'
breadcrumb_title: 'Overview'
weight: 10
meta_title: "PayPal overview - MultiSafepay Docs"
short_description: "Key information, supported countries, currencies, and features"
layout: 'child'
url: '/payment-methods/paypal/product-rules/'
aliases:
    - /payments/methods/wallet/paypal/about/
    - /payments/methods/paypal/product-rules/
    - /payment-methods/paypal/product-rules/
---

|   |   |  
|---|---|
| **Countries**  | Worldwide  | 
| **Currencies**  | [Multiple](https://developer.paypal.com/docs/payouts/reference/country-and-currency-codes/) | 
| **Chargebacks**  | Yes – See [Chargebacks](/payments/chargebacks/).  |
| **Refunds** | [Full and partial](/refunds/full-partial/) {{< br >}} Refunds are only processed if there are enough funds in your PayPal business account. Otherwise, PayPal issues an [eCheck](https://www.paypal.com/us/smarthelp/article/what-is-an-echeck-faq1082). {{< br >}} To avoid PayPal cancelling the refund, in your PayPal account authorize PayPal to withdraw funds from another bank account instead. {{< br >}} For support, contact PayPal – [Help Center Home](https://www.paypal.com/us/smarthelp/home). | 
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after**  | 14 days | |

## PayPal Seller Protection

PayPal Seller Protection covers you in the event of claims, chargebacks, or reversals due to unauthorized purchases or items the customer didn't receive. You are covered for the full amount of all eligible transactions.

To be eligible, for specific countries, transaction requests must contain the correct `state` in the `customer_address`. For a list of the countries, see PayPal API – [State codes](https://developer.paypal.com/docs/nvp-soap-api/state-codes).

For more information, see PayPal – [What is Seller Pretection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156). 


