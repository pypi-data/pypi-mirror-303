#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework import *
from evo_package_firebase.entity import *
from evo_framework.core.evo_core_api.entity.EApiQuery import EApiQuery

#<
import firebase_admin
from firebase_admin import credentials, firestore, storage
from typing import List
import lz4

#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UFirebaseApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UFirebaseApi
"""
class UFirebaseApi():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UFirebaseApi.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UFirebaseApi.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            self.database = None
            self.storage = None
            
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UFirebaseApi instance
    """
    @staticmethod
    def getInstance():
        if UFirebaseApi.__instance is None:
            uObject = UFirebaseApi()  
        return UFirebaseApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):   
        try:
#<
            if self.database is None or  self.storage is None:
                ACCESS_TOKEN_FIREBASE=CSetting.getInstance().doGet("ENV_FIREBASE-API_TOKEN")
                
                if IuText.StringEmpty(ACCESS_TOKEN_FIREBASE):
                    raise Exception("ERROR_REQUIRED_ENV|ENV_FIREBASE-API_TOKEN")
                #print("\n\n",ACCESS_TOKEN_FIREBASE)
                mapFirebase=json.loads(ACCESS_TOKEN_FIREBASE)
                #print("\n\nmapFirebase\n",mapFirebase)
                cred = credentials.Certificate(mapFirebase)
                
                projectID = mapFirebase["project_id"]
                firebase_admin.initialize_app(cred, {
                    'storageBucket': f'{projectID}.appspot.com'
                })
                self.database = firestore.client()
                self.storage = storage.bucket()
