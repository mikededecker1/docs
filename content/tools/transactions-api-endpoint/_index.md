---
title : "Transactions API endpoint"
layout : "single"
tags : "hidden"
---

## Introduction

The transactions API endpoint returns the data of transactions that are associated with your account. Using this endpoint, you can automate business operations and gain insights into your transactions.

To learn more about its applications, we examine four common use cases:

* [**General overview**](#create-a-general-overview): Create an overview of all transactions
* [**Payout specification**](#generate-a-payout-specification): Gain insight into your payouts
* [**Reconciliation**](#perform-reconciliation): Automate your bookkeeping by matching mutations
* [**Refunds overview**](#create-a-refund-overview): Create an overview of your refunds 

{{< br >}}

## Usage

To access the transactions API endpoint, use the following URLs:

**Test**  
`https://testapi.multisafepay.com/v1/json/transactions`

**Live**  
`https://api.multisafepay.com/v1/json/transactions`



The transactions API endpoint supports the `GET` HTTP method. Requests to this endpoint require a [valid API key](/tools/multisafepay-control/get-your-api-key/). Set your key to the `Authorization` header value, like this:

```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" -H "Content-Type: application/json" -H "Authorization: Bearer <your-api-key>"
```

_Note: Make sure to use your test API key when making a request to our test API_


### Functionality


This API endpoint has no required parameters. Calls to the transactions endpoint retrieve an array of all transactions under your account. Use the parameters to filter your requested transactions to include only those relevant to your needs. 

The return type of requests to the transactions endpoint is `JSON` and transactions are formatted as follows:

```
{
  "amount": 0,
  "completed": "string",
  "costs": [
    null
  ],
  "created": "string",
  "currency": "string",
  "debit_credit": "D_C",
  "description": "string",
  "financial_status": "string",
  "invoice_id": "string",
  "order_id": "string",
  "payment_method": "string",
  "site_id": 0,
  "status": "string",
  "transaction_id": 0,
  "type": "string",
  "var1": "string",
  "var2": "string",
  "var3": "string"
}
```

{{< br >}}

### Parameters 

You can use the following parameters to filter the returned transactions:

| Parameter | Description                  |
|------------------|-----------------------|
| site_id | Only transactions for specified `site_id` are returned. Find your site IDs in MultiSafepay Control. By default, the transactions endpoint will return the transactions of all sites under your account. {{< br >}} **Format:** integer (e.g. `12345`) |
| start | Transactions created after `start` are returned. {{< br >}} **Format:** [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g. `2021-01-01T12:00:00`)  ||
| start_epoch  | Transactions created after `start_epoch` are returned. This parameter can be used as an alternative to `start`. If both values are specified, `start` overrules `start_epoch`. {{< br >}} **Format:** [Epoch](https://en.wikipedia.org/wiki/Unix_time) (e.g. `1609502400`)    |
| end     |  Transactions created before `end` are returned. {{< br >}} **Format:** [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g. `2021-01-01T12:00:00`)  |
| end_epoch | Transactions created before `end_epoch` are returned. This parameter can be used as an alternative to `end`. If both values are specified, `end` overrules `end_epoch`. {{< br >}} **Format:** [Epoch](https://en.wikipedia.org/wiki/Unix_time) (e.g. `1609502400`)    |
| financial_status  |  Transactions with matching [financial status](/api/#financial-statuses) are returned. {{< br >}} **Options:** `completed`, `created`, `declined`, `error`, `expired`, `initialized`, `manual`, `new`, `refunded`, `reserved`, `uncleared`, `void`                |
| status    |  Transactions with matching [transaction status](/api/#transaction-statuses) are returned. {{< br >}} **Options:** `completed`, `initialized`, `uncleared`, `declined`, `cancelled`, `void`, `expired`, `refunded`, `partial_refunded`, `reserved`, `chargeback`, `shipped`                |
| payment_method | Transactions with matching payment method are returned. {{< br >}} **Format:** Follows [gateway](/api/#retrieve-a-gateway) conventions (e.g. `VISA`) |
| type | Transactions with matching transaction type are returned. {{< br >}} **Options:** `admin_fee`, `affiliate_payout`, `automatic_payout`, `chargeback`, `coupon`, `currency_conversion`, `deposit`, `fastcheckout`, `monthly_fee`, `payment`, `refund`, `reserve_chargeback`, `singup_fee` |
| limit  | Set `limit` to specify the maximum number of returned results per [page](#pagination). When `limit` is undefined it defaults to `100` to limit the response size. {{< br >}} **Format:** integer (e.g. `10`) |
| after | Use the `after` cursor to request the next page when results are [paginated](#pagination). {{< br >}} **Format:** string (e.g. `ZD1ftlaZLHQ90EQCeQ`)
| before | Use the `before` cursor to request the previous page when results are [paginated](#pagination). {{< br >}} **Format:** string (e.g. `ZD1gIU-ZLPQ9AEX73Q`)

**Please note:** values `site_id`, `financial_status`, `status`, `payment_method`, and `type` can be specified both as single values or as arrays containing multiple values.

{{< br >}}

### Pagination
A request to the transactions endpoint can return a lot of results. To make responses easier to handle, we paginate the results. The amount of transactions returned per call can be specified using the `limit` parameter. If the `limit` parameter is undefined, the value defaults to `100`.

To access the next page of a response, use the `after` cursor from the `pager` object of the response. Upon subsequent calls, use the most recently returned `after` cursor to iterate over all pages. The last page with data will return an `after` pager to an empty page. A request to this page will be succesfull, but won't return any data or new cursors. 

To access the previous page, use the `before` cursor in the `pager` object.

_Please note that results are sorted from new to old. This means that the `after` cursor points to older transactions._

## Use cases

### Create a general overview

_I want to have a complete overview of all transactions associated with my MultiSafepay account_

To create a general overview of your transactions, no parameters are required. Instead, use the parameters to filter the transactions to your needs. 
When making unfiltered requests to the transactions API endpoint, use pagination to make responses easier to handle. To use pagination, set `limit` to the number of transactions to be returned per request.

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?limit=20" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

{{< br >}}

### Generate a payout specification

 _I want to have an overview of all transactions that correspond with my payout_

* Gain insights into the transactions that account for a specific payout
* Management of your accounting and bookkeeping

| Parameter  | Required value |
|------------------|-----------------------|
| start | Specify the start of the payout period {{< br >}} (e.g. `2021-01-01T12:00:00`) |
| end | Specify the end of the payout period {{< br >}} (e.g. `2021-02-01T12:00:00`) |
| financial_status | `completed` |

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?end=2021-02-01T12%3A00%3A00&start=2021-01-01T12%3A00%3A00&financial_status=completed" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

{{< br >}}

### Perform reconciliation

_I want to match mutations to justify the balance in my accounting or bookkeeping records_

* Reconciliation may be required by law
* Automating the reconciliation process can save time and reduce errors

| Parameter  | Required value |
|------------------|-----------------------|
| type | Retrieve all transaction types by not specifying a value. Alternatively, retrieve only specified transaction types like `payment` or `refund`. |
| financial_status           |  `completed` |

Use parameters `end` and `start` to specify a range of dates.

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=payment&financial_status=completed" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

{{< br >}}

### Create a refund overview

_I want to see the refunds associated with customer returns_

* View the orders that are to be paid back as a merchant
* Use the overview to pay back outstanding amounts for returned orders

| Parameter | Required value |
|------------------|-----------------------|
| type (transaction type) | `refund` |

Use parameters `end` and `start` to specify a range of dates.

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=refund" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

{{< br >}}

## Support

If you have any issues or questions, [contact our Integration Team](mailto:integration@multisafepay.com)