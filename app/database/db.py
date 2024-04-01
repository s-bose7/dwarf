
import pymongo

from datetime import datetime
from typing import List, Dict, Any
from urllib.parse import urlparse,  ParseResult


class DataBase:
        
    def __init__(self) -> None:
        self.db_container_ip = "172.17.0.2"
        self.mongo_client = pymongo.MongoClient(
            f"mongodb://{self.db_container_ip}:27017/"
        )
        self.db = self.mongo_client["url_shortener_db"]
        self.urls_collection = self.create_collection()


    def create_collection(self, collection_name="urls"):
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(name=collection_name)
        
        return self.db[collection_name]
    

    def __extract_domain(self, url: str, truncate_scheme: bool = True)-> str:
        domain: str = ""
        parsed_url: ParseResult = urlparse(url)
        if parsed_url.netloc: 
            domain += parsed_url.netloc
        else: 
            domain += parsed_url.path.split('/')[0]        
        if not truncate_scheme: 
            domain = parsed_url.scheme + "://" + domain
        return domain    
    
    
    def insert_url(self, long_url: str, short_url: str)->bool:
        # Define the document schema 
        document = {
            "created_at": datetime.now(),
            "clicks": 100,
            "original_url": long_url,
            "domain": self.__extract_domain(long_url),
            "short_url": short_url,
        }
        self.urls_collection.insert_one(document)


    def retrieve_url(self, short_url:str = None, long_url:str = None)->str | None:
        # create a query
        query: Dict[str: str] = {}
        query = {"long_url": long_url} if short_url is None else {"short_url": short_url}
        result = self.urls_collection.find_one(query)
        if result is None:
            return None
        
        original_url = result["original_url"]
        return original_url