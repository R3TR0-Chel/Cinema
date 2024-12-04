class movie:
    def __init__(self,title,schedule,price):
        self.title = title
        self.schedule = schedule
        self.price = price
        
    def get_schedule(self):
        return self.schedule
    def get_price(self):
        return self.price
    def get_title(self):
        return self.title