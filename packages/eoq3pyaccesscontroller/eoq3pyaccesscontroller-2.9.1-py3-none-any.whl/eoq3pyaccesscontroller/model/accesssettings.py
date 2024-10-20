from eoq3.value import BOL, U32, I64, STR, LST, NON
from eoq3.query import His
from eoq3.command import Cmp

class ACCESS_SETTINGS_PACKETS:
    ACCESSSETTINGS = "https://www.eoq-dsm.org/models/accesssettings"

class ACCESS_SETTINGS_CLASSES:
    ACCESSSETTINGS = "https://www.eoq-dsm.org/models/accesssettings__AccessSettings"
    USER = "https://www.eoq-dsm.org/models/accesssettings__User"
    GENERICPERMISSION = "https://www.eoq-dsm.org/models/accesssettings__GenericPermission"

ACCESS_SETTINGS_CMD = Cmp()\
    .Crt(STR('*M2MODEL'),U32(1),LST([STR('https://www.eoq-dsm.org/models/accesssettings')]),NON(),LST([]),resName='o0')\
    .Crt(STR('*M2CLASS'),U32(1),LST([STR('AccessSettings'),BOL(False),His(STR('o0'))]),NON(),LST([]),resName='o1')\
    .Crt(STR('*M2CLASS'),U32(1),LST([STR('User'),BOL(False),His(STR('o0'))]),NON(),LST([]),resName='o2')\
    .Crt(STR('*M2CLASS'),U32(1),LST([STR('GenericPermission'),BOL(False),His(STR('o0'))]),NON(),LST([]),resName='o3')\
    .Crt(STR('*M2COMPOSITION'),U32(1),LST([STR('users'),His(STR('o1')),His(STR('o2')),I64(-1),BOL(False)]),NON(),LST([]),resName='o4')\
    .Crt(STR('*M2COMPOSITION'),U32(1),LST([STR('genericPermissions'),His(STR('o1')),His(STR('o3')),I64(-1),BOL(False)]),NON(),LST([]),resName='o5')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('groups'),His(STR('o2')),STR('*STR'),I64(-1),NON(),NON()]),NON(),LST([]),resName='o6')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('events'),His(STR('o2')),STR('*STR'),I64(-1),NON(),NON()]),NON(),LST([]),resName='o7')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('superevents'),His(STR('o2')),STR('*STR'),I64(-1),NON(),NON()]),NON(),LST([]),resName='o8')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('description'),His(STR('o2')),STR('*STR'),I64(1),NON(),NON()]),NON(),LST([]),resName='o9')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('passhash'),His(STR('o2')),STR('*STR'),I64(1),NON(),NON()]),NON(),LST([]),resName='o10')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('targetClassId'),His(STR('o3')),STR('*STR'),I64(1),NON(),NON()]),NON(),LST([]),resName='o11')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('featureName'),His(STR('o3')),STR('*STR'),I64(1),NON(),NON()]),NON(),LST([]),resName='o12')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('owner'),His(STR('o3')),STR('*STR'),I64(1),NON(),NON()]),NON(),LST([]),resName='o13')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('group'),His(STR('o3')),STR('*STR'),I64(1),NON(),NON()]),NON(),LST([]),resName='o14')\
    .Crt(STR('*M2ATTRIBUTE'),U32(1),LST([STR('permission'),His(STR('o3')),STR('*I32'),I64(1),NON(),NON()]),NON(),LST([]),resName='o15')