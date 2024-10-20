# mysqld-integration-test
![](https://img.shields.io/pypi/v/mysqld-integration-test.svg) ![](https://img.shields.io/badge/status-alpha-red) ![](https://github.com/jasondcamp/mysqld-integration-test/actions/workflows/mysqld-integration-test.yml/badge.svg)  ![](https://img.shields.io/pypi/pyversions/mysqld-integration-test.svg) ![](https://img.shields.io/badge/license-Apache-lightgrey)

![](https://api.codeclimate.com/v1/badges/e5505727f2fa988debcb/maintainability) ![](https://api.codeclimate.com/v1/badges/e5505727f2fa988debcb/test_coverage)

## Overview
mysqld-integration-test is a python module that creates a temporary mysqld instance to use for testing your application. It is based on the `testing.mysqld` module which has not been updated recently. You will need a working MySQL or MariaDB install. It does not have to be running, the binaries are needed.

## Download and Install
To install use pip:

    $ pip install mysqld-integration-test

Or clone the repo:

    $ git clone https://github.com/jasondcamp/mysqld-integration-test.git

## Configuration
### Class arguments
The following class arguments can be overridden by passing them in, these arguments will override the config file arguments.
| Argument | Description | Default |
| --------------- | -------------- | -------------- |
|username|Username for database|root|
|password|Password for database|root|
|host|Host to bind|127.0.0.1|
|port|Port to bind|random|
|mysql_install_db_binary|Location of mysql_install_db|Searches paths|
|mysqld_binary|Location of mysqld|Searches paths|
|timeout_start|Timeout to start MySQL|30 seconds|
|timeout_stop|Timeout to stop MySQL|30 seconds|
|log_level|Log level|INFO|
|config_file|Configuration file|mysqld-integration-test.cfg|

### mysqld-integration-test config file
Default settings can be overridden in  a config file. The default name is `mysqld-integration-test.cfg` in the local directory and can be overridden by passing in the `config` option to the instance creation.

#### Example config
```
database:
  host: '127.0.0.1'
  port: '9999'
  username: 'root'
  password: 'test'
  mysql_install_db_binary: '/usr/local/bin/mysql_install_db'
  mysqld_binary: '/usr/sbin/mysqld'

general:
  log_level: 'DEBUG'
  timeout_start: 30
  timeout_stop: 30
```


## Usage

#### import

```
from mysqld_integration_test import Mysqld
```

#### run
Starts up the mysql server

```
mysqld = Mysqld()
instance = mysqld.run()
```

#### stop
Stops the mysql server
```
mysqld.stop()
```

### Example Code

```
#!/usr/bin/env python3

from mysqld_integration_test import Mysqld
import mysql.connector

mysqld = Mysqld(config='/some/dir/mysqld-integration-test.cfg')
instance = mysqld.run()

# Make query to database
cnx = mysql.connector.connect(user=instance.username, password=instance.password,
                      host=instance.host, port=instance.port)
cursor = cnx.cursor()
cursor.execute(f"SHOW databases;")

for db in cursor:
   print(db[0])

cursor.close()
cnx.close()

mysqld.stop()
```



