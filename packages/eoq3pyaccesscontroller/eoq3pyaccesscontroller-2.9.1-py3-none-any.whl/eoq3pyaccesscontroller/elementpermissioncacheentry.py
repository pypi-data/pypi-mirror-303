'''
2022 Bjoern Annighoefer

'''

from eoq3.query import Obj

#type checking
from typing import Dict

class ElementPermissionCacheEntry:
    def __init__(self, elem:Obj):
        self.elem = elem
        self.owner = None
        self.group = None
        self.permissions:Dict[str,int] = {}