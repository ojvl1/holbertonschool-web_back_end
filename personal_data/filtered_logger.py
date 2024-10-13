#!/usr/bin/env python3
"""Function that returns the log message obfuscated"""
"""
fields: a list of strings representing all fields to obfuscate
---------------------------------------------------------------------
redaction: a string representing by what the field will be obfuscated
---------------------------------------------------------------------
message: a string representing the log line
---------------------------------------------------------------------
separator: a string representing by which character is separating all
fields in the log line
"""

import re

def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(
        pattern, lambda m: m.group(0).split('=')[0] + f'={redaction}', message)
