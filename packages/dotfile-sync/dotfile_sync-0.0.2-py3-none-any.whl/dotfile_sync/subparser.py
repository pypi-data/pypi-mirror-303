import argparse
import os
import pdb
import shutil
import tempfile

from .preset import Preset


def add_sync_parser(parser: argparse.ArgumentParser):
    parser.add_argument('remote', help='Remote host')
    parser.add_argument('presets', nargs='*', help='Presets to sync', default=[])
    parser.add_argument(
        '-c', '--customs', nargs='*', help='Customs to sync', default=[]
    )

    def ask_confirm():
        while True:
            answer = input('Confirm? [Y/n] ').lower()
            if answer in ('y', ''):
                return True
            elif answer == 'n':
                return False
            else:
                continue

    def interactive(local_path, remote_path):
        if os.environ.get('TERM_PROGRAM') == 'vscode':
            os.system(f'code --diff -w {local_path} {remote_path}')
        else:
            os.system(f'git difftool -y --no-index {local_path} {remote_path}')
        return ask_confirm()

    def ask_interactive(local_path, remote_path):
        while True:
            answer = input('Interavtive? [Y/n] ').lower()
            if answer in ('y', ''):
                return interactive(local_path, remote_path)
            elif answer == 'n':
                return False
            else:
                continue

    def ask_continue(local_path, remote_path):
        while True:
            answer = input('Continue? [Y/n] ').lower()
            if answer in ('y', ''):
                return ask_interactive(local_path, remote_path)
            elif answer == 'n':
                return False
            else:
                continue

    def sync(remote_host, remote_paths, local_paths):
        tmp_dir = tempfile.mkdtemp()
        tmp_dir_local = os.path.join(tmp_dir, 'local')
        tmp_dir_remote = os.path.join(tmp_dir, 'remote')
        os.makedirs(tmp_dir_local)
        os.makedirs(tmp_dir_remote)

        for remote_path, local_path in zip(remote_paths, local_paths):
            remote_path = os.path.expanduser(remote_path)
            local_path = os.path.expanduser(local_path)
            os.system(f'scp -p {remote_host}:{remote_path} {tmp_dir_remote}')
            shutil.copy(local_path, tmp_dir_local)
            tmp_local = os.path.join(tmp_dir_local, os.path.basename(local_path))
            tmp_remote = os.path.join(tmp_dir_remote, os.path.basename(remote_path))
            os.system(f'git diff --no-index {tmp_local} {tmp_remote}')
            if ask_continue(tmp_local, tmp_remote):
                mod = os.stat(local_path).st_mode
                shutil.copy(tmp_local, local_path)
                os.chmod(local_path, mod)

    def resolve(args):
        preset = Preset()
        locals = []
        remotes = []
        for p in args.presets:
            locals.extend(preset.parse(p))
        remotes = locals

        customs = args.customs
        assert len(customs) % 2 == 0
        for i in range(0, len(customs), 2):
            remotes.append(customs[i])
            locals.append(customs[i + 1])

        sync(args.remote, remotes, locals)

    parser.set_defaults(func=resolve)
