'''
2022 Bjoern Annighoefer

'''
from eoq3.query import Obj

#type checking
from typing import Dict, List

class UserRecord:
    def __init__(self, name:str, passhash:str, groups:List[str], events:List[str], superevents:List[str]):
        self.name:str = name
        self.passhash:str = passhash
        self.groups:Dict[str,bool] = {g : True for g in groups}
        self.events:Dict[str,bool] = {e : True for e in events}
        self.superevents:Dict[str,bool] = {s : True for s in superevents}
        self.obj:Obj = None