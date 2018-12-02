import Journee

class RecuperationJournee(Journee.Journee):
    def __init__(self,date,plan):
        self.date = date
        self.plan = plan