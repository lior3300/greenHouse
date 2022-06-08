import json
import os

class Plant:

    kindsList=[]
    plantsLst=[] #list of Plant object that is loaded from json

    def __init__(self,kind,grow_time,temp_min,temp_max) -> None:
        self.kind=kind
        self.grow_time=grow_time
        self.temp_min=temp_min
        self.temp_max=temp_max

    #region setters and getters    
    def __setKind(self,kind):
        self.__kind=kind

    def __getKind(self):
        return self.__kind
    kind=property(__getKind,__setKind)

    def __setGrow_time(self,grow_time):
        self.__grow_time=grow_time

    def __getGrow_time(self):
        return self.__grow_time    
    grow_time=property(__getGrow_time,__setGrow_time)

    def __setTemp_min(self,temp_min):
        self.__temp_min=temp_min
    
    def __getTemp_min(self):
        return self.__temp_min
    temp_min=property(__getTemp_min,__setTemp_min)

    def __setTemp_max(self,temp_max):
        self.__temp_max=temp_max
    
    def __getTemp_max(self):
        return self.__temp_max   
    temp_max=property(__getTemp_max,__setTemp_max)
    #endregion

    def __eq__(self, other) -> bool:
        return self.kind==other.kind

    @staticmethod
    def initPlants():
        '''run this on load in loadPlants()'''
        if not os.path.isfile("plants.json"): #if the file doesn't exist then create it
            with open("plants.json","w") as f:
                f.write("[\n]")

    @staticmethod
    def addPlant(newPlant):
        if len(Plant.kindsList)<8:
            #check if plant kind is in the list
            for p in Plant.plantsLst:
                if p==newPlant:
                    # print("the same plant with the same kind already exist")
                    return False
                    # break
            else:
                Plant.plantsLst.append(newPlant)
                with open("plants.json","w") as f:
                    json.dump([p.__dict__ for p in Plant.plantsLst],f,indent=4)
                    Plant.kindsList.append(newPlant.kind)
                    # print(f"added plant {newPlant.kind} to the list")
                    return True
            
        else:
            return False
            # return "no more space to add more plants"
    
    @staticmethod
    def loadPlants():
        Plant.initPlants()
        with open("plants.json","r") as f:
            jsonLst=json.load(f)

        Plant.plantsLst = [Plant(p["_Plant__kind"],
                            p["_Plant__grow_time"],
                            p["_Plant__temp_min"]
                            ,p["_Plant__temp_max"]) 
                        for p in jsonLst]
        
        Plant.kindsList=[plant.kind for plant in Plant.plantsLst]

    @staticmethod
    def growTimeByKind(kind):
        return next((plant.grow_time for plant in Plant.plantsLst if plant.kind==kind),None)

    @staticmethod
    def tempScopeByKind(kind):
        plt = next((plant for plant in Plant.plantsLst if plant.kind==kind),None)
        if plt is not None:
            return (plt.temp_min,plt.temp_max)
        else:
            return (None,None)

    @staticmethod
    def removePlant():
        with open("plants.json","w") as f:
            json.dump([p.__dict__ for p in Plant.plantsLst],f,indent=4)

# if __name__=="__main__":
#     p1=Plant("a",65,10,45)
#     p2=Plant("b",780,5,50)
#     p3=Plant("c",180,20,50)
    # p4=Plant("d",40,15,80)
    # p5=Plant("e",70,10,45)
    # p6=Plant("f",90,10,45)
    # p7=Plant("g",100,10,45)
    # p8=Plant("h",1080,10,45)
    # plntLst=Plant.initPlants()
    # Plant.loadPlants()
    # Plant.addPlant(p1)
    # Plant.addPlant(p2)
    # Plant.addPlant(p3)
    # print(Plant.growTimeByKind("a"))
    # print(Plant.tempScopeByKind("f"))
    # print(Plant.kindsList)