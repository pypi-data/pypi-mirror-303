# print_pretty.py

import json


def print_pretty_json(data):
    """
    Function for pretty output of JSON data to console with correct line breaks.
    :param data: Dictionary or list to be converted to formatted JSON.
    """
    pretty_json = json.dumps(data, indent=2, ensure_ascii=False)
    pretty_json = pretty_json.replace('\\n', '\n')  # Replacing hyphenation symbols with real hyphens
    print(pretty_json)

