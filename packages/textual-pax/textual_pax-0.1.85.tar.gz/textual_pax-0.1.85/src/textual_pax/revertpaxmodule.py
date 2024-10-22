import asyncio
import aiohttp
import hmac
import time
import hashlib
from urllib.parse import urlencode, urlunsplit
import pandas as pd
import os
from .tui_exceptions import TerminalNotFoundError


class PaxTerms():

    def __init__(self, serialNo:str) -> None:

    
        self.termtool = {
            "119": {"modelName": "E600", "serial_range":"119", "name":"TR_E600", "type":"Ev1_Series", "terminal_no":"12", "resellerName": "Repair","fmName":"E600_PayDroid_7.1.1_Virgo_V04.1.18_20240124", "hasAccessory":True, "accessory":
            {"modelName":"Q20L", "serial_range": "114", "name": "TR_E600-Q20", "type":"Qv1_Series", "terminal_no":"124", "resellerName": "Repair"}},
            "134": {"modelName": "E700", "serial_range":"134", "name":"TR_E700", "type":"Ev1_Series", "resellerName": "Repair","fmName": "E700_PayDroid_7.1.2_Scorpio_V10.1.29_20240320", "hasAccessory":True, "accessory":
            {"modelName":"Q20L", "serial_range": "114", "name": "TR_E700-Q20", "type":"Qv1_Series", "terminal_no":"124", "resellerName": "Repair"}},
            "115": {"modelName": "E500", "serial_range":"115", "name":"TR_E500", "type":"Ev1_Series", "terminal_no":"2", "resellerName": "Repair","fmName": "E500_PayDroid_6.0.1_Taurus_V05.1.25_20230313","hasAccessory":True, "accessory":
            {"modelName":"Q20L", "serial_range": "114", "name": "TR_E500-Q20", "type":"Qv1_Series", "terminal_no":"124", "resellerName": "Repair"}},
            "227": {"modelName": "E600M", "serial_range":"227", "name":"TR_E600M", "type":"Ev2_Series", "terminal_no":"415",  "resellerName": "Repair","fmName": "PayDroid_10.0.0_Acacia_V13.1.18_20240105","hasAccessory":True,"accessory":
            {"modelName":"Q10A", "serial_range": "240", "name": "TR_E600M-Q10", "type":"Qv2_Series", "terminal_no":"416", "resellerName": "Repair"}},
            "082": {"modelName": "A920", "serial_range":"082", "name":"TR_A920", "type":"A_Series", "terminal_no":"1", "resellerName": "Repair","fmName": "PayDroid_5.1.1_Aquarius_V02.3.46_20240410","hasAccessory":False},
            "185": {"modelName": "A920Pro", "serial_range":"185", "name":"TR_A920Pro", "type":"A_Series", "terminal_no":"341", "resellerName": "Repair","fmName": "PayDroid_8.1.0_Sagittarius_V11.1.62_20240411","hasAccessory":False},
            "135": {"modelName": "A60", "serial_range":"135", "name":"TR_A60", "type":"A_Series", "terminal_no":"19",  "resellerName": "Repair","fmName": "A60_PayDroid_6.0_Leo_V07.1.17_20240415","hasAccessory":False},
            "124": {"modelName": "A80", "serial_range":"124", "name":"TR_A80", "type":"A_Series", "terminal_no":"26", "resellerName": "Repair","fmName": "PayDroid_10.0_Cedar_V17.2.19_20240313", "hasAccessory":False},
            "176": {"modelName": "A77", "serial_range":"176", "name":"TR_A77", "type":"A_Series", "terminal_no":"271", "resellerName": "Repair","fmName": "PayDroid_8.1.0_Sagittarius_V11.1.62_20240411","hasAccessory":False},
            "3A4": {"modelName": "SP30s", "serial_range":"3A4", "name":"TR_SP30", "type":"A_Series", "terminal_no":"180", "resellerName": "Repair", "hasAccessory":False},
            "3A6": {"modelName": "SP30s", "serial_range":"3A6", "name":"TR_SP30", "type":"A_Series", "terminal_no":"180", "resellerName": "Repair", "hasAccessory":False},
            "3A7": {"modelName": "SP30s", "serial_range":"3A7", "name":"TR_SP30", "type":"A_Series", "terminal_no":"180", "resellerName": "Repair", "hasAccessory":False},
            "3L0": {"modelName": "SP30s", "serial_range":"3L0", "name":"TR_SP30", "type":"A_Series", "terminal_no":"180", "resellerName": "Repair", "hasAccessory":False},
            "229": {"modelName": "A35", "serial_range":"229", "name":"RKI_A35", "type":"A_Series", "terminal_no":"362", "resellerName": "Repair","fmName": "PayDroid_10.0_Cedar_V17.2.19_20240313", "hasAccessory":False},
            "114": {"modelName": "Q20L", "serial_range":"114","name":"TR_Q20", "type":"Qv1_Series", "hasAccessory":False, "resellerName":"Repair", "fmName":None},
            "240": {"modelName": "Q10A", "serial_range":"240","name":'TR_E600M-Q10', "type":"Qv2_Series","fmName": "Q10A_PayDroid_10_Cedar_V17.1.13_20240322","resellerName":"Repair", "hasAccessory":False},
            "189": {"modelName": "D135", "serial_range":"189", "name":"TR_D135", "type":"D-Series", "terminal_no":"421", "resellerName": "Repair", "hasAccessory":False},
        }
        
        self.pushPATool = {
                "A_SeriespackageName": "com.pax.us.pay.std.broadpos.p2pe",
                "A_SeriespushTemplateName": "PA 6.9.1 E600M BroadPos P2PE V1.05.06",
                "A_SeriestemplateName":  "p2pe_20240325.zip",
                "A_Seriesversion": "V1.05.06_20240325",
                "Qv2_SeriespackageName": "com.pax.us.pay.std.broadpos.p2pe",
                "Qv2_SeriespushTemplateName": "PA 6.9.1 E600M BroadPos P2PE V1.05.06",
                "Qv2_SeriestemplateName": "p2pe_20240325.zip",
                "Qv2_Seriesversion": "V1.05.06_20240325",
                "Qv1_SeriespackageName":"BroadPOS-P2PE-Q20L",
                "Qv1_SeriespushTemplateName": "PA 6.8 Q20 BroadPOS P2PE Q20L V1.01.05_20230413",
                "Qv1_SeriestemplateName": "config.zip",
                "Qv1_Seriesversion": "V1.01.05_20230413",
                "Ev1_SeriespackageName": "com.pax.pdm",
                "Ev1_SeriestemplateName": "BasicSystem-Q20L_V1.00.07.zip",
                "Ev1_Seriesversion": None,
                "Ev1_SeriespushTemplateName": None,
                "Ev2_SeriespackageName": None,
                "Ev2_SeriestemplateName": None,
                "Ev2_Seriesversion": None,
                "Ev2_SeriespushTemplateName": None
        }
        
        
        self.serialNo = serialNo
        for k,v in self.termtool.items():
            if str(self.serialNo)[0:3] == k in self.termtool:
                self.modelName = v["modelName"]
                self.name = v["name"]
                self.resellerName = v["resellerName"]
                self.type = v["type"]
                self.fmName = v["fmName"]
                if v["hasAccessory"]: 
                    self.hasAccessory = True
                    self.accessoryModelName = v["accessory"]["modelName"]
                    self.accessoryName = v["accessory"]["name"]
                    self.accessoryResellerName = v["accessory"]["resellerName"]
                    self.accessoryType = v["accessory"]["type"]
                else: 
                    self.hasAccessory = False
                    self.accessoryModelName = None
                    self.accessoryName = None
                    self.accessoryResellerName = None
                    self.accessoryType = None

        self.bPosPackageName = self.pushPATool[f"{self.type}packageName"]
        self.bPosPushTemplateName = self.pushPATool[f"{self.type}pushTemplateName"]
        self.bPosTemplateName = self.pushPATool[f"{self.type}templateName"]
        self.bPosPackageVersion = self.pushPATool[f"{self.type}version"]


   
                
