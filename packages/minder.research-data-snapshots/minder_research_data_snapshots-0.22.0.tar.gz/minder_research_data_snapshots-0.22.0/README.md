# minder.research-data-snapshots

## Install

```sh
python -m pip install minder.research-data-snapshots
```

This will provide exports in Parquet format, which should be sufficient if you're using Pandas or another dataframe library.

If you require exports in CSV format then use:

```sh
python -m pip install 'minder.research-data-snapshots[csv]'
```

## Use

First retrieve an access token from <https://research.minder.care/>

Then use one of the following methods to retrieve data snapshots

### CLI

```sh
python -m minder.research_data_snapshots --dataset patients raw_heart_rate --organization SABP "H&F" --token-path /path/to/access/token
```

Run `python -m minder.research_data_snapshots --help` to see all options

### Library

```sh
python -m pip install 'pandas[parquet]'
```

```sh
export RESEARCH_PORTAL_TOKEN_PATH=/path/to/access/token
```

```python
from datetime import datetime

import pandas as pd

from minder.research_data_snapshots import download_datasets

patients = pd.concat(pd.read_parquet(dataset) for dataset in download_datasets(["patients"], ["SABP", "H&F"]))

raw_heart_rate = (
    pd.concat(
        pd.read_parquet(
            path,
            filters=[
                ("start_date", ">=", datetime.fromisoformat("2023-01-01T00Z")),
                ("start_date", "<", datetime.fromisoformat("2024-01-01T00Z")),
            ],
            columns=["patient_id", "start_date", "value"],
        )
        for path in download_datasets(["raw_heart_rate"], ["SABP", "H&F"])
    )
    .sort_values("start_date")
    .reset_index(drop=True)
)
```
