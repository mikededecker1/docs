---
title : "Automated Accountant Export"
weight: 61
meta_title: "Automated Accountant Export - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---

## Accountant Export
An Accountant Export containing all successful incoming and outgoing transactions, as well as corresponding costs (where applicable), can be generated to serve your bookkeeping needs. 

## Sending an Automated Accountant Export
As a MultiSafepay client, you can benefit from three ways of accessing/receiving the automated accountant export:

1. Via SFTP - Pull request _(With this method you will receive access to an SFTP server from MultiSafepay)_
2. Via SFTP - Push request _(With this method MultiSafepay would like to receive access to an SFTP server from you)_.
3. Transaction API using the [transactions API endpoint](/tools/transactions-api-endpoint/) (_The associated transaction costs are not included in the returned data_) 

We support SFTP by username/password and username/SSH keys.

_We only support port 22 & 2222 for SFTP connections_


## Requirements

__SFTP - Push Request: For SFTP reporting the following protocol is required:__

sh-ed25519,
rsa-sha2-512,
rsa-sha2-256,
ecdsa-sha2-nistp521,
ecdsa-sha2-nistp384,
ecdsa-sha2-nistp256,
ssh-rsa

This must be supported on the SFTP server otherwise a report cannot be delivered.

## Frequency
MultiSafepay can send the Automated Accountant Export daily, weekly or monthly.  You have the option of choosing the frequency and time. Our reference time is Central Eastern Summer Time (CEST).

## Accountant Export format
The following formats are available for automatically generating an export:

* CAMT053
* CODA
* CSV
* MT940
* XLS
* XLSX

For information regarding the different exports, check out our [export page](https://docs.multisafepay.com/tools/reports/accountant-report-export)   

## How to request an Automated Accountant Export

Automated Accountant Export activation checklist:

* Choice of email, SFTP push or SFTP pull            
* Frequency - daily, weekly or monthly
* Desired file format: CAMT053, CODA, CSV, MT940, XLS or XLSX
* Desired time (_Please note our reference time is CEST_).
* Costs breakdown per transaction OR total costs 


Email the requested documents to the Integration Team at <integration@multisafepay.com> 

_Don't forget to add your Account ID which can be found in the dashboard of your MultiSafepay Control in the top right corner_.



## Whitelisting

If your method of choice is via SFTP, please make sure our IP is whitelisted. For more information, please refer to our [IP ranges documentation](/faq/general/ip-ranges)

## Testing

It is possible to export accountant reports in the test mode of the [MultiSafepay Control](https://testmerchant.multisafepay.com)

Exporting Klarna Payments reports is also included within this test mode.