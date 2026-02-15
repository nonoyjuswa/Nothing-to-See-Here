from model.database import Database

class AppController:
    def __init__(self,view):
        self.view = view
        self.database = Database()