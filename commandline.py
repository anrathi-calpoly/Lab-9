import sys
from typing import List

def main(argv: List[str]) -> None:
    for arg in argv:
        print(arg)

if __name__ == '__main__':
    main(sys.argv)
