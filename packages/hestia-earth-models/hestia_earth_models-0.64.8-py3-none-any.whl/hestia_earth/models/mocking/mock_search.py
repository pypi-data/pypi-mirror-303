from inspect import getmembers, isfunction
import json
from hestia_earth.utils.tools import flatten

from hestia_earth.models.utils import term

IGNORE_FUNC = ['get_lookup_value', 'get_table_value']


def _map_results(results):
    # returning the whole term
    return [results] if isinstance(results, dict) else (
        {'@type': 'Term', '@id': results} if isinstance(results, str) else
        flatten(map(_map_results, results)) if isinstance(results, list) else
        None
    )


def _create_search_result(data: tuple):
    search_query = {}

    original_search = term.search

    def new_search(query: dict, *_a, **_b):
        nonlocal search_query
        search_query = query
        return original_search(query, *_a, **_b)
    term.search = new_search

    original_find_node = term.find_node

    def new_find_node(_n, query: dict, *_a, **_b):
        nonlocal search_query
        search_query = query
        return original_find_node(_n, query, *_a, **_b)
    term.find_node = new_find_node

    function_name, func = data
    res = func()
    return {'name': function_name, 'query': search_query, 'results': _map_results(res)}


def create_search_results():
    funcs = list(filter(lambda v: v[0].startswith('get_') and not v[0] in IGNORE_FUNC, getmembers(term, isfunction)))
    return list(map(_create_search_result, funcs))


def _load_results(filepath: str):
    with open(filepath) as f:
        return json.load(f)


def _find_search_result(filepath: str, query: dict):
    search_results = _load_results(filepath)
    res = next((n for n in search_results if n['query'] == query), None)
    return None if res is None else res.get('results', [])


def _mocked_search(original_func, filepath: str):
    def mock(query: dict, **kwargs):
        result = _find_search_result(filepath, query)
        return original_func(query, **kwargs) if result is None else result
    return mock


def _mocked_find_node(original_func, filepath: str):
    def mock(node_type: str, query: dict, **kwargs):
        result = _find_search_result(filepath, query)
        return original_func(node_type, query, **kwargs) if result is None else result
    return mock


def mock(filepath: str):
    original_search = term.search
    term.search = _mocked_search(original_search, filepath)
    original_find_node = term.find_node
    term.find_node = _mocked_find_node(original_find_node, filepath)
