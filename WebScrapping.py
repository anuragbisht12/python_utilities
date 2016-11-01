import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
def webscrap():
    wiki="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    page=urllib2.urlopen(wiki)
    soup=BeautifulSoup(page,'html')
    #print soup.prettify()
    
    useful_table=soup.find('table',class_='wikitable sortable plainrowheaders')
    #print useful_table
    A,B,C,D,E,F,G=[],[],[],[],[],[],[]
    
    for row in useful_table.findAll("tr"):
        cells=row.findAll('td')
        states=row.findAll('th')
        if len(cells)==6:
            A.append(cells[0].find(text=True)) 
            B.append(states[0].find(text=True))
            C.append(cells[1].find(text=True))
            D.append(cells[2].find(text=True))
            E.append(cells[3].find(text=True))
            F.append(cells[4].find(text=True))
            G.append(cells[5].find(text=True))
        
    #print A,B,C,D,E,F,G
    
    df=pd.DataFrame(A,columns=['Number'])
    df['State/UT']=B
    df['Admin_Capital']=C
    df['Legislative_Capital']=D
    df['Judiciary_Capital']=E
    df['Year_Capital']=F
    df['Former_Capital']=G
    #print df
    file_name="C:\\Users\\ANURAG BISHT\\Desktop\\pythondemos\\test"+"".join(str(datetime.datetime.now()).split(":"))+".csv"
    df.to_csv(file_name,sep=',',encoding='utf-8',index=False)
    print("done")
    
    #while True:
    #    webscrap()
    #    #print datetime.datetime.now()
    #    time.sleep(10000)
    

webscrap()