#>   
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnSet(self, eAction:EAction) -> EAction:
        """doOnSet utility callback
            input: EApiQuery
            output: EFirebaseMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery")

#<        
            await self.doSet(collection=str(eApiQuery.collection),
                             id=eApiQuery.eObjectID, 
                             data=eApiQuery.data)
           
   
            eFirebaseMap = EFirebaseMap()
            eFirebaseMap.doGenerateID()
            eFirebaseMap.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eFirebaseMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnGet(self, eAction:EAction) -> EAction:
        """doOnGet utility callback
            input: EApiQuery
            output: EFirebaseMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            IuLog.doVerbose(__name__, f"doOnGet {eApiQuery}")
          
            data = await self.doGet(collection=str(eApiQuery.collection), id=eApiQuery.eObjectID)
            
            if data is None:
                raise Exception(f"ERROR_GET_{eApiQuery.collection}_{eApiQuery.eObjectID!r}")
            
   
            eFirebaseMap = EFirebaseMap()
            eFirebaseMap.doGenerateID()
            eFirebaseMap.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eFirebaseMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnDel(self, eAction:EAction) -> EAction:
        """doOnDel utility callback
            input: EApiQuery
            output: EFirebaseMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            #Add other check
            '''
            if eApiQuery. is None:
                raise Exception("ERROR_REQUIRED|eApiQuery.|")
            '''
   
            eFirebaseMap = EFirebaseMap()
            eFirebaseMap.doGenerateID()
            eFirebaseMap.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eFirebaseMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnDelAll(self, eAction:EAction) -> EAction:
        """doOnDelAll utility callback
            input: EApiQuery
            output: EFirebaseMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            #Add other check
            '''
            if eApiQuery. is None:
                raise Exception("ERROR_REQUIRED|eApiQuery.|")
            '''
   
            eFirebaseMap = EFirebaseMap()
            eFirebaseMap.doGenerateID()
            eFirebaseMap.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eFirebaseMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnQuery(self, eAction:EAction) -> EAction:
        """doOnQuery utility callback
            input: EApiQuery
            output: EFirebaseMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            #Add other check
            '''
            if eApiQuery. is None:
                raise Exception("ERROR_REQUIRED|eApiQuery.|")
            '''

            eFirebaseMap = await self.doQuery(collection=str(eApiQuery.collection), query=eApiQuery.query)

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eFirebaseMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doSet(self, collection:str, id: bytes, data:bytes, isEncrypt:bool=False):
        try:
            idHex = IuKey.toString(id)
            
            IuLog.doVerbose(__name__, f"doSet: collection:{ collection} idHex:{ idHex}")
            timeCurrent = IuKey.generateTime()
            hashData= IuCryptHash.toSha256(data)
            
            if isEncrypt:
                dataCrypt = IuSettings.doEncrypt(data)
            else:
                dataCrypt = data
             
            blob = self.storage.blob(idHex)
            
            if await asyncio.to_thread(blob.exists):
                IuLog.doWarning(__name__,f"WARNING_update_{collection}_{idHex}_doDel")
                #raise Exception(f"ERROR_{collection}_{iD}_doDel")
                await self.doDel(collection, id)

            await asyncio.to_thread(blob.upload_from_string, dataCrypt)

           # await asyncio.to_thread(blob.make_public)
            
            cyborgaiID = CSetting.getInstance().doGet("CYBORGAI_ID")

            url=blob.public_url
            
            if url is None:
                 raise Exception(f"ERROR_GET_{collection}_{idHex}")
        
            mapInfo = {
                'id':idHex,
                'time':timeCurrent,
                'hash':hashData,
                'encrypt':isEncrypt,
               # 'url':url,
                'cyborgaiID':cyborgaiID
            }
            
            doc_ref = self.database.collection(collection).document(idHex)
            doc_ref.set(mapInfo)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise

# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doGet(self, collection:str, id: bytes ) -> bytes:
        try:
            IuLog.doVerbose(__name__, f"doGet {collection} {id!r}")
            idHex = IuKey.toString(id)
            IuLog.doVerbose(__name__, f"idHex:\n{ idHex}")
            
            doc_ref = self.database.collection(collection).document(idHex)
            doc = doc_ref.get()
            
            IuLog.doVerbose(__name__, f"doc:{ doc.to_dict()}")
          
            if not doc.exists:
                raise Exception(f"ERROR_GET|{collection}_{idHex}")
            
            mapInfo = doc.to_dict()
            
            IuLog.doVerbose(__name__, f"mapInfo:\n{mapInfo}")
            
            if mapInfo is None:
                raise Exception(f"ERROR_GET|MAPINFO{collection}_{idHex}")
                   
            blob = self.storage.blob(mapInfo["id"])
            
            dataEncrypt = await asyncio.to_thread(blob.download_as_bytes)
            
            if dataEncrypt is None:
                raise Exception(f"ERROR|dataEncrypt_{collection}_{idHex}")
            
            data = dataEncrypt
            
            if mapInfo['encrypt']:
                data = IuSettings.doDecrypt(dataEncrypt)
  
            if data is None:
                raise Exception(f"ERROR|data_{collection}_{idHex}")
            
            return data
    
            '''
            async with aiofiles.open(download_path, 'wb') as f:
                await asyncio.to_thread(blob.download_to_file, f)
            '''
            
            
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        

# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doDel(self, collection:str, id: bytes ):
        try:
            idHex = IuKey.toString(id)
            doc_ref = self.database.collection(collection).document(idHex)
            await asyncio.to_thread(doc_ref.delete)
            blob = self.storage.blob(idHex)
            await asyncio.to_thread(blob.delete)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doDelAll(self, collection:str):
        try:           
            docs_ref = self.database.collection(collection)
            arrayDoc = await asyncio.to_thread(docs_ref.stream)
            
            for doc in arrayDoc:
                mapInfo = doc.to_dict()
                await self.doDel(collection, mapInfo["id"] )
                
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doQuery(self, collection:str, query: str) -> EFirebaseMap:
        try:
            eFirebaseMap = EFirebaseMap()
            eFirebaseMap.doGenerateID()
            
            docs_ref = self.database.collection(collection)
            arrayDoc = await asyncio.to_thread(docs_ref.stream)
            
            IuLog.doVerbose(__name__, f"arrayDoc {collection} => {arrayDoc}")
            
            for doc in arrayDoc: 
                mapInfo = doc.to_dict()
                if "id" in mapInfo:
                    IuLog.doVerbose(__name__, f"{collection} => {mapInfo['id']}")
                    eObjectIDHex = mapInfo["id"]
                    eObjectID = IuConvert.fromHex(eObjectIDHex)
                    
                    #TODO: CONVERT to EAPIQUERY REsult
                    eApiQuery = EApiQuery()
                    eApiQuery.id=  IuCryptHash.toSha256Bytes(f"{collection}_{eObjectIDHex}")
                    eApiQuery.eObjectID = eObjectID
                    eApiQuery.collection = int(collection)
                    #data = await self.doGet(collection, eObjectID)
                    #eApiQuery.data = data
                    eFirebaseMap.mapEFirebase.doSet(eApiQuery)
                    
            IuLog.doVerbose(__name__,f"{eFirebaseMap}")
            return eFirebaseMap
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
