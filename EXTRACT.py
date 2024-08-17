import requests
from bs4 import BeautifulSoup
import datetime

class TrendShift:
    
    def __init__(self, startpage: int, finishpage: int):
        self.startpage = startpage
        self.finishpage = finishpage


    def geturl(self, pagex: int):
        url = 'https://trendshift.io/repositories/{}'
        resp = requests.get(url.format(pagex))
        soup = BeautifulSoup(resp.text, 'html.parser')
        print(f"Successfully fetched and parsed page {pagex}..")
        
        return soup
       

    def gettrendshiftid(self):
        list_id=[]
        for z in range(self.startpage,self.finishpage+1):
            list_id.append(z)

        return list_id
    
    def getcreatdate(self):
        createdate=datetime.datetime.now()

        return [createdate] * (self.finishpage - self.startpage + 1)

    def getrepname(self):
        list_rep_names = []
        for page in range(self.startpage, self.finishpage+1):
            soup = self.geturl(page)
            
            names = soup.find_all('div', attrs={'class': 'flex items-center text-indigo-400 text-lg justify-between mb-1'})

            if names:
                for z in names:
                    list_rep_names.append(z.find('div').text)
            else:
                list_rep_names.append('NoInfo')

        return list_rep_names
    
    
    
    def getgiturl(self):
        list_giturl=[]
        for page in range(self.startpage,self.finishpage+1):
            soup=self.geturl(page)

            giturl=soup.find_all('a',attrs={'class':'hover:cursor-pointer hover:underline'})

            if len(giturl)>0:
                if giturl:
                    list_giturl.append(giturl[0]['href'])
                    
                else:
                    list_giturl.append('NoInfo')
            else:
                list_giturl.append('NoInfo')


        return list_giturl

    def getweburl(self):
        list_weburl=[]
        for page in range(self.startpage,self.finishpage+1):
            soup=self.geturl(page)
            weburl=soup.find_all('a',attrs={'class':'hover:cursor-pointer hover:underline'})
            ###### EGER IKINCI SEY YOKSA COK ONEMLI
            if len(weburl)>1:
                weburlvalue=weburl[1]['href']
            else:
                weburlvalue='NoInfo'
            list_weburl.append(weburlvalue)
            

        return list_weburl
    
    def getdescription(self):
        list_desc=[]
        for page in range(self.startpage,self.finishpage+1):
            soup=self.geturl(page)
            description=soup.find_all('div',attrs={'class':'text-sm text-gray-500'})

            if description:
                for z in description:
                    list_desc.append(z.text)
            else:
                list_desc.append('NoInfo')
        return list_desc

    def getlangname(self):
        list_lang_names = []
        for page in range(self.startpage, self.finishpage+1):
            soup = self.geturl(page)
            
            lang_names = soup.find_all('div', attrs={'class': 'text-gray-500 flex items-center text-xs md:text-sm'})

            if lang_names:
                # If elements are found, extract text from each and append to list_lang_names
                for z in lang_names:
                    list_lang_names.append(z.text)
            else:
                 # If no elements are found, append "NoInfo"
                list_lang_names.append("NoInfo")

        return list_lang_names
    
    def getstars(self):
        list_star=[]
        for page in range(self.startpage, self.finishpage+1):
            soup = self.geturl(page)
            starcount=soup.find_all('div',attrs={'class':'flex items-center'})
            if len(starcount)>1:

                if starcount:
                    list_star.append(starcount[1].text)
                else:
                    list_star.append('NoInfo')
            else:
                list_star.append('NoInfo')

        return list_star
    
    def getforks(self):
        list_fork=[]
        for page in range(self.startpage, self.finishpage+1):
            soup = self.geturl(page)
            forkcount=soup.find_all('div',attrs={'class':'flex items-center'})

            if len(forkcount)>2:

                if forkcount:
                    list_fork.append(forkcount[2].text)
                else:
                    list_fork.append('NoInfo')
            else:
                list_fork.append('NoInfo')

        return list_fork

