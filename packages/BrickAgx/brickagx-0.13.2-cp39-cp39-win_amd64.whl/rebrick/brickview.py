#!/usr/bin/env python3
"""
Command line utility that loads Brick files and loads them into an AGX Simulation
"""
import os
import sys
import signal
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Action, SUPPRESS
import agxOSG
from brickbundles import bundle_path

# Import useful utilities to access the current simulation, graphics root and application
from agxPythonModules.utils.environment import init_app, simulation, application, root

from rebrick import InputSignalListener, OutputSignalListener, OsgClickAdapter
from rebrick import load_brick_file, addVisuals, addDeformableVisualUpdaters, __version__, set_log_level, add_file_changed_listener
from rebrick.migration_hint import check_migration_hint
from rebrick.versionaction import VersionAction


class AgxHelpAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        start_agx()
        sys.exit(0)


def parse_args():
    parser = ArgumentParser(description="View brick models", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("brickfile", help="the .brick file to load")
    parser.add_argument("[AGX flags ...]", help="any additional AGX flags", default="", nargs="?")
    parser.add_argument(
        "--bundle-path",
        help="list of path to bundle dependencies if any. Overrides environment variable BRICK_BUNDLE_PATH.",
        metavar="<bundle_path>",
        default=bundle_path(),
    )
    parser.add_argument("--click-addr", type=str, help="Address for Click to listen on, e.g. ipc:///tmp/click.ipc", default="tcp://*:5555")
    parser.add_argument("--debug-render-frames", action="store_true", help="enable rendering of frames for mate connectors and rigid bodies.")
    parser.add_argument("--enable-click", help="Enable sending and receiving signals as Click Messages", action="store_true", default=SUPPRESS)
    parser.add_argument("--loglevel", choices=["trace", "debug", "info", "warn", "error", "critical", "off"], help="Set log level", default="info")
    parser.add_argument("--modelname", help="The model to load (defaults to last model in file)", metavar="<name>", default="")
    parser.add_argument("--reload-on-update", help="Reload scene automatically when brickfile is updated", action="store_true", default=SUPPRESS)
    parser.add_argument("--usage", help="Show AGX specific help", action=AgxHelpAction, nargs=0, default=SUPPRESS)
    parser.add_argument("--version", help="Show version", action=VersionAction, nargs=0, default=SUPPRESS)
    return parser.parse_known_args()


class AllowCtrlBreakListener(agxOSG.ExampleApplicationListener):
    pass


def buildScene():  # pylint: disable=invalid-name

    args, extra_args = parse_args()
    set_log_level(args.loglevel)
    if extra_args:
        print(f"Passing these args to AGX: {(' ').join(extra_args)}")

    result = load_brick_file(simulation(), args.brickfile, args.bundle_path, args.modelname)

    check_migration_hint(args.brickfile, result.errors())

    assembly = result.assembly()
    brick_scene = result.brick_object()

    # Add signal listeners so that signals are picked up from inputs
    input_signal_listener = InputSignalListener(assembly)
    output_signal_listener = OutputSignalListener(assembly, brick_scene)

    simulation().add(input_signal_listener, InputSignalListener.RECOMMENDED_PRIO)
    simulation().add(output_signal_listener, OutputSignalListener.RECOMMENDED_PRIO)

    # Add click listeners unless this is scene-reload, in that case we want to keep our listeners
    # Note that we use globals() since this whole file is reloaded on scene-reload by AGX, so no local globals are kept
    if "click_adapter" not in globals():
        globals()["click_adapter"] = OsgClickAdapter()
        application().addListener(AllowCtrlBreakListener())

        if "reload_on_update" in args:
            print(f"Will reload scene when {args.brickfile} is updated")
            add_file_changed_listener(application(), args.brickfile)

    if "enable_click" in args:
        click_adapter = globals()["click_adapter"]
        click_adapter.add_listeners(application(), simulation(), args.click_addr, brick_scene, output_signal_listener)

    if not addVisuals(result, root(), args.debug_render_frames):
        application().setEnableDebugRenderer(True)
    simulation().add(assembly.get())
    addDeformableVisualUpdaters(result, root())


def ctrl_break_handler(_signum, _frame):
    # Unfortunately os._exit(0) doesn't cut it on Windows, so we're doing the kill to make sure we exit on Windows as well.
    if os.name == "nt":
        os.kill(os.getpid(), 9)
    else:
        application().stop()


def on_shutdown(_):
    if os.name == "nt":
        os.kill(os.getpid(), 9)
    else:
        os._exit(0)


def start_agx():
    # Tell AGX to run this file, even if run was called from another file
    sys.argv[0] = __file__
    # pylint: disable=W0612 # Unused variable 'init'
    # Use __main__ otherwise AGX will just skip the init
    init = init_app(name="__main__", scenes=[(buildScene, "1")], autoStepping=True, onShutdown=on_shutdown)  # Default: False


def run():
    signal.signal(signal.SIGINT, ctrl_break_handler)
    parse_args()
    start_agx()


if __name__ == "__main__":
    run()
