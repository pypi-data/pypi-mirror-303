from setuptools import setup, find_packages

setup(
    name="ip_fetcher_phillip_bridgeman",
    version="4.0",
    description="A Python utility to fetch the current machine's public IP address.",
    author="Phillip Bridgeman",
    author_email="your.email@example.com",
    packages=find_packages(),  # Automatically find and include all packages
    entry_points={
        'console_scripts': [
            'ipfetch=ipfetcher.ip_parser_phillip_bridgeman:main',  # Entry point to run the script
        ],
    },
)