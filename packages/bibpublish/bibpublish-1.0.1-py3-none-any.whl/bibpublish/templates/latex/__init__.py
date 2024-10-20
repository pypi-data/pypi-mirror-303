#!/usr/bin/env python

"""
bibpublish template configuration

Template namespaces:
    - fieldname: the original value of a variable
    - _fieldname: the formatted value of the variable based on the specified
                  ATTRIBUTE_FORMAT
    - link_fieldname: formatting of urls based on LINK_FORMAT
    - entry_fieldname: formatting of entries based on ENTRY_FORMAT
"""
import os.path

TEMPLATE_PATH = os.path.dirname(__file__)

# name of the main output file
OUTFILE = "publications.tex"

ENTRY_ORDER = (
    "article",
    "inproceedings",
    "incollection",
    "book",
    "phdthesis",
    "mastersthesis",
)

ATTRIBUTE_CLEANUP_RULES = {}

ATTRIBUTE_FORMAT = {
    "ID": "{ID}",
    "author": "{author}",
    "editor": ", Ed. {editor}",
    "title": "\\emph{{{title}}}",
    "year": "{year}",
    "volume": ", {volume}",
    "number": "({number})",
    "pages": ":{pages}",
    "journal": "{journal}",
    "booktitle": " {booktitle}",
    "address": ", {address}",
    "publisher": ":{publisher}",
    "school": "{school}",
    "eprint": "{eprint}",
    "note": ", {note}",
    "coins": "",
    "keywords": "{keywords}",
    "abstract": "{abstract}",
}

# links: accessible via link.fieldname
LINK_FORMAT = {
    "eprint": '<a class="download" title="{title}" href="{eprint}">' "[PDF]</a>",
    "abstract": '<a class="abstract" title="Abstract" '
    'target="_blank" href="abstract/{ID}.html">'
    "[Abstract]</a>",
    "ID": '<a class="bib" target="_blank" title="Citation"'
    'href="bib/{ID}.bib">[BIB]</a>',
}

#
# entries: accessible via entry.fieldname
ENTRY_FORMAT = {
    "article": "{_author}. ({_year}). {_title}. {_journal}"
    "{_volume}{_number}{_pages}{_note}",
    "inproceedings": "{_author}. ({_year}). {_title}. {_booktitle}" "{_address}{_note}",
    "incollection": "{_author}. ({_year}). {_title}. {_booktitle}"
    "{_address}{_publisher}{_pages}",
    "book": "{_author}. ({_year}). {_title}. {_publisher}{_address}",
    "unpublished": "{_author}. ({_year}). {_title}{_note}",
    "phdthesis": "{_author}. ({_year}). {_title}, {_school}",
    "mastersthesis": "{_author}. ({_year}). {_title}, {_school}",
}


#
# class used for publishing supplemental material
#
class SupplementalMaterial:

    def __init__(self, output_dir):
        pass

    def generate(self, entry):
        pass
