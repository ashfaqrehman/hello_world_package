"""
Hello world!
"""
import argparse


def main():
    """Prints hello"""
    parser = argparse.ArgumentParser()
    parser.add_argument('value')
    args = parser.parse_args()
    print('Hello,', args.value)


if __name__ == '__main__':
    main()
