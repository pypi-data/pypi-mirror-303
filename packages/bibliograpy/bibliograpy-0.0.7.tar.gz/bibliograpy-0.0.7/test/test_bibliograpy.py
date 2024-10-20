"""Test module for bibliograpy tool"""

from argparse import Namespace
from pathlib import Path
import pydoc
import sys

import yaml

import pytest

from bibliograpy.api import reference

from bibliograpy.process import _process

def _input_file(file: str) -> str:
    """Les fichiers d'entrée se trouvent à côté des scripts de test."""
    return str(Path(Path(__file__).parent, file))

def _output_file(file: str) -> str:
    """Les fichiers de sortie sont générés relativement à l'endroit où la commande est exécutée."""
    return str(Path(Path.cwd(), file))


def test_process_yml_to_yml():
    """test process from a yml bibliography to a yml bibliography"""

    _process(Namespace(CMD='process',
                       file=_input_file('mini.yml'),
                       output_file=_input_file('tutu_bib.yml'),
                       encoding='utf-8',
                       output='.'))

    with open(_input_file('tutu_bib.yml'), encoding='utf-8') as s:
        content = yaml.safe_load(s)
        assert content == [{
            'entry_type': 'misc',
            'cite_key': 'nasa',
            'title': 'NASA'
        },{
            'entry_type': 'misc',
            'cite_key': 'iau',
            'title': 'International Astronomical Union'
        }]

def test_process_yml_to_yml_astroloj():
    """test process from a yml bibliography to a yml bibliography"""

    _process(Namespace(CMD='process',
                       file=_input_file('astroloj.json'),
                       output_file=_input_file('astroloj.py'),
                       encoding='utf-8',
                       output='.'))

def test_process_yml_to_yml_cosmoloj():
    """test process from a yml bibliography to a yml bibliography"""

    _process(Namespace(CMD='process',
                       file=_input_file('cosmoloj.json'),
                       output_file=_input_file('cosmoloj.py'),
                       encoding='utf-8',
                       output='.'))

def test_process_yml_to_py():
    """test process from a yml bibliography to a py source bibliography"""

    _process(Namespace(CMD='process',
                       file=_input_file('mini.yml'),
                       output_file=_input_file('tutu_bib.py'),
                       encoding='utf-8',
                       output='.'))

    from tutu_bib import IAU, NASA

    @reference(IAU, NASA)
    def bib_ref_foo():
        """ma doc avec plusieurs références en varargs"""

    if sys.version_info.minor == 12:
        assert (pydoc.render_doc(bib_ref_foo) ==
"""Python Library Documentation: function bib_ref_foo in module test_bibliograpy

b\bbi\bib\bb_\b_r\bre\bef\bf_\b_f\bfo\boo\bo()
    ma doc avec plusieurs références en varargs

    Bibliography:

    * International Astronomical Union [iau]
    * NASA [nasa]
""")
    else:
        assert (pydoc.render_doc(bib_ref_foo) ==
"""Python Library Documentation: function bib_ref_foo in module test_bibliograpy

b\bbi\bib\bb_\b_r\bre\bef\bf_\b_f\bfo\boo\bo()
    ma doc avec plusieurs références en varargs
    
    Bibliography:
    
    * International Astronomical Union [iau]
    * NASA [nasa]
""")

def test_process_input_file_not_found():
    """test process input file not found"""

    with pytest.raises(FileNotFoundError) as e:
        with open(_output_file('tutu_default.yml'), encoding='utf-8') as s:
            yaml.safe_load(s)

    assert e.value.args[0] == 2
    assert e.value.args[1] == "No such file or directory"