class PaxApiTool():
    """Creates aiohttp.ClientSession request object to interface with the public PaxStore API.
    \nRequired parameters: apiKey, apiSecret, session (aiohttp.ClientSession), operation
    \nPossilbe operations: 'createTerminal', 'findTerminal','activateTerminal', 'disableTerminal', 'moveTerminal'
    """
    def __init__(self, apiKey, apiSecret, session:aiohttp.ClientSession,operation:str,terminalId:str|None=None, serialNo = None, merchantName = None, modelName = None, name = None, resellerName = None, status = None, command = None, packageName = None, pushTemplateName=None, templateName=None, version=None, rkiKey=None, fmName=None, list=None) -> None:

        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.baseUrl = "https://api.paxstore.us"
        self.altbaseUrl = "https://api.whatspos.com"
        self.scheme = "https"
        self.netloc = "api.paxstore.us"
        self.altnetloc =  'api.whatspos.com'
        self.session = session
        self.operation = operation
        self.terminalId = terminalId
        self.serialNo = serialNo
        self.merchantName = merchantName
        self.modelName = modelName
        self.name = name
        self.resellerName = resellerName
        self.status = status

        self.command = command
        self.packageName = packageName
        self.pushTemplateName = pushTemplateName
        self.templateName = templateName
        self.version = version
        self.rkiKey = rkiKey
        self.fmName = fmName
        self.list = list
        self.query = {
            "sysKey": self.apiKey,
            "timeStamp": round(time.time()*1000)
        }
        if self.list:
            self.unpacked = str(f'{", ".join(self.list)}')
        else:
            self.unpacked = None
        self.operations_dict = {
            "createTerminal": {
                "path": "/p-market-api/v1/3rdsys/terminals",
                "method": self.session.post,
                "addQuery": None,
                "body": {
                    "merchantName":self.merchantName,
                    "modelName":self.modelName,
                    "name":self.name,
                    "resellerName":self.resellerName,
                    "serialNo":self.serialNo,
                    "status":self.status
                }
                },
            "findTerminal": {
                "path": "/p-market-api/v1/3rdsys/terminals",
                "method": self.session.get,
                "addQuery": {
                    "snNameTID": self.serialNo,
                },
                "body": None
            },
            "activateTerminal": {
                "path": f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}/active",
                "method": self.session.put,
                "addQuery": None,
                "body": None
            },
            "disableTerminal" : {
                "path": f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}/disable",
                "method": self.session.put,
                "addQuery": None,
                "body": None
            },
            "moveTerminal" : {
                "path": f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}/move",
                "method": self.session.put,
                "addQuery": None,
                "body": {
                    "merchantName": self.merchantName,
                    "resellerName": self.resellerName
                }
            },
            "updateTerminal" : {
                "path" : f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}",
                "method" : self.session.put,
                "addQuery": None,
                "body": {
                    "merchantName":self.merchantName,
                    "modelName":self.modelName,
                    "name":self.name,
                    "resellerName":self.resellerName,
                    "serialNo":self.serialNo,
                    "status":self.status,
                }
            },
            "deleteTerminal" : {
                "path" : f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}",
                "method": self.session.delete,
                "addQuery": None,
                "body": None
            },
            "terminalDetails" : {
                "path" : f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}",
                "method": self.session.get,
                "addQuery" : {
                    "includeDetailInfo" : "true",
                },
                "body": None
            },
            "accessoryDetails" : {
                "path" : f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}",
                "method": self.session.get,
                "addQuery" : {
                    "includeDetailInfo": "true",
                    "includeDetailInfoList" : "true"
                },
                "body": None
            },
            "pushCommand": {
                "path": f"/p-market-api/v1/3rdsys/terminals/{self.terminalId}/operation",
                "method": self.session.post,
                "addQuery": {
                    "Command": self.command
                },
                "body": None
            },
            "pushParamAPK": {
                "path": "/p-market-api/v1/3rdsys/terminalApks",
                "method": self.session.post,
                "addQuery": None,
                "body": {
                    "packageName": self.packageName,
                    "pushTemplateName": self.pushTemplateName,
                    "serialNo": self.serialNo,
                    "templateName": self.templateName,
                    "version": self.version
                }
            },
            "pushAPK": {
                "path": "/p-market-api/v1/3rdsys/terminalApks",
                "method": self.session.post,
                "addQuery": None,
                "body": {
                    "packageName": self.packageName,
                    "serialNo": self.serialNo
                }  
            },
            "pushRKI": {
                "path": "/p-market-api/v1/3rdsys/terminalRkis",
                "method": self.session.post,
                "addQuery": None,
                "body": {
                    "rkiKey": self.rkiKey,
                    "serialNo": self.serialNo
                }
            },
            "pushFirmware": {
                "path": "/p-market-api/v1/3rdsys/terminalFirmwares",
                "method": self.session.post,
                "addQuery": None,
                "body": {
                    
                    "fmName": self.fmName,
                    "serialNo": self.serialNo
                }
            },
            "terminalConfig":{
                "path":"/p-market-api/v1/3rdsys/terminals",
                "method":self.session.get,
                "addQuery": {
                    "includeInstalledApks":"true",
                    "includeInstalledFirmware": "true",
                    "pageNo":"",
                    "pageSize":"",
                    "snNameTID": self.serialNo,

                },
                "body": None
            },
            "appPushHistory": {
                "path": "/p-market-api/v1/3rdsys/parameter/push/history",
                "method":self.session.get,
                "addQuery": {
                    "onlyLastPushHistory": "false",
                    "packageName": self.packageName,
                    "pageNo": 1,
                    "pageSize": 20,
                    "pushStatus":3,
                    "serialNo": self.serialNo
                },
                "body": None
            }

        }

        for k, v in self.operations_dict.items():
            if self.operation == k in self.operations_dict.keys():
                self.path = v["path"]
                if v["addQuery"]:
                    self.query.update(v["addQuery"])
                if v["body"]:
                    self.body = v["body"]
                else: self.body = None
                self.method = v["method"]
                self.encodedQuery = urlencode(self.query)
                self.fullurl = urlunsplit((self.scheme,self.netloc,self.path,self.encodedQuery,None))
                #print(self.fullurl)
                self.signature = hmac.new(self.apiSecret, self.encodedQuery.encode('utf-8'), hashlib.md5).hexdigest().upper()





