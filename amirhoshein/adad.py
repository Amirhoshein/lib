def adad(num):
    count = str(num)

    adad = ['','یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه','ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هیفده','هیجده','نوزده']
    dahgan = ['','','بیست','سی','چهل','پنجاه','شست','هفتاد','هشتاد','نود']
    sadgan = ['','صد','دیویست','سیصد','چهارصد','پونصد','ششصد','هفتصد','هشتصد','نهصد']
    edamash = [' ','هزار', 'میلیون', 'میلیارد', 'تریلیون', 'کادریلیون', 'کوینتیلیون', 'سکستیلیون', 'سپتیلیون', 'اکتیلیون', 'نانیلیون', 'دسیلیون', 'آندسیلیونی', 'دودسیلیونی', 'تریدسیلیونی', 'کواتوردسیلیونی', 'کویندسیلیونی', 'سیدسیلیونی', 'سپت دسیلیونی', 'اکتو دسیلیونی', 'انان دسیلیونی', 'ویگینتیلیون', 'ویگینتیلیونی', 'ویگینتیلیونی دو', 'ویگینتیلیونی سه', 'تریگنتیلیون', 'تریگنتیلیونی', 'کوتریگینتیلیون', 'ویگا انتیلیون', 'ویگا انتیلیونی', 'سکوویژینتیلیون', 'سپتویژینتیلیون', 'اکتوویژینتیلیون', 'نانجینتیلیون', 'نانجینتیلیونی', 'آوتینتیلیون']
    for i in range(10000):
        edamash.append('')
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
    for i2 in range(len(len_adad2)):
        for i in range(2):
            if len_adad2[i2][0:1]:
                a = str(int(len_adad2[i2]))
                len_adad2.remove(len_adad2[i2])
                len_adad2.insert(i2,a)
    #-------------------
    adad_sadi = ''
    edame_taresh2 = len(len_adad2)-1
    for edame_taresh in range(len(len_adad2)):
        edame_taresh3 = edame_taresh2 - edame_taresh
        i = len_adad2[edame_taresh]
        if len(str(int(i))) == 3:
            nana = False
            for aa in range(3): 
                if aa == 0:
                    if not str(sadgan[int(str(i)[0:1])]) == '':
                        adad_sadi= adad_sadi + str(sadgan[int(str(i)[0:1])]) + ' و '
                elif aa == 1:
                    if int(str(i)[1:2]) == 1:
                        nana = True
                    else:
                        adad_sadi= adad_sadi + str(dahgan[int(str(i)[1:2])]) + ' و '
                elif aa == 2 and nana == False:
                    adad_sadi = adad_sadi + str(adad[int(str(i)[2:3])]) + ' ' + str(edamash[edame_taresh3]) + ' و '
                elif nana == True :
                    adad_sadi = adad_sadi + str(adad[int(str(i)[1:3])]) + ' ' + str(edamash[edame_taresh3]) + ' و '
        elif len(str(int(i))) == 2:
            nana = False
            for aa in range(2): 
                if aa == 0:
                    if int(str(i)[0:1]) == 1:
                        nana = True
                    else:
                        adad_sadi= adad_sadi + str(dahgan[int(str(i)[0:1])]) + ' و '
                elif aa == 1 and nana == False:
                    adad_sadi = adad_sadi + str(adad[int(str(i)[1:2])]) + ' ' + str(edamash[edame_taresh3]) + ' و '
                elif nana == True :
                    adad_sadi = adad_sadi + str(adad[int(str(i)[0:2])]) + ' ' + str(edamash[edame_taresh3]) + ' و '
        elif len(str(int(i))) == 1:
            adad_sadi = adad_sadi + str(adad[int(str(i)[0:1])]) + ' ' + str(edamash[edame_taresh3]) + ' و '
    adad_sadi = adad_sadi.replace('و  و','و')
    adad_sadi = adad_sadi.replace(' و  ',' ')
    if adad_sadi[-3:] == ' و ':
        adad_sadi = adad_sadi[0:-3]
    return adad_sadi[:-1]
            