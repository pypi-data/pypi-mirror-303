# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import sys
import os
import argparse
import jureap
import ast
import traceback

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def make_wide(formatter, w=140, h=100):
    """Return a wider HelpFormatter, if possible."""
    try:
        # https://stackoverflow.com/a/5464440
        # beware: "Only the name of this class is considered a public API."
        kwargs = {"width": w, "max_help_position": h}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        warnings.warn("argparse help formatter failed, falling back.")
        return formatter


def log_parser(sp):
    sp.add_argument(
        "--input-version",
        type=jureap.metadata.major_version_type,
        default=jureap.metadata.default_input_version,
        choices=jureap.metadata.supported_input_version_array,
        help="Version of Input File",
    )
    sp.add_argument(
        "--output-version",
        type=jureap.metadata.major_version_type,
        default=jureap.metadata.default_output_version,
        choices=jureap.metadata.supported_output_version_array,
        help="Version of Log File",
    )
    sp.add_argument("--input", type=str, help="Input File")
    sp.add_argument("--output", type=str, help="Output File")
    sp.add_argument("--env", type=str, default=None, help="Environment File")


def report_parser(rp):
    rp.add_argument("--input", required=True, type=str, help="Input Directory")
    rp.add_argument("--pipeline", required=True, type=str, help="Pipeline Array")
    rp.add_argument("--prefix", required=True, type=str, help="Prefix Array")
    rp.add_argument("--workload", required=True, type=str, help="Workload Factor Array")
    rp.add_argument("--output", required=True, type=str, help="Output Report Directory")
    rp.add_argument("--tmp", type=str, help="Temporary Directory", default=os.getcwd())
    rp.add_argument("--type", choices=["jedi", "scaling"], required=True, help="Report Type")


def check_parser(sp):
    sp.add_argument("input_file", type=str, help="Result File")

def manual_parser(mp):
    mp.add_argument("--input", type=str, help="Input Directory")
    mp.add_argument("--output", type=str, help="Output Directory")

def top_level():
    parser = argparse.ArgumentParser(
        description="jureap",
        formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    lp = subparsers.add_parser(
        "log",
        help="Log Generator",
        formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
    )
    rp = subparsers.add_parser("report", help="Report Generator")

    vp = subparsers.add_parser("check", help="check Result File")
    mp = subparsers.add_parser("manual", help="Manual Generator")

    log_parser(lp)
    check_parser(vp)
    report_parser(rp)
    manual_parser(mp)
    return parser


def main():
    bin_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    root_dir = os.path.dirname(bin_dir)
    share_dir = os.path.join(root_dir, "share")

    try:
        raw_args = sys.argv[1:]
        parser = top_level()
        args = parser.parse_args(raw_args)

        if args.subcommand == "check":
            input_filename = args.input_file
            jureap.check.check(input_filename)
        elif args.subcommand == "manual":
            input_dir = args.input
            output_dir = args.output
            jureap.manual.generate(input_dir, output_dir)

        elif args.subcommand == "report":
            pipeline_array = ast.literal_eval(args.pipeline)
            prefix_array = ast.literal_eval(args.prefix)
            workload_factor_array = ast.literal_eval(args.workload)

            jureap.report.generate(
                args.type,
                args.input,
                pipeline_array,
                prefix_array,
                workload_factor_array,
                args.output,
                share_dir,
                args.tmp,
            )
        elif args.subcommand == "log":
            if args.env == None:
                environment = os.environ
            else:
                environment = jureap.detail.env_file_to_dict(args.env)

            jureap.log.log(
                args.input, args.output, environment, args.input_version, args.output_version
            )
        else:
            print("Usage Error: Subcommand " + args.subcommand + " not implemented yet.")
            exit(os.EX_USAGE)
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        print(bcolors.FAIL + "DATA ERROR: " + str(e) + bcolors.ENDC)
        exit(os.EX_DATAERR)

    exit(os.EX_OK)
