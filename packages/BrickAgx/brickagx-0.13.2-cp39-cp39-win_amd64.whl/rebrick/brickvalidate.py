#!/usr/bin/env python3
"""
Command line utility that validates Brick files and prints the result to stdout.
"""
import os
import signal
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import agxOSG
import agxSDK
import agx
from brickbundles import bundle_path
from rebrick import load_brick_file, __version__, set_log_level
from rebrick.migration_hint import check_migration_hint
from rebrick.versionaction import VersionAction

def parse_args():
    parser = ArgumentParser(description="View brick models", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("brickfile", help="the .brick file to load")
    parser.add_argument("--bundle-path", help="list of path to bundle dependencies if any. Overrides environment variable BRICK_BUNDLE_PATH.",
                        metavar="<bundle_path>", default=bundle_path())
    parser.add_argument("--debug-render-frames", action='store_true', help="enable rendering of frames for mate connectors and rigid bodies.")
    parser.add_argument("--loglevel", choices=["trace", "debug", "info", "warn", "error", "critical", "off"], help="Set log level", default="warn")
    parser.add_argument("--modelname", help="The model to load (defaults to last model in file)", metavar="<name>", default="")
    parser.add_argument("--version", help="Show version", action=VersionAction, nargs=0, default=SUPPRESS)
    return parser.parse_args()

class AllowCtrlBreakListener(agxOSG.ExampleApplicationListener):
    pass

def validate():

    args = parse_args()
    set_log_level(args.loglevel)

    _ = agx.init()
    simulation = agxSDK.Simulation()

    result = load_brick_file(simulation, args.brickfile, args.bundle_path, args.modelname)
    check_migration_hint(args.brickfile, result.errors())

    if len(result.errors()) == 0:
        sys.exit(0)
    else:
        sys.exit(255)

def handler(_signum, _frame):
    os._exit(0)

def run():
    signal.signal(signal.SIGINT, handler)
    validate()

if __name__ == '__main__':
    run()
