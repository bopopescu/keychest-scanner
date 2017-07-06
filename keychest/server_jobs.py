#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Server job classes
"""

from past.builtins import cmp
import collections
from tls_domain_tools import TargetUrl


class ScanResults(object):
    """
    Generic scan result (tls, CT, whois)
    """
    def __init__(self, success=False, code=None, aux=None):
        self.success = success
        self.skipped = False  # if skipped test was not performed
        self.code = code
        self.attempts = 0
        self.aux = aux

    def fail(self):
        self.skipped = False
        self.success = False
        self.attempts += 1

    def ok(self):
        self.skipped = False
        self.success = True

    def skip(self, aux=0xdeadbeef):
        self.skipped = True
        if aux != 0xdeadbeef:
            self.aux = aux

    def is_failed(self):
        return not self.success and not self.skipped

    def __repr__(self):
        return '<ScanResults(success=%r, skipped=%r, code=%r, attempts=%r, aux=%r)>' \
               % (self.success, self.skipped, self.code, self.attempts, self.aux)


class JobTypes(object):
    TARGET = 1
    SUB = 2

    def __init__(self):
        pass


class BaseJob(object):
    """
    Base periodic job class
    """
    def __init__(self, type=None, *args, **kwargs):
        """
        :param type:
        :param args:
        :param kwargs:
        """
        self.type = type
        self.attempts = 0
        self.later = 0
        self.success_scan = False

    def reset_later(self):
        """
        Resets later counter
        :return:
        """
        self.later = 0

    def inclater(self):
        """
        Increments later counter for priority counting
        :return:
        """
        self.later += 1

    def key(self):
        """
        Returns hashable key for the job dbs
        :return:
        """
        return None

    def cmpval(self):
        """
        Returns tuple for comparison
        :return:
        """
        return self.attempts, self.later

    def __cmp__(self, other):
        """
        Compare operation for priority queue.
        :param other:
        :type other: BaseJob
        :return:
        """
        return cmp(self.cmpval(), other.cmpval())

    def to_json(self):
        js = collections.OrderedDict()
        return js

    def __repr__(self):
        return '<BaseJob(type=%r, attempts=%r, later=%r)>' % (self.type, self.attempts, self.later)


class PeriodicJob(BaseJob):
    """
    Represents periodic job loaded from the db
    """

    def __init__(self, target=None, periodicity=None, type=None, *args, **kwargs):
        """
        :param target:
        :type target: DbWatchTarget
        :param args:
        :param kwargs:
        """
        super(PeriodicJob, self).__init__(type=JobTypes.TARGET)

        self.target = target
        self.periodicity = periodicity

        self.primary_ip = None
        self.scan_dns = ScanResults()
        self.scan_tls = ScanResults()
        self.scan_crtsh = ScanResults()
        self.scan_whois = ScanResults()

    def key(self):
        return 'w%s' % self.target.id

    def cmpval(self):
        return self.attempts, \
               self.later, \
               self.target.last_scan_at is None, \
               self.target.last_scan_at

    def url(self):
        """
        Returns url object from the target
        :return:
        """
        return TargetUrl(scheme=self.target.scan_scheme, host=self.target.scan_host, port=self.target.scan_port)

    def watch_id(self):
        """
        Returns watch target id
        :return:
        """
        return self.target.id

    def __repr__(self):
        return '<PeriodicJob(target=<WatcherTarget(id=%r, host=%r, self=%r)>, attempts=%r, last_scan_at=%r)>' \
               % (self.target.id, self.target.scan_host, self.target, self.attempts, self.target.last_scan_at)


class PeriodicReconJob(BaseJob):
    """
    Represents periodic job loaded from the db - recon
    """

    def __init__(self, target=None, periodicity=None, type=None, *args, **kwargs):
        """
        :param target:
        :type target: DbSubdomainWatchTarget
        :param args:
        :param kwargs:
        """
        super(PeriodicReconJob, self).__init__(type=JobTypes.SUB)

        self.target = target
        self.periodicity = periodicity
        self.scan_crtsh_wildcard = ScanResults()

    def key(self):
        return 'r%s' % self.target.id

    def cmpval(self):
        return self.attempts, \
               self.later, \
               self.target.last_scan_at is None, \
               self.target.last_scan_at

    def watch_id(self):
        """
        Returns watch target id
        :return:
        """
        return self.target.id

    def __repr__(self):
        return '<PeriodicReconJob(target=<DbSubdomainWatchTarget(id=%r, host=%r, self=%r)>, attempts=%r, later=%r,' \
               'last_scan_at=%r)>' \
               % (self.target.id, self.target.scan_host, self.target, self.attempts, self.later,
                  self.target.last_scan_at)