#python 3.10.7
import time
import random
import os
import string

from urllib import request
from urllib import parse
from fake_useragent import UserAgent
from func_timeout import func_set_timeout

class pythonCrawler():
    timeout = 20
    def __init__(
            self, 
            address : str = "http://www.baidu.com", 
            accessInformation : dict = {}, 
            timeout : float = 20.0) -> None:
        
        self.address             : str    = address
        self.timeout             : float  = timeout
        self.accessInformation   : dict   = accessInformation

    @func_set_timeout(timeout)
    def __theReptileObtainingWebpageHtml(self, url : str = "", headers : dict = {}) -> str:
        return request.urlopen(request.Request(url=url,headers=headers)).read().decode('utf-8')

    def __htmlStorage(self, html : str = "", fileName : str = ""):
        with open(fileName, "w", encoding="utf-8") as htmlText:
            htmlText.write(html.replace("\n", ""))
    
    def __generateHtmlFileName(self) -> str:
        return str("".join(random.sample(string.ascii_letters+string.digits,random.randint(3,9)))+".html")

    def __addressTranscoding(self, address : str = "", accessInformation : dict = {}) -> str:
        return address + parse.urlencode(accessInformation)

    def __getUserAgentUserAgent(self) -> dict:
        userAgent = {}
        ua = UserAgent()
        browserName = random.choice(["Chrome", "Firefox", "Safari", "Edge", "IE"])
        exec("userAgent = ua.%s" % str("Edge"), {"ua":ua}, userAgent)
        return {"User-Agent":userAgent["userAgent"]}

    def __clear_env(self) -> None:
        try:
            for key in globals().keys():
                if not key.startswith("__"):
                    globals().pop(key)
        except:...
        os._exit(0)

    def __outputRunningTime(self, startTime : float = 0.00, operationHours : float = 0.00) -> None:
        calculationResults : float = operationHours - startTime
        if calculationResults < 0.01:
            return print("运行时间:小于%.2f" % 0.01)
        else:
            print("运行时间:%.2f" % calculationResults)
            self.__clear_env()
    def run(self) -> None:
        startTime = time.time()
        urlAddressDecoding = self.__addressTranscoding(self.address, self.accessInformation)
        userAgentInformation = self.__getUserAgentUserAgent()
        webpageHtml = self.__theReptileObtainingWebpageHtml(urlAddressDecoding, userAgentInformation)
        self.__htmlStorage(webpageHtml, self.__generateHtmlFileName())

        operationHours = time.time()
        self.__outputRunningTime(startTime, operationHours)

pc = pythonCrawler("https://tieba.baidu.com/f?", {"kw":"ikun", "ie":"utf-8", "pn":"0"}, 10)
pc.run()
