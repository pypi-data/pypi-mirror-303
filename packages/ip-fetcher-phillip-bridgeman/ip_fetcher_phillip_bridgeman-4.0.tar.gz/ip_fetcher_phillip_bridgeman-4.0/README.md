# IP Fetcher Project

## Author: Phillip Bridgeman
### Date: October 21, 2024

A simple Python script to fetch and display the current public IP address of the machine by parsing the HTML content of the page http://checkip.dyndns.org/.

## Features:

- Fetches current public IP address of machine running script.
- Optional Logging IP address for debugging purposes.

## Installation

To install the package and use the IP fetcher script, follow these steps:

1. **Install the module using pip**:

   After packaging the module, you can install it using pip by running:
   
   ```bash
   pip install ip_parser_phillip_bridgeman
   ```

## Running the script:

Once installed, you can run the module as a script to fetch and display the IP address of the machine. Here's how:

```bash
python3 -m ip_parser_phillip_bridgeman
```

This command will print the current public IP address of your machine.

## Usage:

Run the script using Python to fetch and display the IP address:

```bash
python3 -m ip_parser_phillip_bridgeman
```

*Example*
```bash
IP Address: 198.163.150.11
```

## Optional: Logging
To enable logging and log the fetched IP address (useful for debugging), add the following lines in your script after fetching the IP address:

```py
ip_address = get_ip_address()
log_ip_address(ip_address)
```

This will log the IP address and show additional information:

```bash
2024-10-21 07:02:49,009 - INFO - IP Address: 198.163.150.11
```

## Uninstalling
If you need to uninstall the package, use the following command:

```bash
pip uninstall ip_parser_phillip_bridgeman
```

## Contributions:
At this stage, contributions are welcome but are expected to be small improvements or bug fixes. Feel free to share ideas for future features.

## License:

This project is licensed under the MIT License. Feel free to use, modify, and distribute this code within the terms of the license.