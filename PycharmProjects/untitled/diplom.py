import re
import os
import urllib
import urllib.request
#import numpy as np

#from bs4 import BeautifulSoup

#files = os.listdir("/home/ilia/Документи/yiddish/forverts/forverts")
#path = "/home/ilia/Документи/yiddish/forverts/forverts/"

###reading modes###
csvfile = 'Author@Book Title@Чи@Quote@Dalogue@\n'
file = 'Spektor_elnte_un_farshtosene'
##csvfilename - without extension!! if adding - sum
csvfilename = 'Spektor_elnte_un_farshtosene'

csvmode = 'w'
path = r"C:\Users\Илья\Documents\диплом 2017\yid"
otext = open(path + "\\" +file + '.txt', 'r', encoding="UTF-8")
text = otext.read()
#text = text.replace('\n', ' ')
otext.close
#print (text[:400])
samplestring = "12.01.1994 15.04.2005"

###sa of 11-07-19 not working with vilner geto for some reason
texttitle = re.findall(r'Title: (.*?) \$\$\$', text)
textauthor = re.findall(r'Author: (.*?) \$\$\$', text)


print (texttitle[0])
print (textauthor[0])
###Yiddish_latin
#old
# questionsdialogue = re.findall (r' +?(--- ?.*?\?)', text)
#questionsdialogue2 = re.findall (r'([: "][\w\-\s\;\,\'\:\——-]?.*\?)', text)
#new
#questionsdialogue = re.findall (r'(\n[–|”|“] [a-z|0-—-][\w|\-\s\;\,\'\:\—–—].*?\?)', text)
#questionsdialogue2 = re.findall (r'(: – [a-z|-—-0][\w|żąśł\-\s\;\,\'\:\——].*?\?)', text)

###Yiddish
#old
# questionsdialogue = re.findall (r' +?(--- ?.*?\?)', text)
#questionsdialogue2 = re.findall (r'([: "][\w\-\s\;\,\'\:\——-]?.*\?)', text)
#new
questionsdialogue = re.findall (r'(\n[—|—–|”|“] [a-z|U+0500-U+05FF|0-——-][\w|\-\s\;\,\'\:\—–—].*?\?)', text)
questionsdialogue2 = re.findall (r'(: — [a-z|0500-U+05FF|-—-0][\w|0500-U+05FF\-\s\;\,\'\:\——].*?\?)', text)

# qqnt = 0
# for q in questionsdialogue:
#     qqnt +=1
#     print (q)
#     print (qqnt)
#     print ()

###Ukrainian and Russian
# questionsdialogue = re.findall (r'(\n— ?.*[А-Я|Ї|І|Ґ|Є|-—|-][\w|ґєїі\-\s\;\,\'\:\——]?.*\?)', text)
# questionsdialogue = re.findall (r' \n(— .*\n)', text)
# questionsdialogue2 = re.findall (r'([: ?—|:  —|] [А-Я|Ї|І|Ґ|Є|-—|-][\w|ґєїі\-\s\;\,\'\:\——]?.*\?)', text)


###belarusian
#questionsdialogue = re.findall (r'(\n– ?.*[А-Я|І|Ў|І|-—|-][\w|\-|\s|\;|\,|\'|\:|\——]+\?)', text)
#questionsdialogue = re.findall (r'(\n - ?.*[А-Я|І|Ў|І|-—|-][\w|\-|\s|\;|\,|\'|\:|\——]+\?)', text)

###polish
#questionsdialogue = re.findall (r'(\n — [A-Z|ĄĆĘŁŃÓŚŹŻ|-—-][\w|żąśł\-\s\;\,\'\:\——]?.*\?)', text)
#questionsdialogue2 = re.findall (r'(: — [A-Z|ĄĆĘŁŃÓŚŹŻ|-—-][\w|żąśł\-\s\;\,\'\:\——]?.*\?)', text)

