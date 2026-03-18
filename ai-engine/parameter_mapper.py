import json
import os

def map_parameters(words):
    """
    Maps a list of words to plugin parameters based on a style map.
    """
    style_map_path = os.path.join(os.path.dirname(__file__), 'style_map.json')

    if not os.path.exists(style_map_path):
        return {}

    with open(style_map_path, 'r') as f:
        style_map = json.load(f)

    params = {}
    for word in words:
        if word in style_map:
            params.update(style_map[word])

    return params
