#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: Test script (and module) for unit tests on logging objects.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2024 Frank Brehm, Berlin
@license: LGPL3
"""

import logging
import logging.handlers
import os
import sys

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger

__app__ = 'test_syslog'
LOG = logging.getLogger(__app__)


# =============================================================================
class TestSyslogTestcase(FbLoggingTestcase):
    """Testcase for unit tests on fb_logging.syslog_handler."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        if self.verbose >= 1:
            print()

        py_version = 'Python {}.{}.{}'.format(
            sys.version_info[0], sys.version_info[1], sys.version_info[2])
        LOG.debug('This is %s', py_version)

        mb_chars = 'äöüÄÖÜß»«¢„“”µ·…@ł€¶ŧ←↓→øþ¨æſðđŋħłĸ˝^'
        self.msg_utf8 = "Test {} UTF-8 with wide characters: '{}'.".format(py_version, mb_chars)
        self.msg_utf8 = self.msg_utf8.encode('utf-8')
        self.msg_uni = "Test {} Unicode with wide characters: '{}'.".format(py_version, mb_chars)

        LOG.debug('self.msg_utf8 ({}): {!r}'.format(
            self.msg_utf8.__class__.__name__, self.msg_utf8))
        LOG.debug('self.msg_uni ({}): {!r}'.format(
            self.msg_uni.__class__.__name__, self.msg_uni))

    # -------------------------------------------------------------------------
    def test_import_modules(self):
        """Test importing all appropriate modules."""
        LOG.info(self.get_method_doc())

        import fb_logging.syslog_handler
        LOG.debug('Version of fb_logging.syslog_handler: {!r}.'.format(
            fb_logging.syslog_handler.__version__))

        LOG.debug('Importing FbSysLogHandler from fb_logging.syslog_handler ...')
        from fb_logging.syslog_handler import FbSysLogHandler               # noqa: F401

        import fb_logging.unix_handler
        LOG.debug('Version of fb_logging.unix_handler: {!r}.'.format(
            fb_logging.unix_handler.__version__))

        LOG.debug('Importing UnixSyslogHandler from fb_logging.unix_handler ...')
        from fb_logging.unix_handler import UnixSyslogHandler               # noqa: F401 noqa

    # -------------------------------------------------------------------------
    @unittest.skipUnless(os.path.exists('/dev/log'), "Socket '/dev/log' must exist.")
    def test_logging_syslog(self):
        """Test logging with syslog with FbSysLogHandler."""
        LOG.info(self.get_method_doc())

        from fb_logging.syslog_handler import FbSysLogHandler

        LOG.debug('Init of a test logger instance ...')
        test_logger = logging.getLogger('test.unicode')
        test_logger.setLevel(logging.INFO)
        appname = os.path.basename(sys.argv[0])

        line_tail = ': %(name)s(%(lineno)d) %(funcName)s() %(levelname)s - %(message)s'
        format_str_syslog = appname + line_tail
        format_str_console = '[%(asctime)s]: ' + appname + line_tail

        formatter_syslog = logging.Formatter(format_str_syslog)
        formatter_console = logging.Formatter(format_str_console)

        LOG.debug('Init of a FbSysLogHandler ...')
        lh_syslog = FbSysLogHandler(
            address='/dev/log',
            facility=logging.handlers.SysLogHandler.LOG_USER,
        )

        lh_syslog.setFormatter(formatter_syslog)

        LOG.debug('Init of a StreamHandler ...')
        lh_console = logging.StreamHandler(sys.stderr)
        lh_console.setFormatter(formatter_console)

        LOG.debug('Adding log handlers to test logger instance ...')
        test_logger.addHandler(lh_syslog)
        test_logger.addHandler(lh_console)

        LOG.debug('Logging an UTF-8 message without wide characters ...')
        test_logger.info(self.msg_utf8)
        LOG.debug('Logging an unicode message with wide characters ...')
        test_logger.info(self.msg_uni)

    # -------------------------------------------------------------------------
    def test_unix_syslog(self):
        """Test logging with syslog with UnixSyslogHandler."""
        LOG.info(self.get_method_doc())

        from fb_logging.unix_handler import UnixSyslogHandler

        LOG.debug('Init of a test logger instance ...')
        test_logger = logging.getLogger('test.unix_handler')
        test_logger.setLevel(logging.INFO)
        appname = os.path.basename(sys.argv[0])

        line_tail = ': %(name)s(%(lineno)d) %(funcName)s() %(levelname)s - %(message)s'
        format_str_syslog = appname + line_tail
        format_str_console = '[%(asctime)s]: ' + appname + line_tail

        formatter_syslog = logging.Formatter(format_str_syslog)
        formatter_console = logging.Formatter(format_str_console)

        LOG.debug('Init of a UnixSyslogHandler ...')
        lh_unix_syslog = UnixSyslogHandler(
            ident=appname,
            facility=UnixSyslogHandler.LOG_USER,
        )

        lh_unix_syslog.setFormatter(formatter_syslog)

        LOG.debug('Init of a StreamHandler ...')
        lh_console = logging.StreamHandler(sys.stderr)
        lh_console.setFormatter(formatter_console)

        LOG.debug('Adding log handlers to test logger instance ...')
        test_logger.addHandler(lh_unix_syslog)
        test_logger.addHandler(lh_console)

        LOG.debug('Logging an UTF-8 message without wide characters ...')
        test_logger.info(self.msg_utf8)
        LOG.debug('Logging an unicode message with wide characters ...')
        test_logger.info(self.msg_uni)


# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose, __app__)

    LOG.info('Starting tests ...')

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(TestSyslogTestcase('test_import_modules', verbose))
    suite.addTest(TestSyslogTestcase('test_logging_syslog', verbose))
    suite.addTest(TestSyslogTestcase('test_unix_syslog', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
