---
weight: 220
meta_title: "API Reference - Partial capture - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#partial-capture
---
{{< code-block >}}

> POST - /orders/{order_id}/capture

```json
{
  "amount":2000,
  "new_order_id":"my-order-id-01",
  "new_order_status":"completed",
  "invoice_id":"",
  "tracktrace_code": "",
  "carrier":"",
  "reason":"",
  "description":""
}
```
> JSON response


```json
{
  "success":true,
  "data":{
    "transaction_id":123456789,
    "order_id":"my-order-id-01"
  }
}
```
{{< /code-block >}}
{{< description >}}
### Partial capture

**Parameter**

----------------
`amount` | integer | optional

The amount (in cents) to charge.

For partial captures, specify the amount to capture.

----------------
`new_order_id` | string | optional

Your unique identifier for the order.  
Format: Maximum 50 characters.    

----------------
`new_order_status` | string | required

The updated status of the order.

----------------
`invoice_id` | string | optional

Update an existing order with a reference to your internal invoice ID.  
The invoice ID is added to [reports](/business/accounting/reports/) generated from your MultiSafepay account.  
Format: Maximum 50 characters.  

----------------
`tracktrace_code` | string | optional

The track and trace code linked to the shipment of the order.

----------------
`carrier` | string | optional

The name of the shipping company delivering the customer’s order.

----------------
`reason` | string | optional

The reason for capturing the order.       

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`description` | string | optional

Can be used to store additional information.

----------------

{{% /description %}}