###lithuanian
#questionsdialogue = re.findall (r'(— [A-Z|ĄČĘĖŠŲŪŽĮ|-—-][\w|čęėįšųūž\-\s\;\,\'\:\——]?.*\?)', text)
#questionsdialogue2 = re.findall (r'([: ?—|:  —|] [A-Z|ĄČĘĖŠŲŪŽĮ|-—-][\w|čęėįšųūž\-\s\;\,\'\:\——]?.*\?)', text)

# questions = re.findall (r'[\.|\?|\!|\.\.\.|…|\n|\r] ([А-Я|І|Ґ][\w|\-|\s|\;|\,|\'|\:|\——]+\?)', text)


###Ukrainian
#questions = re.findall (r'([А-Я|І|Ґ|-—|-][\w|\-|\s|\;|\,|\'|\:|\——]+\?)', text)
#questionwords = ['чом', 'чого', 'скільки', 'якого', 'почему', 'коли', 'яке', 'яку', 'яким', 'пощо', 'якой', 'почому', 'який', 'навіщо', 'чия', 'кому', 'чим', 'де', 'ким', 'чия', 'ким', 'чого', 'щось', 'чомусь', 'кого', 'чого', 'яких','звідки', 'нашо', 'нащо', 'шо', 'шо-сь', 'що-сь', 'шо-с', 'куди', 'Куди', 'де','що', 'якої', 'як', 'яка', 'доки',  'де', 'чогось', 'з ким', 'З ким', ' Що', 'що', 'відки', 'Відки', 'чому', 'чьому', 'чому', 'як', 'які', 'нащо', 'Нащо', 'хто', 'Хто', ]
#czylist = ['чи', 'хіба', 'а', 'невже', 'може']

###Russian
# questions = re.findall (r'([А-Я|І|Ґ|-—|-][\w|\-|\s|\;|\,|\'|\:|\——]+\?)', text)
# questionwords = ['почему', 'чем', 'сколько', 'какого', 'почему', 'когда', 'какой', 'какую', 'каким', 'что', 'какому', 'зачто', 'чья', 'кому', 'где', 'кем', 'что-то', 'почему-то', 'каких','откуда', 'шо', 'куда', 'докуда',  'доколе','с кем', 'откуда']
# czylist = ['ли', 'разве', 'а', 'неужели', 'может']
# czy = 'ли'
# hiba = 'разве'
# a = 'а'
# maybe = 'может'

###Yiddish
questions = re.findall (r'[\n\t,.?!]([\n\t\|\s\-—|\-\#\']*?[\w|\-|\s|\;|\,|\'|\:|▮\——\-#]+\?)', text)
questions = re.findall (r'[.?!]([^.?!]+\?)', text)
#for bbb in questions:
#    k = re.sub(r'\s{2,30}', ' ', bbb)
#    k = re.sub(r'-{4,30}', ' ', k)
#    questions.append(k)
questionwords = ['װעלכע','װעם', 'װאָס-זשע', 'װאו', 'װיפֿל', 'װאַנען' , 'װוכינ', 'װוּכינ', 'װער', 'װוּ', 'װענ', 'פֿאַרװאָס', 'פאַרװאָס','װאָרעמ', 'װאַנענ','װאס', 'װאָס', 'װאַנ', 'װאנ', 'װי', 'װעלכע', 'װיפל', 'װוכינ', 'װער', 'װו', 'װענ', 'װען','װאָס','װעמע', 'װיפיעל' ,'פֿאװאס', 'װארעמ', 'װאנענ', 'װאס', 'װאנ','װי', 'פאװאס', 'פֿאַװאס', 'פֿאװאָס','װאַם' , 'װאם']
czylist = ['צי', 'היבע', 'עפֿשער', 'עפשער','אפֿשר', 'אפשר', 'היבע']
czy = 'צי'
hiba = 'היבע'
a = 'NA'
maybe = 'עפֿשער'

###Belorusian

#questions = re.findall (r'([А-Я|І|І|Ў|-—|-][\w|\-|\s|\;|\,|\'|\:|\——]+\?)', text)
#questionwords = ['Чэкго', 'якую', 'якія', 'Хто', 'калi', 'хто', 'што', 'шо', 'каго', 'чаго', 'каму', 'чаму', 'кiм', 'чым', 'чый', 'чыё', 'чыя', 'чыi', 'скуль', 'як', 'які', 'якое', 'якая', 'якi', 'якiя', 'нашто', 'калі', 'куды', 'адкуль', 'чаму', 'дзе']

