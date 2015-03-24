import datetime
import random
import string

import pytz

import simplejson as json

from kickoff import app
from kickoff.model import FennecRelease, ThunderbirdRelease
from kickoff.test.views.base import ViewTest


class TestJSONRequestsAPI(ViewTest):

    def testMajorReleases(self):
        ret = self.get('/json/firefox_history_major_releases.json')
        expected = {
            "2.0": "2005-01-02",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testFennecMajorReleases(self):
        ret = self.get('/json/mobile_history_major_releases.json')
        expected = {
            "24.0": "2015-02-26",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testThunderbirdMajorReleases(self):
        ret = self.get('/json/thunderbird_history_major_releases.json')
        expected = {
            "23.0": "2005-01-01",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testStableReleases(self):
        ret = self.get('/json/firefox_history_stability_releases.json')
        expected = { '2.0.2': '2005-01-02',
            "3.0.1": "2005-01-02",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testFennecStableReleases(self):
        ret = self.get('/json/mobile_history_stability_releases.json')
        expected = {
            "24.0.1": "2015-02-26",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testThunderbirdStableReleases(self):
        ret = self.get('/json/thunderbird_history_stability_releases.json')
        expected = {
            "23.0.1": "2014-01-01",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testBetaReleases(self):
        ret = self.get('/json/firefox_history_development_releases.json')
        expected = {
            "3.0b2": "2005-01-02",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testFennecBetaReleases(self):
        ret = self.get('/json/mobile_history_development_releases.json')
        expected = {
            "23.0b2": "2015-02-26",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testThunderbirdBetaReleases(self):
        ret = self.get('/json/thunderbird_history_development_releases.json')
        expected = {
            "24.0b2": "2005-01-01",
        }
        self.assertEquals(ret.status_code, 200)
        self.assertEquals(json.loads(ret.data), expected)

    def testPrimaryBuilds(self):
        ret = self.get('/json/firefox_primary_builds.json')
        primary = json.loads(ret.data)
        self.assertEquals(ret.status_code, 200)
        # I guess we will always have more than 20 locales
        self.assertTrue(len(primary) > 20)
        # i guess we will always have french or german
        self.assertTrue('fr' in primary)
        self.assertTrue('de' in primary)
        self.assertTrue('en-US' in primary)
        # but no just en
        self.assertTrue('en' not in primary)

    def testTBPrimaryBuilds(self):
        ret = self.get('/json/thunderbird_primary_builds.json')
        primary = json.loads(ret.data)
        self.assertEquals(ret.status_code, 200)
        # I guess we will always have more than 20 locales
        self.assertTrue(len(primary) > 20)
        # i guess we will always have french or german
        self.assertTrue('fr' in primary)
        self.assertTrue('de' in primary)
        self.assertTrue('en-US' in primary)
        # but no just en
        self.assertTrue('en' not in primary)

    def testBetaBuilds(self):
        ret = self.get('/json/firefox_beta_builds.json')
        primary = json.loads(ret.data)
        self.assertEquals(ret.status_code, 200)

    def testBetaBuilds(self):
        ret = self.get('/json/thunderbird_beta_builds.json')
        primary = json.loads(ret.data)
        self.assertEquals(ret.status_code, 200)

#    def testMobile(self):
#        ret = self.get('/json/mobiledetails.json')
#        primary = json.loads(ret.data)
#        self.assertEquals(ret.status_code, 200)
#
    def testFirefoxVersions(self):
        ret = self.get('/json/firefox_versions.json')
        versions = json.loads(ret.data)
        print versions
        self.assertEquals(ret.status_code, 200)

        self.assertTrue("FIREFOX_AURORA" in versions)
        self.assertTrue("FIREFOX_ESR" in versions)
        self.assertTrue("FIREFOX_ESR_NEXT" in versions)
        self.assertTrue("LATEST_FIREFOX_DEVEL_VERSION" in versions)
        self.assertTrue("LATEST_FIREFOX_OLDER_VERSION" in versions)
        self.assertTrue("LATEST_FIREFOX_RELEASED_DEVEL_VERSION" in versions)
        self.assertTrue("LATEST_FIREFOX_VERSION" in versions)
        self.assertTrue("LATEST_THUNDERBIRD_VERSION" not in versions)


    def testThunderbirdVersions(self):
        ret = self.get('/json/thunderbird_versions.json')
        versions = json.loads(ret.data)
        print versions
        self.assertEquals(ret.status_code, 200)

        self.assertTrue("LATEST_THUNDERBIRD_VERSION" in versions)
        self.assertTrue("FIREFOX_ESR" not in versions)
        self.assertTrue("FIREFOX_ESR_NEXT" not in versions)
        self.assertTrue("LATEST_FIREFOX_DEVEL_VERSION" not in versions)
        self.assertTrue("LATEST_FIREFOX_OLDER_VERSION" not in versions)
        self.assertTrue("LATEST_FIREFOX_RELEASED_DEVEL_VERSION" not in versions)
        self.assertTrue("LATEST_FIREFOX_VERSION" not in versions)

