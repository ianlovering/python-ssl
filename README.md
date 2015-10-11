# python-ssl
Copy of the python ssl module to be statically linked with openssl to allow the use of older insecure protocols and cipher suites.

To use download a binary distribution (as it contains the binary module statically linked to openssl) and unpack to the root of the filesystem.

The modules will be installed to /usr/local/lib/python2.7/dist-packages/ilssl.

Do 'import ilssl.ssl as ssl' and use the same way as the built in python ssl module.
