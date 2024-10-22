import importlib
import json
import operator
import random
import string
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from functools import reduce
from itertools import zip_longest


def get_random_string(length):
    letters = string.ascii_lowercase
    result = "".join(random.choice(letters) for _ in range(length))

    return result


def datetime_to_utc(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def get_utc_datetime(offset_seconds=0):
    timestamp = datetime.utcnow() + timedelta(0, offset_seconds)
    formatted = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    return formatted


def urljoin(*fragments, leading_slash=False, trailing_slash=False):
    cleaned = (fragment.strip("/") for fragment in fragments if fragment)
    joined = "/".join(cleaned)

    if leading_slash:
        joined = "/" + joined

    if trailing_slash:
        joined = joined + "/"

    return joined


def import_path_as_module(path, module_name):
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)

    with open(path, "r") as file:
        code = file.read()

    exec(code, module.__dict__)

    sys.modules[module_name] = module

    return module


def grouper(iterable, num_chunks, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks

    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    """

    args = [iter(iterable)] * num_chunks

    return zip_longest(*args, fillvalue=fillvalue)


def make_nested():
    return defaultdict(make_nested)


def get_nested(dictionary, keys):
    return reduce(operator.getitem, keys, dictionary)


def set_nested(dictionary, keys, value):
    target_key = keys[-1]

    parent = get_nested(dictionary, keys[:-1])
    target = parent[target_key]

    if isinstance(target, dict):
        target.update(value)
    else:
        parent[target_key] = make_nested()
        parent[target_key].update(**{target_key: target}, **value)


def organize_cloud_data_list(cloud_data_list, path_root):
    result = make_nested()

    for cloud_data in cloud_data_list:
        keys = [key for key in cloud_data["path"].replace(path_root, "").split("/") if key != ""]

        set_nested(result, keys, json.loads(cloud_data["data"]))

    return result
