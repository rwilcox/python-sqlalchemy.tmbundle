#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import *

${TM_NEW_FILE_TYPENAME}_table = Table('${TM_NEW_FILE_TYPENAME}', metadata,
    Column('${TM_NEW_FILE_TYPENAME}_id', Integer, primary_key=True),
    
)

class ${TM_NEW_FILE_CLASSNAME}(object):
	pass

mapper(${TM_NEW_FILE_CLASSNAME}, ${TM_NEW_FILE_TYPENAME}_table)