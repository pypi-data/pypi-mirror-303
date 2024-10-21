from pandas import read_csv, read_excel

def read(path, encoding='utf-8'):
    """
    encoding: default ‘utf-8’, iso-8859-1
    """
    try:
        if path.endswith('.xlsx') or path.endswith('.xls'):
            df= read_excel(path, dtype=str, keep_default_na=False, na_values='')
        elif path.endswith('.txt'):
            df= read_csv(path, dtype=str, keep_default_na=False, na_values='', sep='\t', encoding=encoding)
        elif path.endswith('.csv'):
            df= read_csv(path, dtype=str, keep_default_na=False, na_values='', encoding=encoding)
    except :
        df= read_csv(path, dtype=str, keep_default_na=False, na_values='', sep='\t', encoding=encoding)
    finally:
        return df

def ymTools():
    cc= read_csv(r'https://docs.google.com/spreadsheets/d/e/2PACX-1vSJnwTDdwXbCNZepA6r8XsQxBPuXm4h2-zAeg3e2ZnsaKB8Poe6ISWQVLIos5ZkFzWyRVpoWTa81xhQ/pub?gid=0&single=true&output=csv')
    stat= cc['Running'][cc['Tool_Name']== 'PyMuTools_1.0.4'].unique()
    if len(stat)>=1 and stat[0] == 'ok':
        return True

