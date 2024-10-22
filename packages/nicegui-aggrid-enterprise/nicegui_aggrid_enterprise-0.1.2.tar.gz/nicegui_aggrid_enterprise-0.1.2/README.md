# NiceGUI AG Grid Enterprise
This is a custom component for NiceGUI that integrates AG Grid Enterprise, a powerful and feature-rich data grid for JavaScript. This component allows you to easily incorporate AG Grid Enterprise into your NiceGUI applications, providing advanced grid functionalities such as sorting, filtering, and editing.

## Installation
To install the NiceGUI AG Grid Enterprise component, use the following pip command:

`pip install nicegui-aggrid-enterprise`

## Usage
Below is a minimally usable example of how to use the AG Grid Enterprise component in your NiceGUI application:

```python
from nicegui import ui
from nicegui_aggrid_enterprise import aggrid

# Set license key
aggrid.license_key = "MY_AGGRID_LICENSE_KEY"

# Define grid options
options = {
    'columnDefs': [
        {'headerName': 'Make', 'field': 'make'},
        {'headerName': 'Model', 'field': 'model'},
        {'headerName': 'Price', 'field': 'price'}
    ],
    'rowData': [
        {'make': 'Toyota', 'model': 'Celica', 'price': 35000},
        {'make': 'Ford', 'model': 'Mondeo', 'price': 32000},
        {'make': 'Porsche', 'model': 'Boxster', 'price': 72000}
    ],
    'rowSelection': 'single',
    'editable': True
}

# Create an instance of aggrid
grid = aggrid(options=options)

# Start the NiceGUI application
ui.run()
```
