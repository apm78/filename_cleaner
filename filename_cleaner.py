#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import os.path
import re
import sys

DEFAULT_ROOT = '.'
NON_ASCII_REGEX = re.compile(r'[^\u0000-\u007f]')


def check_filename(filename):
    return re.search(NON_ASCII_REGEX, filename) is not None


def new_filename(filename):
    return re.sub(
        NON_ASCII_REGEX, '_', filename.replace(
            '\u00df', 'ss').replace(
            '\u00e4', 'ae').replace(
            '\u00c4', 'Ae').replace(
            '\u00f6', 'oe').replace(
            '\u00d6', 'Oe').replace(
            '\u00fc', 'ue').replace(
            '\u00dc', 'Ue'))


def fix_file_or_dir_name(filename, dirpath, dry_run, force):
    if check_filename(filename):
        new_name = new_filename(filename)
        full_file_path = os.path.join(dirpath, filename)
        full_new_file_path = os.path.join(dirpath, new_name)
        if dry_run:
            logging.info(f'Rename {full_file_path} to {new_name}')
        if not dry_run:
            if force or not os.path.exists(full_new_file_path):
                logging.info(f'Renaming {full_file_path} to {new_name}')
                os.replace(full_file_path, full_new_file_path)
            else:
                logging.error(f'Failed to rename {full_file_path} to {full_new_file_path}, because file exists.')


def fix_illegal_filenames(root_dir, dry_run, force):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        abs_path_dir = os.path.abspath(dirpath)
        for filename in filenames:
            fix_file_or_dir_name(filename, abs_path_dir, dry_run, force)
        os.path.basename(abs_path_dir)
        fix_file_or_dir_name(os.path.basename(abs_path_dir), os.path.dirname(abs_path_dir), dry_run, force)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    parser = argparse.ArgumentParser(description='Replace non-ascii filename characters like umlauts')
    parser.add_argument('root', help='root directory of the search and replace algorithm', default=DEFAULT_ROOT)
    parser.add_argument('-d', '--dryrun', help='traverse the directory without renaming', type=bool, default=False)
    parser.add_argument('-f', '--force', help='force replace even with duplicates', type=bool, default=False)
    args = parser.parse_args()
    if not os.path.exists(args.root):
        logging.error(f'The root directory {args.root} does not exist')
        sys.exit(1)
    fix_illegal_filenames(args.root, args.dryrun, args.force)
