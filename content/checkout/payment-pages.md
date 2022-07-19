---
title: 'Payment pages'
category: 62bd999547298d001abc714c
order: 30
hidden: false
slug: 'payment-pages'
---
Payment pages are hosted by MultiSafepay and are the easiest way to integrate all payment methods. 

They are completely secure, fully mobile responsive, and can be styled to fit the look and feel of your site.

# How it works

A customer selects a payment method at checkout, and is redirected to a secure page to complete payment with a URL starting with `payv2.multisafepay.com`.

If you specify a payment method <<glossary:gateway>>, the page is tailored for that payment method. For example, for Visa, the page includes fields for the customer to enter their credit card details.  

If you don't specify a gateway, all payment methods enabled in your account appear on the payment page.

# Activation

You can activate payment pages yourself in your dashboard.

<details id="how-to-activate-payment-pages">
<summary>How to activate payment pages</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Click the relevant site.
4. Select the **Use new payment pages** checkbox.

> **Note:** If the **Use new payment pages** checkbox is not visible, email <integration@multisafepay.com>
</details>

# Integration 

See API recipe – [Create a payment page](/recipes/create-a-payment-pagelink).

<details id="known-errors">
<summary>Known errors</summary>
<br>

A cross-site request forgery (CSRF) warning appears on payment pages when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a [create order](/reference/createorder/) request.
 
- `https://api.multisafepay.com` accepts `POST` and `GET` requests.
- `https://payv2.multisafepay.com` only accepts `GET` requests.
</details>
<br>

---

# User guide

## Deprecated version

The deprecated version of the payment page (URL: `pay.multisafepay.com`) is still fully supported, but we strongly recommend upgrading to the current version.

<details id="unsupported-payment-methods">
<summary>Unsupported payment methods</summary>
<br>

We cannot guarantee that the deprecated version will support any new payment methods we add to our platform.

It does **not** support the following methods:

| Method type | Unsupported methods |
|---|---|
| **BNPL** | AfterPay, Betaal per Maand, in3, Klarna |
| **Wallets** | Alipay, Apple Pay, WeChat Pay |
| **Banking** | Bancontact QR, Belfius, CBC/KBC, EPS, iDEAL QR, Request to Pay, Sofort, Trustly |
| **Prepaid cards** | PaySafecard |

</details>

## Google Analytics tracking

You can track the behavior of customers on payment pages through Google Analytics tracking. When the customer is redirected to the payment page, the UA-code is generated and appears in the HTML.

## iframes

An inline frame (iframe) is an HTML document embedded inside another HTML document on a site. 
 
Although MultiSafepay doesn't prohibit embedding payment pages as an `<iframe>`, we do **not** recommend it. This is because:

- Some payment methods may not work for privacy and security reasons. 
- Some banks use scripts that can't run within `<iframe>` elements.
- Modern browsers can block them due to stricter security checks.

Instead, we recommend using [payment components](/docs/payment-components/) to embed payments into your site. 

## Languages

Payment pages are supported in 19 languages. 

<details id="supported-languages">
<summary>Supported languages</summary>
<br>

Payment pages support the following languages:

| Supported languages | Supported languages |
|---|---|
| Arabic | Japanese |
| Czech | Mandarin |
| Danish | Norwegian |
| Dutch | Polish |
| English | Portuguese |
| Finnish | Russian |
| French | Spanish |
| German | Swedish |
| Hebrew | Turkish |
| Italian ||

</details>

## Payment links

You can manually generate a [link to a payment page](/docs/payment-links/) to send to a customer to complete payment. 

## Payment methods

If a customer's country is unclear or your integration doesn't let you provide the correct country code, consider displaying **all** your enabled payment methods on the payment page. This is not supported for the deprecated version.

<details id="how-to-display-all-payment-methods">
<summary>How to display all payment methods</summary>
<br>

To display all payment methods on the payment page, follow these steps:

1. [Create an order](/reference/createorder/) to retrieve the payment link.
2. Add `&methods=all` at the end of the payment link, e.g. `https://testpayv2.multisafepay.com/connect/822LtiM8RjN313Yo5C46E2cjqmuL5qVfc7w/?lang=en_NL&methods=all`
3. Redirect the customer to the adapted link.

> **Note:** This is not a standard option in our [ready-made integrations](/docs/our-integrations/).


</details>

## Shopping cart

If you include a `shopping_cart` object when you [create an order](/reference/createorder/), the cart details are displayed on the payment page by default. That is, all items in the customer's order, with the price and VAT for each.

<details id="how-to-hide-shopping-cart">
<summary>How to hide the shopping cart</summary>
<br>

1. To request to enable **Advanced website templates** for your MultiSafepay account, email <integration@multisafepay.com>
2. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/). 
3. Go to **Settings** > **New payment pages**.
4. Next to the relevant site, click **Template**.
5. Under **Configure page style**, click **Settings**, and then select the **Hide cart details** checkbox. 

</details>

## Styling 

We recommend styling payment pages to be consistent with the look and feel of your site.

<details id="in-your-dashboard">
<summary>In your dashboard</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings** > **Website**.
3. Click the **Template** button. 
4. Use the WYSIWYG editor to style the payment page template.  

    **Choosing colors**  
    In the left menu, a color chart appears when you click on the field of a page element. You can also enter a [Hex color](https://www.w3schools.com/colors/colors_picker.asp) in the input field next to it.  

    **Selecting a logo or header image**  
    In **Settings** > **Payment page templates**, upload files for logos or header backgrounds. They may take up to 5 minutes to process, and then automatically appear in the list in the editor.  

    **Setting a default template**  
    If you have more than one template and want to set one as your default template, use the **Set default** option. You can also give this template a name, which is used as the `template_id`.   

    **Editing saved templates**  
    Click **Edit template** (top-left corner).  

    **Duplicating styling to another template**  
    Click **Apply style from** (top-right corner). Save the template to the relevant site.  

5. To save the finished template to the relevant site, click **Submit website**. 

</details>

<details id="via-the-api">
<summary>Via the API</summary>
<br>

You can dynamically style the payment page template for specific transaction requests via our API. 

See API reference – [Create order](/reference/createorder/) > Payment page/link > `payment_options` object. 

The `items` parameter is an HTML string for displaying order items on the payment page, instead of including a `shopping_cart`. The following HTML tags and elements are supported (all others are stripped out):

- b, br
- div (align)
- em
- font (color, face, size)
- h1, h2, h3, h4, h5, h6, hr
- i, img (width, height, alt, scale, border, align)
- li
- nobr
- ol
- p
- small, span, strong
- table (width, border, bordercolor, cellpadding, cellspacing), thead, tbody, tfoot, th (width, scope, colspan, align), td (height, width, align, valign, colspan, bgcolor), tr (bgcolor, valign)
- u, ul

</details>

## Requirements for Visa

When customers select Visa as payment method, Visa requires us to display on the payment page the city and country where your webshop is located. This measure aims to increase reliability, transparency, and safety for customers.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)