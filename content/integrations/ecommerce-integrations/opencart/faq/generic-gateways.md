---
title : "Generic gateways"
meta_title: "Generic gateways - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
---
The OpenCart plugin offers a [generic gateway](/faq/general/generic-gateways/). The generic gateway can be found on the plugin settings page, listed in the payment methods tab.

All of our payment methods are supported. It is possible to set the gateway code, gateway logo, gateway label, and whether the shopping cart should be included in refund transactions. Specifying whether the shopping cart should be included in refund transactions is required if the gateway code used is that of a billing suite payment method.

Similar to other gateways, it is possible to filter the generic gateway by:

* geographic zone
* currency
* min amount
* max amount
* customer groups

Furthermore, you can set a custom initial order status.

Full refunds, partial refunds (except for billing suite payment methods), and backend orders are fully supported.