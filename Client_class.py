class Client:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.wached_movies=[]
        self.admin_status = None
        
    def get_name(self):
        return self.name
    def get_password(self):
        return self.password
    
    def get_movies(self):
        return self.wached_movies