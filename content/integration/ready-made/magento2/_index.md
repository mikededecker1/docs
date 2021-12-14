---
title: "MultiSafepay plugin for Magento 2"
breadcrumb_title: "Magento 2"
github_url : "https://github.com/MultiSafepay/Magento2"
changelog_url : "."
faq: "."
type: 'Plugin'
layout: 'single-old-button'
meta_title: "Magento 2 plugin - MultiSafepay Docs"		
meta_description: "Free plugin to integrate MultiSafepay payment solutions into your Magento 2 webshop."
changelog: https://github.com/MultiSafepay/magento2/blob/master/CHANGELOG.md
weight: 01
logo: "/logo/Plugins/Magento_2.svg"
title_short: "Magento 2"
url: '/magento-2/'
aliases: 
    - /plugins/magento2
    - /integrations/plugins/magento2
    - /integrations/magento2
    - /support-tab/magento2/manual
    - /plugins/magento2/manual
    - /integrations/plugins/magento2/manual
    - /integrations/magento2/manual
    - /integrations/ecommerce-integrations/magento2
    - /integrations/plugins/magento2/beta
    - /integrations/ecommerce-integrations/magento2
    - /payments/integrations/ecommerce-platforms/magento2/
    - /ecommerce-platforms/magento-2/
---

This technical manual is for installing and configuring our new free plugin for integrating MultiSafepay payment solutions into your Magento 2 webshop.

