---
weight: 208
meta_title: "API Reference - Adjust payment link lifetime - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /api/#days_active--seconds_active
    - /faq/api/lifetime-of-a-payment-link
    - /faq/api/adjusting-payment-link-lifetimes
    - /developer/api/adjusting-payment-link-lifetimes/
---
{{< code-block >}}

```json 
{
  "days_active":30,
  "seconds_active":60,
  "description":"Test order description"
}
```
{{< /code-block >}}

{{< description >}}
### Adjust payment link lifetimes

The lifetime of a [payment link](/payments/checkout/payment-link/) is how long it remains valid for the customer to complete payment. The default is 30 days, after which the link expires. Except for:  

- [Bank Transfer](/payments/methods/banks/bank-transfer/): 60 days
- [PayPal](/payments/methods/wallet/paypal/): 14 days
- [Post-payment methods](/payments/methods/billing-suite/): You cannot adjust payment link lifetimes.

To cancel a payment link, see [Cancel an order](/api/#cancel-an-order).

**Second Chance**  
You cannot edit payment links in [Second Chance](/payments/boost/second-chance/) emails, because the `session_id` of the initial transaction has already been used. You can only edit the link in the initial `POST /orders` request. 

If set for under 24 hours:  

- `days_active`: The payment link displays an error message when opened.
- `seconds_active`: The second email is still sent, even though the payment link it contains is no longer valid. This can't be changed.  

**Parameters**

Include in your `POST /orders` request:

----------------

`days_active` | string | optional

The number of days the payment link is valid for.  
If not set, or if `seconds_active` is also set, `seconds_active` is used.  
If neither `days_active` nor `seconds_active` is set, the default is used.  
Default: 30 days.

----------------
`seconds_active` | string | optional

The number of seconds the payment link is valid for.  
Example: 86.400 `seconds_active` = 1 `days_active`.  
If set and larger than 0, `seconds_active` overrides `days_active`.  
If neither `days_active` nor `seconds_active` is set, the default is used.  
Default: 30 days. 

----------------
`description` | string | optional

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------

{{< /description >}}