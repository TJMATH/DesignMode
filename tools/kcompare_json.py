import argparse
import os
import logging
import json

d1_only = []
d2_only = []
diff = []

def load_json(json_path):
    with open(json_path, 'r') as f:
        d = json.load(f)
    return d

def compare(d1, d2):
    for key in d1.keys():
        if key not in d2:
            d1_only.append((key, d1[key]))
        elif isinstance(d1[key], dict):
            compare(d1[key], d2[key])
        elif d1[key] != d2[key]:
            diff.append((key, d1[key], d2[key]))
    for key in d2.keys():
        if key not in d1:
            d2_only.append((key, d2[key]))

def show(res, header):
    if len(res) == 0:
        return
    print('\t| '.join(header))
    for r in res:
        r = [str(x) for x in r]
        print('\t| '.join(r))

def main(json1, json2):
    d1 = load_json(json1)
    d2 = load_json(json2)
    compare(d1, d2)
    show(d1_only, header=('key', json1))
    show(d2_only, header=('key', json2))
    show(diff, header=('key', json1, json2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json1', type=str, help="first json")
    parser.add_argument('--json2', type=str, help="second json")
    args = parser.parse_args()
    main(args.json1, args.json2)