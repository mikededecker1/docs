---
title : "About 3D Secure"
weight: 1
meta_title: "FAQ Payment regulations - About 3D Secure - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/payment-regulations/3D-secure
    - /payment-methods/credit-and-debit-cards/creditcards/what-is-3d-secure/
    - /faq/general/what-is-3d-secure
---

3D Secure (3DS) is an authentication protocol for online transactions. 3D Secure is also known by its branded names like Mastercard Identity Check, Visa Secure or American Express SafeKey. Two versions of the 3D Secure protocol coexist (3DS 1.0 and 3DS 2.0).

**Please note:** All Europe-based transactions through our platform use the 3D Secure protocol in order to comply with PSD2 regulations.

## How does 3D Secure relate to PSD2 and SCA?

The Payment Services Directive 2 [(PSD2)](/faq/payment-regulations/payment-service-directive-2) is a set of laws and regulations that aims to improve European consumer rights while promoting competition within the financial industry. One of the requirements of PSD2 is Strong Customer Authentication [(SCA)](/faq/payment-regulations/strong-customer-authentication). SCA combines two elements of authentication to reduce the risk of fraud. The 3D Secure authentication protocol is a widely implemented form of SCA that complies with PSD2 regulations.

## What's new in 3DS 2.0?

**Please note:** We are working on supporting 3DS 2.0 and we expect to rollout the support in 2021. In the meantime, transactions use 3DS 1.0 and are fully PSD2 compliant.

3DS 2.0 aims to provide better security and greater customer experience than its predecessor. This is achieved through the collection of more contextual data from the customer. The contextual data is used 'behind-the-scenes' to verify the identity of the customer. This reduces the complexity of the check-out flow, resulting in higher conversion and lower cart abandonment.

Based on the risk level of the transaction, two flows can emerge: the *frictionless flow* and *challenge flow*. Both flows start after the customer has provided his or her card information. Along with the card information, contextual information from the customer's device is shared with the issuer and merchant to make an informed decision as to request additional authentication or not.

{{< br >}}
{{< responsive_svg src="/diagrams/svg/3DS-flow" alt="3D Secure Flow" align="center" title="3DS Flow">}}
{{< br >}}
{{< br >}}

Examples of data used for risk assessment include:

* The value of the transaction
* New or existing customer
* Transactional history
* Location of customer

If the contextual data indicates a legitimate transaction, the payment is verified without further user-side authentication. This is also called a frictionless flow. In case the contextual data include abnormalities, the customer is asked to provide additional authentication (e.g. through password, code via SMS or fingerprint).