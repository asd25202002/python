import requests
import bs4
import pandas as pd
import time
import wget
import os
from PIL import Image
import glob

def jp():
        '''連上網頁'''
        # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        # res = requests.get('https://gamewith.tw/pricone-re/article/show/87390',headers=headers)
        # content = res.content.decode()
        url = 'https://gamewith.jp/pricone-re/article/show/92923'
        tsmchtml = requests.get(url)
        objSoup = bs4.BeautifulSoup(tsmchtml.text, 'html.parser')

        '''開始'''
        print('連接完成.....')

        '''建立字典'''
        df = {}
        '''輸入資料'''
        print('資料輸入中.....')
        table = objSoup.select('.puri_chara')
        table = table[0].find('table')
        for tr in table:
                '''角色名稱'''
                name = tr.get('data-col1')
                if (name != None and '<br>' in name):
                        name = name.replace('<br>','')
                '''角色類型'''
                type_ = tr.get('data-col2')
                '''角色評分(無專武)'''
                score_1 = tr.get('data-col3')
                '''角色評分(有專武)'''
                score_2 = tr.get('data-col4')
                '''角色評分(6星)'''
                score_3 = tr.get('data-col5')
                '''角色介紹連結和圖片'''
                td = tr.find('td')
                if td != None:
                        info = td.find('a').get('href')
                        head =  td.find('a').find('img').get('src')

                        '''角色介紹'''
                        print('目前正抓取 {} 的角色資料....'.format(name))
                        df[name] = []

                        '''角色頭貼下載'''
                        filename = name + '.png'
                        if os.path.isdir('./head/png_jp'):
                                filepath = os.path.join('./head/png_jp',filename)
                        if not os.path.isfile(filepath):
                                wget.download(head,filepath)
                                '''轉檔'''
                                frames = []
                                imgs = glob.glob(os.path.join('./head/png_jp',(name + '.png')))
                                for i in imgs:
                                        new_frame = Image.open(i)
                                        frames.append(new_frame)
                                
                                frames[0].save(os.path.join('./head/gif_jp',(name + '.gif')), format='GIF',
                                        append_images=frames[1:],
                                        save_all=True,
                                        duration=300, loop=0)

                        tsmchtml_ = requests.get(info)
                        objSoup_ = bs4.BeautifulSoup(tsmchtml_.text, 'html.parser')

                        '''角色立繪下載'''
                        src = objSoup_.find('div',class_='pcr_img_charatop').find('img').get('src')
                        filename = name + '.png'
                        if os.path.isdir('./people/png_jp'):
                                filepath = os.path.join('./people/png_jp',filename)
                        if not os.path.isfile(filepath):
                                wget.download(src,filepath)
                                '''轉檔'''
                                frames = []
                                imgs = glob.glob(os.path.join('./people/png_jp',(name + '.png')))
                                for i in imgs:
                                        new_frame = Image.open(i)
                                        frames.append(new_frame)
                                
                                frames[0].save(os.path.join('./people/gif_jp',(name + '.gif')), format='GIF',
                                        append_images=frames[1:],
                                        save_all=True,
                                        duration=300, loop=0)

                        '''角色台詞'''
                        tips = objSoup_.find('div',class_="puri_tips").find('p').text

                        '''角色評價'''
                        table = objSoup_.find('div',class_='puri_hyouka_table')
                        comment = table.select('td')[2].text

                        '''角色站位'''
                        sop = objSoup_.find('div',class_='puri_kihon_table') 
                        sop = sop.select('td')[0].text.split('/')[0].replace(' ','')

                        '''新增字典'''
                        df[name].extend([sop,tips,score_1,score_2,score_3,type_,comment])
                        time.sleep(1)

        '''建立資料表'''
        print('正在建立資料表.....')
        df = pd.DataFrame(df)
        df.to_csv('character_jp.csv', index=False)
        print('建立完成!!')

