import argparse
import json
import xmltodict


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("datafile", help="Name of Legends XML export")
    args = argparser.parse_args()

    with open(args.datafile, 'rb') as f:
        ldata = f.read()

    legends = xmltodict.parse(ldata, encoding='cp437')

    print json.dumps(legends, indent=2)


if __name__ == "__main__":
    main()
