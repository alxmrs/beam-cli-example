import argparse
import apache_beam as beam
import itertools

from apache_beam.options.pipeline_options import PipelineOptions

import typing as t

from .helper import pass_through


def run(argv: t.List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str)

    known_args, pipeline_args = parser.parse_known_args(argv[1:])

    pipeline_opts = PipelineOptions(pipeline_args)

    with beam.Pipeline(options=pipeline_opts) as p:
        (
            p
            | 'Create' >> beam.Create(list(itertools.product(known_args.keyword, repeat=2)))
            | 'Process' >> beam.MapTuple(pass_through)
            | 'Print' >> beam.Map(print)
        )
