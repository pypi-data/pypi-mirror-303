#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

#========================================================================================================================================
"""EHuggingfaceChatInput

	EHuggingfaceInput DESCRIPTION
	
"""
class EHuggingfaceChatInput(EObject):

	VERSION:int = 134812973045988992

	def __init__(self):
		super().__init__()
		self.Version:int = self.VERSION
		
		self.username:str = None
		self.password:str = None
		self.input:str = None
		self.isWebSearch:bool = False
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteStr(self.username, stream)
		self._doWriteStr(self.password, stream)
		self._doWriteStr(self.input, stream)
		self._doWriteBool(self.isWebSearch, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.username = self._doReadStr(stream)
		self.password = self._doReadStr(stream)
		self.input = self._doReadStr(stream)
		self.isWebSearch = self._doReadBool(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tusername:{self.username}",
				f"\tpassword:{self.password}",
				f"\tinput:{self.input}",
				f"\tisWebSearch:{self.isWebSearch}",
							]) 
		return strReturn
	