---
title: 'in3'
category: 6298bd782d1cf4006032e765
order: 204
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'in3'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/in3.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

[in3](https://payin3.eu/en/) is a Dutch <<glossary:BNPL>> method where customers pay in 3 installments, at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). in3 guarantees <<glossary:settlement>> after receiving the first installment.

Read how in3 can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/in3)

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | The Netherlands – in3 checks the customer's country, and billing/shipping address to confirm.  | 
| [Currencies](/docs/currencies/)  | EUR  |  
| [Chargebacks](/docs/chargebacks/)  | No  |
| [Discounts](/docs/discounts/) | Yes <br> You can request in3 to process a full or partial refund, either before <<glossary:payout>> or up to 1 year afterwards. |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/in3-payment-flow.svg" alt="in3 payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| in3's credit check is in progress. You can still cancel. | Initialized   | Initialized  |
| in3 is waiting for the customer to pay the first installment (within 5 mins). | Uncleared  | Initialized  |
| The customer has paid the first installment. Settlement is now guaranteed. <br> You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| You can [manually change the order status to shipped](#shipment) for your records, but this is not required to trigger invoicing. | Shipped | Uncleared | 
| MultiSafepay has collected payment. | Completed | Completed |
| in3 declined the transaction. | Declined | Declined |
| The customer cancelled the transaction or abandoned the first installment. | Void | Void |
| The customer didn't pay the first installment. | Expired | Expired |
| **Refunds:** in3 has successfully processed a full or partial refund. | Completed | Completed |
| **Refunds:** The refund was declined. | Declined | Declined   |

# Activation 

First apply to MultiSafepay, and then activate in your dashboard.

<details id="how-to-activate-in3"> 
<summary>How to activate in3</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > BNPL order. 
- Examples > in3 direct/redirect.
- Transactions expire after 2 hours.

### Ready-made integrations
in3 (direct) is supported in:
- [Craft Commerce](/docs/craft-commerce/)
- [Magento 1](/docs/magento-1/)
- [OpenCart](/docs/opencart/)
- [PrestaShop 1.7](/docs/prestashop-1-7/)
- [VirtueMart](/docs/virtuemart/)
- [WooCommerce](/docs/woocommerce/)

### Testing
To test in3 payments, see [Testing](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

Different billing and shipping addresses are supported.

## Amount limits

- Minimum amount: 100 EUR 
- Maximum amount: 3000 EUR 

You can adjust these limits in the <<glossary:backend>> of our [ready-made integrations](/docs/our-integrations/) to show or hide in3 on your checkout page depending on the order value.

## Gift cards

When paying with a gift card and in, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. This is because in3 collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Shipment

When you ship the order, you can change the order status to **Shipped** for your records, bu this is not required to trigger invoicing.

<details id="how-to-change-order-status-to-shipped">
<summary>How to change the order status to shipped</summary>
<br>

You can change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped**:

**In your dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

</details>

### Surcharges

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email <sales@multisafepay.com> 
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)