import apache_beam as beam
import apache_beam.metrics


def pass_through(first: str, second: str):
    beam.metrics.Metrics.counter('Success', 'Pass_through').inc()
    return first, second
