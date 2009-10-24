#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import *
from sqlalchemy.ext.assignmapper import assign_mapper
from turbogears.database import metadata, session

${TM_NEW_FILE_TYPENAME}_table = Table('${TM_NEW_FILE_TYPENAME}', metadata,
    Column('${TM_NEW_FILE_TYPENAME}_id', Integer, primary_key=True),
    
)

class ${TM_NEW_FILE_CLASSNAME}(object):
	pass

assign_mapper(session, ${TM_NEW_FILE_CLASSNAME}, ${TM_NEW_FILE_TYPENAME}_table)
