import os
import re

path = "/Users/user/Downloads/3-Pandas-Data Analysis/"


def main():
    for count, filename in enumerate(os.listdir(path)):
        result = re.search(r"\.ts|\.mp4$", filename)
        if result:
            dst = str(count) + "-" + filename
            src = path + filename
            dst = path + dst

            re.sub(r'\d+-', '&', filename)


if __name__ == '__main__':
    main()
