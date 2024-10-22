import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd

def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
    return list(td.get_text(strip=True) for td in tr.find_all(coltag))

async def get_warranty_info(serial_numbers: list) -> dict:
    """
    Fetches warranty information for a list of serial numbers using aiohttp.

    Args:
        serial_numbers (list): A list of serial numbers.

    Returns:
        dict: A dictionary mapping serial numbers to their warranty information.
    """

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(get_warranty_data(session, serial)) for serial in serial_numbers]
        responses = await asyncio.gather(*tasks)
        return {response for  response in responses}

async def get_warranty_data(session: aiohttp.ClientSession, serial: str) -> dict:
    """
    Fetches warranty data for a single serial number.

    Args:
        session (aiohttp.ClientSession): The HTTP client session.
        serial (str): The serial number.

    Returns:
        dict: A dictionary containing warranty details or an empty dict if not found.
    """

    url = "http://216.238.144.195:5000/result"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",  

        "Cache-Control": "max-age=0",
        "Origin": "http://216.238.144.195:5000",  

        "Referer": "http://216.238.144.195:5000/sn/search",
        "Upgrade-Insecure-Requests": "1"
    }
    data = {"refer": serial}

    async with session.post(url, headers=headers, data=data) as response:
        if response.status == 200:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            table = soup.find('table')

            if table:
                key_list = ['SN:', 'model:', 'part_number:', 'ShipDate:', 'So:', 'Po:', 'Address:', 'WarrExp:']
                value_list = []
                try:
                    tr = table.find('tr')
                    di = rowgetDataText(tr)
                    for string in di:
                        if string not in set(key_list):
                            value_list.append(string)
                    
                except IndexError:
                    for x in key_list:
                        value_list.append("NONE")
                except AttributeError:
                    for x in key_list:
                        value_list.append('NOT FOUND IN DATABASE')
                return dict(zip(key_list, value_list))

    
serial_list = [1140132687,1140137499,1240293522,1240325245,1240325500,1240325635,1240325763,1240328029,1240328078,1240336344,1240336475,1340031332,1340032080,1340032081,1340032105,1340032115,1340032405,1340032448,1340032526,1340032621,1340032655,1340032661,1340032688,1340032931,1340033022,1340033036,1340033159,1340033161,1340033544,1340036616,1340036802,1340036811,1340036944,1340037902,1340037954,1340038028,1340038047,1340038106,1340038193,1340038234,1340038253,1340038256,1340038731,1340038789,1340040107,1340040137,1340047418,1340047459,1340047470,1340047522,1340047524,1340047695,1340048992,1340049103,1340049122,1340049138,1340049766,1340050039,1340050073,1340050493,1851161772,1851166134,1851338849,1851343933,1851343995,1851344050,1851490630,1851635819,1851636230,1851636245,1851637965,1851641476,1851642626,1851674117,1851674270,1851676275,1851690237,1851724514,1851724517,1851725422,1851725771,1851729511,1851729534,1851730846,1851730979,1851731001,1851732226,1851735470,1851737328,1851756464,1851756575,1851756578,1851756581,1851756953,1851757066,1851758594,1851759405,1851759921,1851760203,1851760252,1851760508,1851760572,1851805459,1851805504,1851805817,1851805819,1851805863,1851805981,1851806270,1851806275,1851806432,1851806584,1851806611,1851806715,1851806851,1851806855,1851806919,1851807209,1851807299,1851807961,1851807995]
	
info = asyncio.run(get_warranty_info(serial_list))
print(info)
df = pd.DataFrame(info)
df.to_excel('warrout.xlsx')