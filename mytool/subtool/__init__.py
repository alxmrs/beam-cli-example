from .main import run


def cli(extra=[]):
    import sys
    run(sys.argv + extra)
