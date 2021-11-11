---
weight: 330
meta_title: "API reference - Create a Postepay order - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders 

```json 
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"VISA",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"it_IT",
    "ip_address":"123.123.123.123"
  }
}
```

> JSON response 

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=it_IT"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Postepay

- See also Payment methods – [Postepay](/payment-methods/postepay).
- Redirect only.


**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The gateway identifier.  
Value: `VISA` or `MASTERCARD`.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Note:** To see Postepay as a payment option, `customer.locale` must be set to: `"it_IT"`.

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}