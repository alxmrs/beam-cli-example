from setuptools import setup, find_packages


setup(
    name='mytool',
    packages=find_packages(),
    author='Alex Rosengarten',
    author_email='alxrsngrtn@google.com',
    url='https://github.com/alxrsngrtn/beam-cli-example',
    description='A toy python project to demo packaging a dataflow pipeline in a CLI.',
    install_requirements=['apache-beam[gcp]'],
    scripts=['boom']
)
