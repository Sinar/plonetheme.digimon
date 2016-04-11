# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.digimon


class PlonethemeDigimonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plonetheme.digimon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.digimon:default')


PLONETHEME_DIGIMON_FIXTURE = PlonethemeDigimonLayer()


PLONETHEME_DIGIMON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_DIGIMON_FIXTURE,),
    name='PlonethemeDigimonLayer:IntegrationTesting'
)


PLONETHEME_DIGIMON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_DIGIMON_FIXTURE,),
    name='PlonethemeDigimonLayer:FunctionalTesting'
)


PLONETHEME_DIGIMON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_DIGIMON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeDigimonLayer:AcceptanceTesting'
)
