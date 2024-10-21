#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@summary: General used functions an objects used for unit tests on the logging python modules.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2024 Frank Brehm, Berlin
@license: AGPL
"""

import argparse
import logging
import os
import platform
import pprint
import re
import sys
import textwrap
from logging import Formatter
try:
    import unittest2 as unittest
except ImportError:
    import unittest


# =============================================================================

LOG = logging.getLogger(__name__)


# =============================================================================
def get_arg_verbose():
    """Get and return command line arguments."""
    arg_parser = argparse.ArgumentParser()

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '-v', '--verbose', action='count',
        dest='verbose', help='Increase the verbosity level')
    args = arg_parser.parse_args()

    return args.verbose


# =============================================================================
def init_root_logger(verbose=0, appname=None):
    """Initialize the root logger."""
    from fb_logging import WARNING, NOTICE, INFO, TRACE

    root_log = logging.getLogger()
    root_log.setLevel(TRACE)

    logging.addLevelName(TRACE, 'TRACE')
    logging.addLevelName(NOTICE, 'NOTICE')

    log_lvl = WARNING
    if verbose:
        log_lvl = INFO
        if verbose > 1:
            log_lvl = 5

    if appname:
        appname = str(appname).strip()
    if not appname:
        appname = os.path.basename(sys.argv[0])

    app_logger = logging.getLogger(appname)
    app_logger.setLevel(log_lvl)
    format_str = appname + ': '
    if verbose:
        if verbose > 1:
            format_str += '%(name)s(%(lineno)d) %(funcName)s() '
        else:
            format_str += '%(name)s '
    format_str += '%(levelname)s - %(message)s'
    formatter = None
    formatter = Formatter(format_str)

    # create log handler for console output
    lh_console = logging.StreamHandler(sys.stderr)
    # if verbose:
    #     lh_console.setLevel(DEBUG)
    # else:
    #     lh_console.setLevel(INFO)
    lh_console.setFormatter(formatter)

    app_logger.addHandler(lh_console)


# =============================================================================
def pp(value, indent=4, width=99, depth=None):
    """
    Return a pretty print string of the given value.

    @return: pretty print string
    @rtype: str
    """
    pretty_printer = pprint.PrettyPrinter(
        indent=indent, width=width, depth=depth)
    return pretty_printer.pformat(value)


# =============================================================================
def terminal_can_colors(debug=False):
    """
    Detect, whether the current terminal is able to perform ANSI color sequences.

    Both stdout and stderr are checked.

    @return: both stdout and stderr can perform ANSI color sequences
    @rtype: bool

    """
    cur_term = ''
    if 'TERM' in os.environ:
        cur_term = os.environ['TERM'].lower().strip()

    colored_term_list = (
        r'ansi',
        r'linux.*',
        r'screen.*',
        r'[xeak]term.*',
        r'gnome.*',
        r'rxvt.*',
        r'interix',
    )
    term_pattern = r'^(?:' + r'|'.join(colored_term_list) + r')$'
    re_term = re.compile(term_pattern)

    ansi_term = False
    env_term_has_colors = False

    if cur_term:
        if cur_term == 'ansi':
            env_term_has_colors = True
            ansi_term = True
        elif re_term.search(cur_term):
            env_term_has_colors = True
    if debug:
        sys.stderr.write('ansi_term: {a!r}, env_term_has_colors: {h!r}\n'.format(
            a=ansi_term, h=env_term_has_colors))

    has_colors = False
    if env_term_has_colors:
        has_colors = True
    for handle in [sys.stdout, sys.stderr]:
        if (hasattr(handle, 'isatty') and handle.isatty()):
            if debug:
                msg = '{} is a tty.'.format(handle.name)
                sys.stderr.write(msg + '\n')
            if (platform.system() == 'Windows' and not ansi_term):
                if debug:
                    sys.stderr.write('Platform is Windows and not ansi_term.\n')
                has_colors = False
        else:
            if debug:
                msg = '{} is not a tty.'.format(handle.name)
                sys.stderr.write(msg + '\n')
            if ansi_term:
                pass
            else:
                has_colors = False

    return has_colors


# =============================================================================
class FbLoggingTestcase(unittest.TestCase):
    """Base test case for all testcase classes of this package."""

    # -------------------------------------------------------------------------
    def __init__(self, methodName='runTest', verbose=0):
        """Initialize the base testcase class."""
        self._verbose = int(verbose)

        appname = os.path.basename(sys.argv[0]).replace('.py', '')
        self._appname = appname

        super(FbLoggingTestcase, self).__init__(methodName)

        self.assertGreaterEqual(
            sys.version_info[0], 3, 'Unsupported Python version {}.'.format(sys.version))

        if sys.version_info[0] == 3:
            self.assertGreaterEqual(
                sys.version_info[1], 6, 'Unsupported Python version {}.'.format(sys.version))

        if self.verbose >= 3:
            LOG.debug('Used Phyton version: {!r}.'.format(sys.version))

    # -------------------------------------------------------------------------
    @property
    def verbose(self):
        """Return the verbosity level."""
        return getattr(self, '_verbose', 0)

    # -------------------------------------------------------------------------
    @property
    def appname(self):
        """Return the name of the current running application."""
        return self._appname

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        pass

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Tear down routine for calling each particular test method."""
        pass

    # -------------------------------------------------------------------------
    @classmethod
    def current_function_name(cls, level=0):
        """Return the name of the function, from where this method was called."""
        return sys._getframe(level + 1).f_code.co_name

    # -------------------------------------------------------------------------
    @classmethod
    def get_method_doc(cls):
        """Return the docstring of the method, from where this method was called."""
        func_name = cls.current_function_name(1)
        doc_str = getattr(cls, func_name).__doc__
        cname = cls.__name__
        mname = '{cls}.{meth}()'.format(cls=cname, meth=func_name)
        msg = 'This is {}.'.format(mname)
        if doc_str is None:
            return msg
        doc_str = textwrap.dedent(doc_str).strip()
        if doc_str:
            msg = '{m} - {d}'.format(m=mname, d=doc_str)
        return msg


# =============================================================================
if __name__ == '__main__':

    pass

# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
