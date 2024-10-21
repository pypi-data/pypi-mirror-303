# Azure Blob Storage `StacIO`

[![PyPI version](https://badge.fury.io/py/az-blob-stacio.svg)](https://badge.fury.io/py/az-blob-stacio)
![CI](https://github.com/bmcandr/az-blob-stacio/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/github/bmcandr/az-blob-stacio/graph/badge.svg?token=CEJTBDWZZE)](https://codecov.io/github/bmcandr/az-blob-stacio)
![GitHub License](https://img.shields.io/github/license/bmcandr/az-blob-stacio)

An implementation of `pystac`'s `StacIO` for reading static STACs stored in Azure Blob Storage. See [the pystac docs](https://pystac.readthedocs.io/en/stable/concepts.html#i-o-in-pystac) for more info.

## Installation

Either:

* `pip install az-blob-stacio`
* `uv add az-blob-stacio`

## Usage

Set the global default `StacIO` to `BlobStacIO`:

```python
import os

from az_blob_stacio import BlobStacIO

BlobStacIO.conn_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

pystac.StacIO.set_default(BlobStacIO)

catalog = pystac.Catalog.from_file("https://myaccount.blob.core.windows.net/mycontainer/catalog.json")
```

Or use a context manager to temporarily set `BlobStacIO` as the default `StacIO` and reset to `DefaultStacIO` upon exiting the context:

```python
import os

from az_blob_stacio import BlobStacIO, custom_stacio

BlobStacIO.conn_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

with custom_stacio(BlobStacIO):
    catalog = pystac.Catalog.from_file("https://myaccount.blob.core.windows.net/mycontainer/catalog.json")
```

Overwrite behavior is configurable by setting `BlobStacIO.overwrite` (defaults to `True`).

### Credentials

Azure Blob Storage credentials can be provided by setting either of the following class variables:

* `BlobStacIO.conn_str`: a [connection string](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string#configure-a-connection-string-for-an-azure-storage-account) for the Azure storage account. Checks for `AZURE_STORAGE_CONNECTION_STRING` in your environment by default.
* `BlobStacIO.credential`: a [credential](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#credentials) that provides access to the storage account hosting the static STAC.

    ```python
    from azure.core.credentials import AzureSasCredential

    BlobStacIO.credential = AzureSasCredential("my-sas-token")
    ```