#operation:str, terminalId = None, serialNo = None, merchantName = None, modelName = None, name = None, resellerName = None, status = None, command = None

#terminalId = None, serialNo = None, merchantName = None, modelName = None, name = None, resellerName = None, status = None, command = None
async def buildRequest(session,operation:str,**kwargs):
    
    apiKey = os.environ.get("APIKEY").encode('utf-8')
    apiSecret = os.environ.get("APISECRET").encode("utf-8")
    term = PaxApiTool(apiKey,apiSecret,session,operation, **kwargs)
    headers = {"Content-Type": "application/json; charset=UTF-8","signature":term.signature}
    method = term.method
    print(term.body)
    print(term.fullurl)
    async with method(term.fullurl,json=term.body,headers=headers) as resp:
        term_data = await resp.json(content_type=None)
    
        if operation == "findTerminal" and not term_data["dataset"]:
            serial_no = kwargs.get("serialNo", None)  # Retrieve serial number from kwargs if available
            raise TerminalNotFoundError(serial_no)
    
    return term_data

async def findTerminal(serialNoList: list) -> list:

    """
Purpose:
Locates a PaxStore terminal based on its serial number.
   
Parameters: serialNoList (list): A list of serial numbers to search for.

Returns: list: A list of JSON responses, each containing information about a found terminal. If a terminal is not found, its corresponding response will be an empty list."""
    
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for serialNo in serialNoList:
            tasks.append(asyncio.ensure_future(buildRequest(session, "findTerminal", serialNo = serialNo)))
        responses = await asyncio.gather(*tasks)
    cleanResponses = []
    for resp in responses:
        #print(resp)
        cleanResponses.append(*resp['dataset'])
    return cleanResponses

