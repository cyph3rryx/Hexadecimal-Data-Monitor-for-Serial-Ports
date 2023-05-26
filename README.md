# Serial Data Hex Dump

This code allows you to connect to a serial port and display incoming data in real-time. It also includes options to format, filter, and log the data.

## Code Description

The code is written in Python and requires the `serial` and `sys` modules. It includes the following features:

### Data Format Options

The following data format options are available:

- `hex`: binary data is converted to a hexadecimal string representation
- `ascii`: binary data is converted to an ASCII string representation
- `binary`: binary data is converted to a binary string representation

### Logging Options

The following logging options are available:

- `none`: no data is logged
- `file`: data is logged to a specified file

### Filtering Options

The following filtering options are available:

- `none`: no filtering is applied
- `printable`: only printable ASCII characters are included in the output

## Procedure

The following is the recommended procedure for using the code:

1. Clone the repository or download the code
2. Install the required modules (`serial` and `sys`)
3. Connect to the serial port
4. Specify the baud rate and any optional parameters (data format, logging, and filtering)
5. Run the code
6. View the incoming data in real-time
7. The data can be optionally filtered and/or logged for analysis later

## Example Usage

To connect to a serial port at 9600 baud and display incoming data in hexadecimal format, use the following command:

```python
python serialdatalogger.py COM1 9600 hex
```
To filter out non-printable ASCII characters from the output, use the following command:

``` python
python serialdatalogger.py COM1 9600 hex none none printable
```

To log the incoming data to a file called log.txt, use the following command:

``` python
python serialdatalogger.py COM1 9600 hex file log.txt none
```

## Summarizing 

The serial data hex dump code provides a flexible and customizable tool for digital forensics investigators to extract and analyze data from devices that communicate via a serial port. By using the various formatting, filtering, and logging options, investigators can obtain valuable information that can aid in their investigations.
