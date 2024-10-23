# <font color="#3498DB">Sanau Automation SDK</font>

This is **package for python** that you can install by:  
```pip install SanauAutomationSDK```

## <font color="#2874A6">Quick start</font>

```python
from SanauAutomationSDK import SanauAutomationSDK   # import the library

sasdk = SanauAutomationSDK(region, domain, access_key)  # create an object of class
sasdk.client.get_databases()
```

***SanauAutomationSDK*** simplifies work with the outsourcing API.  
Thanks to this library, you only have to write the functions you need without writing additional wrapper and logic. Everything is already written for you.

## <font color="#2874A6">Documentation</font>

**SanauAutomationSDK(region, domain, access_key)**  
- region - country in which outsourcing operates
- domain - domain of outsourcing
- access_key - access_key for outsourcing API

SanauAutomationSDK has several classes:
- **Api**
- **Client**
- **FileVault**
- **OGD**

And each of these classes has functions for working with APIs specific to them

> **<font color="#85C1E9">Api</font> class** provides work with APIs that are in no way related to specific outsourcing

| Method                              | Explanation                          |
|-------------------------------------|--------------------------------------|
| `get_currency_rates(currency_date)` | gets currency rates at specific date |
| ``get_domains()``                   | gets all sanau domains               |

> **<font color="#85C1E9">Client</font> class** provides work with APIs that are in no way related to specific outsourcing

| Method                                  | Explanation                                  |
|-----------------------------------------|----------------------------------------------|
| ``get_databases()``                     | gets all databases that outsourcing contains |
| ``get_db_employees(db_name)``           | gets employees of a specific database        |
| ``post_alerts(params)``                 | posts alerts                                 |
| ``post_taxation_organ(out_dict)``       | posts taxation organ                         |
| ``resole_alert(params)``                | deletes specific alert                       |
| ``resolve_all_alerts(entity_id, keys)`` | deletes all alerts of specific database      |

> **<font color="#85C1E9">FileVault</font> class** provides work with file vault

| Method               | Explanation                        |
|----------------------|------------------------------------|
| ``get_file(params)`` | gets specific file from file vault |

> **<font color="#85C1E9">OGD</font> class** provides work with OGD

| Method              | Explanation       |
|---------------------|-------------------|
| ``get_ogd_excel()`` | gets excel of ogd |