async def terminalDetails(idList: list, serialNoList=None, df=None) -> list:
    """
    Retrieves detailed information for a list of terminals.

    Args:
        id_list (list): A list of terminal IDs.
        serial_no_list (list, optional): A list of serial numbers (alternative to id_list).
        df (pd.DataFrame, optional): A DataFrame containing terminal information.

    Returns:
        list: A list of JSON responses, each containing detailed information about a terminal.
    """
    
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = [asyncio.create_task(buildRequest(session, "terminalDetails", terminalId=id)) for id in idList]
        responses = await asyncio.gather(*tasks)
        cleanResponses = []
    for resp in responses:
        #print(resp)
        cleanResponses.append(resp['data']['terminalDetail'])
        #print(cleanResponses)

    return cleanResponses
            
async def accessoryDetails(df:pd.DataFrame):
    """tasks = []
    accessoryList = []
    print(df)
    idList = df['id'].to_list()"""

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        
        tasks = [asyncio.ensure_future(buildRequest(session, "accessoryDetails", terminalId=id)) for id in df["id"]]
        responses = await asyncio.gather(*tasks)
        accessoryList = [resp["data"]["terminalAccessory"]["basic"][0]["content"] if "terminalAccessory" in resp["data"] else None for resp in responses]
        qf = pd.DataFrame({"accessory":accessoryList}, dtype=object)
        ndf = pd.concat([df,qf],axis=1)
        print(ndf)

    
    accessoryid = await findTerminal(ndf['accessory'].dropna())
    mqf = pd.DataFrame(accessoryid,dtype=object)
    print(mqf)
    bqf = pd.concat([ndf,mqf], ignore_index=True)
    print(bqf)
    print(accessoryid)
    return bqf

