class Mobile:
    Price=6000
    def __init__(self,Name,Model,Storage,Performance):
        self.Name=Name
        self.Model=Model
        self.Storage=Storage
        self.Performance=Performance

    @classmethod
    def Original_cost(cls,cost):
        cls.Price=cost
    
Mobile.Original_cost(9000)
m1=Mobile("Redmi",9,64,"Good")
print(m1.Price)
print(m1.Name)
print(m1.Model)
print(m1.Performance)