###Lithuanian
#questions = re.findall (r'([A-ĄČĘĖŠŲŪŽĮ-—-][\wčęėįšųūž\-\s\;\ ,\':|\——]+\?)', text)
#questionwords = ['kokį', 'koki', 'kokius', 'kokiais', 'kokiem', 'kokią', 'koke', 'kame', 'kuriam', 'kokių', 'kuom', 'kurį', 'kurių', 'kokio', 'kaip', 'kad', 'Kokiais' 'kurgi',  'kaipgi', 'kokiu', 'kokia', 'koks', 'ką', 'kas', 'kodėl', 'kodel', 'ka', 'ko', 'kur', 'kiek', 'kada', 'kam', 'kuo', 'kelintas','kuris', 'kieno', 'kelinta',  'kokie', 'kokios']
#czylist = ['ar', 'gal', 'galgi', 'argi', 'o', 'nejau', 'nejaugi']
#questionaffix = ['gi']
#newquestionwords = []
#for q in questionwords:
#    newquestionwords.append(q)
#    for qr in questionaffix:
#        newword = q + qr
#        newquestionwords.append(newword)
#questionwords = newquestionwords

###Polish
#questions = re.findall (r'([A-ZĄĆĘŁŃÓŚŹŻ-—-][\wżął\-\s\;\ ,\':|\——]+\?)', text)
#questionwords = ['zkąd', 'skąd', 'gdy', 'ktorędy', 'dokąd', 'coś', 'cóż', 'czém', 'czegoż', 'zaco', 'poco', 'czém', ' kiedyż','gdzie','coby', 'jakim', 'dlaczego','kiedy', 'cośmy', 'kto', 'któ','co','ile','jaka','która','jak','kogo','czego', 'komu', 'czem',  'czemu', 'kim', 'czym']
#questionaffix = ['ż', 'że', 'by', 'to', 'żeś', 'ś', 'byś']
#newquestionwords = []
#for q in questionwords:
#    newquestionwords.append(q)
#    for qr in questionaffix:
#        newword = q + qr
#        newquestionwords.append(newword)
#questionwords = newquestionwords
#czylist = ['czy', 'chyba', 'a', 'może']
#czy = 'czy'
#hiba = 'chyba'
#a = 'a'
#maybe = 'może'
###End Polish

questcount = 0
questcount2 = 0
counterydialogue = 0
counterndialogue = 0
czycount = 0
czyqwordcount = 0
questions2 = []
sentwithqword = []
czysentences = []
sentwithoutqword = []
rightsent = ''
questions3 = []
nocapitalletter = []
nocapitallettercounter = 0
newcount = 0
newestcount = 0
#SECTION 1
print ('SECTION 1')
ncnt = 0

for sent in questions:
    ncnt +=1
    print ()
    print ("##################")
    print (ncnt)
    print ("input sent")
    print (sent)
    #as for 24.07.19 I don't know what this code does
    # if sent[0].islower():
    #     nocapitalletter.append(sent)
    #     nocapitallettercounter += 1
    #     continue
    sentindialogue = False
    for b in questionsdialogue[:3]:
        if sent in b:
            sentindialogue = True
            # print ("DIALOGUE SENT")
            # print (sent)
            # print ("Dialogue Context" + b)
            # print ()
    #for bb in questionsdialogue2:
    #    if sent in bb:
    #        sentindialogue = True
    # sent2 = re.sub ('^[—-—]? ?', '', sent)
    newestcount += 1
    # print (newestcount)
    if sentindialogue:
        sentmodified = sent + '@DIALOGUE'
        counterydialogue +=1
        print ("this was a dialogue sentence")
    else:
        if "—" in sent:
            sentmodified = sent + '@DIALOGUE'
            counterydialogue += 1
            print("this was a dialogue sentence")
        else:
            sentmodified = sent + '@NOTDIALOGUE'
            counterndialogue+=1
            print ("this was NOT a dialogue sentence")

    questions2.append(sentmodified+'@')

