# beam-cli-example

## Installation

```shell script
git clone git@github.com:alxrsngrtn/beam-cli-example.git
pip install .
```

## Intended Usage
```shell script
boom roasted \
    --runner DataflowRunner \
    --project $PROJECT \
    --region $REGION \
    --temp_location gs://$BUCKET/tmp
```

Workaround: 
```shell script
boom roasted \
    --runner DataflowRunner \
    --project $PROJECT \
    --region $REGION \
    --temp_location gs://$BUCKET/tmp
    --setup_file=$(pwd)/setup.py
```

Error received (even with workaround): `ModuleNotFoundError: No module named 'mytool'`
