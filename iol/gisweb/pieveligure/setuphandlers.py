from plone.app.controlpanel.security import ISecuritySchema
from plone import api
from Products.Five.utilities.marker import mark
from .interfaces import IIolApp
import logging

PROFILE_ID = 'iol.gisweb.pieveligure.replication:default'
logger = logging.getLogger('iol.gisweb.pieveligure')

def initPackage(context):
    catalog = api.portal.get_tool('portal_catalog')
    brains = catalog(portal_type='PlominoDatabase')
    for brain in brains:
        db = brain.getObject()
        for doc in db.getAllDocuments():
            if not IIolApp.providedBy(doc):
                mark(doc,IIolApp)
