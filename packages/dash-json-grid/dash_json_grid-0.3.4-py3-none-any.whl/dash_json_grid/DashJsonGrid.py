# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashJsonGrid(Component):
    """A DashJsonGrid component.
DashJsonGrid is a Dash porting version for the React component:
`react-json-grid/JSONGrid`

This component provides a JSON Grid viewer used for viewing complicated and
unstructured serializable JSON data.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- data (dict | list | number | string | boolean; required):
    The JSON object or array to be transformed into a grid table.

- default_expand_depth (number; default 0):
    The depth to which the grid is expanded by default.

- default_expand_key_tree (dict; optional):
    Tree-like structure with all keys that needs to be expanded. This
    structure needs to be a dictionary mimicing the structure of the
    data.

- highlight_selected (boolean; default True):
    Whether to highlight the selected item or not.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- search_text (string; optional):
    The text that needs to be searched in the JSON data.

- selected_path (list; optional):
    keyPath captured by the onSelect method of the grid viewer. This
    value is a sequence of indicies used for locating the element of
    the selected data.  Due to the limitation of the exported
    functionalities, this value cannot be reset by the callback. In
    other words, using it with callbacks.Output will not take effects.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- theme (dict; default "default"):
    The theme (name) that needs to be applied. If a dictionary is
    specified, will customize the color code of each part of grid
    viewer.

    `theme` is a a value equal to: "default", "dracula", "monokai",
    "oceanicPark", "panda", "gruvboxMaterial", "tokyoNight", "remedy",
    "atlanticNight", "defaultLight", "defaultLight2", "slime",
    "spacegray", "blueberryDark", "nord", "nightOwl", "oneMonokai",
    "cobaltNext", "shadesOfPurple", "codeBlue", "softEra",
    "atomMaterial", "evaDark", "moonLight", "inherit", "unset" | dict
    with keys:

    - bgColor (string; optional):
        Background color.

    - booleanColor (string; optional):
        Text color of boolean variables.

    - cellBorderColor (string; optional):
        Background color of table cells.

    - highlightBgColor (string; optional):
        Background color when this part is highlighted.

    - indexColor (string; optional):
        Text color of array indicies.

    - keyNameColor (string; optional):
        Text color of JSON keys.

    - numberColor (string; optional):
        Text color of numeric values.

    - objectColor (string; optional):
        Text color of unrecognized objects.

    - searchHighlightBgColor (string; optional):
        Background color of the part highlighted by the search.

    - stringColor (string; optional):
        Text color of strings.

    - tableBorderColor (string; optional):
        Border color of the whole table.

    - tableHeaderBgColor (string; optional):
        Background color of the table header.

    - tableHeaderColor (string; optional):
        Text color of the table header."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_json_grid'
    _type = 'DashJsonGrid'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, class_name=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, default_expand_depth=Component.UNDEFINED, default_expand_key_tree=Component.UNDEFINED, selected_path=Component.UNDEFINED, highlight_selected=Component.UNDEFINED, search_text=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'class_name', 'data', 'default_expand_depth', 'default_expand_key_tree', 'highlight_selected', 'loading_state', 'search_text', 'selected_path', 'style', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'class_name', 'data', 'default_expand_depth', 'default_expand_key_tree', 'highlight_selected', 'loading_state', 'search_text', 'selected_path', 'style', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashJsonGrid, self).__init__(**args)
