#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import getpass
import json
import os
import sys
import uuid
import sys
import platform
import logging
from datetime import datetime, timedelta

from . import config

log = logging.getLogger(__name__)


def parse_unicode(bytestring):
    decoded_string = bytestring.decode(sys.getfilesystemencoding())
    return decoded_string


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', help='Set web server listening host', default='127.0.0.1')
    parser.add_argument('-P', '--port', type=int, help='Set web server listening port', default=5000)
    parser.add_argument('--db', help='Connection String to be used. (default: sqlite)',
                        default='sqlite')
    parser.add_argument('-d', '--debug', type=str.lower, help='Debug Level [info|debug]', default=None)
    parser.add_argument('-k', '--key', type=str.lower, help='Hash Key', default=None, required=True)
    parser.add_argument('-sd', '--delay', type=int, help='Delay in milliseconds between map requests', default=250)

    return parser.parse_args()


def get_pokemon_name(pokemon_id):
    return get_locale()[str(pokemon_id)]

def get_locale():
    if (not hasattr(get_locale, 'names')
            or config['LOCALE'] != get_locale.locale):
        get_locale.locale = config['LOCALE']
        file_path = os.path.join(
                config['ROOT_PATH'],
                config['LOCALES_DIR'],
                'pokemon.{}.json'.format(config['LOCALE']))
        with open(file_path, 'r') as f:
            get_locale.names = json.loads(f.read())

    return get_locale.names

def get_encryption_lib_path():
    # win32 doesn't mean necessarily 32 bits
    hash_lib = None
    arch = platform.architecture()[0]
    if sys.platform == "win32" or sys.platform == "cygwin":
        if arch == '64bit':
            encrypt_lib = "libpcrypt-windows-x86-64.dll"
            hash_lib = "libniahash-windows-x86-64.dll"
        else:
            encrypt_lib = "libpcrypt-windows-i686.dll"
            hash_lib = "libniahash-windows-i686.dll"
    elif sys.platform == "darwin":
        if arch == '64bit':
            encrypt_lib = "libpcrypt-macos-x86-64.dylib"
            hash_lib = "libniahash-macos-x86-64.dylib"
        else:
            encrypt_lib = "libpcrypt-macos-i386.dylib"
            hash_lib = "libniahash-macos-i386.dylib"
    elif os.uname()[4].startswith("arm") and arch == '32bit':
        encrypt_lib = "libpcrypt-linux-arm32.so"
        hash_lib = "libniahash-linux-arm32.so"
    elif os.uname()[4].startswith("aarch64") and arch == '64bit':
        encrypt_lib = "libpcrypt-linux-arm64.so"
        hash_lib = "libniahash-linux-arm64.so"
    elif sys.platform.startswith('linux'):
        if arch == '64bit':
            encrypt_lib = "libpcrypt-linux-x86-64.so"
            hash_lib = "libniahash-linux-x86-64.so"
        else:
            encrypt_lib = "libpcrypt-linux-i386.so"
            hash_lib = "libniahash-linux-i386.so"
    elif sys.platform.startswith('freebsd'):
        if arch == '64bit':
            encrypt_lib = "libpcrypt-freebsd-x86-64.so"
            hash_lib = "libniahash-freebsd-x86-64.so"
        else:
            encrypt_lib = "libpcrypt-freebsd-i386.so"
            hash_lib = "libniahash-freebsd-i386.so"
    else:
        err = "Unexpected/unsupported platform '{}'".format(sys.platform)
        log.error(err)
        raise Exception(err)
    encrypt_lib_path = os.path.join(os.path.dirname(__file__), "lib", encrypt_lib)
    hash_lib_path = os.path.join(os.path.dirname(__file__), "lib", hash_lib)
    if not os.path.isfile(encrypt_lib_path):
        err = "Could not find {} encryption library {}".format(sys.platform, encrypt_lib_path)
        log.error(err)
        raise Exception(err)
    if not os.path.isfile(hash_lib_path):
        err = "Could not find {} hashing library {}".format(sys.platform, hash_lib_path)
        log.error(err)
        raise Exception(err)
    return encrypt_lib_path


def get_hash_lib_path():
    # win32 doesn't mean necessarily 32 bits
    hash_lib = None
    arch = platform.architecture()[0]
    if sys.platform == "win32" or sys.platform == "cygwin":
        if arch == '64bit':
            encrypt_lib = "libpcrypt-windows-x86-64.dll"
            hash_lib = "libniahash-windows-x86-64.dll"
        else:
            encrypt_lib = "libpcrypt-windows-i686.dll"
            hash_lib = "libniahash-windows-i686.dll"
    elif sys.platform == "darwin":
        if arch == '64bit':
            encrypt_lib = "libpcrypt-macos-x86-64.dylib"
            hash_lib = "libniahash-macos-x86-64.dylib"
        else:
            encrypt_lib = "libpcrypt-macos-i386.dylib"
            hash_lib = "libniahash-macos-i386.dylib"
    elif os.uname()[4].startswith("arm") and arch == '32bit':
        encrypt_lib = "libpcrypt-linux-arm32.so"
        hash_lib = "libniahash-linux-arm32.so"
    elif os.uname()[4].startswith("aarch64") and arch == '64bit':
        encrypt_lib = "libpcrypt-linux-arm64.so"
        hash_lib = "libniahash-linux-arm64.so"
    elif sys.platform.startswith('linux'):
        if arch == '64bit':
            encrypt_lib = "libpcrypt-linux-x86-64.so"
            hash_lib = "libniahash-linux-x86-64.so"
        else:
            encrypt_lib = "libpcrypt-linux-i386.so"
            hash_lib = "libniahash-linux-i386.so"
    elif sys.platform.startswith('freebsd'):
        if arch == '64bit':
            encrypt_lib = "libpcrypt-freebsd-x86-64.so"
            hash_lib = "libniahash-freebsd-x86-64.so"
        else:
            encrypt_lib = "libpcrypt-freebsd-i386.so"
            hash_lib = "libniahash-freebsd-i386.so"
    else:
        err = "Unexpected/unsupported platform '{}'".format(sys.platform)
        log.error(err)
        raise Exception(err)
    encrypt_lib_path = os.path.join(os.path.dirname(__file__), "lib", encrypt_lib)
    hash_lib_path = os.path.join(os.path.dirname(__file__), "lib", hash_lib)
    if not os.path.isfile(encrypt_lib_path):
        err = "Could not find {} encryption library {}".format(sys.platform, encrypt_lib_path)
        log.error(err)
        raise Exception(err)
    if not os.path.isfile(hash_lib_path):
        err = "Could not find {} hashing library {}".format(sys.platform, hash_lib_path)
        log.error(err)
        raise Exception(err)
    return hash_lib_path