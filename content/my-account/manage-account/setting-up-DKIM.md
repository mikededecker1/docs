---
title: "Setting up DKIM email authentication"
weight: 12
meta_title: "Setting up DKIM email authentication - MultiSafepay Docs"
read_more: "."
url: '/my-account/setting-up-dkim/'
---

MultiSafepay supports DomainKeys Identified Mail (DKIM) email authentication for all emails that we send. DKIM lets email servers verify that received emails actually came from the specified domain and haven't been altered or forged.

## Adding TXT records
To set up DKIM you need to add a TXT record for MultiSafepay through your hosting provider, domain registrar, or DNS provider.

### MultiSafepay email servers
1. Add a TXT record named: `msp-2021._domainkey.{your domain}`, e.g. `msp-2021._domainkey.example.com`.

2. Add the following content to your TXT record:
    ```
    v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4pizvsOWTWxtcxthGR0k4rEcGsJH4hRy1fpoUAs3fUi0yMkygwsYUCtFLQY2TwrOtfPfaZ/2bPKXwyjC4kg93zFvSJTIQtQiFfKNT2aDtnDmZRwII4+s2k7+LHn4V/SjIxEBylN3Rt0g4iVlkZzgncEXeVksXj5eux8uDAUeZxj0Fp8PWSkxsBNVaJFb5sfR+c5piJ+8RmlqYUf7w/gXOW8mChC509//V9dfMaV39b7WoEf/JRw9KGM69C3hIdtb7cVKD/B6VxQIq3z1DCAcmSCXpcaXUaFbVaF4u/vEi+3v5DdPtDl/0rOy2NUFNL5XULW8OxdofzUbdL9SWN/IbwIDAQAB;
    ```
You have successfully added a TXT record for MultiSafepay's email servers.

### Mandrill

If you have [E-Invoicing](/payment-methods/e-invoicing/) or [Pay After Delivery](/payment-methods/pay-after-delivery/) activated, we also use Mandrill to send emails in addition to our own mail servers. In this case, you need to add another TXT record for Mandrill.

1. Add a TXT record named: `mandrill._domainkey.{your domain}`, e.g. `mandrill._domainkey.example.com`.

2. Add the following content to your TXT record:
    ```
    v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrLHiExVd55zd/IQ/J/mRwSRMAocV/hMB3jXwaHH36d9NaVynQFYV8NaWi69c1veUtRzGt7yAioXqLj7Z4TeEUoOLgrKsn8YnckGs9i3B3tVFB+Ch/4mPhXWiNfNdynHWBcPcbJ8kjEQ2U8y78dHZj1YeRXXVvWob2OaKynO8/lQIDAQAB;
    ```
You have successfully added a TXT record for Mandrill.

## See also
[Adding SPF records for MultiSafepay emails](/my-account/adding-spf-records/)




