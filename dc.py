import argparse
import json
import os
import xmltodict


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("directory", help="Directory with export data")
    args = argparser.parse_args()

    dirlist = os.listdir(args.directory)
    for each in dirlist:
        if each.endswith('xml'):
            datafile = each
            break

    with open(os.path.join(args.directory, datafile), 'rb') as f:
        ldata = f.read()

    legends = xmltodict.parse(ldata, encoding='cp437')

    print json.dumps(legends, indent=2)


if __name__ == "__main__":
    main()
