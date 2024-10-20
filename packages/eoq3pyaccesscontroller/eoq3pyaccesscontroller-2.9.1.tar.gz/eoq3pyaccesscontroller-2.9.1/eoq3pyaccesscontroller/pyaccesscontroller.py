'''
2022 Bjoern Annighoefer

'''
from .userrecord import UserRecord
from .genericpermission import GenericPermission
from .elementpermissioncacheentry import ElementPermissionCacheEntry
from .util import VerifyPassword, IsValidPasshash
from .model import ACCESS_SETTINGS_CMD, ACCESS_SETTINGS_CLASSES

from eoq3.accesscontroller import AccessController, PERMISSION_FLAGS, WILDCARD_FEATURE_NAME, ParseFeaturePermissionStr
from eoq3.value import STR, I32, I64, PRM, NON, LST
from eoq3.query import Obj, His
from eoq3.command import Cmp
from eoq3.error import EOQ_ERROR, EOQ_ERROR_INVALID_VALUE, EOQ_ERROR_ACCESS_DENIED
from eoq3.concepts import CONCEPTS, MXELEMENT, NormalizeFeatureName,\
                          M2CLASS, M2ATTRIBUTE, M2ASSOCIATION, M2COMPOSITION,\
                          M1OBJECT, M1COMPOSITION, M1ATTRIBUTE, M1ASSOCIATION 
from eoq3.domain import Domain
from eoq3.config import Config, EOQ_DEFAULT_CONFIG

import re

#type checking
from typing import Dict, List, Tuple, Union


ACCESS_SETTINGS_M1_MODEL_NAME = 'acm'

