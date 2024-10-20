#!/usr/bin/env python3

"""
bibpublish - publishes bibtex files

(C)opyrights 2020-2024 Albert Weichselbraun
"""

import sys
from pathlib import Path

import bibtexparser
from bibtexparser.bparser import BibTexParser
from optparse import OptionParser

from bibpublish.template import Template

DEFAULT_TEMPLATE = "wordpress"


def get_parser():
    """parses the options specified by the user"""
    parser = OptionParser()
    parser.add_option(
        "-o", "--output-dir", dest="output_dir", default=".", help="output directory."
    )
    parser.add_option(
        "-t",
        "--template",
        dest="template",
        default=DEFAULT_TEMPLATE,
        help=f"template to use ({DEFAULT_TEMPLATE}).",
    )
    parser.add_option(
        "-f",
        "--filter",
        dest="filter",
        default="True",
        help="one consider items that match the given filter" "criterion.",
    )
    return parser


def cli():
    parser = get_parser()
    options, args = parser.parse_args()
    if len(args) == 0:
        parser.print_help()
        sys.exit()

    parser = BibTexParser()
    parser.add_missing_from_crossref = True
    with open(args[0]) as bibfile:
        # only consider entries that match the given filter criteria
        bibtex_entries = []
        for entry in bibtexparser.load(bibfile, parser).entries:
            locals().update(**entry)
            if eval(options.filter):
                bibtex_entries.append(entry)

        template = Template(options.template, bibtex_entries, Path(options.output_dir))
        template.generate_output()


"""
MAIN
"""
if __name__ == "__main__":
    cli()
