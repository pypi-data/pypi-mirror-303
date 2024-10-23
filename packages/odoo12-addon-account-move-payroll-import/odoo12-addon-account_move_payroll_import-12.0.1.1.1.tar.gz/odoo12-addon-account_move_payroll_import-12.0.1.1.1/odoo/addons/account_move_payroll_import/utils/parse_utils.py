# -*- coding: utf-8 -*-


def parse_float(value, thousands_sep=",", decimal_sep="."):
    """
    Parse a float value.
    :param thousands_sep: the thousands separator.
    :param decimal_sep: the decimal separator.
    :param value: the value to parse.
    :return: the parsed float value.
    """
    if type(value) in (int, float, bool):
        return float(value)

    value = str(value).strip()
    if not value:
        return 0.0

    value = value.replace(thousands_sep, "").replace(decimal_sep, ".")
    return float(value)


def abs_float(value, thousands_sep=",", decimal_sep="."):
    """
    Parse a float value and return its absolute value.
    :param thousands_sep: the thousands separator.
    :param decimal_sep: the decimal separator.
    :param value: the value to parse.
    :return: the absolute value of the parsed float value.
    """
    try:
        return abs(parse_float(value, thousands_sep, decimal_sep))
    except ValueError:
        raise ValueError("Invalid float value: %s" % value)
