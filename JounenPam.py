import os
import datetime
import winsound
import threading 
import schedule
import time
import Journee
import RecuperationJournee
import RecuperationActivite
import RecuperationDeadline

print "*******************************************************************************************"
print "                                      Jounen Pa m'                                         "
print "*******************************************************************************************"
save_day = open('C:\Users\Yv-Arnel\Desktop\journee.txt','a+')
save_deadline = open('C:\Users\Yv-Arnel\Desktop\deadline.txt','a+')
save_day.seek(0)
save_day_read = save_day.readlines()
save_day.close()
save_deadline.seek(0)
save_deadline_read = save_deadline.readlines()
save_deadline.close()
plan = []
if os.stat('C:\Users\Yv-Arnel\Desktop\journee.txt').st_size==0:
    print "Vous n'avez rien de prevu du tout ..."
    print "Parlons-en"
    print "Il est :"
    print datetime.datetime.time(datetime.datetime.now())
    reponse = raw_input("Voulez prevoir des activites: ")
    if reponse == "oui" or reponse == 'Oui':
        ma_journee = Journee.Journee()
        ma_journee.Start()
    else:
        print "Ben ok"
else:
    print "Vous avez des plans"
    for i in save_day_read:
        print i

if os.stat('C:\Users\Yv-Arnel\Desktop\deadline.txt').st_size==0:
    print "Aucun deadline ne vous pend sur la gueule"
else:
    print "Vous avez des deadlines"
    for i in save_deadline_read:
        print i
#print save_day_read
for i in save_day_read:
    if len(i)== 12:
        annee = i
        mois = i
        jour = i
        try:
            date_journee = datetime.date(int(annee[:4:]),int(mois[5:7:]),int(jour[8:10:]))

        except Exception as ex:
            print str(ex)
        else:
            if date_journee == datetime.date.today():
                aujourd = True

            else:
                aujourd = False
    if i[0] == ' ' and aujourd:
        debut = i
        fin   = i
        nom   = i
        debut = i[1:6:]
        fin = i[10:15:]
        nom = i[26]
        x = 27

        while i[x] != '-':
            nom += i[x]
            x += 1

        while i[x] == '-':
            x += 1

        description = i[x::]

        description.split()
        acti = RecuperationActivite.RecuperationActivite(nom,debut,fin,description)
        plan.append(acti)

if plan != []:
    today = RecuperationJournee.RecuperationJournee(datetime.date.today(),plan)
    today.Start()
    print "Vous n'avez pas d'autre plan pour aujourd'hui..."
    plan  = []
else:
    print "Vous n'avez pas de plan pour aujourd'hui"