async def updateTerminals(idList,serialNoList, df=None):
    tasks = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:

        for serialNo,id in list(zip(serialNoList,idList)): 
            terminal = PaxTerms(serialNo)
            #nameList.append(terminal.name)
            tasks.append(asyncio.ensure_future(buildRequest(serialNo=serialNo,terminalId=id,session=session, operation="updateTerminal",merchantName="North American Bancard",name=terminal.name,modelName=terminal.modelName,resellerName=terminal.resellerName,status = "A")))
        responses = await asyncio.gather(*tasks)
        print(responses)
        return responses

async def findGroup(serialNoList:list)->pd.DataFrame:
    func = apiPaxFunctions()
    group = await findTerminal(serialNoList)
    disable = await func.disableTerminals(group['id'])
    return group

async def resetTerminals(df:pd.DataFrame, idList=None,serialNoList=None):
    func = apiPaxFunctions()
    disable = await func.disableTerminals(df['id'])
    delete = await func.deleteTerminals(df['id'])
    create = await func.createTerminals(df['serialNo'])
    filteredDataFrame = df.drop(df[(df.modelName=="Q20L")|(df.modelName=="Q10A")].index)
    time.sleep(5)

class apiPaxFunctions(): 

    def __init__(self) -> None:
        pass

    
    
    async def startPaxGroup(self, serialNoList,handleAccessory =True,idList=None,df=None)->pd.DataFrame:
        self.idList = []
        self.serialNoList = serialNoList
        findResp = await findTerminal(serialNoList)
        fullserial_List = []
        for resp in findResp:   
            print("\n\n\nRESP:",resp)
            self.idList.append(resp['id'])
        detailresp = await terminalDetails(self.idList)
        print("\n\n\nfindResp:",*findResp)
        self.groupList = []
        for fresp,dresp in list(zip(findResp,detailresp)):
            resp.update(dresp)
            self.groupList.append(fresp)
        if not handleAccessory:
            return pd.DataFrame(self.groupList)
        else:
            group_df = pd.DataFrame(self.groupList, dtype=object)
            accessoryDetail = await accessoryDetails(group_df)
            return accessoryDetail
        
    async def activateTerminals(self, idList, serialNoList=None, df=None):
        
        tasks = []
        responses = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for id in idList:
                tasks.append(asyncio.ensure_future(buildRequest(session,"activateTerminal",terminalId = id)))
            result = await asyncio.gather(*tasks)
        for res in result:
            if res == None:
                responses.append({'businessCode':0, 'message':'The terminal has been activated'})
            else: responses.append(res)   
        return responses

    async def disableTerminals(self, idList:list, serialNoList=None, df=None):
        responses = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            tasks=[(asyncio.ensure_future(buildRequest(session,'disableTerminal', terminalId = id)))for id in idList]
            result = await asyncio.gather(*tasks)
            for res in result:
                if res == None:
                    responses.append({'businessCode':0, 'message':'The terminal has been disabled'})
                else: responses.append(res)   
        return responses
        
    async def moveTerminals(self, idList, resllerName, merchantName,serialNoList=None, df=None):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            tasks = [asyncio.ensure_future(buildRequest(session,"moveTerminal",resellerName = resllerName, merchantName = merchantName,terminalId = id)) for id in idList]
            results = await asyncio.gather(*tasks)
            responses = [f"Terminal Moved to {resllerName} successfully" for message in results if message == None]
            return responses
        
    async def createTerminals(self,serialNoList):

        tasks = []
        cleanResponses = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for serialNo in serialNoList: 
                terminal = PaxTerms(serialNo)
                tasks.append(asyncio.ensure_future(buildRequest(serialNo=serialNo,session=session, operation="createTerminal",merchantName="North American Bancard",name=terminal.name,modelName=terminal.modelName,resellerName=terminal.resellerName,status = "A")))
            result = await asyncio.gather(*tasks) 
            for resp in result:
                cleanResponses.append(resp['data'])
            #cleanResponses.append(*[resp['data'] for resp in result])
            return cleanResponses

    async def deleteTerminals(self, idList, df=None):
        tasks = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for id in idList:
                tasks.append(asyncio.ensure_future(buildRequest(session, "deleteTerminal", terminalId = id )))
            result = await asyncio.gather(*tasks)
            return result
    
    async def pushTerminalAPK(self, serialNoList:list, paramApp:bool=None, packageName:str=None):
        tasks = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for serialNo in serialNoList: 
                if paramApp:
                    terminal = PaxTerms(serialNo)
                    tasks.append(asyncio.ensure_future(buildRequest(session, "pushParamAPK",serialNo=serialNo,packageName=terminal.bPosPackageName,templateName=terminal.bPosTemplateName,version=terminal.bPosPackageVersion)))
                else:
                    tasks.append(asyncio.ensure_future(buildRequest(session, "pushAPK",serialNo=serialNo, packageName=packageName)))
            result = await asyncio.gather(*tasks)
            return result

    async def pushThingy(self, terminalList ,operation:str, **kwargs):
        """Pushes thing to group of terminals. """
        tasks = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for serialNo in terminalList:
                tasks.append(asyncio.ensure_future(buildRequest(session,operation, serialNo=serialNo, **kwargs)))
            result = await asyncio.gather(*tasks)
            return result
        
