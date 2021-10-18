---
title : "Integrating a single payment method"
breadcrumb_title : "Step 2"
meta_title: "Payment Components - Integrating a single payment method step 2 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
url: '/payment-components/single/step-2/'
--- 

## Step 2: Initialize the component

### Generate an API token
Payment Components require a MultiSafepay API token. See API reference&nbsp;–&nbsp;[Generate an API token](/api/#generate-an-api-token).

{{< alert-notice >}} **Note:** To keep your API key private, request the token from your own server. {{< /alert-notice >}} 

### Construct the component object

**1.** Initialize an `orderData` object, containing information about the customer's order collected during the checkout process:

```
const orderData = {
    currency: 'EUR',
    amount: 10000,
    customer: {
        locale: 'en',
        country: 'NL',
        reference: 'Customer123'
    },
    template : {
        settings: {
            embed_mode: true
        }
    }
};
```

{{< details title="View properties" >}}

| Key | Value |
| ---- | ---- |
| currency| The currency of the order. Format: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. **Required**. |
| amount| The value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**. |
| customer.country| The customer's country code. Checks the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Optional**. |
|customer.locale | The customer's language. Sets the language of the Payment Component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
| customer.reference| Your unique customer reference. **Required for recurring payments**. |
| recurring.model| The [tokenization model](/payments/features/tokenization/). **Required for recurring payments**. |
| template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |

{{< /details >}}

{{< details title="Processing recurring payments" >}}

[Recurring payments](/payments/features/tokenization/) let you store a customer’s payment details as a secure, encrypted token.

Upon subsequent payments, customers can select their stored payment details and pay with a single click.

To process recurring payments in your Payment Component:

- Add the `cardOnFile` recurring model
- Provide the relevant `customer.reference`

```
const orderData = {
    currency: 'EUR',
    amount: 10000,
    customer: {
        locale: 'en',
        country: 'NL',
        reference: 'Customer123'
    },
    recurring: {
        model: 'cardOnFile'
    }
};
```

Recurring payments are supported for all credit card payments.

To use recurring payments in your Payment Component, you need to enable recurring payments for your account. If you haven't already, email your account manager at <sales@multisafepay.com>

{{< /details >}}

**Note:** We use the `orderData` object to ensure the payment method is enabled and the currency, country, and transaction amount are supported. 

**2.** Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

```
PaymentComponent = new MultiSafepay({
    env: 'test',
    apiToken: apiToken,
    order: orderData
});
```

### Initialize the component

**1.** Call the `PaymentComponent.init()` method with the following arguments:

```
PaymentComponent.init('payment', {
    container: '#MultiSafepayPayment',
    gateway: '<GATEWAY>',
    onLoad: state => {
        console.log('onLoad', state);
    },
    onError: state => {
        console.log('onError', state);
    }
});
```
**2.** Replace the `<GATEWAY>` placeholder with the relevant payment gateway code.
{{< details title="View gateway codes" >}}

| Payment method| Gateway code|
|---|---|
| Bank transfer | `BANKTRANS` |
| Bancontact | `MISTERCASH` |
| Credit cards |`CREDITCARD`|
| iDEAL|`IDEAL`|
| PayPal | `PAYPAL` |
| SEPA Direct Debit | `DIRDEB` |
| Sofort | `DIRECTBANK`|

{{< /details >}}

**3.** Create event handlers for the following events:

{{< details title="View events" >}}

| Event | Event handler |
| ---- | ---- |
|`onError`| Called when an error occurs in the Payment Component|
|`onLoad`| Called when the Payment Component UI is rendered |
|`onSelect`| Occurs when the customer selects an issuer with iDEAL. |
|`onSubmit`| Occurs when the customer clicks the payment button (when using the button generated by the component). |
|`onValidation`| Occurs when form validation changes. Can be used to disable the payment button until all fields are validated. |

{{< /details >}}

**Note:** The `PaymentComponent` uses the following methods:

{{< details title="View methods" >}}

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error details, e.g. error messages or codes|
|`hasErrors`| Returns a boolean value depending on whether errors have been registered |
|`getPaymentData`| Returns a `payment_data` object with a `payload` containing the customer's payment details, used to [create orders](/payment-components/single/step-3/), and the `gateway`.|
|`getOrderData`| Returns an object containing a `payment_data` object and the full order configuration. |

{{< /details >}}

{{< two-buttons

href-1="/payment-components/single" header-1="Back" text-1="Step 1: Add the elements" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payment-components/single/step-3" header-2="Next" text-2="Step 3: Create an order" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

