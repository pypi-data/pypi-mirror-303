#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework import *
from evo_package_huggingface.entity import *
from evo_package_huggingface.utility import *
from evo_package_chat.entity.EChatInput import EChatInput
from evo_package_chat.entity.EChatMessage import EChatMessage
from evo_package_chat.entity.EChatMapModel import EChatMapModel
from evo_package_chat.entity.EChatMapMessage import EChatMapMessage
from evo_package_chat.entity.EChatMapSession import EChatMapSession

# ---------------------------------------------------------------------------------------------------------------------------------------
# CHuggingfaceChatApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""CHuggingfaceChatApi
"""
class CHuggingfaceChatApi(CApi):
	__instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
	def __init__(self):   
		if CHuggingfaceChatApi.__instance != None:
			raise Exception("ERROR:SINGLETON")
		else:
			super().__init__()
			CHuggingfaceChatApi.__instance = self
			self.currentPath = os.path.dirname(os.path.abspath(__file__))
			
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""getInstance Singleton

	Raises:
		Exception:  api exception

	Returns:
		_type_: CHuggingfaceChatApi instance
	"""
	@staticmethod
	def getInstance():
		if CHuggingfaceChatApi.__instance is None:
			cObject = CHuggingfaceChatApi()  
			cObject.doInit()  
		return CHuggingfaceChatApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""doInit

	Raises:
		Exception: api exception

	Returns:

	"""   
	def doInit(self):   
		try:			
			UHuggingfaceChatApi.getInstance()
		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise	  
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""doAddApi

	Raises:
		Exception: api exception

	Returns:

	"""
	@override   
	def doAddApi(self):
		try:			
			
			api0 = self.newApi("huggingface-chatstream", callback=self.onChatStream, input=EChatInput, output=EChatMessage )
			api0.description="huggingface-chatstream _DESCRIPTION_ [USE evo.package.chat API]"
			api0.required="*"

			api1 = self.newApi("huggingface-get_mapmodel", callback=self.onGetMapModel, input=EChatInput, output=EChatMapModel )
			api1.description="huggingface-get_mapmodel _DESCRIPTION_ [USE evo.package.chat API]"
			api1.required="eChatInput.token"

			api2 = self.newApi("huggingface-get_mapmessage", callback=self.onGetMapMessage, input=EChatInput, output=EChatMapMessage )
			api2.description="huggingface-get_mapmessage _DESCRIPTION_ [USE evo.package.chat API]"
			api2.required="eChatInput.token|eChatInput.sessionID"

			api3 = self.newApi("huggingface-get_mapsession", callback=self.onGetMapSession, input=EChatInput, output=EChatMapSession )
			api3.description="huggingface-get_mapsession _DESCRIPTION_ [USE evo.package.chat API]"
			api3.required="eChatInput.token"
  
		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onChatStream api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onChatStream(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onChatStream: {eAction} ")

					
			async for eActionOutput in UHuggingfaceChatApi.getInstance().doOnChatStream(eAction):
				#IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onGetMapModel api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGetMapModel(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGetMapModel: {eAction} ")

					
			async for eActionOutput in UHuggingfaceChatApi.getInstance().doOnGetMapModel(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onGetMapMessage api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGetMapMessage(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGetMapMessage: {eAction} ")
	
			async for eActionOutput in UHuggingfaceChatApi.getInstance().doOnGetMapMessage(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onGetMapSession api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGetMapSession(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGetMapSession: {eAction} ")

					
			async for eActionOutput in UHuggingfaceChatApi.getInstance().doOnGetMapSession(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------
