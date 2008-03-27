from random import *
from Dbase.DBaseManagement import RuntimeNodeRegister,VarDefs


class NodeVarInit(RuntimeNodeRegister,VarDefs):
    def __init__(self):
        pass

    def _NewNodeID(self):
        chc="false"
        ID=0
        while chc is "false":
            ID=randrange(1000,1000000)
            chc=self.IDChc(ID)
        return ID


    def _NewPreviewNodeID(self):
        chc="false"
        ID=0
        while chc is "false":
            ID=randrange(0,999)
            chc=self.IDChc(ID)
        return ID

    def _initVars(self,TargetCanvas,ID,x,y,Ident,Functype):
        VarInitReturn=[]
        VarInitReturn.append(TargetCanvas)
        VarInitReturn.append(str(ID))
        cord=(x,y)
        VarInitReturn.append(cord)
        VarInitReturn.append(Ident)
        VarInitReturn.append(str(Functype))
        VarsFromDb=self.GetVars(Functype)
        VarInitReturn.append(VarsFromDb)
        if Ident == "MAIN":
            print Functype+" created (" + str(VarInitReturn[1]) + ")"
        else:
            VarInitReturn[1]=self._NewPreviewNodeID()

        return VarInitReturn

    def _name(self):
        return "NodeVarInit"

    def GenerateVars(self,TargetCanvas,x,y,Ident,Functype):
        ID=self._NewNodeID()
        ReturnVar=self._initVars(TargetCanvas,ID,x,y,Ident,Functype)
        return ReturnVar

    def forceID(self,VariableSet,NewID):
        VariableSet[1]=NewID
        return VariableSet