{{< alert-notice>}} If you are still using the [deprecated plugin](https://github.com/MultiSafepay/Magento2Msp), we recommend migrating to this new version as soon as possible. {{< /alert-notice >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Magento Open Source version 2.3.x & 2.4.x **or** Adobe Commerce version 2.3.x & 2.4.x (For GraphQL, only Magento Open Source versions 2.4.x are supported)
- PHP 7.1+

{{< /details >}}

{{< details title="Features" >}}

The new plugin features code improvements, and unit and integration testing. It is built on top of the Magento payment provider gateway structure. Some payment methods now skip the MultiSafepay payment page, which increases [conversion](/getting-started/glossary/#conversion-rate).

We support most Magento functionalities. For any questions, email the Integration Team at <integration@multisafepay.com>

### New features

- Improved:
    - Magento [backend](/getting-started/glossary/#backend) configuration
    - Translations
    - Error handling
    - Event and error logs
- Support information available in the Magento backend
- Clear explanation of each payment method with links to docs
- Modular setup, providing more installation flexibility
- PWA (GraphQL) endpoints

As of version 2.4.0, we also support [Magento Vault](https://devdocs.magento.com/guides/v2.4/payments-integrations/vault/vault-intro.html) and [Instant Purchase](https://docs.magento.com/user-guide/sales/checkout-instant-purchase.html). For more information, see MultiSafepay Blog - [Magento 2: Boost conversion through Magento Vault & Instant Purchase](https://www.multisafepay.com/blog/magento-2-boost-conversion-through-magento-vault-instant-purchase). 

These features are based on [recurring payments](/features/recurring-payments/).

### Obsolete features
Features that are no longer available:

- Recurring payments – replaced by Magento Vault and Instant Purchase
- FastCheckout – no longer supported
- PWA (REST) endpoints – replaced by GraphQL endpoints

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- [Magento Slack channel](https://magentocommeng.slack.com) #multisafepay-payments

Our plugin is supported by a certified Magento 2 Solution Specialist and receives regular updates for the latest features from Magento and MultiSafepay.

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payment-methods/american-express)
- [Maestro](/payment-methods/maestro)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
- [TrustPay](/payment-methods/trustpay) 

**Pay later methods**

- [AfterPay](/payments/methods/billing-suite/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payments/methods/wallet/applepay)
- [Google Pay](/payment-methods/google-pay)
- [PayPal](/payment-methods/paypal)
- [WeChat Pay](/payment-methods/wechat-pay)

**Prepaid cards**

- Baby gift card
- Beauty and Wellness gift card
- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Edenred](/payment-methods/edenred)
- [Fashioncheque](https://www.fashioncheque.com/nl/)
- [Fashion gift card](https://www.fashion-giftcard.nl/)
- Fietsenbon
- [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome/)
- [Givacard](https://www.givacard.nl/)
- [Good4fun](https://www.good4fun.nl/)
- Goodcard
- [Nationale tuinbon](https://www.nationale-tuinbon.nl/)
- [Paysafecard](/payment-methods/paysafecard)
- [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl/)
- [Podium](https://www.podiumcadeaukaart.nl/)
- [Sport en Fit](https://www.sportenfitcadeau.nl/)
- [VVV gift card](https://www.vvvcadeaukaarten.nl/)
- [Webshop gift card](https://www.webshopgiftcard.nl/)
- [Wellness gift card](https://www.wellnessgiftcard.nl/)
- Wijncadeau
- [Winkelcheque](https://www.winkelcheque.nl/)
- [Yourgift](https://www.yourgift.nl)

{{< /details >}}

## Modules

{{< details title="View modules" >}}
The plugin consists of several Magento modules:

| Module  | Description  |
|---|---|
| [Multisafepay-magento2-core](https://github.com/MultiSafepay/magento2-core)   | Provides core functionalities  |
| [Multisafepay-magento2-frontend](https://github.com/MultiSafepay/magento2-frontend)  | Enables payment gateways in the Magento checkout  |
| [Multisafepay-magento2-adminhtml](https://github.com/MultiSafepay/magento2-adminhtml)  | Enables/disables payment gateways, and changes settings in the Magento backend  |
| [Multisafepay-magento2-msi](https://github.com/MultiSafepay/magento2-msi)  | Handles stock when MSI is enabled  |
| [Multisafepay-magento2-catalog-inventory](https://github.com/MultiSafepay/magento2-catalog-inventory)  | Handles stock when MSI is disabled  |
| [Multisafepay-magento2](https://github.com/MultiSafepay/magento2)  | Meta package that installs all the above  |
| [Multisafepay-magento2-graphql](https://github.com/MultiSafepay/magento2-graphql)| For GraphQL support, extends and adds GraphQL queries and mutations |

{{< /details >}}

{{< details title="View module dependencies" >}}

The meta-package has a dependency on MSI. This means the MSI modules must be available (but not necessarily enabled) in your store. 

If you have removed MSI (e.g. with a composer-replace trick like [yireo/magento2-replace-inventory](https://github.com/yireo/magento2-replace-inventory)), you can't install the meta-package. To integrate with MultiSafepay, instead of installing the meta-package, install the magento2-frontend module and the magento2-catalog-inventory module.

The magento2-frontend module has a dependency on the magento2-core and magento2-adminhtml modules, so they are all installed together. In some cases, you also then need a stock-handling module. Since MSI is not available, you can install the magento2-catalog-inventory module instead.

The installation process is the same for the Adobe Commerce version.

{{< /details >}}

## Installation

**Note:** Make sure you finish processing all orders created in the deprecated plugin **before** you [delete it](/magento-2/deleting-deprecated-plugin/). Meanwhile, it can run in parallel with the new plugin. 

**1.** We recommend installing the meta-package using Composer:

``` 
composer require multisafepay/magento2
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

**2.** To enable all the modules, use the following command in the Magento 2 root directory:
```
./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
```

### Stock handling

When you disable MSI in Magento 2, you must also disable the MultiSafepay MSI module using the following command:
```
php bin/magento module:disable MultiSafepay_ConnectMSI
```
If you have enabled MSI in Magento 2, to disable the MultiSafepay CatalogInventory module, use the following command:
```
php bin/magento module:disable MultiSafepay_ConnectCatalogInventory
```

## Configuration
Sign in to your Magento 2 backend, and go to **Stores** > **Configuration** > **MultiSafepay**. This section contains the following pages:

- **General information:** Contains all the main support information. We recommend reading this first.
- **General settings:** Contains all main settings.  
  - Here you can configure all gateways and gift cards.  
  - For finding your account ID, site ID, site secure code, or [API key](/getting-started/glossary/#api-key), see [Get your API key](/tools/multisafepay-control/get-your-api-key).   
  - Your account ID appears in the top-right corner of your MultiSafepay account.
- **Payment methods:** Contains the configuration options for all MultiSafepay payment methods.  
    - Make sure you have activated your selected payment methods in your [MultiSafepay account](https://merchant.multisafepay.com).
- **Gift cards:** Contains the configuration options for all gift cards supported by MultiSafepay.  
    - Make sure you have activated your selected gift cards in your [MultiSafepay account](https://merchant.multisafepay.com).  
    - For more information, see [Gift cards](/payments/methods/prepaid-cards/gift-cards).
  
{{< blue-notice >}}MultiSafepay is an official partner of [OneStepCheckout.com](/payments/integrations/ecommerce-platforms/magento2/faq/supported-magento2-checkouts/). {{< /blue-notice >}}