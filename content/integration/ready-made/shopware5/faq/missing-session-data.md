---
title : "Missing session data"
meta_title: "Shopware 5 plugin - Missing session data - MultiSafepay Docs"

layout: "faqdetail"
read_more: "."
url: '/shopware/session-data/'
aliases:
    - /payments/integrations/ecommerce-platforms/shopware5/faq/missing-session-data/
---

It can happen that Shopware 5 will remove sessions before the order is created within the Shopware backend.
To prevent this from happening we recommend making the following changes to the [config.php](https://developers.shopware.com/developers-guide/shopware-config/).

```
'session' => [
    'save_handler' => 'db',
    'gc_probability' => 0,
    'gc_divisor' => 1000
],
```

This is also explained on the following page:
https://developers.shopware.com/sysadmins-guide/sessions/#blocking-transactions