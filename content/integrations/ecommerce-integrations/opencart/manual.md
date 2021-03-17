---
title : "MultiSafepay OpenCart installation & configuration manual"
meta_title: "OpenCart plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases:
    - /support-tab/opencart/manual
    - /plugins/opencart/manual
    - /integrations/plugins/opencart/manual
    - /integrations/opencart/manual
---

### Introduction

{{% introduction_plugin "OpenCart" %}}

### 1. Requirements
- OpenCart 2.X, 3.X
- Tested on PHP 7.2, 7.3

### 2. Installation
1. For security, always create backup of your OpenCart application.
2. Download the Plugin_OpenCart_3.x.x.ocmod.zip.
3. Log in to your backend and navigate to _Extensions_ → _Installer_.
4. Click on the upload button and select in your computer the downloaded file.
5. Wait until the installation process finish. 
6. Click in the menu item Dashboard.
7. On the upper right corner of the screen, click on the blue button with a cog wheel icon, and then click on the refresh icon to clean both caches. 
8. Go to _Extensions_ → _Modifications_ and click on refresh button.
9. Go to _Extensions_ → _Payments_ → _MultiSafepay_ and click in the button with the install icon.
10. You just installed the plugin. Now you need to configure the settings. 

### 3. Configuration
1. Log in to your backend and navigate to _Extensions_ → _Extensions_ → _Payments_→ _MultiSafepay_.
2. On the MultiSafepay configuration page, enter the required information presented on each tab. 
3. You can find your API Key on our [API key page](/tools/multisafepay-control/get-your-api-key)
4. Enable and configure the desired payment methods you wish to offer in _Payment Methods_ tab.
5. Configure the _Order Status_ tab, matching each possible MultiSafepay callback status with one of the order statuses previously setup on your OpenCart webshop.
6. Configure the _Options_ tab. 

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

### 5. Updates
#### Update the plugin from plugin version higher or equals than 2.2.0 to 3.x.x
1. For security, always create backup of your OpenCart application.
2. Download the Plugin_OpenCart_3.x.x.ocmod.zip.
3. Before you update the plugin, we strongly recommend have a backup of your production environment
4. Log in to your backend and navigate to _Extensions_ → _Installer_.
5. Click on the upload button and select in your computer the downloaded file.
6. Wait until the installation process finish. 
7. Click in the menu item _Dashboard_.
8. On the upper right corner of the screen, click on the blue button with a cog wheel icon, and then click on the refresh icon to clean both caches. 
9. Go to _Extensions_ → _Modifications_ and click on refresh button.
10. Go to _Extensions_ → _Payments_ → _MultiSafepay_ and click in the edit button to access the settings page.
11. You will see a warning notification message, indicating is needed to make some maintenance tasks to delete old plugin files. 
12. Go to _Maintenance_ tab and at the end of the list; click on the button to delete old plugin files. 
13. You just update the plugin. Now you need to configure the settings. 


#### Update the plugin from plugin version lower or equals than 2.1.0 to 3.x.x
1. For security, create backup of your OpenCart platform. Especially if you are doing this in a production environment.
2. Manually remove all the files from the MultiSafepay extension using an FTP program or server file administration program.
3. Follow the instruction to install our latest extension using the extension installer tool built in OpenCart.
