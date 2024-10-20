"""
bibliograpy process module
"""
import json
import logging
from argparse import Namespace
from pathlib import Path
from typing import Any

import yaml

from bibliograpy.api import Misc, TechReport, Unpublished, Proceedings, Article, Book, Booklet, Inbook, Conference, \
    Manual, Mastersthesis, Incollection, Inproceedings, Phdthesis, Reference

LOG = logging.getLogger(__name__)

_TYPES: dict[str, type[Reference]] = {
    'article': Article,
    'book': Book,
    'booklet': Booklet,
    'inbook': Inbook,
    'incollection': Incollection,
    'inproceedings': Inproceedings,
    'conference': Conference,
    'manual': Manual,
    'mastersthesis': Mastersthesis,
    'misc': Misc,
    'phdthesis': Phdthesis,
    'proceedings': Proceedings,
    'techreport': TechReport,
    'unpublished': Unpublished
}

def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    in_extension = ns.file.split('.')[-1]
    output_dir = Path(Path.cwd(), ns.output)
    output_file = ns.output_file
    out_extension = output_file.split('.')[-1]

    LOG.info('open configuration file %s', ns.file)
    with open(ns.file, encoding=ns.encoding) as s:

        if in_extension == 'yml':
            content = yaml.safe_load(s)
        elif in_extension == 'json':
            content = json.load(s)
        else:
            raise ValueError(f'unsupported configuration format {in_extension}')

        with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
            if out_extension == 'py':

                scope: dict[str, Any] = {}

                o.write('from bibliograpy.api import *\n')
                o.write('\n')
                for ref in content:
                    if ref['entry_type'] in _TYPES:
                        o.write(f"{_TYPES[ref['entry_type']].from_dict(ref, scope).to_source_bib()}\n")
            elif out_extension in ['yml', 'yaml']:
                yaml.dump(content, o, sort_keys=False)
