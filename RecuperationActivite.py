import Activite
import datetime
class RecuperationActivite(Activite.Activite):
    def format(self,heure_planifier):
        hours = heure_planifier
        minute = heure_planifier
        #if int(heure_planifier[0]) == 0:
         #   hours = int(hours[1:2:])
        #else:
        hours = int(hours[:2:])
        #if int(heure_planifier[3]) == 0:
        #    minute = int(minute[5:6:])
        #else:
        minute = int(minute[3:5:])
        try:
            heure_planifier_bon_format = datetime.time(hours,minute)
        except Exception as ex:
            print str(ex)
        return heure_planifier_bon_format
    
    def __init__(self,nom,heure_debut,heure_fin,description,execute=False,bilan=False):
        self.nom = nom
        self.debut = self.format(heure_debut)
        self.fin = self.format(heure_fin)
        self.description = description
        self.bilan_fait=bilan
        self.execute=execute