#SECTION 2
print ('SECTION 2')
for l in questions2:
    rightsent = l.replace('\n', ' ')
    rightsent = re.sub('( ){3,10}',' ',rightsent)
    #print (rightsent)
    questions3.append(rightsent)

#for n in questions2:
#   questcount +=1
#    print (n)
#    print (questcount)


#SECTION 3
print ('SECTION 3')
for k in questions3:
    csvfile += (textauthor[0] + '@' + texttitle[0] + '@')

    qwordwxists = False
    czyexists = False
    czyqwordexists = False
    czyqwordexists2 = False
    hibaexists = False
    aexists = False
    neuzhelexists = False
    takexists = False
    doubleczyexists = False
    mozheexists = False
    #print (k)
    #print (questcount)
    for qqq in czylist:
        for nnn in questionwords:
            if nnn in re.split('[ ,.?:;« —]', k.lower()):
                czyqwordexists = True
            if qqq in re.split('[ ,.?:;« —]', k.lower()):
                if qqq == czy:
                        if czyqwordexists:
                            czyqwordexists2 = True
                        elif re.match(czy + r'.*' + czy, k.lower()) is not None:
                            doubleczyexists = True
                        else:
                            czyexists = True
                if qqq == hiba:
                    hibaexists = True
                #if qqq == 'невже':
                #    neuzhelexists = True
                if qqq == maybe:
                    mozheexists = True
                if qqq == a:
                    if not czyqwordexists:
                        aexists = True
    if czyexists and czyqwordexists2:
        czysentences.append(k)
        czyqwordcount += 1
        csvfile += ('CZYQWORD@' + k + '\n')
    elif doubleczyexists:
        czysentences.append(k)
        czyqwordcount += 1
        csvfile += ('2CZY@' + k + '\n')
    elif czyexists:
        czysentences.append(k)
        czycount += 1
        csvfile += ('CZY@' + k + '\n')
    elif hibaexists:
        czysentences.append(k)
        czycount += 1
        csvfile += ('HIBA@'+k +'\n')
    elif neuzhelexists:
        czysentences.append(k)
        czycount += 1
        csvfile += ('Nevzhe@' + k + '\n')
    elif mozheexists:
        czysentences.append(k)
        czycount += 1
        csvfile += ('Mozhe@' + k + '\n')
    elif aexists:
        czysentences.append(k)
        czycount += 1
        csvfile += ('A@' + k + '\n')
    else:
        for qq in questionwords:
            if qq in re.split('[ ,.?:;« —]', k.lower()):
                qwordwxists = True
        if qwordwxists:
            print('with: ' + k)
            sentwithqword.append(k)
            questcount2 += 1
            csvfile += ('QWORD@' + k+'\n')
        else:
            sentwithoutqword.append(k)
            csvfile += ('NOQWORD@' + k+'\n')

print ('##########')
print ('sentences with чи')
for t in czysentences:
    print (t)
print ('###########')

print ('sentences without qword')

sentwithoutqwordcount = 0
for b in sentwithoutqword:
    sentwithoutqwordcount += 1
   # print(sentwithoutqwordcount)
    print (b)
print ('')
print ('###############')
print ('no capital letters:')
for l in nocapitalletter:
    print (l)
print ('')
print ('%%%%%%%%%%%%%')

print('no capital latters:', nocapitallettercounter)
print ('with qword', questcount2, 'without qword', sentwithoutqwordcount, 'with чи', czycount, 'with czyqword', czyqwordcount)
print ('')
print ('YDialogue:', counterydialogue, 'Ndialogue', counterndialogue)

print ('\n\n')

print (newcount)

#print (csvfile)

#print (csvfile)
csvtext = open(path + "\\" +csvfilename + '.csv', csvmode, encoding="UTF-8")
csvtext.write (csvfile)
csvtext.close()

# print (questionsdialogue)