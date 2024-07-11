import random as r 
import amirhoshein.jok as jokk 
import amirhoshein.font as f 
import amirhoshein.adad as ad
import amirhoshein.danestani as danestanii
import amirhoshein.hadis as hadiss
import amirhoshein.khatere as khateree
import amirhoshein.dastan as dastann
import amirhoshein.chistan as chistann
import amirhoshein.joojoo as j
class joojoo:
    def en(text:str):
        a = j.encode(text)
        return a
    def de(text:str):
        a = j.decode(text)
        return a
def joda(text:str,amount : int):
    """a = joda("ali",1) => a = ['a','l','i']"""
    amount = int(amount)
    edame = error = False
    text_f = ''
    try:
        text_int = len(text)
    except:
        print('Error!\nText vared shode , type str nis!')
        error = True
    if error == False:
        try:
            text_int2 = text_int / amount
            if not text_int2 % 1 == 0:
                edame = True
                text_int2 = int(text_int2)
            for i in range(int(text_int2)):
                i2 = i*amount
                text0 = text[i2:i2+amount]
                text1 = text0.replace(f'{text0}',f'{text0}^^^')
                text_f = text_f + text1  
            text_f2 = text_f.split('^^^')
            text_f2.remove(text_f2[-1])
            if edame == True:
                text_f2.insert(999**999,text[i2+amount:999**999])
            return text_f2
        except:
            print('Error!\nadad vared shode zir 1 hast!')
    else:
        None
def gore(sherkat_konande_ha:list , tedad_dafehat_charkhandan_gardone=100):
    import random
    emtiaza = {}
    for i in range(int(tedad_dafehat_charkhandan_gardone)):
        b = random.choice(sherkat_konande_ha)
        try:
            emtiaza[b] += 1
        except:
            emtiaza[b] = 1
    emtiaza2 = list(emtiaza)
    for i in range(len(emtiaza2)):
        emtiaza[emtiaza2[i]] = emtiaza[emtiaza2[i]] * 100 / tedad_dafehat_charkhandan_gardone
    emtiaza3 = list(dict(sorted(emtiaza.items(),key=lambda item: item[1])))
    emtiaza4 = {}
    for i in emtiaza3:
        emtiaza4[i] = emtiaza[i]
    return emtiaza4
def copy(text):
    import pyperclip
    pyperclip.copy(str(text))
def byte(text:str):
    byte1 = bytes(text,'utf-8') 
    return byte1
class code:
    """
a = code.en('salam') => a = 'c2FsYW0='
b = code.de('c2FsYW0=') => b = 'salam'"""
    def en(text:str):
        import base64
        text_code_en1 = str(text)
        text_code_en2 = base64.b64encode(text_code_en1.encode('utf-8'))
        text_code_en3 = str(text_code_en2)[2:-1]
        return text_code_en3
    def de(text:str):
        import base64
        text_code_de1 = str(text)
        text_code_de2 = base64.b64decode(text_code_de1).decode('utf-8')
        return text_code_de2
def num(count):
    count = str(count)
    len_adad = len(str(count))
    len_adad2 = []
    def namdanam():
        for i in range(len_adad//3+1):
            if not str(count)[i*3:i*3+3] == '':
                len_adad2.append(str(count)[i*3:i*3+3])
    namdanam()
    while not len(len_adad2[-1]) == 3:
        len_adad2 = []
        namdanam()
        if not len(len_adad2[-1]) == 3:
            count = '0' + count
    for i in range(2):
        if len_adad2[0][0:1]:
            a = str(int(len_adad2[0]))
            len_adad2.remove(len_adad2[0])
            len_adad2.insert(0,a)
    len_adad3 = str(len_adad2).replace("', '",',')
    len_adad3 = len_adad3.replace("']",'')
    len_adad3 = len_adad3.replace("['",'')
    return len_adad3
def sleep(value:float):
    import time
    time.sleep(value)
def exec(codes : str):
    """a = amirhoshein.exec("print('hi')") ==>  a = "hi" """
    file = open('exec_amir','w')
    file.write("import amirhoshein as am\n")
    file.write("fileaaaa=open('exec_amir','w')\n")
    file.write("fileprinttext = ''\n")
    file.write("def print(a='',b='',c='',d='',e='',f='',g='',end='\\n'):\n")
    file.write("    global fileprinttext\n")
    file.write("    fileprinttext= fileprinttext + f'{a}{b}{c}{d}{e}{f}{g}{end}'\n")
    file.write(f"exec(am.code.de('''{code.en(codes)}'''))\n\n")
    file.write("maxed = am.code.en(fileprinttext)\n")
    file.write("fileaaaa.write(maxed)\n")
    file.write("fileaaaa.close()")
    file.close()
    import os
    os.system('python exec_amir')
    file = open('exec_amir','r')
    file2 = file.read()
    file3 = code.de(file2)
    if file3[-1:] == '\n':
        file3 = file3[0:-1]
    return file3

class time:
    def year():
        import datetime
        now = datetime.datetime.now()
        year = now.year
        return year
    def month():
        import datetime
        now = datetime.datetime.now()
        month = now.month
        return month
    def day():
        import datetime
        now = datetime.datetime.now()
        day = now.day
        return day
    def hour():
        import datetime
        now = datetime.datetime.now()
        hour = now.hour
        return hour
    def minute():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        return minute
    def second():
        import datetime
        now = datetime.datetime.now()
        second = now.second
        return second
    def microsecond():
        import datetime
        now = datetime.datetime.now()
        microsecond = now.microsecond
        return microsecond
    def worldtime():
        import datetime
        now = datetime.datetime.now()
        worldtime = ((now.year*31536000)+(now.month*2592000)+(now.day*86400)+(now.hour*3600)+(now.minute*60)+(now.second))
        return worldtime
def download(filelink:str ,filename:str , filetype:str):
    import requests
    downloadfile = open(f"{filename}.{filetype}",'wb')
    download1 = requests.get(filelink).content
    downloadfile.write(download1)
    downloadfile.close()
def chasb(lis1:list):
    chasb1 = ''
    for i in range(len(lis1)):
        chasb1 = chasb1 + str(lis1[i])
    return chasb1
def font(text:str):
    font = f.font
    a = font(text)
    return a
def adad(num):
    num1 = ad.adad(num)
    return num1
def jok():
    jok1 = str(r.randint(1,len(list(jokk.a))))
    jok2 = jokk.a
    return jok2[jok1]
def dastan():
    dastan1 = str(r.randint(1,len(list(dastann.a))))
    dastan2 = dastann.a
    return dastan2[dastan1]
def danestani():
    danestani1 = str(r.randint(1,len(list(danestanii.a))))
    danestani2 = danestanii.a
    return danestani2[danestani1]
def hadis():
    hadis1 = str(r.randint(1,len(list(hadiss.a))))
    hadis2 = hadiss.a
    return hadis2[hadis1]
def khatere():
    khatere1 = str(r.randint(1,len(list(khateree.a))))
    khatere2 = khateree.a
    return khatere2[khatere1]
def chistan():
    chistan1 = str(r.choice(chistann.a['result']))
    return eval(chistan1)
def bomber(Number : str , timer=0.1):
    import amirhoshein.bomber as bomberr
    bomberr.bomber(Number , timer)
def html(Url : str):
    from requests import get
    a = get(Url).text
    return a

    