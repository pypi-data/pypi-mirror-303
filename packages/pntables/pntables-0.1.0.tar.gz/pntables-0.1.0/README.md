# pntables

**pntables** renders pandas DataFrames as interactive tables using the [Tabulator](http://tabulator.info/) component in [Panel](https://panel.holoviz.org/) directly in Jupyter notebooks. It automatically integrates with pandas, so DataFrames display interactively with no extra setup.

## Roadmap:

- Make pagination responsive to slider widget

## Features

- Automatic conversion of DataFrames to interactive tables.

## Installation

```bash
pip install pntables
```

## Usage

Just `import pntables` and use pandas as you would.

```python
import pandas as pd
import pntables

df = pd.DataFrame({
    'Sample': ['A', 'B', 'C'],
    'Score': [25, 30, 35],
    'Location': ['San Diego', 'Berlin', 'Seattle']
})

df
```
![](./doc/assets/pntables_preview.png)


## License

Licensed under the BSD 3-Clause License. See [LICENSE](LICENSE) for details.
