from setuptools import setup, find_packages

setup(
    name="docketpy",
    version="2.0.3",
    packages=find_packages(include=("docketpy", "docketpy.*")),
    description='Docket Python library',
    author='VST',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)