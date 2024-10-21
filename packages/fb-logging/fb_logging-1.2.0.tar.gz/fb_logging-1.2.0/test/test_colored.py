#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: Testing colored logging formatter.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2024 Frank Brehm, Berlin
@license: LGPL3
"""

import logging
import os
import sys
from random import randint

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger, pp

__app__ = 'test_colored'
LOG = logging.getLogger(__app__)


# =============================================================================
class TestColored(FbLoggingTestcase):
    """Testcase for unit tests on fb_logging.colored."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        if self.verbose >= 1:
            print()

    # -------------------------------------------------------------------------
    def test_import_modules(self):
        """Test importing module fb_logging.colored."""
        LOG.info(self.get_method_doc())

        LOG.debug('Importing fb_logging.colored ...')
        import fb_logging.colored

        LOG.debug('Version of fb_logging.colored: {!r}.'.format(fb_logging.colored.__version__))

        LOG.debug('Checking available color keys ...')

        from fb_logging.colored import Colors
        colors = Colors.keys()
        if self.verbose >= 2:
            LOG.debug('Valid color names:\n{}'.format(pp(colors)))

    # -------------------------------------------------------------------------
    def test_colorcode_4bit(self):
        """Test colored output 4 bit colors."""
        LOG.info(self.get_method_doc())

        from fb_logging.colored import Colors
        from fb_logging.colored import colorstr
        from fb_logging.colored import ColorNotFoundError, WrongColorTypeError

        msg = 'Colored output'

        print('')
        max_len = 1
        normal_colors = Colors.keys()
        for color in normal_colors:
            if len(color) > max_len:
                max_len = len(color)
        max_len += 1
        tpl = '{{c:<{}}} {{msg}}'.format(max_len)
        for color in normal_colors:
            LOG.debug('Testing color {clr!r} ({cls}) ...'.format(
                clr=color, cls=color.__class__.__name__))
            try:
                c = '{}:'.format(color)
                print(tpl.format(c=c, msg=colorstr(msg, color)))
            except Exception as e:
                self.fail('Failed to generate colored string {c!r} with {cls}: {e}'.format(
                    c=color, cls=e.__class__.__name__, e=e))

        print('')
        LOG.info('Testing combined colored output ...')
        print('')

        colors = (
            ('cyan',),
            ('green', 'strike'),
            ('dark_red', 'green_bg', 'underline'),
        )
        for color in colors:
            LOG.debug('Testing color {clr} ...'.format(clr=pp(color)))
            try:
                print('{c}: {msg}'.format(c=pp(color), msg=colorstr(msg, color)))
            except Exception as e:
                self.fail('Failed to generate colored string {c!r} with {cls}: {e}'.format(
                    c=color, cls=e.__class__.__name__, e=e))

        print('')
        LOG.info('Testing legacy colors ...')
        print('')
        max_len = 1
        legacy_colors = sorted(Colors.legacy_colors.keys())
        for color in legacy_colors:
            if len(color) > max_len:
                max_len = len(color)
        max_len += 1
        tpl = '{{c:<{}}} {{msg}}  ({{real}})'.format(max_len)
        for color in legacy_colors:
            real_color = Colors.legacy_colors[color]
            LOG.debug('Testing legacy color {clr!r} == {real!r} ({cls}) ...'.format(
                clr=color, real=real_color, cls=color.__class__.__name__))
            try:
                c = '{}:'.format(color)
                print(tpl.format(c=c, msg=colorstr(msg, color), real=real_color))
            except Exception as e:
                self.fail('Failed to generate colored string {c!r} with {cls}: {e}'.format(
                    c=color, cls=e.__class__.__name__, e=e))

        print('')
        LOG.info('Testing invalid colors ...')
        print('')

        wrong_colors = (
            None,
            False,
            {2: 3},
            -4,
            'uhu',
        )
        for color in wrong_colors:
            LOG.debug('Testing wrong color {clr} ...'.format(clr=pp(color)))
            with self.assertRaises((ColorNotFoundError, WrongColorTypeError)) as cm:
                msg = colorstr(msg, color)

            e = cm.exception
            LOG.debug('Got a {c}: {e}.'.format(c=e.__class__.__name__, e=e))

    # -------------------------------------------------------------------------
    def test_colorcode_8bit(self):
        """Test colored output 8 bit colors."""
        LOG.info(self.get_method_doc())

        from fb_logging.colored import Colors

        print('')
        LOG.info('Testing foreground colors ...')

        for i in list(range(256)):

            bg_color = 0
            modulus = i % 16
            if modulus < 8:
                bg_color = 15

            msg = (str(i) + ' ').rjust(5)
            out = Colors.colorize_8bit(msg, i, bg_color)
            if self.verbose:
                print(out, end='')
                if modulus == 15:
                    print()

        print('')
        LOG.info('Testing background colors ...')

        for i in list(range(256)):

            fg_color = 0
            modulus = i % 16
            if modulus < 8:
                fg_color = 15

            msg = (str(i) + ' ').rjust(5)
            out = Colors.colorize_8bit(msg, fg_color, i)
            if self.verbose:
                print(out, end='')
                if modulus == 15:
                    print()

    # -------------------------------------------------------------------------
    def test_colorcode_24bit(self):
        """Test colored output 24 bit colors."""
        LOG.info(self.get_method_doc())

        from fb_logging.colored import colorstr_24bit

        test_colors = [
            ((0, 0, 0), (255, 255, 255)),
            ((255, 255, 255), (0, 0, 0)),
            ((255, 0, 0), None),
            ((0, 255, 0), None),
            ((0, 0, 255), None),
            ((127, 0, 127), None),
            ((255, 0, 255), None),
            ((0, 127, 127), None),
            ((0, 255, 255), None),
            ((127, 127, 0), None),
            ((255, 255, 0), None),
            (None, (63, 63, 63)),
        ]

        i = 0
        while i < 10:
            i += 1
            c = ((randint(0, 255), randint(0, 255), randint(0, 255)), None)
            test_colors.append(c)

        i = 0
        while i < 3:
            i += 1
            c = (None, (randint(0, 255), randint(0, 255), randint(0, 255)))
            test_colors.append(c)

        msg = 'Colored output'
        print('')

        for color in test_colors:

            ctxt = '{!r}'.format(color)
            LOG.debug('Testing color {clr} ...'.format(clr=ctxt))

            print('{ctxt:<30} {msg}'.format(
                ctxt=(ctxt + ':'), msg=colorstr_24bit(msg, color[0], color[1])))


# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose, __app__)

    LOG.info('Starting tests ...')

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(TestColored('test_import_modules', verbose))
    suite.addTest(TestColored('test_colorcode_4bit', verbose))
    suite.addTest(TestColored('test_colorcode_8bit', verbose))
    suite.addTest(TestColored('test_colorcode_24bit', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list
