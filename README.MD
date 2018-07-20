# EmulatorFrontier

A prototyped Brave Frontier Web Server written in Python 2.7

### Requirements
 - PyCrypto (pip install pycrypto)

### Status
 [x] Handle HTTP Requests with Headers and PHP '?' Arguments
 [x] Bind an Asyncrous Server
 [ ] Configuration (Hard coded now)
 [ ] Login
 [x] Terms
 [x] Background
 
### How to use (Global Version 1.10.30.0)
 Extract libgame.so, change '68 74 74 70 73 3A 2F 2F' (01626430, 01633EC0, 0164D690) to '68 74 74 70 3A 2F 2F 00'.
 
 Then, on 01634C60 change
 '68 74 74 70 73 3A 2F 2F 61 70 69 2E 6C 69 76 65 2E 67 75 6F 69 2E 73 67 2F'
 to
 '68 74 74 70 3A 2F 2F 61 70 69 2E 6C 69 76 65 2E 67 75 6D 69 2E 73 67 2F 00'
 
 Create a DNS Server and redirect '*.bravefrontier.gumi.sg' and '*.live.gumi.sg' into this Server
 
### How to shutdown
 ATTENTION: You can only do this on localhost
 
 Go to '127.0.0.1/shutdown_server' and the server will be shutting down

### Special Thanks:
 - [https://github.com/bsuh/bfdb](bfdb) for AES, PKCS5 and base64 algorithm and parts of the encrypted bf names

