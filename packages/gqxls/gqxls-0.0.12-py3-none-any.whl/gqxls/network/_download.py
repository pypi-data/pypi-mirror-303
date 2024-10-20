import urllib, os, requests
from typing import Union, List, Literal
from ..path import paths
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
class download:
    def __init__(self,theard_pool:bool=False,max_workers:int=4):
        self.theard_pool = theard_pool
        self.max_workers = max_workers

    def check(self, url: str)-> bool:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.438.400 QQBrowser/13.0.6071.400',
            'Accept': 'application/vnd.android.package-archive'
        }
        try:
            response = requests.get(url, stream=True, allow_redirects=True, timeout=5, headers=headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    def download(self,url:Union[str,List[str]],storage_path:str,title:Union[str,List[str]])->None:
        if isinstance(url,str) :
            if self.check(url):
                if title!="" and isinstance(title,str):
                    paths().maker_path(storage_path)
                    urllib.request.urlretrieve(url, os.path.join(storage_path,title))
                else:
                    raise ValueError(F"title:{title}参数错误，请输入有效title")
            else:
                raise ValueError(F"url:{url}参数错误，请输入有效url")
        elif isinstance(url,List) and all(isinstance(i,str) for i in url):
            if all(self.check(i) for i in url):
                if title!=[] and all(isinstance(i,str) for i in title) and len(title)==len(url):
                    paths().maker_path(storage_path)
                    xian_pool=ThreadPoolExecutor(max_workers=self.max_workers)
                    try:
                        if self.theard_pool:
                            for url_data in range(len(url)):
                                xian_pool.submit(urllib.request.urlretrieve,url[url_data],os.path.join(storage_path,title[url_data]))
                            xian_pool.shutdown()
                        else:
                            for url_data in range(len(url)):
                                urllib.request.urlretrieve(url[url_data],os.path.join(storage_path,title[url_data]))
                    except:
                        raise TypeError(F"下载发生错误，下载失败")
                else:
                    raise ValueError(F"title:{title}参数错误，请输入有效title")
            else:
                raise ValueError(F"url:{url}部分无效，请输入有效url")
        else:
            raise ValueError(F"url:{url}参数错误，请输入list[str]类型或str类型")
    def get_title(self,url:str)->str:
        if isinstance(url,str):
            if self.check(url):
                try:
                    response = requests.get(url)
                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = str(soup.title)[7:-8]
                    response.close()
                    return title
                except:
                    raise ValueError("获取网页标题失败")
            else:
                raise ValueError(F"url:{url}参数错误，请输入有效url")
        else:
            raise ValueError(F"url:{url}参数错误，请输入str类型")