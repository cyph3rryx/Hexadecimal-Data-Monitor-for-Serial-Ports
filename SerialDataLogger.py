import serial
import sys
import argparse
import datetime

# Added data format options
FORMAT_HEX = 'hex'
FORMAT_ASCII = 'ascii'
FORMAT_BINARY = 'binary'

# Added logging options
LOG_NONE = 'none'
LOG_FILE = 'file'

# Added filtering options
FILTER_NONE = 'none'
FILTER_PRINTABLE = 'printable'


def hexdump(data):
    """
    Convert binary data to a hexadecimal string representation
    """
    return ' '.join('{:02X}'.format(byte) for byte in data)


def asciidump(data):
    """
    Convert binary data to an ASCII string representation
    """
    return ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in data)


def binarydump(data):
    """
    Convert binary data to a binary string representation
    """
    return ''.join('{:08b}'.format(byte) for byte in data)


def filterdata(data, filter_type):
    """
    Filter binary data based on the filter type
    """
    if filter_type == FILTER_NONE:
        return data
    elif filter_type == FILTER_PRINTABLE:
        return bytearray(byte for byte in data if 32 <= byte <= 126)
    else:
        raise ValueError('Invalid filter type: {}'.format(filter_type))


def logdata(data, log_type, log_file):
    """
    Log binary data based on the log type
    """
    if log_type == LOG_NONE:
        pass
    elif log_type == LOG_FILE:
        with open(log_file, 'ab') as f:
            f.write(data)
    else:
        raise ValueError('Invalid log type: {}'.format(log_type))


def main():
    """
    Connect to a serial port and display incoming data in real-time
    """
    parser = argparse.ArgumentParser(description='Serial Data Hex Dump')
    parser.add_argument('port', help='serial port')
    parser.add_argument('baudrate', type=int, help='baud rate')
    parser.add_argument('--format', choices=[FORMAT_HEX, FORMAT_ASCII, FORMAT_BINARY], default=FORMAT_HEX,
                        help='data format (default: hex)')
    parser.add_argument('--log', choices=[LOG_NONE, LOG_FILE], default=LOG_NONE, help='log type (default: none)')
    parser.add_argument('--logfile', help='log file name')
    parser.add_argument('--filter', choices=[FILTER_NONE, FILTER_PRINTABLE], default=FILTER_NONE,
                        help='filter type (default: none)')

    args = parser.parse_args()

    ser = serial.Serial(args.port, args.baudrate, timeout=1)

    while True:
        try:
            data = ser.read(1)
            if data:
                # Added support for multiple data formats
                if args.format == FORMAT_HEX:
                    output = hexdump(data)
                elif args.format == FORMAT_ASCII:
                    output = asciidump(data)
                elif args.format == FORMAT_BINARY:
                    output = binarydump(data)
                else:
                    raise ValueError('Invalid data format: {}'.format(args.format))

                # Added support for filtering and logging data
                filtered_data = filterdata(data, args.filter)
                logdata(filtered_data, args.log, args.logfile)

                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                sys.stdout.write(f'[{timestamp}] {output}\n')
                sys.stdout.flush()

        except (serial.SerialException, ValueError) as e:
            sys.stderr.write(f'Error: {str(e)}\n')
            sys.stderr.flush()
            # Optionally, you can attempt to reconnect to the serial port here


if __name__ == '__main__':
    main()
