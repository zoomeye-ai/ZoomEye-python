#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
* Filename: tools.py
* Description:
* Time: 2025.12.05
*/
"""
import hashlib

from zoomeyeai import config


def md5_convert(string):
    """
    calculate the md5 of a string
    :param string: input string
    :return: md5 string
    """
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def convert_str(s):
    """
    convert arbitrary string to another string, for print and human readable
    :param:
    :return:
    """
    res = []
    d = {
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '\b': '\\b',
        '\a': '\\a',
    }
    for c in s:
        if c in d.keys():
            res.append(d[c])
        else:
            res.append(c)
    return ''.join(res)

def omit_str(text, index=0):
    """
    ignore part of the string
    :param text: str, text to be omitted
    :param index: int, position omitted on the longest basis
    :return: str, ex: string...
    """
    if len(text) < config.STRING_MAX_LENGTH:
        return text

    return text[:config.STRING_MAX_LENGTH - index] + '...'
