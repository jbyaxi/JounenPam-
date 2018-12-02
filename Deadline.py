#TO_TEST
# A Class to create deadline on projects and goals
import datetime
import schedule
class Deadline(object):
    """
    Allow the user to create an manipulate a deadline
    """

    def EntreDate(self):
        msg = "Votre valeur doit etre un entier"
        #Date de mon deadline
        annee = raw_input("Entre la valeur de votre Annee...")
        annee = self.CheckInt(annee,msg)
        mois = raw_input("Entre la valeur de votre mois")
        mois = self.CheckInt(mois,msg)
        jour = raw_input("Entrez la valuer de votre jour")
        jour = self.CheckInt(jour,msg)
        #heure de mon deadline
        heure  = raw_input("Entrez l'heure de votre deadline")
        heure  = self.CheckInt(heure,msg)
        minute =  raw_input("Entrez la minute de votre deadline")
        minute  = self.CheckInt(minute,msg)
        mon_deadline = datetime.datetime(annee,mois,jour,heure,minute)
        return mon_deadline
    
    #T0_TEST
    def __init__(self):
        import datetime
        now = datetime.datetime.now()
        self.Nom = raw_input('Entrez le nom de votre deadline: ')
        self.description = raw_input('Entrez une description de votre deadline')
        while 0==0:
            try:
                self.mon_deadline = self.EntreDate()
                while self.mon_deadline.date() < datetime.date.today():
                    print "Votre date fait parti du passe"
                    self.mon_deadline = self.EntreDate()
                    
            except Exception as ex:
                print "Exception: " + str(ex)
                if str(ex) == "day is out of range for month":
                    print "ce mois n'a pas autant de jour..."
                if str(ex) == "month must be in 1..12":
                    print "Ce mois n'existe pas entrer un chiffre compris entre 1 et 12..."
                if str(ex) == "year is out of range":
                    print "La valeur maximal de l'annee est 9999..."
            else:
                print "Tout est OK!!!"
                break
        print "Si vous vouliez entrer des secondes vous etes un maniac, desole de vous le dire"
    
        
    def CheckInt(self,val,msg):
        while True:
            try:
                annee = int(val)
                return annee
            except:
                print "Votre valeur doit etre un entier..."
            else:
                break
    
    #DONE
    def Thedeadline(self):
        now = datetime.datetime.now()
        #use of <<< timedelta >>> to compute the difference between my deadline and the exact time and date
        msg = "Il vous reste "
        self.remain = self.mon_deadline - datetime.datetime.now()
        msg += "%s"+"\n" %(self.remain)
        print msg
    
    def remind(self):
       schedule.every(15*self.remain/100).minutes.do(self.Thedeadline) 