import argparse
import os
import json

def load_json(json_path):
    with open(json_path, 'r') as f:
        d = json.load(f)
    return d

def tree_json(d, L, s=''):
    dict_len = len(d)
    idx = 0
    for k,v in d.items():
        idx += 1
        line = s + '\\_' + k if s != '' else k
        print(line)
        if isinstance(v, dict) and L > 0:
            if s == '':
                line = '    '
            elif idx == dict_len:
                line = s + '    '
            else:
                line = s + '|   '
            tree_json(v, L-1, line)

def main(js, L):
    d = load_json(js)
    tree_json(d, L)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=str, help="json file path")
    parser.add_argument('--L', type=int, default=100, help="deep")
    args = parser.parse_args()
    main(args.json, args.L)