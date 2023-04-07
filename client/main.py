import argparse
import configparser
from client import Client

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Set or get currency exchange rates.')
    parser.add_argument('method', choices=['GET', 'POST'], help='HTTP method to use')
    parser.add_argument('rate', type=float, nargs='?', help='rate value')
    args = parser.parse_args()

    # Read configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    server_url = config['server']['url']
    currency_pair = config['currency']['pair']

    client = Client(server_url)

    if args.method == 'POST':
        if args.rate is None:
            print('Rate value is required for POST method.')
            return
        response = client.set_rate(currency_pair, args.rate)
    else:
        response = client.get_rate(currency_pair)

    print(response)

if __name__ == '__main__':
    main()
