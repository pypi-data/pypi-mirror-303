#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework import *
from evo_package_huggingface.entity import *
from evo_package_chat.entity.EChatInput import EChatInput
from evo_package_chat.entity.EChatMessage import EChatMessage
from evo_package_chat.entity.EChatMapMessage import EChatMapMessage
from evo_package_chat.entity.EChatMapSession import EChatMapSession
from evo_package_chat.entity.EChatMapModel import EChatMapModel

#<
from hugchat import hugchat
from hugchat.hugchat import ChatBot, MessageNode, Assistant
from hugchat.login import Login
from evo_package_assistant import *
from evo_package_chat import *
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UHuggingfaceChatApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UHuggingfaceChatApi
"""
class UHuggingfaceChatApi(IChatProtocol):
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UHuggingfaceChatApi.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UHuggingfaceChatApi.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            self.mapSession:EvoMap = EvoMap()
            self.isUseDefault:bool = False
            self.defaultModelID:str = None
            self.defaultAssistantID:str = None
            self.clientChat:ChatBot = None
            self.eChatModelMap:EChatModelMap = None
            self.mapClientChat = {}
            self.mapConversation = {}
            self.mapModel = {}
            self.packageName:str = "huggingface"
            self.mapAssistantHF = {}
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UHuggingfaceChatApi instance
    """
    @staticmethod
    def getInstance():
        if UHuggingfaceChatApi.__instance is None:
            uObject = UHuggingfaceChatApi()  
            uObject.doInit()
        return UHuggingfaceChatApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):
        try:
            
            #self.mapAssistantHF["CyborgAI"] = "66a963f2f82d83bc8e35a40e"
            
            
            defaultOpenaiToken = CSetting.getInstance().doGet("ACCESS_TOKEN_HUGGING_FACE_TEST")
            self.defaultModelID = CSetting.getInstance().doGet("OPENAI_DEFAULT_MODELID")
            self.defaultAssistantID = CSetting.getInstance().doGet("OPENAI_DEFAULT_ASSISTANTID")
        
            isUseDefault:bool = True

            if IuText.StringEmpty(defaultOpenaiToken):
                isUseDefault=False
                
            if  IuText.StringEmpty(self.defaultModelID):
                isUseDefault=False
                
            if  IuText.StringEmpty(self.defaultAssistantID):
                isUseDefault=False
                
            self.isUseDefault = isUseDefault
            
            
            if self.isUseDefault:
                arrayLogin = str(defaultOpenaiToken).split("~")
                username = arrayLogin[0]
                password = "".join(arrayLogin[1:])
                
                hashToken=IuCryptHash.toSha256(username)
                cookie_path_dir = f"/tmp/cookies_{hashToken}/" 
            
                IuLog.doVerbose(__name__, f"log: {username}, {password}, {cookie_path_dir}")
            
                sign = Login(username, password)
                cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
            
                #IuLog.doVerbose(__name__, cookies.get_dict())
                self.clientChat = hugchat.ChatBot(cookies=cookies.get_dict())
                self.__doUpdateMapModel(clientChat=self.clientChat)
                IuLog.doWarning(__name__, "HuggingfaceChat ENV is SET")
            else:
                IuLog.doWarning(__name__,"HuggingfaceChat is none will use only client token input")
                #Cached 2024.1019
                arrayModel = [
                            'meta-llama/Meta-Llama-3.1-70B-Instruct',
                            'meta-llama/Meta-Llama-3.1-405B-Instruct-FP8', 
                            'CohereForAI/c4ai-command-r-plus' , 
                            'mistralai/Mixtral-8x7B-Instruct-v0.1' ,
                            'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO'
                            '01-ai/Yi-1.5-34B-Chat',
                            'mistralai/Mistral-7B-Instruct-v0.3',
                            'microsoft/Phi-3-mini-4k-instruct',
                            'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF'
                            ] 
                
               
                eChatMapModel = EChatMapModel()
                eChatMapModel.doGenerateID(self.packageName)
                eChatMapModel.apiPackage = self.packageName
                eChatMapModel.doGenerateTime()
              
                for model in arrayModel:
               
                    eChatModel = EChatModel()
                    eChatModel.doGenerateID(f"{self.packageName}|{model}", isHash=True)
                    eChatModel.name = f"{self.packageName}|{model}"
                    eChatModel.typeInput = 0 
                    eChatModel.apiPackage = self.packageName
                    eChatModel.callback = self
                    eChatMapModel.mapEChatModel.doSet(eChatModel)
                    UChatApi.getInstance().eChatMapModel.mapEChatModel.doSet(eChatModel)
                
                self.eChatModelMap = eChatMapModel
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise


