# h2o-drive

Python Client for H2O Drive.

## Installation

```sh
pip install h2o-drive
```

## Usage

### Connecting to H2O Drive

```py
import h2o_drive

drive = h2o_drive.connect()
```

When used within the [H2O AI Cloud](https://h2o.ai/platform/ai-cloud/) environment or locally with the [H2O AI Cloud CLI](https://docs.h2o.ai/h2o-ai-cloud/developerguide/cli) configured, no further configuration is needed.

`h2o_drive.connect()` can be configured via optional parameters:

- `discovery`: The h2o_discovery.Discovery object through which to discover services for determining connection details
- `userdrive_url`: URL to Drive's userdrive service.
- `workspace_url`: URL to Drive's workspacedrive service.
- `sts_url`: URL to the STS service.
- `token_provider`: A token provider generating authentication credentials.

### Object Operations

To perform object operations, first open any Drive bucket. For example:

```py
bucket = drive.user_bucket()
# or
bucket = drive.workspace_bucket("default")
```

Buckets have the following methods:

- `upload_file()` uploads a local file, resulting in a new object at the specified key in the bucket. It takes two arguments:
    - `filename`: The file to upload. The contents of this file will become an object in the Drive bucket.
    - `key`: The key at which to store the resulting object. In other words, the name attached to the object.

- `list_objects()` returns the list of objects in the bucket. It takes one optional argument:
    - `prefix`: When specified, only objects at keys starting with the specified value are listed.

- `download_file()` downloads the object at the specified key and writes it to the specified local file. It takes two arguments:
    - `key`: The key of the object to download.
    - `filename`: The file, on the local filesystem, the object is written to.

- `delete_object()` deletes the object at the specified key. It takes a single argument:
  - `key`: The key of the object to delete.

- `generate_presigned_url()` generates a presigned URL for accessing the object at the specified key in the bucket. It takes two arguments:
  - `key`: The key to generate a presigned URL for.
  - `duration_seconds`: (Optional) The duration, in seconds, for which the URL should be valid. Defaults to 1 day.
- `with_prefix()` returns a prefixed view of this bucket. All the keys in each of its object operations are automatically prefixed with the specified value. It takes a single argument:
  - `prefix`: The key prefix to automatically apply to all object operations. 

## Examples

### Example: Open the storage bucket for your personal H2O workspace, write a local file, and list its contents

```py
import h2o_drive

# Prepare a local test file.
with open("test-file.txt", "w") as f:
    f.write("Hello, world!")

drive = h2o_drive.connect()
bucket = drive.workspace_bucket("default")

await bucket.upload_file("test-file.txt", "drive-test/uploaded-test-object.txt")

objects = await bucket.list_objects()
print(objects)
```
