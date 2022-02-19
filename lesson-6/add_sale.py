import sys


def save_to_file(text: str):
    with open('./bakery.csv', mode='a', encoding='utf-8') as bakery:
        bakery.write(f'{text}\n')


if __name__ == '__main__':
    args = sys.argv[1:]
    save_to_file(args[0])
