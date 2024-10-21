import requests
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from numpy import  save
from os import makedirs, getlogin
from datetime import datetime
import shutil

class sendRequests():
    def __init__(self):      
        #create folder to save byts
        self.folder_path= rf'C:\Users\{getlogin()}\Documents\NP_'+ datetime.now().strftime("%Y-%m-%d %H.%M")
        self.header={
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5"}      
    def getResponse(self, url):  
        try:
            pdf= url.replace('http://download.siliconexpert.com', r'\\10.199.104.160').replace('/', '\\')
            with open(pdf, 'rb') as file:
                return url, BytesIO(file.read())
        except:
            try:
                response= requests.get(url, timeout=10, headers= self.header)
                if response.status_code == 422:
                    url= url.replace('http','https')
                    response= requests.get(url, timeout=10, headers= self.header)
                return url, BytesIO(response.content)
            except:
                try:
                    response= requests.get(url.replace('https', 'http'), timeout=10, headers= self.header)
                    return url, BytesIO(response.content)
                except:
                    return url, None
                
    def threadRequests(self, URLs):
        with ThreadPoolExecutor() as excuter:
            results= list(excuter.map(self.getResponse, URLs))
        return {url:byts for url, byts in results}
    
    def RunAndSave(self, URLs):
        chunk_size= int(len(URLs)/10)
        chunk_size= chunk_size if chunk_size > 0 else 1
        Chunks=  [URLs[chunk: chunk+chunk_size] for chunk in range(0, len(URLs), chunk_size)]
        makedirs(self.folder_path)
        for idx, chunk in enumerate(Chunks):
            save(rf'{self.folder_path}\{idx}.npy', self.threadRequests(chunk))

    def rmtreeResponse(self, folder_path):
        """Deletes a folder and its contents recursively.
        Args:
            folder_path (str): The path to the folder to be deleted.
        """
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' and its contents deleted successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_path}' not found.")
        except PermissionError:
            print(f"Permission denied to delete folder '{folder_path}'.")
        except Exception as e:
            print(f"Error deleting folder: {e}")