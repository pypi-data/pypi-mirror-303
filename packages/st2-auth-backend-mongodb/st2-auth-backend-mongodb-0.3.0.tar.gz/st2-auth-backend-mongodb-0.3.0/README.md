# MongoDB authentication plugin for StackStorm Community edition

[![Build Status](https://api.travis-ci.org/StackStorm/st2-auth-backend-mongodb.svg?branch=master)](https://travis-ci.org/StackStorm/st2-auth-backend-mongodb) [![IRC](https://img.shields.io/irc/%23stackstorm.png)](http://webchat.freenode.net/?channels=stackstorm)

The MongoDB backend reads and authenticates user against data from a MongoDB collection named 
``users``. The ``users`` collection and the user entries  will have to be generated manually.
Entries need to have the following attributes:

| field    | description                                                  |
| ---------|--------------------------------------------------------------|
| username | User name                                                    |
| salt     | Password salt                                                |
| password | SHA256 hash for the salt+password - SHA256(salt+password)    |

### Configuration Options

| option      | required | default   | description                                              |
|-------------|----------|-----------|----------------------------------------------------------|
| db_host     | no       | localhost | Hostname for the MongoDB server                          |
| db_port     | no       | 27017     | Port for the MongoDB server                              |
| db_name     | no       | st2auth   | Database name in MongoDB                                 |
| db_username | no       | None      | Username for MongoDB login                               |
| db_password | no       | None      | Password for MongoDB login                               |

### Configuration Example

Please refer to the authentication section in the StackStorm
[documentation](http://docs.stackstorm.com) for basic setup concept. The
following is an example of the auth section in the StackStorm configuration file for the flat-file
backend.

```
[auth]
mode = standalone
backend = mongodb
backend_kwargs = {"db_username": "admin", "db_password": "pass123"}
enable = True
use_ssl = True
cert = /path/to/ssl/cert/file
key = /path/to/ssl/key/file
logging = /path/to/st2auth.logging.conf
api_url = https://myhost.example.com:9101
debug = False
```

## Copyright, License, and Contributors Agreement

Copyright 2015 StackStorm, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in
compliance with the License. You may obtain a copy of the License in the [LICENSE](LICENSE) file,
or at: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

By contributing you agree that these contributions are your own (or approved by your employer) and 
you grant a full, complete, irrevocable copyright license to all users and developers of the
project, present and future, pursuant to the license of the project.
