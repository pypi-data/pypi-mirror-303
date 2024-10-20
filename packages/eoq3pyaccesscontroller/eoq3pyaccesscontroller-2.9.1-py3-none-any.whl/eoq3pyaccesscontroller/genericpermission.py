'''
2022 Bjoern Annighoefer

'''
from eoq3.query import Obj

class GenericPermission:
    '''Generic permissions can replace local element user, owner and permissions if those are not available
    '''
    def __init__(self, targetClassId:str, featureName:str, owner:str, group:str, permission:int):
        self.targetClassId:str = targetClassId
        self.featureName:str = featureName
        self.owner:str = owner
        self.group:str = group
        self.permission:int = permission
        self.obj:Obj = None #the reference to the information in the mdb
