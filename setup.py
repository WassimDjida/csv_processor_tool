from setuptools import setup, find_packages

setup(
    name="csv_processor_tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    author="Ouassim",
    description="A tool to process Sanofi* CSV files",
    url="https://github.com/yourusername/csv_processor_tool",
)

