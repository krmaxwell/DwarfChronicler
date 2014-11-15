import argparse
import json
import os
import sys
import xmltodict


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("directory", help="Directory with export data")
    args = argparser.parse_args()

    dirlist = os.listdir(args.directory)
    for each in dirlist:
        if each.endswith('xml'):
            datafile = each
        elif each.endswith('world_history.txt'):
            histfile = each
        elif each.endswith('world_sites_and_pops.txt'):
            sitefile = each

    with open(os.path.join(args.directory, datafile), 'rb') as f:
        ldata = f.read()

    with open(os.path.join(args.directory, histfile), 'rb') as f:
        hdata = f.readlines()

    with open(os.path.join(args.directory, sitefile), 'rb') as f:
        sdata = f.readlines()

    sys.stderr.write('Parsing data for %s\n' % hdata[0])
    legends = xmltodict.parse(ldata, encoding='cp437')

    print json.dumps(legends, indent=2)


if __name__ == "__main__":
    main()
