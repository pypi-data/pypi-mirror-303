#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: Python modules to extend the logging mechanism in Python.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2024 by Frank Brehm, Berlin
@license: LGPL3+
"""

from __future__ import print_function

import datetime
import os
import pprint
import re
import sys
import textwrap
from pathlib import Path

# Third party modules

# own modules:
__module_name__ = 'fb_logging'
__setup_script__ = Path(__file__).resolve()
__base_dir__ = __setup_script__.parent
__bin_dir__ = __base_dir__ / 'bin'
__lib_dir__ = __base_dir__ / 'lib'
__module_dir__ = __lib_dir__ / __module_name__
__init_py__ = __module_dir__ / '__init__.py'

PATHS = {
    '__setup_script__': str(__setup_script__),
    '__base_dir__': str(__base_dir__),
    '__bin_dir__': str(__bin_dir__),
    '__lib_dir__': str(__lib_dir__),
    '__module_dir__': str(__module_dir__),
    '__init_py__': str(__init_py__),
}

def pp(obj):
    """Human friendly output of data structures."""
    pprinter = pprint.PrettyPrinter(indent=4)
    return pprinter.pformat(obj)


# print("Paths:\n{}".format(pp(PATHS)))

if os.path.exists(__module_dir__) and os.path.isfile(__init_py__):
    sys.path.insert(0, os.path.abspath(__lib_dir__))

import fb_logging

from setuptools import setup

ENCODING = 'utf-8'

__packet_version__ = fb_logging.__version__

__packet_name__ = __module_name__
__debian_pkg_name__ = __module_name__.replace('_', '-')

__author__ = 'Frank Brehm'
__contact__ = 'frank@brehm-online.com'
__copyright__ = '(C) 2024 Frank Brehm, Berlin'
__license__ = 'LGPL3+'
__url__ = 'https://github.com/fbrehm/fb-logging'
__description__ = 'Python modules to extend the logging mechanism in Python.'


__open_args__ = {}
if sys.version_info[0] < 3:
    __open_args__ = {'encoding': ENCODING, 'errors': 'surrogateescape'}

# -----------------------------------
def read(fname):
    """Read in a file and return content."""
    content = None
    fn = str(fname)

    if sys.version_info[0] < 3:
        with open(fn, 'r') as fh:
            content = fh.read()
    else:
        with open(fn, 'r', **__open_args__) as fh:
            content = fh.read()

    return content


# -----------------------------------
def is_python_file(filename):
    """Evaluate, whether a file is a Pyton file."""
    fn = str(filename)
    if fn.endswith('.py'):
        return True
    else:
        return False


# -----------------------------------
__debian_dir__ = __base_dir__ / 'debian'
__changelog_file__ = __debian_dir__ / 'changelog'
__readme_file__ = __base_dir__ / 'README.md'


# -----------------------------------
def get_debian_version():
    """Evaluate current package version from Debian changelog."""
    if not __changelog_file__.is_file():
        return None
    changelog = read(__changelog_file__)
    first_row = changelog.splitlines()[0].strip()
    if not first_row:
        return None
    pattern = r'^' + re.escape(__debian_pkg_name__) + r'\s+\(([^\)]+)\)'
    match = re.search(pattern, first_row)
    if not match:
        return None
    return match.group(1).strip()


__debian_version__ = get_debian_version()

if __debian_version__ is not None and __debian_version__ != '':
    __packet_version__ = __debian_version__


# -----------------------------------
def write_local_version():
    """Write evaluated version from Debian changelog into local_version.py."""
    local_version_file = __module_dir__ / 'local_version.py'
    local_version_file_content = textwrap.dedent('''\
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
        """
        @summary: {desc}

        @author: {author}
        @contact: {contact}
        @copyright: © {cur_year} by {author}, Berlin
        """

        __author__ = '{author} <{contact}>'
        __copyright__ = '(C) {cur_year} by {author}, Berlin'
        __contact__ = {contact!r}
        __version__ = {version!r}
        __license__ = {license!r}

        # vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list
        ''')

    cur_year = datetime.date.today().year
    content = local_version_file_content.format(
        author=__author__, contact=__contact__, cur_year=cur_year,
        version=__packet_version__, license=__license__, desc=__description__)

    with local_version_file.open('wt', **__open_args__) as fh:
        fh.write(content)


# Write lib/storage_tools/local_version.py
write_local_version()

# -----------------------------------
__requirements__ = [
    'six'
]

# -----------------------------------
def read_requirements():
    """Read in and evaluate file requirements.txt."""
    req_file = __base_dir__ / 'requirements.txt'
    if not req_file.is_file():
        return

    f_content = read(req_file)
    if not f_content:
        return

    re_comment = re.compile(r'\s*#.*')
    re_module = re.compile(r'([a-z][a-z0-9_]*[a-z0-9])', re.IGNORECASE)

    for line in f_content.splitlines():
        line = line.strip()
        line = re_comment.sub('', line)
        if not line:
            continue
        match = re_module.search(line)
        if not match:
            continue
        module = match.group(1)
        if module not in __requirements__:
            __requirements__.append(module)

    # print("Found required modules: {}\n".format(pp(__requirements__)))


read_requirements()

# -----------------------------------
__scripts__ = []

def get_scripts():
    """Try to get all executable scripts and store them in __scripts__."""
    if not __bin_dir__.is_dir():
        return

    for bin_file in __bin_dir__.glob('*'):
        script = str(bin_file.relative_to(__base_dir__))
        if not bin_file.is_file():
            continue
        if not os.access(bin_file, os.X_OK):
            continue

        if script not in __scripts__:
            __scripts__.append(script)

    # print("Found scripts: {}\n".format(pp(__scripts__)))


get_scripts()


# -----------------------------------
setup(
    version=__packet_version__,
    long_description=read(__readme_file__),
    scripts=__scripts__,
    requires=__requirements__,
    package_dir={'': 'lib'},
)


# =============================================================================
# vim: fileencoding=utf-8 filetype=python ts=4 et list
