---
title : "Coppermine integration for MultiSafepay"
meta_title: "Coppermine integration for MultiSafepay - MultiSafepay Docs"
layout: 'single'
meta_description: "Integrate MultiSafepay payment solutions into your Coppermine ecommerce platform."
logo: "/logo/Integrations/coppermine-docs.svg"
weight: 32
title_short: "Coppermine"
type: 'Integration'
description_short: "Integrate MultiSafepay payment solutions into your Coppermine ecommerce platform."
layout: 'single'
url: '/coppermine/'
---

MultiSafepay has partnered with [Coppermine](https://www.coppermine.nl/), which offers a complete ecommerce suite including CRM, B2B, B2C, subscriptions, customer service, logistics, and finance.

To integrate MultiSafepay as your payment service provider, follow these steps:

## 1. In your dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Website settings** and [add the required site(s)](/account/managing-websites/#adding-websites) to your account.
3. In the **Website settings** page for each site:
    - [Activate the required payment methods](/payments/activating-payment-methods/).
    - In the **Notification URL** field, add the Coppermine webhook endpoint for sending status updates and other notifications. For more information, see [Webhook](https://docs.multisafepay.com/developer/webhooks/).
4. Copy your:
    - Account ID (top-right corner of the dashboard)
    - [Site ID, API key, and secure code](/account/site-id-api-key-secure-code/)

## 2. In Coppermine

1. Sign in to your Coppermine backend, and then go to **Settings**.
2. To configure the MultiSafepay PaymentMethod Gateway, enter your:
    - MultiSafepay account ID
    - Site ID, API key, and secure code

## 3. Testing

1. Place some test orders in your webshop and Coppermine backend.
2. Check the transactions in Coppermine and your MultiSafepay dashboard. 
3. When everything is working correctly, in your Coppermine backend, set the PaymentMethod Gateway to **Production** mode.