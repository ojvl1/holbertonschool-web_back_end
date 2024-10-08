#!/usr/bin/env python3
"""Function that returns the log message obfuscated"""


import re


def filter_datum(fields, redaction, message, separator):
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

    return re.sub(rf'({"|".join(fields)})=[^{separator}]*', lambda m: f"{m.group().split('=')[0]}={redaction}", message)
    