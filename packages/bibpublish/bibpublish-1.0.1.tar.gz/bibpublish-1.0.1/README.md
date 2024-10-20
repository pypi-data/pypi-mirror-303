bibpublish
==========
bibpublish uses templates for publishing BibTex bibliographies in different formats such as HTML and LaTeX:

```bash
Usage: bibpublish [options]

Options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir=OUTPUT_DIR
                        output directory.
  -t TEMPLATE, --template=TEMPLATE
                        template to use (wordpress).
  -f FILTER, --filter=FILTER
                        one consider items that match the given
                        filter criterion.
```

Example
-------
Publish all BibTex entries that have been published after 2014:

```bash
bibpublish mybib.bib -f 'int(year) > 2014'
```

Installation
------------
I recommend using pipx to install bibpublish::

  pipx install bibpublish


Supported templates
-------------------

- latex: Used for integrating bibliographies into the CV
- snf: Creates an HTML file which is meant for import into a word processing software.
- web: Template used for the Web page. Creates the publication HTML and supporting files (abstracts and bibtex fiels).
- wordpress: Legacy version of the web template (without doi support).


Background
----------
bibPublish is a Python 3+ compatible replacement for `bibTexSuite <https://github.com/AlbertWeichselbraun/bibTexSuite>`_.
