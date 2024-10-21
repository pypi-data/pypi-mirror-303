# SPDX-FileCopyrightText: 2023 Samsung Electronics Co., Ltd
#
# SPDX-License-Identifier: BSD-3-Clause

import argparse
import sys
import textwrap
import traceback
from pathlib import Path
from typing import List, NoReturn

from spex.jsonspec.lint import Code
from spex.jsonspec.parserargs import ParserArgs
from spex.log import ULog, logger
from spex.parse import parse_spec
from spex.validate import validate_json


def arg_input(arg: str) -> Path:
    p = Path(arg)
    if not p.exists():
        raise RuntimeError(f"no file at '{p}'")
    elif not p.is_file():
        raise RuntimeError(f"path '{p}' exists, but is not a file")
    return p


def arg_output(arg: str) -> Path:
    p = Path(arg)
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
    if not p.is_dir():
        raise RuntimeError("output must be a directory (or omitted)")

    return p


def arg_lintcode(arg: str) -> List[Code]:
    return [Code[c.strip().upper()] for c in arg.split(",")]


class CliParser(argparse.ArgumentParser):
    def error(self, message: str) -> NoReturn:
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        sys.exit(2)


def main() -> None:
    lint_codes = "\n".join(f"      * {entry.name}  - {entry.value}" for entry in Code)
    epilog = textwrap.dedent(
        f"""
    Notes:
    ~~~~~~
    * Linting:
      During production of the NVMe-model, a number of linting codes are raised.
      These signify potential and definite issues encountered when parsing the
      source HTML model, in turn derived from the docx specification document.

      You may choose to ignore classes of errors during processing.
      For instance, to ignore lint errors of code T1000 and T1001, add the
      following to your command: `--lint-ignore=T1000,T1001`.

      The linting codes, and their general meaning, are as follows:
      ---
{lint_codes}
      ---
    * output:
      if `output` is a directory, then any output(s) generated from processing
      (NVMe (JSON) models, HTML models, CSS files) will be placed in the
      specified directory. If `output` is omitted, files will be placed into the
      current working directory.
    """
    )
    cli_parser = CliParser(
        description="Extract data-structures from .docx spec or HTML model",
        epilog=epilog,
        prog="spex",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    cli_parser.add_argument(
        "-s",
        "--skip-figure-on-error",
        default=False,
        dest="skip_fig_on_error",
        action="store_true",
        help=(
            "If processing a figure fails, do not abort,"
            " but skip it and continue processing the remaining figures"
        ),
    )
    cli_parser.add_argument(
        "input",
        nargs="+",
        type=arg_input,
        help=(
            "One or more .docx specifications"
            " or HTML models to extract data-structures from"
        ),
    )
    cli_parser.add_argument(
        "-o",
        "--output",
        type=arg_output,
        default=None,
        help="path to directory where the resulting file(s) should be stored.",
    )
    cli_parser.add_argument(
        "--validate-json", action=argparse.BooleanOptionalAction, default=False
    )
    cli_parser.add_argument(
        "-v", "--verbose", action=argparse.BooleanOptionalAction, default=False
    )
    cli_parser.add_argument("--lint-ignore", type=arg_lintcode, default=[])

    args = cli_parser.parse_args()

    # if no explicit output directory is specified, use the current working directory
    if args.output is None:
        args.output = Path.cwd()

    pargs = ParserArgs(
        output_dir=args.output or Path.cwd(),
        skip_fig_on_error=args.skip_fig_on_error,
        lint_codes_ignore=args.lint_ignore,
        validate_json=args.validate_json,
        verbose=args.verbose,
    )

    try:
        for spec in args.input:
            logger.log(ULog.INFO, f"parsing '{spec}'...")
            if spec.suffix == ".json":
                # lint code filtering is applied at the point of writing the lint errors
                # into the resulting NVMe (JSON) model.
                sys.stderr.write(
                    "cannot operate on NVMe model (JSON), "
                    "requires the HTML model or docx spec as input\n"
                )
                sys.stderr.flush()
                sys.exit(1)

            if spec.suffix not in (".html", ".docx"):
                sys.stderr.write(
                    f"invalid input file ({spec!s}), "
                    "requires a HTML model or the docx specification file\n"
                )
                sys.stderr.flush()
                sys.exit(1)

            parser = parse_spec(Path(spec), pargs, yield_progress=False)
            try:
                while True:
                    next(parser)
            except StopIteration as e:
                if args.validate_json and e.value is not None:
                    validate_json(e.value)

    except Exception:
        logger.exception("unhandled exception bubbled up to top-level")

        logger.log(
            ULog.ERROR,
            "\n  ".join(
                [
                    "Program exited in error!",
                    "",
                    "This typically happens if spex failed to parse one or "
                    "more figures.",
                    "Check the log messages above to see which figures are "
                    "causing errors.",
                    "",
                    "If you believe Spex *should* be able to parse this figure"
                    " - and that",
                    "it is not simply a matter of changing to the "
                    "figure to follow conventions",
                    "then perhaps a bug report for Spex is in order.",
                    "When filing the bug report, please attach the `spex.log` "
                    "file which resides",
                    "in this directory.",
                    "Note that the `spex.log` file is rewritten on each execution",
                    "",
                ]
            ),
        )
        if pargs.verbose:
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
