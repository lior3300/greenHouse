from PlantingPoint import PlantingPoint,Plant
import json,os,copy

class Greenhouse:
    def __init__(self,avgTemp,greenhousID):
        self.greenhousID=greenhousID
        self.avgTemp=avgTemp
        self.palntingPoints=[]

    #region getters and setters
    def setGreenhousid(self,greenhousID):
        self.__greenhousID=greenhousID

    def getGreenhousid(self):
        return self.__greenhousID
    greenhousID=property(getGreenhousid,setGreenhousid)

    def __setAvgtemp(self,avgTemp):
        self.__avgTemp=avgTemp

    def __getAvgtemp(self):
        return self.__avgTemp
    avgTemp=property(__getAvgtemp,__setAvgtemp)
    #endregion

    #region loading managment
    @staticmethod
    def loadGreenhouses()->list:
        '''on application start this will load all the greenhouses from the json and return it as a list'''
        jsons=[f for f in os.listdir("./greenhouses")] #get all the files in the directory
        #sort them by number from 1-10, if not do convert to int will be: 1.json,10,json,2.json,3.json .... 9.json
        jsons.sort(key=lambda x:int(x.split(".")[0]))

        grnhssLst=[] #to return
        for j in jsons:
            with open(f"./greenhouses/{j}","r") as f: #load the file, create the greenhouse,load the points, add to returned list
                jsonRead=json.load(f)
                greenHouseTmp=Greenhouse(jsonRead["_Greenhouse__avgTemp"],jsonRead["_Greenhouse__greenhousID"])
                
                greenHouseTmp.loadPlantingPoints(jsonRead)
                grnhssLst.append(greenHouseTmp)

        return grnhssLst

    def loadPlantingPoints(self,fileRead):
        '''this method is called from loadGreenhouses()'''
        pointsLoad=[
                    PlantingPoint(p["_PlantingPoint__pointId"],
                                p["_PlantingPoint__isUsed"],
                                p["_PlantingPoint__pantKind"],
                                p["_PlantingPoint__pantingDate"])
                    for p in fileRead["palntingPoints"]
                ]
        self.palntingPoints=pointsLoad
    #endregion

    #region manage greenhouse
    def createPoints(self):
        '''this is called when a greenhouse is created on first load'''
        self.palntingPoints = [PlantingPoint(i) for i in range(1,501)]

    def harvestPlants(self)->dict: #loop on planting points and call harvestPlant() in PlantingPoint
        '''loops on all planting point and those that were harvested.\n
        will count how many of each kind was harvested'''
        harvested={k:0 for k in Plant.kindsList}
        for pp in self.palntingPoints:
            kind=pp.pantKind
            if pp.harvestPlant():
                harvested[kind]+=1
        self.updateJson()
        return harvested


    def clearGreenhouse(self): #call on each plantingpoint removePlant() from PlantingPoint
        for pp in self.palntingPoints:
            pp.removePlant()
        self.updateJson()
    
    def removePlant(self,kind):
        hasChanges=False
        for pp in self.palntingPoints: 
            if pp.pantKind==kind:
                pp.removePlant()
                hasChanges=True
        if hasChanges: self.updateJson()
    #endregion

    def updateJson(self): #on each change in the greenhouse call this
        gh=copy.deepcopy(self)
        tmp=gh.__dict__
        for i,p in enumerate(tmp["palntingPoints"]):
            tmp["palntingPoints"][i]=p.__dict__

        with open(f"greenhouses/{self.greenhousID}.json","w") as f:
            json.dump(tmp,f,indent=4)

        


