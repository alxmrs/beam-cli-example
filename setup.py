from setuptools import setup, find_packages


setup(
    name='mytool',
    packages=find_packages(),
    author='Alex Merose',
    author_email='alxr@google.com',
    url='https://github.com/alxmrs/beam-cli-example',
    description='A toy python project to demo packaging a dataflow pipeline in a CLI.',
    install_requirements=['apache-beam[gcp]'],
    scripts=['mytool/boom']
)