class PyAccessController(AccessController):
    ''' An access controller that will check users and permissions based on a user db 
    stored in the domain
    '''
    def __init__(self,\
                  users:List[UserRecord] = [],
                  genericPermissions:List[GenericPermission] = [],
                  superAdminPasshash:str="7mjDFTt6Jrwov+beGIeSIJVWxLsooD8Q5gLxDXLW5OHeQHV6vWKsrBB/M6GK+eVdancrryEc2uZRekW/yqZdKQ==", #= 'DAMMMMN!#' use util/generatepasshash to fill this 
                  config:Config = EOQ_DEFAULT_CONFIG):
        super().__init__()
        self.config = config
        ## initialize the internal user list
        self.users:Dict[str,UserRecord] = {}
        self.usersObjLut:Dict[Obj,UserRecord] = {}
        #make sure the super admin is added to the user list
        self.superAdmin = UserRecord(self.config.superAdminName, superAdminPasshash, [], [], [])
        if(self.config.superAdminName not in self.users):
            self.users[self.config.superAdminName] = self.superAdmin
        #add all the other users
        for u in users:
            self.users[u.name] = u
        ## initializer the internal generic permissions list
        self.genericPermissions:Dict[Tuple[str,str],GenericPermission] = {(g.targetClassId,g.featureName) : g for g in genericPermissions}
        self.genericPermissionsLut:Dict[Obj:GenericPermission] = {} #necessary to synchronize with domain changes
        ## initialize the permissions cache
        self.permissionsCache:Dict[Obj,ElementPermissionCacheEntry] = {}
        
    def Connect(self, domain:Domain, sessionId:str)->None:
        '''Connecting to the domain will upload the user model 
        and meta-model to the domain and keep track of any changes on that 
        '''
        self.domain = domain
        self.sessionId = sessionId
        #upload the user meta model
        cmd = ACCESS_SETTINGS_CMD
        self.accessSettingsMetaModel = self.domain.Do(cmd,self.sessionId,asDict=True)['o0']
        #upload the user model and link to the local elements
        cmd = Cmp()
        cmd.Crt(CONCEPTS.M1MODEL,I32(1),[self.accessSettingsMetaModel,ACCESS_SETTINGS_M1_MODEL_NAME],resName='acm')
        cmd.Crt(CONCEPTS.M1OBJECT,I32(1),[ACCESS_SETTINGS_CLASSES.ACCESSSETTINGS,His('acm'),'acmroot'],resName='acmroot')
        i = 0
        for u in self.users.values():
            uid = "user%d"%(i)
            cmd.Crt(CONCEPTS.M1OBJECT,I32(1),[ACCESS_SETTINGS_CLASSES.USER,His('acm'),u.name],mute=True,resName=uid)
            cmd.Crt(CONCEPTS.M1ATTRIBUTE,I32(1),['passhash',His(uid),u.passhash],mute=True)
            #cmd.Upd(His(-1),'passhash',u.passhash,mute=True)
            for n in u.groups.keys():
                cmd.Crt(CONCEPTS.M1ATTRIBUTE,I32(1),['groups',His(uid),n],mute=True)
            #cmd.Upd(His(-2),'groups*',[n for n in u.groups.keys()],I64(-1),mute=True)
            for n in u.events.keys():
                cmd.Crt(CONCEPTS.M1ATTRIBUTE,I32(1),['events',His(uid),n],mute=True)
            #cmd.Upd(His(-3),'events*',[n for n in u.events.keys()],I64(-1),mute=True)
            for n in u.superevents.keys():
                cmd.Crt(CONCEPTS.M1ATTRIBUTE,I32(1),['superevents',His(uid),n],mute=True)
            #cmd.Upd(His(-4),'superevents*',[n for n in u.superevents.keys()],I64(-1),mute=True)
            cmd.Crt(CONCEPTS.M1COMPOSITION,I32(1),['users',His('acmroot'),His(uid)],mute=True)
            #cmd.Upd(His('acm'),'users*',His(-5),I64(-1),mute=True)
            i += 1
        self.accessSettingsModel = self.domain.Do(cmd,self.sessionId,asDict=True)['acmroot']
        
    ### INITIAL ACCESS ###
    
    def AuthenticateUser(self, user:str, password:str)->bool:
        ''' Returns true if the user and password are known.
        Returns false otherwise
        '''
        decision = False
        if(None != user and None != password and user in self.users):
            userRecord = self.users[user]
            if(None != userRecord.passhash): 
                decision = VerifyPassword(password, userRecord.passhash)
        return decision
    
    
    ### OBSERVATION ###
    
    #@Override
    def IsAllowedToObserve(self, user:str, eventType:str)->bool:
        decision = False
        if(None != user and user in self.users):
            userRecord = self.users[user]
            decision = eventType in userRecord.events
            if(userRecord == self.superAdmin):
                decision = True
        return decision
    
    #@Override
    def IsAllowedToSuperobserve(self, user:str, eventType:str)->bool:
        decision = False
        if(None != user and user in self.users):
            userRecord = self.users[user]
            decision = eventType in userRecord.superevents
            if(userRecord == self.superAdmin):
                decision = True
        return decision
    
    ### PRE VERIFICATION ###
    
    def ReadPreVerify(self, target:Obj, featureName:STR, context:Obj=NON(), user:str=None)->None:
        if(not self.__IsAllowedToRead(target, featureName, user)):
            fName = '*' if featureName.IsNone() else featureName.GetVal()
            raise EOQ_ERROR_ACCESS_DENIED('User %s cannot read %s/%s'%(user,target,fName))
    
    def UpdatePreVerify(self, target:Obj, featureName:STR, value:PRM, position:I64=I64(0), user:str=None)->None:
        #1. check if the target can be updated
        if(not self.__IsAllowedToUpdate(target, featureName, user)):
            fName = '*' if featureName.IsNone() else featureName.GetVal()
            raise EOQ_ERROR_ACCESS_DENIED('User %s cannot update %s/%s'%(user,target,fName))
        #2. check if the value is an element and has read and write access
        elif(isinstance(value,Obj) and (
               not self.__IsAllowedToRead(value, NON(), user) or 
               not self.__IsAllowedToUpdate(value, NON(), user))): 
            raise EOQ_ERROR_ACCESS_DENIED('User %s has no access to value %s'%(user,value))
    
    
    def DeletePreVerify(self, target:Obj, user:str=None)->None:
        if(not self.__IsAllowedToDelete(target, user)):
            raise EOQ_ERROR_ACCESS_DENIED('User %s cannot delete %s'%(user,target))
    
    ### POST VERIFICATION ###
    
    def CreatePostVerify(self, classId:Union[STR,Obj], createArgs:LST, target:Obj, recoveryArgs:LST, user:str=None)->None:
        #general check if object can be created
        if(not self.__IsAllowedToCreate(target, user)):
            raise EOQ_ERROR_ACCESS_DENIED('User %s cannot create %s'%(user,classId))
        #if it one of the own elements, make additional sanity checks
        elif(ACCESS_SETTINGS_CLASSES.USER == self.__GetClassId(target)):
            nameStr = createArgs[2].GetVal() if len(createArgs)>1 else None
            user = None
            if(None != nameStr):
                if(nameStr in self.users):
                    user = self.users[nameStr]
                    if(None != user.obj): #this user is already linked to another object
                        raise EOQ_ERROR_INVALID_VALUE("User with name %s does already exist."%(nameStr))
                elif(not self.__IsValidUserName(nameStr)):
                    raise EOQ_ERROR_INVALID_VALUE("User name contains invalid chars. Only use A-Z, a-z, 0-9."%(nameStr))
        elif(ACCESS_SETTINGS_CLASSES.GENERICPERMISSION == classId.GetVal()):
            pass
        else: 
            #take special care of m1 features
            conceptId = self.__GetConceptIdIfIsM1Feature(target)
            if(not conceptId.IsNone()):
                updateEquivalents = self.__GetUpdParamsFromM1FeatureCreate(conceptId, target, createArgs)
                for f in updateEquivalents:
                    if(not self.__IsAllowedToUpdate(f[1], f[2], user)): 
                        raise EOQ_ERROR_ACCESS_DENIED('User %s cannot create %s.%s'%(user,f[1],f[2]))
                    self.__ValidateAccessModelUpdates(f[1],f[2].GetVal(),f[3])
            
    
