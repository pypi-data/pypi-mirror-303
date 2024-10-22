# Floods-HTML

Floods-HTML is a python package to simplify the generation of HTML pages of flood forecasting products typically provided for EFAS and GloFAS.

## Installation

Clone source code repository

    $ git clone https://github.com/ecmwf/floods-html.git
    $ cd floods-html

Create and activate conda environment

    $ conda create -n floods_html python=3.10
    $ conda activate floods_html

For default installation, run

    $ pip install .

For a developer installation (includes linting and test libraries), run

    $ pip install -e .[dev]
    $ pre-commit install

If you only plan to run the tests, instead run

    $ pip install -e .[test]

If you plan to build a source and a wheel distribution, it is additionally required to run

    $ pip install build

## Usage
-

## Supported JSON Format

```
{"data": [
    {"type": OBJECT_NAME, "data": OBJECT},
    {"type": OBJECT_NAME, "data": OBJECT},
    ...
]}
```

Supported objects are currently

- `"figure"`
```
{
    "title": FIGURE_NAME,
    "name": FIGURE_FILENAME,
    "width": FIGURE_WIDTH, (optional)
    "height": FIGURE_HEIGHT (optional)
}
```

- `"table"`
```
{
    "title": TABLE_NAME,
    "header": [
        TABLE_ENTRY,
        TABLE_ENTRY,
        ...
    ],
    "rows": [
        [
            TABLE_ENTRY,
            TABLE_ENTRY,
            ...
        ],
        [
            TABLE_ENTRY,
            TABLE_ENTRY,
            ...
        ],
        ...
    ]
}
```
where a table entry is
```
{
"value": ENTRY_VALUE,
"background_color": ENTRY_COLOUR_HEX (optional),
"text_color": ENTRY_COLOUR_HEX (optional),
"col_span": INT (optional),
}
```
