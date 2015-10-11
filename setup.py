from distutils.core import setup, Extension

module1 = Extension('ilssl._ssl',
    include_dirs = ['include','include/modules','/usr/local/ssl/include'],
    extra_objects = ['/usr/local/ssl/lib/libssl.a', '/usr/local/ssl/lib/libcrypto.a'],
    sources = ['src/_ssl.c'])

setup (name = 'ilssl',
    version = '1.0',
    description = 'Version of the standard ssl module statically linked to openssl with support for older protocols and cipher suites.',
    author = 'Ian Lovering',
    author_email = 'ian@bathouse.co.uk',
    url = 'https://github.com/ianlovering/python-ssl',
    packages = ['ilssl'],
    ext_modules = [module1])

