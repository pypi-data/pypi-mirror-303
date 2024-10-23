#!/usr/bin/env python3
"""
Command line utility that helps converting AGX files to Brick files.
"""
import os
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import agx
import agxIO
import agxSDK
from rebrick import AgxToBrickMapper, __version__, set_log_level
from rebrick.versionaction import VersionAction

init = agx.AutoInit()


def parse_args():
    parser = ArgumentParser(description="Convert .agx and .aagx files to .brick", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("agxfile", help="the .agx or .aagx file to load")
    parser.add_argument("--root-system-name", metavar="<root system name>", help="Override the name of the root system model")
    parser.add_argument("--export-folder", metavar="<export folder>", help="Where to write exported trimesh:es", default="./")
    parser.add_argument("--loglevel", choices=["trace", "debug", "info", "warn", "error", "critical", "off"], help="Set log level", default="info")
    parser.add_argument("--version", help="Show version", action=VersionAction, nargs=0, default=SUPPRESS)
    parser.add_argument("--realprecision", help="Set precision of generated real values", type=int, default=6)
    return parser.parse_known_args()


def run():
    args, _ = parse_args()
    set_log_level(args.loglevel)
    simulation = agxSDK.Simulation()
    assembly = agxSDK.AssemblyRef(agxSDK.Assembly())
    if args.root_system_name is not None:
        assembly.setName(args.root_system_name)
    agxIO.readFile(args.agxfile, simulation, assembly.get())

    # Export trimeshes relative to the current directory
    export_folder = args.export_folder if os.path.isabs(args.export_folder) else os.path.join(os.getcwd(), args.export_folder)
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    mapper = AgxToBrickMapper(export_folder, True, args.realprecision)
    if ".agx" in args.agxfile:
        output_file = os.path.basename(args.agxfile.replace(".agx", ".brick"))
    elif ".aagx" in args.agxfile:
        output_file = os.path.basename(args.agxfile.replace(".aagx", ".brick"))
    else:
        sys.exit("Invalid file format. Only .agx and .aagx files are supported.")


    print("writing to", output_file)
    with open(output_file, "w", encoding="utf8") as file:
        file.writelines(mapper.assemblyToBrick(assembly))

if __name__ == '__main__':
    run()
