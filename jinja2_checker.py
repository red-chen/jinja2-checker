#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import json
import argparse

from jinja2 import Template

def load_tmpl(path):
    with open(path) as fp:
        return fp.read()

def load_value(path):
    with open(path) as fp:
        return json.load(fp) 

def handle_apply(args):
    template = Template(load_tmpl(args.tmpl))
    out = template.render(load_value(args.value))
    print out

def gen_parser():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(title="Sub Commands")

    sub = subs.add_parser('apply', help="Apply the jj2 file.")
    sub.add_argument('-v', '--value', dest='value', required=True, help='Json value file')
    sub.add_argument('-t', '--tmpl', dest='tmpl', required=True, help='Template file')
    sub.set_defaults(func=handle_apply)

    return parser

def main():
    parser = gen_parser()
    result = parser.parse_args(sys.argv[1:])
    result.func(result)

if __name__ == '__main__':
    main()
