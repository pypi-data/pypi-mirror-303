from web_fetch.web_fetch import ZhiPuWebSearch
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("zhipu_api_key")
if __name__=='__main__':
    search_engine = ZhiPuWebSearch(api_key=api_key)
    results = search_engine.search("东北石油大学保研规则是什么？", "nepu.edu.cn")
    print(results)