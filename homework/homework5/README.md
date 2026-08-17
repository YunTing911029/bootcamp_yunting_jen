## Data Storage

### Folder Structure

The project separates raw and processed data into two directories:

```text
data/
├── raw/          # Raw data stored as CSV
└── processed/    # Processed data stored as Parquet
```

### Storage Formats

* **CSV** is used for raw data because it is human-readable, easy to inspect, and widely supported.
* **Parquet** is used for processed data because it provides efficient storage, preserves data types, and is well suited for analytical workflows.

### Environment-Driven Paths

Data paths are configured through the `.env` file:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

The notebook loads these variables and creates the directories if they do not already exist:

```python
RAW_DIR = pathlib.Path(os.getenv("DATA_DIR_RAW", "data/raw"))
PROC_DIR = pathlib.Path(os.getenv("DATA_DIR_PROCESSED", "data/processed"))
```

### Reading and Writing Data

The `write_df()` and `read_df()` utility functions determine the file format from the file extension. CSV files are written and read with Pandas CSV functions, while Parquet files use Pandas Parquet functions.

This makes the storage process reusable while keeping file locations configurable through environment variables.