async def notnain():
    tasks=[]
    id_list = []
    task2 = []
    
    serial_list = input('Please scan QR:\n>>>>')
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as s:
        for serial in serial_list:   
            terminal = PaxTerms(serial)
            tasks.append(asyncio.ensure_future(buildRequest(serialNo=serial, session = s, operation="createTerminal",merchantName="North American Bancard",name=terminal.name,modelName=terminal.modelName,resellerName=terminal.resellerName,status = "P")))
        res = await asyncio.gather(*tasks)
        print(res)

class PushConfigs():
    
    def __init__(self) :
        self.task = apiPaxFunctions()

        

    async def pushPAConfig(self, serialNoList, idList = None, df = None):
        """Pushes current version of:\n BroadPosP2PE (PA Template),\n CheckUp,\n PAInstaller, \n PayDroid Firmware, \n RKI"""

        bpospush = await self.task.pushTerminalAPK(serialNoList,True)
        print("BroadPosP2PEPush:",bpospush)
        installerPush = await self.task.pushTerminalAPK(serialNoList,False, "com.nabancard.painstaller")
        print("PAInstallerPush:", installerPush)
        checkupPush = await self.task.pushTerminalAPK(serialNoList,False,"com.pax.checkup")
        print("CheckUpPush",checkupPush)
        rki = await self.task.pushThingy(serialNoList,"pushRKI",rkiKey="EPX_PIN_Slot1_Data_Slot3")
        print(rki)

    async def paPushByReseller(self, idList, **kwargs):
        deactivate = await self.task.disableTerminals(idList)
        move = await self.task.moveTerminals(idList=idList,resllerName="A920 Config",merchantName="North American Bancard")
        activate = await self.task.activateTerminals(idList)
        return activate
    
    async def pushBroadPosEPX(self, serialNoList,idList = None, df = None):    
        checkupPush = await self.task.pushTerminalAPK( serialNoList,False,"com.pax.checkup")
        print("CheckUpPush",checkupPush)
        rki = await self.task.pushThingy(serialNoList,"pushRKI",rkiKey="EPX_PIN_Slot1_Data_Slot3")
        print(rki)


    async def pushBroadPos_nonEPX(self, serialNoList,idList = None, df = None):
        
        checkupPush = await self.task.pushTerminalAPK(serialNoList,False,"com.pax.checkup")
        print("CheckUpPush",checkupPush)
        

async def getInstalledConfig(serialNoList):
    devices = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = [asyncio.ensure_future(buildRequest(session, "terminalConfig", serialNo=serialNo))for serialNo in serialNoList]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            if response['businessCode'] == 0: 
                data = response['dataset']
                devices.extend(device for device in data)
    return devices



        