# ---------------------------------------------------------------------------------------------------------------------------------------
    @override
    async def doOnChatStream(self, eAction:EAction, eChatInputIn:EChatInput|Any = None) -> EAction:
        """doOnChatStream utility callback
            input: EChatInput
            output: EChatMessage

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:
            #USE evo_package_chat 
            if eChatInputIn is None:
                eChatInput:EChatInput = eAction.doGetInput(EChatInput)
                #Dispose eAction.input for free memory
                eAction.input = b''
                
                if eChatInput is None:
                    raise Exception("ERROR_REQUIRED|eChatInput|")
            else:
                eChatInput = eChatInputIn
 
#<        

            #Add other check
            IuLog.doVerbose(__name__, f"{eChatInput}")
            
            if IuText.StringEmpty(eChatInput.apiToken):
                raise Exception("ERROR_REQUIRED|eChatInput.apiToken")
            
            if IuText.StringEmpty(eChatInput.text):
                raise Exception("ERROR_REQUIRED|eChatInput.text")
            
            eAssistant = await self.__doGetEAssistant(eChatInput)
            
            if eAssistant.callback is  None:
                raise Exception("ERROR_NOT_VALID|eAssistant.callback")
            
            cAssistantCallback = eAssistant.callback.clone()
            
            userMessage = await cAssistantCallback.onStart({"userMessage": eChatInput.text})

            clientChat = await self.__doGetClientChat(eChatInput)
            await self.__doUpdateMapModel(clientChat=clientChat)
                    
            eChatMessage = EChatMessage()
            eChatMessage.doGenerateID()
            eChatMessage.doGenerateTime()
            
            
            if eChatInput.modelID is not None:
                if eChatInput.modelID in self.mapModel: 
                    clientChat.current_conversation.model = self.mapModel[eChatInput.modelID]
            
             #TODO to foundation
            if eChatInput.sessionID is not None :# and eChatInput.sessionID in self.mapConversation:
                IuLog.doVerbose(__name__, f"session {eChatInput.sessionID}")
                if eChatInput.sessionID in self.mapConversation:
                    conversation = self.mapConversation[eChatInput.sessionID]
                else:   
                    try:
                        if eChatInput.sessionID not in self.mapConversation: 
                            await self.__doUpdateMapConversation(clientChat=clientChat, eChatInput=eChatInput)
                          
                            #conversation = chatbot.get_conversation_from_id("66a7475541b1e1acdffef6f1")
                        conversation = self.mapConversation[eChatInput.sessionID]
                        if conversation is not None:
                            conversation = clientChat.change_conversation(conversation)
                    except Exception as exception:
                        IuLog.doError(__name__,exception)
                    
                    #sys.exit(0)
            else:
                idNode = IuCryptHash.toSha256(eChatInput.text)
                system_prompt = eAssistant.systemMessage
                IuLog.doVerbose(__name__, f"new---- {system_prompt}")
                #conversation = clientChat.current_conversation
                #conversation.system_prompt = system_prompt
                #conversation.history.append(MessageNode(idNode,))
                #conversation.title = IuCryptHash.toSha256(eChatInput.text)
                
                if eAssistant.name in self.mapAssistantHF.keys():
                    IuLog.doVerbose(__name__, f"{eAssistant.name} {self.mapAssistantHF} ")
                    assistantID = self.mapAssistantHF[eAssistant.name]
                    #assistantHF = Assistant()
                    IuLog.doError(__name__, f"{assistantID} ")
                    conversation = clientChat.new_conversation(assistant=assistantID, switch_to=True) # create a new conversation with assistant
                else:
                    conversation = clientChat.new_conversation(system_prompt=system_prompt, switch_to=True)
                #clientChat.current_conversation = conversation
                #conversation = chatbot.new_conversation(system_prompt="act as senior engineer")
                eChatMessage.sessionID = IuKey.generateId(conversation.id)
                self.mapConversation[eChatMessage.sessionID] =  conversation
                

            conversation = clientChat.current_conversation
            eChatMessage.sessionID = IuKey.generateId(conversation.id)

            for resp in clientChat.chat(
                    userMessage,
                    conversation=conversation,
                    stream=True
                ):
                    if resp is None:
                        message = None
                    else:
                        message = resp["token"]
                    eApiText:EApiText =  await cAssistantCallback.doParser(message) #self.__doGetEApiTextEvent(eOpenaiInfo, event)
                    if eApiText is not None:
                        eChatMessage.eApiText = eApiText
                        eChatMessage.doGenerateTime()
                        eAction.enumApiAction = EnumApiAction.PARTIAL
                        
                        if eApiText.isComplete:
                            eAction.enumApiAction = EnumApiAction.COMPLETE
                            
                        if eApiText.isError:
                            eAction.enumApiAction = EnumApiAction.ERROR
                            eAction.error = eApiText.text.encode()
                        
                        eAction.doSetOutput(eChatMessage)        
                        
                        yield eAction
                        
                        if eApiText.isError:
                            break
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    @override
    async def doOnGetMapSession(self, eAction:EAction, eChatInputIn:EChatInput|Any = None) -> EAction:
        """doOnGetMapSession utility callback
            input: EChatInput
            output: EChatMapSession

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:
#<  
            #USE evo_package_chat 
            if eChatInputIn is None:
                eChatInput:EChatInput = eAction.doGetInput(EChatInput)
                #Dispose eAction.input for free memory
                eAction.input = b''
                
                if eChatInput is None:
                    raise Exception("ERROR_REQUIRED|eChatInput|")
            else:
                eChatInput = eChatInputIn
           
      
            username, _ = self.__doGetClientApiToken(eChatInput)
            
            clientChat = await self.__doGetClientChat(eChatInput)
            

            conversation_list = clientChat.get_remote_conversations(replace_conversation_list=True)
            sessionMapID = IuKey.generateId(f"huggingface_{username}", isHash=True)
        
            eChatMapSession = EChatMapSession()
            eChatMapSession.id = sessionMapID
            eChatMapSession.doGenerateTime()
                     
            for conversation in conversation_list:
                sessionID =  IuKey.generateId(conversation.id)
                eChatSession = EChatSession()
                eChatSession.name = conversation.title
                eChatSession.id = sessionID
                eChatSession.sessionID = sessionID
                eChatMapSession.mapEChatSession.doSet(eChatSession)
                self.mapConversation[sessionID] = conversation
                #UChatApi.getInstance().eChatMapSession.mapEChatSession.doSet(eChatSession)
                
            eAction.enumApiAction = EnumApiAction.COMPLETE
            
            
            IuLog.doVerbose(__name__, f"eChatMapSession: {eChatMapSession}")
            
            eAction.doSetOutput(eChatMapSession)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    @override
    async def doOnGetMapMessage(self, eAction:EAction, eChatInputIn:EChatInput|Any = None) -> EAction:
        """doOnGetMapMessage utility callback
            input: EChatInput
            output: EChatMapMessage

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:
#< 
            #USE evo_package_chat 
            if eChatInputIn is None:
                eChatInput:EChatInput = eAction.doGetInput(EChatInput)
                #Dispose eAction.input for free memory
                eAction.input = b''
                
                if eChatInput is None:
                    raise Exception("ERROR_REQUIRED|eChatInput|")
            else:
                eChatInput = eChatInputIn
           
     
          
            clientChat = await self.__doGetClientChat(eChatInput)
     
            conversation_list = clientChat.get_remote_conversations(replace_conversation_list=True)
            
            
            # Get conversation list(local)
            #conversation_list = clientChat.get_conversation_list()
            

            for conversation in conversation_list:
                try:
                    eChatMapMessage = EChatMapMessage()
                    eChatMapMessage.doGenerateID()
                    
                    conversation1 =clientChat.get_conversation_info(conversation.id)
                
                    
                    for messageNode in conversation1.history:
                        try:
                            enumChatRole = EnumChatRole.ASSISTANT
                            if messageNode.role.lower == "USER":
                                enumChatRole == EnumChatRole.USER
                            
                            if messageNode.role.lower == "SYSTEM":
                                enumChatRole == EnumChatRole.SYSTEM
                                
                            eChatMessage = EChatMessage()
                            eChatMessage.doGenerateID(messageNode.id)
                            eChatMessage.enumChatRole = enumChatRole
                            
                            eChatMessage.eApiText = EApiText()
                            eChatMessage.eApiText.doGenerateID()
                            eChatMessage.eApiText.text = messageNode.content
                            eChatMapMessage.mapEChatMessage.doSet(eChatMessage)
                            
                            
                        except Exception as exception:
                            IuLog.doException(__name__,exception)
                except Exception as exception:
                    IuLog.doException(__name__,exception)
                   
                   # IuLog.doVerbose(__name__, f"{messageNode.id}\n\t\t{messageNode.role}\n\t\t{messageNode.content}")
                   

           

            eAction.enumApiAction = EnumApiAction.COMPLETE
            IuLog.doVerbose(__name__, f"eChatMapMessage:{eChatMapMessage}")
            eAction.doSetOutput(eChatMapMessage)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnGetMapModel(self, eAction:EAction) -> EAction:
        """doOnGetMapModel utility callback
            input: EChatInput
            output: EChatModelMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:
           
