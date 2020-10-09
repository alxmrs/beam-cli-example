# beam-cli-example

## Installation

```shell script
git clone git@github.com:alxrsngrtn/beam-cli-example.git
pip install .
```

## Usage
```shell script
boom roasted \
    --runner DataflowRunner \
    --project $PROJECT \
    --region $REGION \
    --temp_location gs://$BUCKET/tmp
```

