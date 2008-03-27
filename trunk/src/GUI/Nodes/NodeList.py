from NodeTypes.NodeVarInit import NodeVarInit
from NodeTypes.NodeType01 import NodeType01
from NodeTypes.NodeType02 import NodeType02



class _CreateType01(NodeType01):
    def __init__(self):
        pass

    def _name(self):
        return "CreateType01"

    def _mainNode01(self,InputParameters):
        return self.BasicShape01(InputParameters)

    def _previewNode01(self,InputParameters):
        return self.PreviewShape01(InputParameters)

class _CreateType02(NodeType02):

    def __init__(self):
        pass

    def _name(self):
        return "CreateType02"

    def _mainNode02(self,InputParameters):
        return self.BasicShape02(InputParameters)

    def _previewNode02(self,InputParameters):
        return self.PreviewShape02(InputParameters)


class Nodes(_CreateType01,_CreateType02):
    def __init__(self):
        pass

    def _name(self):
        return "CreateNode"

    def _CreateMainNode(self,InputParameters):
        if InputParameters[5][0] == 'SHAPE01':
            return self._mainNode01(InputParameters)
        elif InputParameters[5][0] == 'SHAPE02':
            return self._mainNode02(InputParameters)
        else:
            pass

    def _CreatePreviewNode(self,InputParameters):
        if InputParameters[5][0] == 'SHAPE01':
            return self._previewNode01(InputParameters)
        elif InputParameters[5][0] == 'SHAPE02':
            return self._previewNode02(InputParameters)
        else:
            pass


    def PutNode(self,InputParameters):
        if InputParameters[3] == 'MAIN':
            return self._CreateMainNode(InputParameters)
        else:
            return self._CreatePreviewNode(InputParameters)


class NodeListCategoriser(Nodes,NodeVarInit):
    def __init__(self):
        pass

    def _name(self):
        return "NodeListCantegoriser"

    def CreateNodefromList(self,TargetCanvas,x,y,Type,Ident):

            Generated=self.GenerateVars(TargetCanvas,x,y,Ident,Type)
            self.PutNode(Generated)
            if Ident =="MAIN":
                self.RegisterRuntimeNode(Generated)
            else:
                pass

