import  argparse
from var1.dir_walker import walk_dir


def parse_ars():
    parser = argparse.ArgumentParser(description="T6_s15t06")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директорию')
    args = parser.parse_args()
    return args.p

def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))

if __name__ == '__main__':
    main()
