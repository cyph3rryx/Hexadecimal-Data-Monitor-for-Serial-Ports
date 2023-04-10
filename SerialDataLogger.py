import serial
import sys

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
    # Added command-line arguments and options
    port = sys.argv[1]
    baudrate = int(sys.argv[2])
    data_format = FORMAT_HEX if len(sys.argv) < 4 else sys.argv[3]
    log_type = LOG_NONE if len(sys.argv) < 5 else sys.argv[4]
    log_file = None if len(sys.argv) < 6 else sys.argv[5]
    filter_type = FILTER_NONE if len(sys.argv) < 7 else sys.argv[6]

    ser = serial.Serial(port, baudrate)

    while True:
        data = ser.read(1)
        if data:
            # Added support for multiple data formats
            if data_format == FORMAT_HEX:
                output = hexdump(data)
            elif data_format == FORMAT_ASCII:
                output = asciidump(data)
            elif data_format == FORMAT_BINARY:
                output = binarydump(data)
            else:
                raise ValueError('Invalid data format: {}'.format(data_format))

            # Added support for filtering and logging data
            filtered_data = filterdata(data, filter_type)
            logdata(filtered_data, log_type, log_file)

            sys.stdout.write(output)
            sys.stdout.flush()

if __name__ == '__main__':
    main()
