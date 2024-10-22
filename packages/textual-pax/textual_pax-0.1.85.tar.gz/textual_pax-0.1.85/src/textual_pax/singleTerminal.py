from .revertpaxmodule import apiPaxFunctions, terminalDetails, getInstalledConfig
import pandas as pd



async def parseList(serialNoList)->dict:
    thing = apiPaxFunctions()
    termDetail = await thing.startPaxGroup(serialNoList, handleAccessory=False)
    config = await getInstalledConfig(serialNoList)
    for item in config:
        apklist = item['installedApks']
    termDetails_dict = termDetail.to_dict('records')

    return termDetails_dict, apklist

async def parseApk(serialNoList):
    config = await getInstalledConfig(serialNoList)
    for item in config:
        apklist = item['installedApks']
        df = pd.DataFrame(apklist)
    return df