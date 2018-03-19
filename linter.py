#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Michał Sochoń
# Copyright (c) 2017 Michał Sochoń
#
# License: MIT
#

"""This module exports the AnsibleReview plugin class."""

from SublimeLinter.lint import Linter, util
import re
import logging
logger = logging.getLogger('SublimeLinter.plugin.ansbile-review')


class AnsibleReview(Linter):
    """Provides an interface to ansible-review."""

    # ansbile-lint verison requirements check
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.13.4'

    # linter settings
    cmd = ('ansible-review', '${file}')
    regex = r'^.+:(?P<line>\d+): \[(?P<error>.+)\] (?P<message>.+)'
    # -p generate non-multi-line, pep8 compatible output
    multiline = False

    # ansible-lint does not support column number
    word_re = False
    line_col_base = (1, 1)

    tempfile_suffix = 'yml'
    error_stream = util.STREAM_STDOUT

    defaults = {
        'selector': 'source.ansible',
        'args': '',  # '-v -q'
        '-c': '',
        '-d': '',
        '-r': '',
        '-s': '',
    }
    inline_overrides = ['c', 'd', 'r', 's']
