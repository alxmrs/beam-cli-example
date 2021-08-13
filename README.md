# beam-cli-example

## Installation

```shell script
pip install git+https://github.com/alxmrs/beam-cli-example.git#egg=mytool
```

## Usage
```shell script
boom roasted \
    --runner DataflowRunner \
    --project $PROJECT \
    --region $REGION \
    --temp_location gs://$BUCKET/tmp
```

