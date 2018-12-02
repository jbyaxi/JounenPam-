import datetime
import Activite
import threading
import schedule
import time
class Journee(object):
    """
     This class is the representation of a day it can contain many activities to be achieve
    """
    #TO_DO
    def __init__(self):
        print "***********************************************"
        print "*           A NEW DAY JUST STARTED            *"
        print "***********************************************"
        self.plan = []
        date = raw_input("Voulez vous entrez la date de votre journee? Si vous choissisez non la date d'aujourd'hui sera considere")
        if date =='non':
            print "Aujourd'hui est %s" %(datetime.date.today())
            print "Il est " + str(datetime.datetime.time(datetime.datetime.now()))
            f = open('C:\Users\Yv-Arnel\Desktop\journee.txt','a')
            f.write(str(datetime.date.today())+":"+"\n")
            reponse = raw_input("Voulez-vous ajouter une nouvelle activite a cette journee?")
            while reponse == 'oui':
                # specifik = raw_input("Quelle genre d'activite???")
                # if specifik == "lecture":
                #     acti = lecture()
                # elif specifik == "programmation":
                #     acti = programming()
                # elif specifik == 'sport':
                #     acti = sport()
                # else:
                #     acti = Activite()
                acti = Activite.Activite()
                f.write(" "+str(acti.debut)+"-"+str(acti.fin)+"--------"+str(acti.nom)+"--------"+str(acti.description)+"\n")
                self.plan.append(acti)
                reponse = raw_input("Voulez-vous ajouter une nouvelle activite")
            
        elif date=='oui':
            try:
                self.ma_date = self.EntreDate()
                print "Votre date fait partie du passe"
                while datetime.date.today() <  self.ma_date:
                    self.ma_date = self.EntreDate()
                f = open('C:\Users\Yv-Arnel\Desktop\journee.txt','a')
                f.write(str(self.ma_date)+":"+"\n")
                reponse = raw_input("Voulez-vous ajouter une nouvelle activite a cette journee?")
                while reponse == 'oui':
                # specifik = raw_input("Quelle genre d'activite???")
                # if specifik == "lecture":
                #     acti = lecture()
                # elif specifik == "programmation":
                #     acti = programming()
                # elif specifik == 'sport':
                #     acti = sport()
                # else:
                #     acti = Activite()
                    acti = Activite.Activite()
                    f.write(" "+str(acti.debut)+"-"+str(acti.fin)+"--------"+str(acti.nom)+"--------"+str(acti.description)+"\n")
                    self.plan.append(acti)
                    reponse = raw_input("Voulez-vous ajouter une nouvelle activite")
                f.close()
            except Exception as ex:
                if str(ex) == "day is out of range for month":
                    print "ce mois n'a pas autant de jour..."
                if str(ex) == "month must be in 1..12":
                    print "Ce mois n'existe pas entrer un chiffre compris entre 1 et 12..."
                if str(ex) == "year is out of range":
                    print "La valeur maximal de l'annee est 9999..."
    
    #TO_DO
    def addActivite(self,actu):
        self.plan.append(actu)
    
    def bilan(self):
        for i in self.plan:
            if datetime.datetime.now()<i.debut:
                print i
    
    def PlanJourne(self):
        for i in self.plan:
            print "%s  :    %s \n" %(i.debut,i.Nom)

    def DeleteActivite(self):
        print "Si vous lisez ceci c'est que vous etes vivant et tant que vous etes vivant on annule pas"

    def EntreDate(self):
        rappel = "Votre valeur doit etre un entier"
        #Date de ma journee
        #Annee
        annee = self.CheckInt(rappel,"Entre la valeur de votre Annee...")
        #Mois
        mois = self.CheckInt(rappel,"Entrez la valeur de votre mois")
        #Jour
        jour = self.CheckInt(rappel,"Entrez la valeur de votre jour")
        ma_date = datetime.date(annee,mois,jour)
        return ma_date
    
    def Start(self):
        for i in self.plan:
            #t = threading.Thread(target=self.Prev,args=(i,))
            #t.start()
            schedule.every().day.at(str(i.debut)[:5:]).do(i.Start)
            schedule.every().day.at(str(i.fin)[:5:]).do(i.bilan)
        while True:
            schedule.run_pending()
            time.sleep(1)
            if schedule.jobs == []:
                break

    def Prev(self,task):
        schedule.every().day.at(str(task.debut)[:5:]).do(task.Start)
        actual_time = datetime.datetime.now()
        comparant = datetime.time(actual_time.hour,actual_time.minute) 
        while not task.execute:
            time.sleep(1)
            schedule.run_pending()
            if task.debut<comparant:
                print "boom"
                break
        schedule.every().day.at(str(task.fin)[:5:]).do(task.bilan)
        while not task.bilan_fait:
            time.sleep(1)
            schedule.run_pending()
            

    def CheckInt(self,rap,msg):
        while True:
            try:
                val = int(raw_input(msg))
                return val
            except:
                print rap
            else:
                break