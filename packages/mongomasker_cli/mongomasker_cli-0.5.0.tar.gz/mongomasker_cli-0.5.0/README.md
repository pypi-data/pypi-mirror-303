
# MongoMasker

MongoMasker is a tool designed to anonymize specified fields in a MongoDB collection. It uses the `faker` library to generate realistic fake data, processes documents in batches for improved performance, and leverages asynchronous processing with `motor` for efficiency.

## Features

- Anonymizes specified fields with realistic fake data
- Supports nested fields and fields within objects in arrays
- Processes documents in batches for better performance
- Uses asynchronous processing for efficiency

## Requirements

- Python 3.6+
- `motor` library
- `pymongo` library
- `faker` library
- `typer` library

## Installation

Install the required libraries using pip:

```bash
poetry install
```


## Usage

1. Create a JSON file specifying the fields to anonymize. For example, `fields_to_anonymize.json`:

```json
{
    "field1": "name",
    "nested.field": "email",
    "array.field": "address",
    "dateField": "date",
    "location.zipcode": "zipcode",
    "user.stateCode": "stateCode",
    "user.lastname": "lastname",
    "address.city": "city"
}
```

2. Run the script from the command line:

```bash
mongomasker \
    "mongodb://your_username:your_password@your_host:your_port" \
    source_database \
    source_collection \
    target_database \
    target_collection \
    fields_to_anonymize.json \
    --batch-size 100
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
