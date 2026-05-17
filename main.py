import argparse
from rich import print

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port",
                        help="serial port, usually COMx or /dev/ttyXX",
                        type=str)
    parser.add_argument("-br", "--baudrate",
                        help="serial port baud rate",
                        default=115200,
                        type=int)
    parser.add_argument("-c", "--config",
                        help="specificy config.json or config.yaml",
                        type=str)
    
    args = parser.parse_args()

    print('Starting serial tool..') 
    if args.port and args.baudrate:

        print(f'Port = {args.port}, Baud = {args.baudrate}')


if __name__ == "__main__":
    main()
