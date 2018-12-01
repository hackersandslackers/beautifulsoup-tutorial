from setuptools import setup, find_packages

setup(
    # ...,
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
)
