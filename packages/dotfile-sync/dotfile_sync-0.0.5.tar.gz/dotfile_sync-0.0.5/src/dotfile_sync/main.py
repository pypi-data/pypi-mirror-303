#!/usr/bin/env python3
import argparse
import os
import pdb
import shutil
import tempfile


def get_version():
    import importlib.metadata

    try:
        # To be used in a package
        version = importlib.metadata.version('dotfile-sync')
    except:
        version = '0.0'

    return version


def ask_confirm(remote_path, local_path):
    while True:
        answer = input('Which one do you want? [r/l/c/h] ').lower()
        if answer in ('r'):
            return remote_path
        elif answer == 'l':
            return local_path
        elif answer == 'c':
            return False
        elif answer == 'h':
            print('Usage: r: remote, l: local, c: cancel, h: help')


def interactive(remote_path, local_path):
    if os.environ.get('TERM_PROGRAM') == 'vscode':
        os.system(f'code --diff -w {local_path} {remote_path}')
    else:
        os.system(f'git difftool -y --no-index {local_path} {remote_path}')
    return ask_confirm(remote_path, local_path)


def ask_interactive(remote_path, local_path):
    while True:
        answer = input('Interavtive? [Y/n] ').lower()
        if answer in ('y', ''):
            return interactive(remote_path, local_path)
        elif answer == 'n':
            return False
        else:
            continue


def ask_continue(remote_path, local_path):
    while True:
        answer = input('Continue? [Y/n] ').lower()
        if answer in ('y', ''):
            return ask_interactive(remote_path, local_path)
        elif answer == 'n':
            return False
        else:
            continue


def sync(remote_host, remote_path, local_path):
    tmp_dir = tempfile.mkdtemp()
    tmp_dir_local = os.path.join(tmp_dir, 'local')
    tmp_dir_remote = os.path.join(tmp_dir, 'remote')
    os.makedirs(tmp_dir_local)
    os.makedirs(tmp_dir_remote)

    local_path = os.path.expanduser(local_path)
    os.system(f'scp -p {remote_host}:{remote_path} {tmp_dir_remote}')
    shutil.copy(local_path, tmp_dir_local)
    tmp_local = os.path.join(tmp_dir_local, os.path.basename(local_path))
    tmp_remote = os.path.join(tmp_dir_remote, os.path.basename(remote_path))
    os.system(f'git diff --no-index {tmp_local} {tmp_remote}')
    if target := ask_continue(tmp_remote, tmp_local):
        shutil.copy(local_path, f'{local_path}.dsbak')
        print(f'Backup: {local_path}.dsbak')
        shutil.copy(target, local_path)


def main():
    parser = argparse.ArgumentParser(description='Sync dotfiles')
    parser.add_argument('-v', '--version', action='version', version=get_version())
    parser.add_argument('remote_host')
    parser.add_argument('remote_path')
    parser.add_argument('local_path')
    args = parser.parse_args()
    sync(args.remote_host, args.remote_path, args.local_path)


if __name__ == '__main__':
    main()
