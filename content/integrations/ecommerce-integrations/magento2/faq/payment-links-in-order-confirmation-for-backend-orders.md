---
title : "Payment link in order confirmation email for backend orders"
meta_title: "Magento 2 plugin FAQ - Payment links - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
summary: "We have added a feature to include the payment link in the order confirmation mail. This feature is customizable and can be changed to your liking."
read_more: "."
aliases:
    - /magento2/faq/payment-links-in-order-confirmation-for-backend-orders
    - /integrations/magento2/faq/payment-links-in-order-confirmation-for-backend-orders/
---

We have added a feature to include the payment link in the order confirmation mail. This feature is customizable and can be changed to your liking. This feature can be implemented by the following steps:

1. Log in to your Magento backend 
2. Go to _Marketing_ → _Email Templates_
3. Add a template (import from _new order_)
4. Add the following code snippet to the template:

`{{depend order.getPayment().getAdditionalInformation('payment_link')}}`
`<a href="{{var order.getPayment().getAdditionalInformation('payment_link')}}">Pay now with {{var order.getPayment().getAdditionalInformation('method_title')}}</a>`
`{{/depend}}`

The email template syntax is different for Magento 2.3.4+.  
For these versions you can add this sample code instead:

`{{depend order.payment.additional_information.payment_link}}`
`<a href="{{var order.payment.additional_information.payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>`
`{{/depend}}`

There is also a 'payment_link' variable that you can use in e-mail templates for order confirmation e-mails created in the backend of Magento. This variable is not available for orders that are created in the frontend. With a simple 'if/else' statement in the e-mail template, you can add logic to only add the payment link to order confirmation e-mails for orders created in the backend. For orders created in the frontend, you can show something else, for example, only the payment method title:

`{{if payment_link}}`
`<a href="{{var payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>`
`{{else}}`
`<p>{{var order.payment.additional_information.method_title}}</p>`
`{{/if}}`

1. Go to _Stores → Configuration → Sales → Sales Emails_
2. Change the "New Order Confirmation Template" with your template
3. After these changes, the template should be tested to confirm it is working.

_Note: This can also be implemented directly in the email template files._
