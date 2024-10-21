# Flat file authentication plugin for StackStorm Community edition

[![Build Status](https://api.travis-ci.org/StackStorm/st2-auth-backend-flat-file.svg?branch=master)](https://travis-ci.org/StackStorm/st2-auth-backend-flat-file) [![IRC](https://img.shields.io/irc/%23stackstorm.png)](http://webchat.freenode.net/?channels=stackstorm)

Flat file backend supports reading credentials from an Apache HTTPd htpasswd formatted file. To
manage this file you can use [htpasswd](https://httpd.apache.org/docs/2.2/programs/htpasswd.html)
utility which comes with a standard Apache httpd distribution or by installing apache2-utils
package on Ubuntu / Debian.

### Configuration Options

| option    | required | default | description                                                |
|-----------|----------|---------|------------------------------------------------------------|
| file_path | yes      |         | Path to the file containing credentials                    |

### Configuration Example

Please refer to the authentication section in the StackStorm
[documentation](http://docs.stackstorm.com) for basic setup concept. The
following is an example of the auth section in the StackStorm configuration file for the flat-file
backend.

```ini
[auth]
mode = standalone
backend = flat_file
backend_kwargs = {"file_path": "/path/to/.htpasswd"}
enable = True
use_ssl = True
cert = /path/to/ssl/cert/file
key = /path/to/ssl/key/file
logging = /path/to/st2auth.logging.conf
api_url = https://myhost.example.com:9101
debug = False
```

The following is an sample htpasswd command to generate a password file with a user entry.

```
htpasswd -cs /path/to/.htpasswd stark
```

## Copyright, License, and Contributors Agreement

Copyright 2015 StackStorm, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in
compliance with the License. You may obtain a copy of the License in the [LICENSE](LICENSE) file,
or at: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

By contributing you agree that these contributions are your own (or approved by your employer) and
you grant a full, complete, irrevocable copyright license to all users and developers of the
project, present and future, pursuant to the license of the project.
