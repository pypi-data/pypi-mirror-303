#!/usr/bin/env python3
"""
Command line utility that helps migrating Brick files to a newer version
"""
from pathlib import Path
import itertools
import os
import tempfile
import json
import urllib.request
import zipfile
from io import BytesIO
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from rebrick import __version__, get_error_strings
from rebrick.Core import BrickContext, parseFromFile, analyze, StringVector, DocumentVector
from rebrick.migrations import collect_migrations, ReplaceOp
from rebrick.versionaction import VersionAction

def download_package_version(package_name, version):
    """Download a specific version of a package from PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    with urllib.request.urlopen(url, timeout=16) as response:
        content = response.read().decode('utf-8')
    data = json.loads(content)
    return data['urls'][0]['url']

def unzip_package(url, extract_to):
    """Download and unzip a package."""
    with urllib.request.urlopen(url, timeout=32) as response:
        file_data = BytesIO(response.read())
    with zipfile.ZipFile(file_data) as zip_file:
        zip_file.extractall(extract_to)

def parse_args():
    parser = ArgumentParser(description="Migrates a .brick file from an older to a newer version", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("brickfile", metavar="path", help="the .brick file or directory to migrate")
    parser.add_argument("--version", help="Show version", action=VersionAction, nargs=0, default=SUPPRESS)
    parser.add_argument("--from-version", help="Version to convert from", required=True)
    parser.add_argument("--to-version", help="Version to convert to", default=__version__)
    return parser.parse_known_args()

def parse_and_analyze(brickfile, brick_context):
    parse_result = parseFromFile(str(Path(brickfile).absolute()), brick_context)

    analyze(brick_context, None)

    documents = DocumentVector()
    documents.push_back(parse_result[0])
    return documents

def has_errors(brick_context):
    if brick_context.hasErrors():
        error_strings = get_error_strings(brick_context.getErrors())
        for e_s in error_strings:
            print(e_s)
        return True
    return False

def refactor_brick_file(brickfile, bundle_path_vec, from_version, to_version) -> bool:
    print(f"Migrating {brickfile} from {from_version} to {to_version}")
    brick_context = BrickContext(bundle_path_vec)
    migrations = collect_migrations(from_version, to_version)

    documents = parse_and_analyze(brickfile, brick_context)

    if has_errors(brick_context):
        return False

    print(f"Found {len(migrations)} migrations ", [m.__name__ for m in migrations])

    order_group = [(key, list(group)) for key, group in itertools.groupby(migrations, lambda m: m.brick_order)]
    order_group.sort(key=lambda pair: pair[0])

    for _, migration_group in order_group:
        ops = []
        for migration in migration_group:
            ops.extend(migration(documents))

        for key, op_group in itertools.groupby(ops, lambda op: op.path):
            if Path(brickfile).samefile(key):
                with open(key, 'r', encoding="utf8") as file:
                    lines = file.readlines()
                lines = ReplaceOp.apply_many(op_group, lines)
                with open(key, 'w', encoding="utf8") as file:
                    file.writelines(lines)
    return True

def run_brick_migrate(args):

    package_name = 'brickbundles'

    # Download the package
    url = download_package_version(package_name, args.from_version)
    if url is None:
        print(f"Could not find the source distribution for {package_name}=={args.from_version}.")
        return

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = str(Path(os.path.realpath(tmpdirname)).absolute())
        print(f"Extracting to temporary directory: {tmp_path}")
        unzip_package(url, tmp_path)
        print(f"Package {package_name}=={args.from_version} extracted to {tmp_path}")
        bundle_path = str((Path(tmp_path) / 'brickbundles').absolute())

        print(f'Using bundle path {bundle_path}')
        print(os.listdir(bundle_path))

        bundle_path_vec = StringVector()
        bundle_path_vec.push_back(bundle_path)
        success = True
        # Apply the refactoring
        if os.path.isdir(args.brickfile):
            for root, _, files in os.walk(args.brickfile):
                for file in files:
                    if file.endswith(".brick") and not file.endswith("config.brick"):
                        brickfile = os.path.join(root, file)
                        if not refactor_brick_file(brickfile, bundle_path_vec, args.from_version, args.to_version):
                            success = False
        else:
            if not refactor_brick_file(args.brickfile, bundle_path_vec, args.from_version, args.to_version):
                success = False
        if success:
            print(f"Refactor from {args.from_version} to {args.to_version} complete!")
        else:
            print(f"Refactor from {args.from_version} to {args.to_version} failed due to errors!")
            print("Note, some files might have been partially migrated.")

if __name__ == '__main__':
    arguments, _ = parse_args()
    run_brick_migrate(arguments)
