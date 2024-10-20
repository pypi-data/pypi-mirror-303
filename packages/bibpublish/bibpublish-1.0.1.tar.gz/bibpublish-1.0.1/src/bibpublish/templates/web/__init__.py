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
import os
from pathlib import Path

TEMPLATE_PATH = (Path(__file__)).parent


# name of the main output file
OUTFILE = "index.html"

ENTRY_ORDER = (
    "article",
    "inproceedings",
    "incollection",
    "book",
    "techreport",
    "phdthesis",
    "mastersthesis",
    "unpublished",
)

ATTRIBUTE_CLEANUP_RULES = {
    "--": "-",
    "\\&": "&amp",
    "\n": " ",
    "{": "",
    "}": "",
    "\\_": "_",
}

ATTRIBUTE_FORMAT = {
    "ID": "{ID}",
    "author": '<span class="author">{author}</span>',
    "editor": '<span class="editor">, Ed. {editor}</span>',
    "title": '<span class="title" title="{title}">“{f"""<a href="{eprint}">'
    '{title}</a>""" if "eprint" in locals() else title}”</span>',
    "year": '<span class="year">{year}</span>',
    "volume": ', <span class="volume">{volume}</span>',
    "number": '(<span class="number">{number}</span>)',
    "pages": ':<span class="pages">{pages}</span>',
    "journal": '<span class="booktitle">{journal}</span>',
    "doi": '. doi: <span class="doi"><a href="https://doi.org/{doi}">{doi}</a></span>.',
    "booktitle": ' <span class="booktitle">{booktitle}</span>',
    "address": ', <span class="address">{address}</span>',
    "publisher": '<span class="publisher">:{publisher}</span>',
    "school": '<span class="school">{school}</span>',
    "type": "{type}",
    "date": "{date}",
    "location": "{location}",
    "eprint": "{eprint}",
    "note": ", {note}",
    "event_name": "{note}",
    "coins": "",
    "keywords": "{keywords}",
    "abstract": "{abstract}",
    "abstract_title": "Abstract: {title}",
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
    "{_volume}{_number}{_pages}{_note}{_doi}",
    "inproceedings": "{_author}. ({_year}). {_title}. {_booktitle}" "{_address}{_note}",
    "incollection": "{_author}. ({_year}). {_title}. {_booktitle}"
    "{_address}{_publisher}{_pages}{_doi}",
    "book": "{_author}. ({_year}). {_title}. {_publisher}{_address}",
    # talks
    "unpublished": "{_title} ({_year}). {_type}. {_event_name}. {_location}. {_date}",
    "phdthesis": "{_author}. ({_year}). {_title}, {_school}",
    "mastersthesis": "{_author}. ({_year}). {_title}, {_school}",
    "techreport": "{_author}. ({_year}). {_title}. {_journal}"
    "{_volume}{_number}{_pages}{_note}",
}


#
# class used for publishing supplemental material
#
#
# class used for publishing supplemental material
#
class SupplementalMaterial:

    def __init__(self, output_path: Path):
        # setup output directories
        self.output_path_abstracts = output_path / "abstract"
        self.output_path_abstracts.mkdir(parents=True, exist_ok=True)
        self.output_path_bib = output_path / "bib"
        self.output_path_bib.mkdir(parents=True, exist_ok=True)
        print("**", output_path, self.output_path_abstracts, self.output_path_bib)

        # read abstracts template
        self.abstract_template = (TEMPLATE_PATH / "abstract.tmpl").read_text()

    def generate(self, entry):
        self.generate_abstract(entry)
        self.generate_bibtex(entry)

    def generate_abstract(self, entry):
        if "abstract" in entry:
            locals().update(entry)
            with (self.output_path_abstracts / (entry["ID"] + ".html")).open("w") as f:
                f.write(eval("f'''" + self.abstract_template + "'''"))

    def generate_bibtex(self, entry):
        with (self.output_path_bib / (entry["ID"] + ".bib")).open("w") as f:
            f.write("@" + entry["ENTRYTYPE"] + "{" + entry["ID"] + ",\n")
            entries = [
                "   {} = {{{}}}".format(key, value)
                for key, value in sorted(entry.items())
                if key not in ("ENTRYTYPE", "ID", "citation") and "_" not in key
            ]
            f.write(",\n".join(entries))
            f.write("\n}")