#     def ReadPostVerify(self, target:Obj, featureName:STR, context:Obj)->None:
#         '''Raises an exception if the read needs to be undone.
#         '''
#         pass
    
    def UpdatePostVerify(self, target:Obj, featureName:STR, value:PRM, position:I64=I64(0), oldValue:PRM=NON(), user:str=None)->None:
        #3. check if the old value has read and write access  
        if(not oldValue.IsNone() and isinstance(oldValue,Obj) and (#...check if the value is and element and is allowed to be read and changed.
               not self.__IsAllowedToRead(oldValue, NON(), user) or
               not self.__IsAllowedToUpdate(oldValue, NON(), user))):
            raise EOQ_ERROR_ACCESS_DENIED('User %s has no access to old value %s'%(user,oldValue)) 
        
        # check correctness of own data objects
        '''This is a callback informing the access controller that an update took place
        '''
        featureNameStr = featureName.GetVal()
        self.__ValidateAccessModelUpdates(target,featureNameStr,value)
        
    
    def DeletePostVerify(self, target:Obj, classId:STR, createArgs:LST, recoveryArgs:LST, user:str=None)->None:
        #check own data element modifications
        #see if a user is going to be deleted
        if(target in self.usersObjLut): 
            user = self.usersObjLut[target]
            #the super admin can never be deleted 
            if(user == self.superAdmin):
                raise EOQ_ERROR_ACCESS_DENIED('Cannot delete superadmin.')
        #see if a generic permission is going to be deleted
        elif(target in self.genericPermissionsLut): #see if a user is going to be deleted
            pass
        #take special care about m1 features
        elif(self.__IsM1Feature(classId)):
            updateEquivalents = self.__GetUpdParamsFromM1FeatureDelete(classId, createArgs)
            for f in updateEquivalents:
                if(not self.__IsAllowedToUpdate(f[1], f[2], user)): 
                    raise EOQ_ERROR_ACCESS_DENIED('User %s cannot create %s.%s'%(user,f[1],f[2]))
                self.__ValidateAccessModelUpdates(f[1],f[2].GetVal(),f[3])
    
    
    ### NOTIFIERS ####
    
    def CreateNotify(self, classId:Union[STR,Obj], createArgs:LST, target:Obj, recoveryArgs:LST, user:str=None)->None:
        '''This is a callback informing the access controller that a create took place
        '''
        targetClassId = self.__GetClassId(target)
        if(ACCESS_SETTINGS_CLASSES.USER == targetClassId.GetVal()):
            nameStr = createArgs[2].GetVal() if len(createArgs)>1 else None
            user = None
            if(None != nameStr):
                if(nameStr in self.users):
                    user = self.users[nameStr]
            #if not existing, create and empty user record
            if(None == user):
                user = UserRecord(nameStr, None, [], [], [])
                if(None != nameStr):
                    self.users[nameStr] = user
            #link user to MDB
            user.obj = target
            self.usersObjLut[target] = user
        elif(ACCESS_SETTINGS_CLASSES.GENERICPERMISSION == targetClassId.GetVal()):
            gp = GenericPermission(None,None,None,None,None)
            self.genericPermissionsLut[target] = gp
            gp.obj = target
        else:
            #take special care about m1 features
            conceptId = self.__GetConceptIdIfIsM1Feature(target)
            if(not conceptId.IsNone()):
                updateEquivalents = self.__GetUpdParamsFromM1FeatureCreate(conceptId, target, createArgs)
                for f in updateEquivalents:
                    self.__TrackAccessSettingsUpdates(f[1],f[2].GetVal(),f[3],f[4])
        #for every object: respect that in the cache
        self.permissionsCache[target] = ElementPermissionCacheEntry(target)#add new entry in permission cache

    def UpdateNotify(self, target:Obj, featureName:STR, value:PRM, position:I64, oldValue:PRM, user:str=None)->None:
        '''This is a callback informing the access controller that an update took place
        '''
        featureNameStr = featureName.GetVal()
        #update the generic element permissions
        if(MXELEMENT.PERMISSIONS == featureNameStr):
            if(not value.IsNone()):
                (f, p) = ParseFeaturePermissionStr(value.GetVal())
                self.permissionsCache[target].permissions[f] = p #add or update permission to the list
            if(not oldValue.IsNone()): #delete a permission entry
                (f, p) = ParseFeaturePermissionStr(oldValue.GetVal())
                del self.permissionsCache[target].permissions[f] #delete this permission from the list
        elif(MXELEMENT.OWNER == featureNameStr):
            self.permissionsCache[target].owner = value.GetVal()
        elif(MXELEMENT.GROUP == featureNameStr):
            self.permissionsCache[target].group = value.GetVal()
        else:
            self.__TrackAccessSettingsUpdates(target, featureNameStr, value, oldValue)
            
        
    def DeleteNotify(self, target:Obj, classId:STR, createArgs:LST, recoveryArgs:LST, user:str=None)->None:
        '''This is a callback informing the access controller that a deletion took place
        '''
        #see if a user is going to be deleted
        if(target in self.usersObjLut): 
            user = self.usersObjLut[target]
            if(user.name in self.users): del self.users[user.name] #must check, because the user might never was registered when his name is still None
            del self.usersObjLut[target]
        #see if a generic permission is going to be deleted
        elif(target in self.genericPermissionsLut): #see if a user is going to be deleted
            gp = self.genericPermissionsLut[target]
            gpKey = (gp.targetClassId,gp.featureName)
            if(gpKey in self.genericPermissions): del self.genericPermissions[gpKey]
            del self.genericPermissionsLut[target]
        elif(self.__IsM1Feature(classId)):
            updateEquivalents = self.__GetUpdParamsFromM1FeatureDelete(classId, createArgs)
            for f in updateEquivalents:
                self.__TrackAccessSettingsUpdates(f[1],f[2].GetVal(),f[3],f[4])
        #remove the element from the permission cache in any case
        del self.permissionsCache[target]
    
    
    ### PRIVATE METHODS ###
    
    def __IsAllowedToRead(self, target:Obj, featureName:STR, user:str = None)->bool:
        return self.__IsAllowedToCheck(target, user, PERMISSION_FLAGS.OWNER_READ, PERMISSION_FLAGS.GROUP_READ, PERMISSION_FLAGS.ANYBODY_READ, featureName)
    
    #@Override
    def __IsAllowedToUpdate(self, target:Obj, featureName:STR, user:str = None)->bool:
        return self.__IsAllowedToCheck(target, user, PERMISSION_FLAGS.OWNER_UPDADE, PERMISSION_FLAGS.GROUP_UPDADE, PERMISSION_FLAGS.ANYBODY_UPDADE, featureName)
    
    #@Override
    def __IsAllowedToDelete(self, target:Obj, user:str = None)->bool:
        return self.__IsAllowedToCheck(target, user, PERMISSION_FLAGS.OWNER_DELETE, PERMISSION_FLAGS.GROUP_DELETE, PERMISSION_FLAGS.ANYBODY_DELETE)
    
    #@Override
    def __IsAllowedToCreate(self, target:Obj, user:str = None)->bool:
        return self.__IsAllowedToCheck(target, user, PERMISSION_FLAGS.OWNER_CREATE, PERMISSION_FLAGS.GROUP_CREATE, PERMISSION_FLAGS.ANYBODY_CREATE)

    
    ### PRIVATE METHODS ###
    
    
    def __IsValidUserName(self, name:str)->bool:
        VALID_USER_NAME_RE = re.compile('[^A-Za-z0-9]')
        return (None == VALID_USER_NAME_RE.search(name))
    
    def __IsAllowedToCheck(self, target:Obj, user:str, ownerFlag, groupFlag:int, anonymousFlag:int, featureName:STR=NON())->bool:
        decision = False #by default the decision is No. Lets find a reason the user is allowed.
        #normalize the feature name if given
        normFeatureName = None
        if(not featureName.IsNone()):
            normFeatureName = NormalizeFeatureName(featureName.GetVal())
        #retrieve the access attributes (owner, group and permission) for the target
        (owner, group, permission) = self.__GetOwnerGroupPermission(target,normFeatureName)
        #first check for anonymous, because it is the most frequent case
        if(self.__CheckAnonymousPermission(permission,anonymousFlag)):
            decision = True
        #second, see if it a known user
        if(None != user and user in self.users):
            userRecord = self.users[user]
            #third group permission
            if(self.__CheckGroupPermission(userRecord, group, permission, groupFlag)):
                decision = True
            #fourth owner permission
            elif(self.__CheckOwnerPermission(userRecord, owner, permission, ownerFlag)):
                decision = True
            #fifth, super admin?
            elif(self.superAdmin == userRecord): #the super admin has no restriction
                decision = True
        return decision
    
    def __GetUserRecord(self, user:str)->UserRecord:
        try:
            return self.users[user]
        except KeyError:
            raise EOQ_ERROR_ACCESS_DENIED('Unknown user: %s'%(user))
        
    # PERMISSION RETRIVAL
        
    def __GetOwnerGroupPermission(self, target:Obj, normFeatureName:str=None)->Tuple[str,str,int]:
        ''' Retrieves owner, group and permission for an element 
        This can be set for the element itself or 
        if not set the parents are parent owner, group or permission are inherited 
        if available. If nothing is set for the element and all parents
        owner and group are None and permissions are default permissions.
        ''' 
        ## this is the global element access properties resolval chain
        #1. try if properties for the element itself are available
        (owner,group,permission) = self.__GetSingleElementOGP(target, normFeatureName)
        #2. see if all information is resolved or if something is missing if yes, continue with the parents
        if(None == owner or None == group or None == permission):
            (parent, parentFeatureName) = self.__GetParentAndFeatureName(target)
            if(not parent.IsNone()): #if it has a parent, inherit owner, group or permission
                #loop over all parents until no more parent or owner, group and permission are known
                while(not parent.IsNone() and (None == owner or None == group or None == permission)):
                    (powner,pgroup,ppermission) = self.__GetSingleElementOGP(parent, NormalizeFeatureName(parentFeatureName.GetVal()))
                    if(None == owner): owner = powner
                    if(None == group): group = pgroup
                    if(None == permission): permission = ppermission
                    #look for next parent
                    (parent, parentFeatureName) = self.__GetParentAndFeatureName(parent)
        #3. is still something is unset, check if there are wildcard generic permissions for everything
        if((None == owner or None == group or None == permission) and 
             (WILDCARD_FEATURE_NAME,WILDCARD_FEATURE_NAME) in self.genericPermissions):
            genericPermission = self.genericPermissions[(WILDCARD_FEATURE_NAME,WILDCARD_FEATURE_NAME)]
            if(None==owner): owner = genericPermission.owner
            if(None==group):group = genericPermission.group
            if(None==permission):permission = genericPermission.permission
        #4. if still access properties are unresolved, use the global default values
        if(None==owner): owner = self.config.defaultOwner
        if(None==group): group = self.config.defaultGroup
        if(None==permission): permission = self.config.defaultPermission
        #return direct or inherit permission, owner and group
        return (owner,group,permission)
    

    def __GetSingleElementOGP(self, target:Obj, normFeatureName:str)->Tuple[str,str,int]:
        '''Return the owner, group and permission for a single element either from the element data or the 
        generic features
        '''
        #initialize return values
        owner:str = None
        group:str = None
        permission:int = None
        entry:ElementPermissionCacheEntry = None
        #check the cache for the element
        if(not target.IsNone() and target in self.permissionsCache):
            entry = self.permissionsCache[target]
        #retrieve the class id for checking generic permissions
        classId:str = self.__GetClassId(target).GetVal()
        ## In the following is access property priority chain on element level
        # 1. check if we have a complete match in the element permissions
        if(None != entry and None != normFeatureName and normFeatureName in entry.permissions):
            owner = entry.owner
            group = entry.group
            permission = entry.permissions[normFeatureName]
        #2. look for a generic permission with a perfect match of target and feature
        if((None == owner or None == group or None == permission) and 
           None != normFeatureName and None != classId and 
           (classId,normFeatureName) in self.genericPermissions):
            genericPermission = self.genericPermissions[(classId,normFeatureName)]
            if(None==owner): owner = genericPermission.owner
            if(None==group): group = genericPermission.group
            if(None==permission): permission = genericPermission.permission
        #3. look for the target wildcard feature permissions
        if((None == owner or None == group or None == permission) and 
           None != entry and WILDCARD_FEATURE_NAME in entry.permissions):
            if(None==owner): owner = entry.owner
            if(None==group): group = entry.group
            if(None==permission): permission = entry.permissions[WILDCARD_FEATURE_NAME]
        #4. check if we have a feature match for wild card class names
        if((None == owner or None == group or None == permission) and 
           None != normFeatureName and
             (WILDCARD_FEATURE_NAME,normFeatureName) in self.genericPermissions):
            genericPermission = self.genericPermissions[(WILDCARD_FEATURE_NAME,normFeatureName)]
            if(None==owner): owner = genericPermission.owner
            if(None==group):group = genericPermission.group
            if(None==permission):permission = genericPermission.permission
        #4. check if we have a wildcard feature match for all objects
        if((None == owner or None == group or None == permission) and 
           None != classId and 
             (classId,WILDCARD_FEATURE_NAME) in self.genericPermissions):
            genericPermission = self.genericPermissions[(classId,WILDCARD_FEATURE_NAME)]
            if(None==owner): owner = genericPermission.owner
            if(None==group):group = genericPermission.group
            if(None==permission):permission = genericPermission.permission
        return (owner,group,permission)
    
    # PERMISSION CHECKING
    
    def __CheckOwnerPermission(self, userRecord:UserRecord, owner:str, permission:int, permissionFlag:int)->bool:
        ''' Check if owner and user are set and the owner matches the user.
        If all previous is true, see if the permission flag is set
        '''
        return (None != owner and owner == userRecord.name and permission & permissionFlag)
    
    def __CheckGroupPermission(self, userRecord:UserRecord, group:str, permission:int, permissionFlag:int)->bool:
        ''' Check if group is set and the user is member of a group.
        If all previous is true, see if the permission flag is set
        '''
        return (None != group and group in userRecord.groups and permission & permissionFlag)
    
    def __CheckAnonymousPermission(self, permission:int, permissionFlag:int)->bool:
        ''' Check if the permission flag is set
        '''
        return (permission & permissionFlag)
    
    def __GetParentAndFeatureName(self, target:Obj)->Tuple[Obj,STR]:
        parent = NON()
        featureName = NON()
        try: #catch the fact that the parent is not accessible
            conceptId = self.mdb.Read(target, STR(MXELEMENT.CONCEPT))
            if(CONCEPTS.M1OBJECT == conceptId):
                m1comp = self.mdb.Read(target, STR(M1OBJECT.CHILDCOMPOSITION))
                if(not m1comp.IsNone()):
                    parent = self.mdb.Read(m1comp, STR(M1COMPOSITION.PARENT))
                    m2comp = self.mdb.Read(m1comp, STR(M1COMPOSITION.M2COMPOSITION))
                    featureName = self.mdb.Read(m2comp, STR(M2COMPOSITION.NAME))
        except EOQ_ERROR:
            #return NON
            parent = NON()
            featureName = NON()
        return (parent,featureName)
    
    #@Override
    def __GetClassId(self, target:Obj)->STR:
        classId = NON()
        try: #catch if no class or class name are available
            conceptId = self.mdb.Read(target, STR(MXELEMENT.CONCEPT))
            if(CONCEPTS.M1OBJECT == conceptId):
                clazz = self.mdb.Read(target, STR(M1OBJECT.M2CLASS))
                classId = self.mdb.Read(clazz, STR(MXELEMENT.STRID))
            else:
                classId = conceptId
        except EOQ_ERROR:
            classId = NON()
        return classId
    
    def __GetConceptIdIfIsM1Feature(self,target:Obj)->STR:
        conceptId = self.mdb.Read(target, STR(MXELEMENT.CONCEPT))
        return conceptId if self.__IsM1Feature(conceptId) else NON()
    
    def __IsM1Feature(self,conceptId:STR)->bool:
        return conceptId.GetVal() in [CONCEPTS.M1ATTRIBUTE,CONCEPTS.M1ASSOCIATION,CONCEPTS.M1COMPOSITION]
    
    def __GetUpdParamsFromM1FeatureCreate(self, conceptId:STR, target:Obj, createArgs:LST)->List[Tuple[STR,Obj,STR,PRM,PRM]]:
        '''Returns the feature name if the target is an M1 Feature.
        Else it returns NON.
        returns:
            res: List of triples composed of conceptId:STR, featureName(s) Target:Obj, featureName:STR
        '''
        res = []
        if(CONCEPTS.M1ATTRIBUTE == conceptId):
            featureParent = self.mdb.Read(target, STR(M1ATTRIBUTE.OBJECT))
            featureNameStr = self.mdb.Read(self.mdb.Read(target, STR(M1ATTRIBUTE.M2ATTRIBUTE)), STR(M2ATTRIBUTE.NAME))
            res.append((conceptId,featureParent,featureNameStr,createArgs[2],NON()))
        elif(CONCEPTS.M1ASSOCIATION == conceptId):
            m2Feature = self.mdb.Read(target, STR(M1ASSOCIATION.M2ASSOCIATION))
            #associations have two ends
            featureParent = self.mdb.Read(target, STR(M1ASSOCIATION.SRC))
            featureNameStr = self.mdb.Read(m2Feature, STR(M2ASSOCIATION.SRCNAME))
            res.append((conceptId,featureParent,featureNameStr,createArgs[1],NON()))
            featureParent = self.mdb.Read(target, STR(M1ASSOCIATION.DST))
            featureNameStr = self.mdb.Read(m2Feature, STR(M2ASSOCIATION.DSTNAME))
            res.append((conceptId,featureParent,featureNameStr,createArgs[2],NON()))
        elif(CONCEPTS.M1COMPOSITION == conceptId):
            m2Feature = self.mdb.Read(target, STR(M1COMPOSITION.M2COMPOSITION))
            #compositions have two ends, but only one is relevant
            featureParent = self.mdb.Read(target, STR(M1COMPOSITION.PARENT))
            featureNameStr = self.mdb.Read(m2Feature, STR(M2COMPOSITION.NAME))
            res.append((conceptId,featureParent,featureNameStr,createArgs[2],NON()))
        return res
    
    def __GetUpdParamsFromM1FeatureDelete(self, conceptId:STR, createArgs:LST)->List[Tuple[STR,Obj,STR,PRM,PRM]]:
        '''Returns the feature name if the target is an M1 Feature.
        Else it returns NON.
        returns:
            res: List of triples composed of conceptId:STR, featureName(s) Target:Obj, featureName:STR
        '''
        res = []
        if(CONCEPTS.M1ATTRIBUTE == conceptId):
            featureParent = createArgs[1]
            featureNameStr = self.mdb.Read(createArgs[0], STR(M2ATTRIBUTE.NAME))
            res.append((conceptId,featureParent,featureNameStr,NON(),createArgs[2]))
        elif(CONCEPTS.M1ASSOCIATION == conceptId):
            m2Feature = createArgs[0]
            #associations have two ends
            featureParent = createArgs[1]
            featureNameStr = self.mdb.Read(m2Feature, STR(M2ASSOCIATION.SRCNAME))
            res.append((conceptId,featureParent,featureNameStr,NON(),createArgs[1]))
            featureParent = createArgs[2]
            featureNameStr = self.mdb.Read(m2Feature, STR(M2ASSOCIATION.DSTNAME))
            res.append((conceptId,featureParent,featureNameStr,NON(),createArgs[2]))
        elif(CONCEPTS.M1COMPOSITION == conceptId):
            m2Feature = createArgs[0]
            #compositions have two ends, but only one is relevant
            featureParent = createArgs[1]
            featureNameStr = self.mdb.Read(m2Feature, STR(M2COMPOSITION.NAME))
            res.append((conceptId,featureParent,featureNameStr,NON(),createArgs[2]))
        return res
    
    def __UnsetValueAndOldValue(self)->None:
        self.m1Values = []
        self.m1OldValues = []
    
    def __GetUpdateValueFromCreateArgs(self,conceptId:STR,createArgs:LST)->List[PRM]:
        values = []
        if(CONCEPTS.M1ATTRIBUTE == conceptId):
            value = createArgs[2] if len(createArgs)>1 else None
            values.append(value)
        elif(CONCEPTS.M1ASSOCIATION == conceptId):
            value = createArgs[2] if len(createArgs)>1 else None
            values.append(value)
        elif(CONCEPTS.M1COMPOSITION == conceptId):
            value = createArgs[2] if len(createArgs)>1 else None
            values.append(value)
        return values
    
    def __TrackAccessSettingsUpdates(self,target:Obj,featureNameStr:str, value:PRM, oldValue:PRM):
        # Check if a known user was updated
        if(target in self.usersObjLut):
            user = self.usersObjLut[target]
            normFeatureName = NormalizeFeatureName(featureNameStr)
            # #USER NAME UPDATE #not possible with concepts
            # if('name' == normFeatureName):
            #     name = value.GetVal()
            #     oldName = oldValue.GetVal()
            #     user.name = name
            #     #if the user name is set the first time, add it to the cache
            #     if(None == oldName):
            #         self.users[name] = user
            #     #if the user was renamed, update the cache
            #     elif(oldName and oldName in self.users):
            #         del self.users[oldName]
            #         self.users[name] = user
            # PASSHASH UPDATE        
            if('passhash' == normFeatureName):
                passhash = value.GetVal()
                user.passhash = passhash
            # USER GROUP UPDATE
            elif('groups' == normFeatureName):
                group = value.GetVal()
                oldGroup = oldValue.GetVal()
                #delete the old group if existing (don not care about the position)
                if(None != oldGroup): #delete group
                    del user.groups[oldGroup] #delete the group
                #add the new group if desired
                if(None != group):
                    user.groups[group] = True #add new group membership
            # USER EVENT UPDATE
            elif('events' == normFeatureName):
                eventType = value.GetVal()
                oldEventType = oldValue.GetVal()
                #delete the old event type if existing (don not care about the position)
                if(None != oldEventType):
                    del user.events[oldEventType] #delete the event
                #add the new event if desired
                if(None != eventType):
                    user.events[eventType] = True #add new event observation
            # USER SUPER EVENT UPDATE
            elif('superevents' == normFeatureName):
                eventType = value.GetVal()
                oldEventType = oldValue.GetVal()
                #delete the old event type if existing (don not care about the position)
                if(None != oldEventType): #delete 
                    del user.superevents[oldEventType] #delete the event
                #add the new event if desired
                if(None != eventType):
                    user.superevents[eventType] = True #add new event observation
        # Check if a known generic permission was updated
        elif(target in self.genericPermissionsLut):
            gp = self.genericPermissionsLut[target]
            normFeatureName = NormalizeFeatureName(featureNameStr)
            #USER NAME UPDATE
            if('targetClassId' == normFeatureName):
                gpClassId = value.GetVal()
                gpFeatureName = gp.featureName
                # if the feature name has already been set, we must check if this new class ID is unique
                if(None != gpFeatureName):
                    gpKey = (gpClassId,gpFeatureName)
                    self.genericPermissions[gpKey] = gp
                    #check if an old entry needs to be removed
                    if(not oldValue.IsNone()):
                        oldClassId = oldValue.GetVal()
                        oldGpKey = (oldClassId,gpFeatureName)
                        if(oldGpKey in self.genericPermissions):
                            del self.genericPermissions[oldGpKey]
                #not existing so change value
                gp.targetClassId = gpClassId
            elif('featureName' == normFeatureName):
                gpClassId = gp.targetClassId
                gpFeatureName = value.GetVal()
                # if the feature name has already been set, we must check if this new class ID is unique
                if(None != gpClassId):
                    gpKey = (gpClassId,gpFeatureName)
                    self.genericPermissions[gpKey] = gp
                    #check if an old entry needs to be removed
                    if(not oldValue.IsNone()):
                        oldClassId = oldValue.GetVal()
                        oldGpKey = (oldClassId,gpFeatureName)
                        if(oldGpKey in self.genericPermissions):
                            del self.genericPermissions[oldGpKey]
                #not existing so change value
                gp.featureName = gpFeatureName
            elif('owner' == normFeatureName):
                gp.owner = value.GetVal()
            elif('group' == normFeatureName):
                gp.group = value.GetVal()
            elif('permission' == normFeatureName):
                gp.permission = value.GetVal()
                
    def __ValidateAccessModelUpdates(self,target:Obj,featureNameStr:str,value:PRM):
        if(target in self.usersObjLut):
            user = self.usersObjLut[target]
            normFeatureName = NormalizeFeatureName(featureNameStr)
            #USER NAME UPDATE
            if('name' == normFeatureName):
                name = value.GetVal()
                #check if that name is already used
                if(name in self.users and user != self.users[name]):
                    raise EOQ_ERROR_INVALID_VALUE("User with name %s does already exist."%(name))
                #check if the user name is valid
                if(not self.__IsValidUserName(name)):
                    raise EOQ_ERROR_INVALID_VALUE("User name contains invalid chars. Only use A-Z, a-z, 0-9."%(name))
            # PASSHASH UPDATE        
            elif('passhash' == normFeatureName):
                passhash = value.GetVal()
                #check if the passhash is valid
                if(None != passhash and not IsValidPasshash(passhash)):
                    raise EOQ_ERROR_INVALID_VALUE("Invalid passhash.")
            # USER GROUP UPDATE
            elif('groups' == normFeatureName):
                pass
            # USER EVENT UPDATE
            elif('events' == normFeatureName):
                pass
            # USER SUPER EVENT UPDATE
            elif('superevents' == normFeatureName):
                pass
        # Check if a known generic permission was updated
        elif(target in self.genericPermissionsLut):
            gp = self.genericPermissionsLut[target]
            normFeatureName = NormalizeFeatureName(featureNameStr)
            #USER NAME UPDATE
            if('targetClassId' == normFeatureName):
                gpClassId = value.GetVal()
                gpFeatureName = gp.featureName
                # if the feature name has already been set, we must check if this new class ID is unique
                if(None != gpFeatureName):
                    gpKey = (gpClassId,gpFeatureName)
                    if(gpKey in self.genericPermissions):
                        #check uniqueness of permission
                        if(gp != self.genericPermissions[gpKey]):
                            raise EOQ_ERROR_INVALID_VALUE('Generic permission %s : %s does already exist.'%(gpClassId,gpFeatureName))
            elif('featureName' == normFeatureName):
                gpClassId = gp.targetClassId
                gpFeatureName = value.GetVal()
                # if the feature name has already been set, we must check if this new class ID is unique
                if(None != gpClassId):
                    gpKey = (gpClassId,gpFeatureName)
                    if(gpKey in self.genericPermissions):
                        #check uniqueness of permission
                        if(gp != self.genericPermissions[gpKey]):
                            raise EOQ_ERROR_INVALID_VALUE('Generic permission %s : %s does already exist.'%(gpClassId,gpFeatureName))
            elif('owner' == normFeatureName):
                pass
            elif('group' == normFeatureName):
                pass
            elif('permission' == normFeatureName):
                pass

    

    
