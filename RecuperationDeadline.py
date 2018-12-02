import Deadline

class RecuperationDeadline(Deadline.Deadline):
    """
    this class was created in order to allow me to create deadline in a different way by retrieving 
    data entered by the user in a file
    """
    def __init__(self,nom,description,heure):
        self.nom = nom
        self.description = description
        self.mon_deadline = heure