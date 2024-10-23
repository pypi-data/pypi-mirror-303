from setuptools import setup, find_packages

setup(
    name='financial_tools',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'start=financial_tools.module:main_function',
        ],
    },
)