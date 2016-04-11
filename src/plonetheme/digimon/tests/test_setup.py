# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.digimon.testing import PLONETHEME_DIGIMON_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.digimon is properly installed."""

    layer = PLONETHEME_DIGIMON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.digimon is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.digimon'))

    def test_browserlayer(self):
        """Test that IPlonethemeDigimonLayer is registered."""
        from plonetheme.digimon.interfaces import (
            IPlonethemeDigimonLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeDigimonLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_DIGIMON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.digimon'])

    def test_product_uninstalled(self):
        """Test if plonetheme.digimon is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.digimon'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeDigimonLayer is removed."""
        from plonetheme.digimon.interfaces import IPlonethemeDigimonLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeDigimonLayer, utils.registered_layers())
