import argparse
from rich import print

from serial_handler import SerialHandler
from serial_handler import serial_list_ports

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--list",
                        help="list available serial ports",
                        action='store_true')
    parser.add_argument("-p", "--port",
                        help="serial port, usually COMx or /dev/ttyXX",
                        type=str)
    parser.add_argument("-b", "--baud",
                        help="serial port baud rate",
                        type=int,
                        default=115200)
    parser.add_argument("-f", "--flow",
                        help="software ('x' for xon/xoff), hardware \
                            ('h' for rts/cts), or no ('n') flow control",
                        type=str,
                        default='n')
    parser.add_argument("-pa", "--parity",
                        help="set the parity mode, 'o': odd, 'e': even, 'n': none",
                        type=str,
                        default='n')
    parser.add_argument("-c", "--config",
                        help="specificy config.json or config.yaml",
                        type=str)

    args = parser.parse_args()

    if args.list:
        serial_list_ports()
        exit(0)

    # Grab and validate inputs
    port = args.port
    baudrate = args.baud
    flow_ctl = args.flow.lower()
    parity = args.parity.lower()
    config = args.config
    if flow_ctl not in ('x', 'h', 'n'):
        print('[bold red]Invalid flow control setting[/bold red]')
        parser.print_help()
        parser.exit(1)
    if parity not in ('e', 'o', 'n'):
        print('[bold red]Invalid parity setting[/bold red]')
        parser.print_help()
        parser.exit(1)
    

    print('Starting serial tool..')



if __name__ == "__main__":
    main()
