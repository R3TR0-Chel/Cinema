class Movie:
    def __init__(self,title,schedule,price):
        self.title = title 
        self.schedule = schedule
        self.price = price
        self.quant = 0
        
    def get_title(self):
        return self.title
    def get_schedule(self):
        return self.schedule
    def get_quant(self):
        return self.quant
    def add_quant(self,quant):
        self.quant += quant
    def refund(self,quant):
        self.quant-=quant