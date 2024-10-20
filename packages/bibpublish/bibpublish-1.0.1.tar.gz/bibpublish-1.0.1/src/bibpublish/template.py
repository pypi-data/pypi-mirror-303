"""
Implements the template mechanism used for translating templates to
the corresponding output documents.
"""

import importlib
import os
import os.path
from pathlib import Path

from bibpublish.entry import Entry

TEMPLATE_PATH = "bibpublish.templates."


class Template:

    def __init__(self, template_name, bibtex_entries, output_dir: Path):
        self.template = importlib.import_module(TEMPLATE_PATH + template_name)
        self.bibtex_entries = bibtex_entries

        # setup output infrastructure
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # setup infrastructure for supplemental material
        self.supplemental_material = self.template.SupplementalMaterial(output_dir)

    def _load_template(self, section, template_type):
        return open(
            os.path.join(self.template.TEMPLATE_PATH, section + template_type)
        ).read()

    def _get_relevant_entries(self, section):
        return sorted(
            [entry for entry in self.bibtex_entries if entry["ENTRYTYPE"] == section],
            key=lambda x: x["year"],
            reverse=True,
        )

    def generate_section(self, section):
        output = [self._load_template(section, "-head.tmpl")]
        entry_template = self._load_template(section, "-entry.tmpl")
        for entry in self._get_relevant_entries(section):
            entry = Entry(self.template).format_entry(entry)
            output.append(entry_template.format(**entry))

            # set citation key
            entry["citation"] = entry["entry_" + section]
            self.supplemental_material.generate(entry)
        output.append(self._load_template(section, "-foot.tmpl"))
        return output

    def generate_output(self):
        output = [self._load_template("", "head.tmpl")]
        for section in self.template.ENTRY_ORDER:
            output.extend(self.generate_section(section))
        output.append(self._load_template("", "foot.tmpl"))

        output = "\n".join(output)
        # cleanup
        output = output.replace("..", ".").replace(" . ", ". ")
        with open(os.path.join(self.output_dir, self.template.OUTFILE), "w") as f:
            f.write(output)
