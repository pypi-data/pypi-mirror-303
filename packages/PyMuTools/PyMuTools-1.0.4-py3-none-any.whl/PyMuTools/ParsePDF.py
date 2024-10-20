import pymupdf
from pathlib import Path
from os import getlogin 
from numpy import load
from .ReadFile import ymTools 

class parsePDF():
    def __init__(self , byts_path=False):
        pymupdf.TOOLS.mupdf_display_errors(False)

        if not ymTools():
            raise
        self.byts_path= Path(rf'C:\Users\{getlogin()}\Documents\{byts_path}').glob('*')
 
    def getPdfData(self, how='default'):
        results= {}
        for np_file in self.byts_path:
            np_file= load(np_file, allow_pickle=True).item()
            for url, values in np_file.items():
                try:
                    if how == 'line':
                        results[url]= self.GetLines(values)
                    elif how == 'table':
                        results[url]= self.GetTables(values)
                    else:
                        results[url]= self.GetDefault(values)
                except:
                    pass
        return results
    
    def GetLines(self, content):
        with pymupdf.open(stream=content) as doc:
            words = (sorted(page.get_text_words(), key= lambda x: x[3])  for page in doc.pages())
            page_lines=[]
            for page in words:
                page_words={}
                #here got the words which share the same line
                for word in page:
                    curent_botom_postion= int(word[3])
                    if curent_botom_postion+2 in page_words:
                        page_words[curent_botom_postion+2].append(word)
                    elif curent_botom_postion-2 in page_words:
                        page_words[curent_botom_postion-2].append(word)
                    elif curent_botom_postion+1 in page_words:
                        page_words[curent_botom_postion+1].append(word)
                    elif curent_botom_postion-1 in page_words:
                        page_words[curent_botom_postion-1].append(word)
                    elif curent_botom_postion in page_words :   
                        page_words[curent_botom_postion].append(word) 
                    else:
                        page_words[curent_botom_postion]= [word]
                #here after got all words which share same line,each line are dict words
                #so here sort words in the same line by left postion
                page_values= (sorted(line, key= lambda x: x[0]) for line in page_words.values())
                #here got the word text 
                page_lines.append(tuple(' '.join(word[4] for word in line) for line in page_values))
            return page_lines
    def GetDefault(self, content):
        with pymupdf.open(stream=content) as doc:
            return tuple(page.get_text()  for page in doc.pages())
    def GetTables(self, content):
        with pymupdf.open(stream=content) as doc:
            return {idex:tuple(table.to_pandas() for table in page.find_tables()) for idex, page in enumerate(doc.pages())}
        