#<        
            eChatInput:EChatInput = eAction.doGetInput(EChatInput)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if len(self.mapModel) == 0:
                if eChatInput is not None:
                    clientChat = await self.__doGetClientChat(eChatInput)
                    await self.__doUpdateMapModel(clientChat)
                
            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(self.eChatModelMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def __doUpdateMapConversation(self,clientChat:ChatBot,  eChatInput:EChatInput) :
        try:
          
            conversation_list = clientChat.get_remote_conversations(replace_conversation_list=True)
          
            eChatMapSession = EChatMapSession()
           # eChatMapSession.id = sessionMapID
            eChatMapSession.doGenerateTime()
                     
            for conversation in conversation_list:
                sessionID =  IuKey.generateId(conversation.id)
                eChatSession = EChatSession()
                eChatSession.id = sessionID
                eChatSession.sessionID = sessionID
                eChatMapSession.mapEChatSession.doSet(eChatSession)
                self.mapConversation[sessionID] = conversation
      
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
        
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def __doUpdateMapModel(self, clientChat:ChatBot) :
        try:
            
            if len(self.mapModel) == 0:
                
                eChatMapModel = EChatMapModel()
                eChatMapModel.doGenerateID(self.packageName)
                eChatMapModel.apiPackage = self.packageName
                eChatMapModel.doGenerateTime()
                
                
                arrayModel = clientChat.get_remote_llms()
                IuLog.doVerbose(__name__, f"arrayModel:\n {arrayModel}")
              
                for model in arrayModel:
          
                    eChatModel = EChatModel()
                    eChatModel.doGenerateID(f"{self.packageName}|{model.id}", isHash=True)
                    eChatModel.name = f"{self.packageName}|{model.displayName}"
                    eChatModel.typeInput = 0 
                    eChatModel.apiPackage = self.packageName
                    eChatModel.callback = self
                    eChatMapModel.mapEChatModel.doSet(eChatModel)
                    UChatApi.getInstance().eChatMapModel.mapEChatModel.doSet(eChatModel)
                    self.mapModel[eChatModel.id] = model
                   
            
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def __doGetEAssistant(self, eChatInput:EChatInput) -> EAssistant:
        try:
          
            if IuText.StringEmpty(eChatInput.eAssistantID):
                eAssistantID = self.defaultAssistantID
            else:
                eAssistantID= eChatInput.eAssistantID

            if IuText.StringEmpty(eAssistantID):
              raise Exception("ERROR_REQUIRED|eChatInput.eAssistantID|")
            
            eAssistant= await UAssistantApi.getInstance().doGetEAssistant(eAssistantID)
            
            return eAssistant
            
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise

# ---------------------------------------------------------------------------------------------------------------------------------------
    
    def __doGetClientApiToken(self, eChatInput:EChatInput):
        try:

            if IuText.StringEmpty(eChatInput.apiToken):
                raise Exception("ERROR_REQUIRED|eChatInput.apiToken")
        
            arrayLogin = str(eChatInput.apiToken).split("~")
            username = arrayLogin[0]
            password = "".join(arrayLogin[1:])
            
            return username, password
                    
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise 
# ---------------------------------------------------------------------------------------------------------------------------------------
    
    async def __doGetClientChat(self, eChatInput:EChatInput) -> ChatBot:
        try:
            
            if self.clientChat is not None:
                return self.clientChat
            else:
                
                if IuText.StringEmpty(eChatInput.apiToken):
                    raise Exception("ERROR_REQUIRED|eChatInput.apiToken")
                
                username, password = self.__doGetClientApiToken(eChatInput)

                hashToken=IuCryptHash.toSha256(username)
                
                if hashToken in self.mapClientChat:
                    chatbot:ChatBot = self.mapClientChat[hashToken]
                    #TODO:check remome after
                    return  chatbot
                
                else:

                    cookie_path_dir = f"/tmp/cookies_{hashToken}/"    
                    IuLog.doVerbose(__name__, f"log: {username} {cookie_path_dir}")
                
                    sign = Login(username, password)
                    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
                    
               
                    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
                    self.mapClientChat[hashToken] = chatbot
                    return chatbot
                    
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
      
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
