from setuptools import setup, find_packages, tests_require, packages, name

with open("README", 'r') as f:
    long_description = f.read()

setup = (
    name='linkbox',
    version='1.0',
    description='Generates a JSON object containing link preview information by passing a URL parameter.',
    long_description=long_description,
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    url="https://github.com/toddbirchard/Link-Preview-API",
    packages=['endpoint', 'tests'],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
)
