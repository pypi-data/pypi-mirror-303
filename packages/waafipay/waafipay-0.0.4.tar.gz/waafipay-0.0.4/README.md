# WaafiPay Python Client

<img src="https://merchant.waafipay.com/assets/images/waafipay-tab.png" alt="WaafiPay Logo" width="200"/>

## Overview

The **WaafiPay Python Client** is a simple and intuitive library for integrating with the WaafiPay payment gateway. It allows you to perform various payment operations such as preauthorizing payments, committing transactions, and canceling preauthorizations, all while managing your API requests seamlessly.

## Features

- **Preauthorize Payments**: Easily initiate payment preauthorizations with just a few lines of code.
- **Commit Transactions**: Securely commit preauthorized payments to finalize transactions.
- **Cancel Preauthorizations**: Cancel any pending preauthorizations quickly and efficiently.
- **Easy to Use**: Designed with simplicity in mind, making integration straightforward.
- **Secure**: Handles sensitive payment information with care.

## Installation

You can install the WaafiPay package via pip:

```bash
pip install waafipay
```

## Usage

### 1. Import the Client

First, import the `WaafiPayClient` class from the package:

```python
from waafipay import WaafiPayClient
```

### 2. Initialize the Client

```python
client = WaafiPayClient(
    merchant_uid="XXXXXXX",  # Your merchant UID
    api_user_id="XXXXXX",     # Your API user ID
    api_key="API-XXXXXXXX"  # Your API key
)


