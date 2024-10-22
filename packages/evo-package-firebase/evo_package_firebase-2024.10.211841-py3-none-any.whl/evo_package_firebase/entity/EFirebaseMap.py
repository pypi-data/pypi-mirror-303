#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EApiQuery import EApiQuery
#========================================================================================================================================
"""EFirebaseMap

    EFirebaseMap DOC
    
"""
class EFirebaseMap(EObject):

    VERSION:int=7428769006888398516

    def __init__(self):
        super().__init__()
        self.Version:int = self.VERSION
        
        self.mapEFirebase:EvoMap = EvoMap()
  
    def toStream(self, stream):
        super().toStream(stream)
        
        self._doWriteMap(self.mapEFirebase, stream)
        
    def fromStream(self, stream):
        super().fromStream(stream)
        
        self.mapEFirebase = self._doReadMap(EApiQuery, stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                super().__str__(),
                            
                f"\tmapEFirebase:{self.mapEFirebase}",
                            ]) 
        return strReturn
    