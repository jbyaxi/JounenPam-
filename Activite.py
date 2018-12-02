import datetime
import schedule
import winsound
import threading
class Activite(object):
    #DONE
    """
    Parent class of most of the classes below except deadline and day content info on schedule activities
    """
    #ALL the commented code in this program are subject to be part of upgrade

    def __init__(self,execute=False,bilan=False):
        self.nom = raw_input("Entrez le nom de la tache: ")
        #heure debut
        T = self.saisiTemps("Entrez les infos sur quand on doit commenncer")
        self.debut = datetime.time(T[0],T[1])
        #heure Fin
        T = self.saisiTemps("Entrez les infos sur quand on doit terminer")
        self.fin = datetime.time(T[0],T[1])
        while self.debut > self.fin:
            print "La date de fin doit etre plus grand que celle du debut..."
            T = self.saisiTemps("Entrez les infos sur quand on doit terminer")
            self.fin = datetime.time(T[0],T[1])
        #description de la tache
        self.description = raw_input("Faites une description de la tache: ")
        self.description = self.formatTampon(self.description,50)
    #DONE
    def saisiTemps(self,msg):
        print msg
        heure = int(raw_input("Entrez l'heure"))
        while heure > 24:
            heure = int(raw_input("Entrez l'heure: "))
        minute = int(input("Entrez la minute"))
        while minute > 60:
            minute = int(raw_input("Entrez les minutes: "))
        t = (heure,minute)
        return t
    #DONE
    def formatTampon(self,text,x):
        er_partie = text[:x:] +"\n"
        reste = text[x::]
        while(len(reste)>x):
            while not(reste[x]==" "):
                x -=1
            er_partie +=reste[:x:].strip() +"\n"
            reste = reste[x::]
        er_partie +=reste.strip()
        return er_partie
    #DONE
    def fich(self):
        self.f = open('E:\Projet\Schedule-Python/bilan.txt','a')
    #DONE
    def wfich(self,Sort_of_tampon):
        self.f.write(Sort_of_tampon)
        self.f.close()
    #DONE
    def check(self,key):
        winsound.PlaySound("E:\Projet\Schedule-Python\sound/Cop Car Siren-SoundBible.com-1231381021.wav",winsound.SND_FILENAME|winsound.SND_LOOP|winsound.SND_ASYNC)
        key.wait()
    #DONE
    def checko(self,key):
        key.wait()
        winsound.PlaySound(None,winsound.SND_PURGE)
        
    #DONE
    def Start(self):
        self.execute = True
        print "************************"
        print "           %s        "  %(self.nom)
        print "************************"
        #PLay sound to attract attention
        key = threading.Event()
        t1 = threading.Thread(target=self.check , args=(key,))
        t2 = threading.Thread(target=self.checko, args=(key,))
        t1.start()
        t2.start()
        k = raw_input(" Press Any key to Start ")
        if k:
            key.set()
        return schedule.CancelJob
    
    def stop(self):
        print"Pour me debarasser de l'erreur qui m'emmende"
        #Le calcule avec le moment possible du debut et celui de la fin dans certains cas
    #TO_DO
    #count the moment the timer spend on brake to write it in the register
    #DONE
    def bilan(self):
        """Will be call at the end of the time to register what as been done and how good the activity was."""
        self.bilan_fait = True
        date = str(datetime.datetime.now()) +":\n"
        rapport = raw_input("Entrez le bilan de l'activite: Ce qui a ete fait - Ce qui reste a faire...: ")
        bill = date + self.nom +"\n"+ rapport
        bill = self.formatTampon(bill,50)
        self.fich()
        self.wfich(bill)
        return schedule.CancelJob
    #TO_DO
    def setStatut(self,statu):
        self.statut = statu
    #DONE
    def __str__(self):
        return self.description
    #WORK_IN_PROGRESS
