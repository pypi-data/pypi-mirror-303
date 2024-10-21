#!/usr/bin/env python
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
import syslog

try:
    import unittest2 as unittest
except ImportError:
    import unittest

libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

from general import FbLoggingTestcase, get_arg_verbose, init_root_logger, pp

__app__ = 'test_fb_logging'
LOG = logging.getLogger(__app__)


# =============================================================================
class TestFbLogging(FbLoggingTestcase):
    """Testcase for unit tests on fb_logging in general."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        if self.verbose >= 1:
            print()

    # -------------------------------------------------------------------------
    def test_import_modules(self):
        """Test importing module fb_logging."""
        LOG.info(self.get_method_doc())

        LOG.debug('Importing fb_logging ...')
        import fb_logging
        from fb_logging import valid_syslog_facilities, syslog_facility_names

        LOG.debug('Version of fb_logging: {!r}.'.format(fb_logging.__version__))

        facilities = valid_syslog_facilities()
        fac_names = syslog_facility_names()
        if self.verbose >= 3:
            LOG.debug('Valid syslog facilities:\n{}'.format(pp(facilities)))
            LOG.debug('Syslog facility names:\n{}'.format(pp(fac_names)))

    # -------------------------------------------------------------------------
    def test_use_unix_syslog_handler(self):
        """Test fb_logging.use_unix_syslog_handler()."""
        LOG.info(self.get_method_doc())

        os_name = os.uname()[0]
        LOG.debug('Current OS kernel name: {!r}.'.format(os_name))

        from fb_logging import use_unix_syslog_handler

        use_ux_handler = use_unix_syslog_handler()
        LOG.debug('Return value of use_unix_syslog_handler(): {!r}.'.format(use_ux_handler))

        if os_name.lower() == 'sunos':
            self.assertTrue(
                use_ux_handler, 'On a {os!r} system {func}() must return {ret!r}.'.format(
                    os=os_name, func='use_unix_syslog_handler', ret=True))
        else:
            self.assertFalse(
                use_ux_handler, 'On a {os!r} system {func}() must return {ret!r}.'.format(
                    os=os_name, func='use_unix_syslog_handler', ret=False))

    # -------------------------------------------------------------------------
    def test_get_syslog_facility_name(self):
        """Test fb_logging.get_syslog_facility_name()."""
        LOG.info(self.get_method_doc())

        from fb_logging import FbSyslogFacilityInfo
        from fb_logging import use_unix_syslog_handler, syslog_facility_name
        from fb_logging import SyslogFacitityError

        FbSyslogFacilityInfo.raise_on_wrong_facility_name = True

        use_ux_handler = use_unix_syslog_handler()

        if use_ux_handler:
            valid_test_data = [
                [syslog.LOG_AUTH, 'syslog.LOG_AUTH', 'auth'],
                [syslog.LOG_DAEMON, 'syslog.LOG_DAEMON', 'daemon'],
                [syslog.LOG_LOCAL2, 'syslog.LOG_LOCAL2', 'local2'],
                [syslog.LOG_MAIL, 'syslog.LOG_MAIL', 'mail'],
                [0.0, 'syslog.LOG_KERN', 'kern'],
            ]
            invalid_test_data = [10, None, 'blah', 1024, -3, 0.4, 99.4]
            invalid_test_values = [10, 1024, -3, 0.4, 99.4]
        else:
            valid_test_data = [
                [
                    logging.handlers.SysLogHandler.LOG_AUTH,
                    'logging.handlers.SysLogHandler.LOG_AUTH',
                    'auth',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_AUTHPRIV,
                    'logging.handlers.SysLogHandler.LOG_AUTHPRIV',
                    'authpriv',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_DAEMON,
                    'logging.handlers.SysLogHandler.LOG_DAEMON',
                    'daemon',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_LOCAL2,
                    'logging.handlers.SysLogHandler.LOG_LOCAL2',
                    'local2',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_MAIL,
                    'logging.handlers.SysLogHandler.LOG_MAIL',
                    'mail',
                ],
                [
                    logging.handlers.SysLogHandler.LOG_SYSLOG,
                    'logging.handlers.SysLogHandler.LOG_SYSLOG',
                    'syslog',
                ],
                [
                    0.0,
                    'logging.handlers.SysLogHandler.LOG_KERN',
                    'kern',
                ],
            ]
            invalid_test_data = [None, 'blah', 1024, -3, 0.4, 99.4]
            invalid_test_values = [1024, -3, 0.4, 99.4]

        for test_tuple in valid_test_data:

            fac_id = test_tuple[0]
            fac_origin = test_tuple[1]
            expected = test_tuple[2]

            LOG.debug('Test syslog_facility_name({id}) -> {ex!r} ({origin}).'.format(
                id=fac_id, ex=expected, origin=fac_origin))
            result = syslog_facility_name(fac_id)
            LOG.debug('Got {!r}.'.format(result))
            self.assertEqual(expected, result)

        for test_id in invalid_test_data:

            LOG.debug('Test exception on syslog_facility_name({!r}).'.format(test_id))

            with self.assertRaises(SyslogFacitityError) as cm:
                result = syslog_facility_name(test_id)

            e = cm.exception
            LOG.debug('Got a {c}: {e}.'.format(c=e.__class__.__name__, e=e))

        LOG.info('Testing {} with wrong values without raising an exception ...'.format(
            'syslog_facility_name()'))

        FbSyslogFacilityInfo.raise_on_wrong_facility_name = False

        for test_id in invalid_test_values:

            LOG.debug('Test returning None on syslog_facility_name({!r}).'.format(test_id))
            result = syslog_facility_name(test_id)
            LOG.debug('Got {!r}.'.format(result))
            self.assertIsNone(result)

    # -------------------------------------------------------------------------
    def test_get_syslog_facility_id(self):
        """Test fb_logging.syslog_facility_id()."""
        LOG.info(self.get_method_doc())

        from fb_logging import FbSyslogFacilityInfo
        from fb_logging import use_unix_syslog_handler, syslog_facility_id
        from fb_logging import SyslogFacitityError

        FbSyslogFacilityInfo.raise_on_wrong_facility_name = True

        use_ux_handler = use_unix_syslog_handler()

        if use_ux_handler:
            valid_test_data = [
                ['auth', syslog.LOG_AUTH, 'syslog.LOG_AUTH'],
                ['Kern', syslog.LOG_KERN, 'syslog.LOG_KERN'],
                ['LOCAL0', syslog.LOG_LOCAL0, 'syslog.LOG_LOCAL0'],
                ['local6', syslog.LOG_LOCAL6, 'syslog.LOG_LOCAL6'],
                ['uSer', syslog.LOG_USER, 'syslog.LOG_USER'],
            ]
            invalid_test_data = [
                0, 4.6, None, object, True, 'uhu', 'local 1', 'authpriv', 'syslog']
            invalid_test_values = ['uhu', 'local 1', 'authpriv', 'syslog']
        else:
            valid_test_data = [
                ['auth', logging.handlers.SysLogHandler.LOG_AUTH,
                    'logging.handlers.SysLogHandler.LOG_AUTH'],
                ['AuthPriv', logging.handlers.SysLogHandler.LOG_AUTHPRIV,
                    'logging.handlers.SysLogHandler.LOG_AUTHPRIV'],
                ['Kern', logging.handlers.SysLogHandler.LOG_KERN,
                    'logging.handlers.SysLogHandler.LOG_KERN'],
                ['LOCAL0', logging.handlers.SysLogHandler.LOG_LOCAL0,
                    'logging.handlers.SysLogHandler.LOG_LOCAL0'],
                ['local6', logging.handlers.SysLogHandler.LOG_LOCAL6,
                    'logging.handlers.SysLogHandler.LOG_LOCAL6'],
                ['Syslog', logging.handlers.SysLogHandler.LOG_SYSLOG,
                    'logging.handlers.SysLogHandler.LOG_SYSLOG'],
                ['uSer', logging.handlers.SysLogHandler.LOG_USER,
                    'logging.handlers.SysLogHandler.LOG_USER'],
            ]
            invalid_test_data = [
                0, 4.6, None, object, True, 'uhu', 'local 1']
            invalid_test_values = ['uhu', 'local 1']

        for test_tuple in valid_test_data:

            fac_name = test_tuple[0]
            expected = test_tuple[1]
            fac_origin = test_tuple[2]

            LOG.debug('Test syslog_facility_id({name!r}) -> {ex} ({origin}).'.format(
                name=fac_name, ex=expected, origin=fac_origin))
            result = syslog_facility_id(fac_name)
            LOG.debug('Got {!r}.'.format(result))
            self.assertEqual(expected, result)

        for test_name in invalid_test_data:

            LOG.debug('Test exception on syslog_facility_id({!r}).'.format(test_name))

            with self.assertRaises(SyslogFacitityError) as cm:
                result = syslog_facility_id(test_name)

            e = cm.exception
            LOG.debug('Got a {c}: {e}.'.format(c=e.__class__.__name__, e=e))

        LOG.info('Testing syslog_facility_id() with wrong values without raising an exception ...')

        FbSyslogFacilityInfo.raise_on_wrong_facility_name = False

        for test_name in invalid_test_values:

            LOG.debug('Test returning None on syslog_facility_id({!r}).'.format(test_name))
            result = syslog_facility_id(test_name)
            LOG.debug('Got {!r}.'.format(result))
            self.assertIsNone(result)


# =============================================================================
if __name__ == '__main__':

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose, __app__)

    LOG.info('Starting tests ...')

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(TestFbLogging('test_import_modules', verbose))
    suite.addTest(TestFbLogging('test_use_unix_syslog_handler', verbose))
    suite.addTest(TestFbLogging('test_get_syslog_facility_name', verbose))
    suite.addTest(TestFbLogging('test_get_syslog_facility_id', verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)


# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list
