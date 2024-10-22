#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework import *
from evo_package_firebase.entity import *
from evo_package_firebase.utility import *
from evo_framework.core.evo_core_api.entity.EApiQuery import EApiQuery

# ---------------------------------------------------------------------------------------------------------------------------------------
# CFirebaseApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""CFirebaseApi
"""
class CFirebaseApi(CApi):
	__instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
	def __init__(self):   
		if CFirebaseApi.__instance != None:
			raise Exception("ERROR:SINGLETON")
		else:
			super().__init__()
			CFirebaseApi.__instance = self
			self.currentPath = os.path.dirname(os.path.abspath(__file__))
			
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""getInstance Singleton

	Raises:
		Exception:  api exception

	Returns:
		_type_: CFirebaseApi instance
	"""
	@staticmethod
	def getInstance():
		if CFirebaseApi.__instance is None:
			cObject = CFirebaseApi()  
			cObject.doInit()  
		return CFirebaseApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""doInit

	Raises:
		Exception: api exception

	Returns:

	"""   
	def doInit(self):   
		try:			
			UFirebaseApi.getInstance().doInit()
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
			
			api0 = self.newApi("firebase-set", callback=self.onSet, input=EApiQuery, output=EFirebaseMap )
			api0.description="firebase-set description"
			api0.required="*"

			api1 = self.newApi("firebase-get", callback=self.onGet, input=EApiQuery, output=EFirebaseMap )
			api1.description="firebase-get description"
			api1.required="*"

			api2 = self.newApi("firebase-del", callback=self.onDel, input=EApiQuery, output=EFirebaseMap )
			api2.description="firebase-del description"
			api2.required="*"

			api3 = self.newApi("firebase-del_all", callback=self.onDelAll, input=EApiQuery, output=EFirebaseMap )
			api3.description="firebase-del_all description"
			api3.required="*"

			api4 = self.newApi("firebase-query", callback=self.onQuery, input=EApiQuery, output=EFirebaseMap )
			api4.description="firebase-query description"
			api4.required="*"
  
		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onSet api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onSet(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onSet: {eAction} ")

					
			async for eActionOutput in UFirebaseApi.getInstance().doOnSet(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onGet api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGet(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGet: {eAction} ")

					
			async for eActionOutput in UFirebaseApi.getInstance().doOnGet(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onDel api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onDel(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onDel: {eAction} ")

					
			async for eActionOutput in UFirebaseApi.getInstance().doOnDel(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onDelAll api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onDelAll(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onDelAll: {eAction} ")

					
			async for eActionOutput in UFirebaseApi.getInstance().doOnDelAll(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onQuery api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onQuery(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onQuery: {eAction} ")

					
			async for eActionOutput in UFirebaseApi.getInstance().doOnQuery(eAction):
				IuLog.doVerbose(__name__, f"{eActionOutput}")
				yield eActionOutput	


		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------
