from datetime import datetime
from Plant import Plant


class PlantingPoint:
    def __init__(self,pointId,isUsed=False,pantKind=None,pantingDate=None):
        self.isUsed=isUsed
        self.pantKind=pantKind
        self.pantingDate=pantingDate
        self.pointId=pointId

    #region getters and setters
    def __setPointid(self,pointId):
        self.__pointId=pointId

    def __getPointid(self):
        return self.__pointId
    pointId=property(__getPointid,__setPointid)

    def __setPantingdate(self,pantingDate):
        self.__pantingDate=pantingDate

    def __getPantingdate(self):
        return self.__pantingDate
    pantingDate=property(__getPantingdate,__setPantingdate)

    def __setPantkind(self,pantKind):
        self.__pantKind=pantKind

    def __getPantkind(self):
        return self.__pantKind
    pantKind=property(__getPantkind,__setPantkind)

    def __setIsused(self,isUsed):
        self.__isUsed=isUsed

    def __getIsused(self):
        return self.__isUsed
    isUsed=property(__getIsused,__setIsused)
    #endregion

    def enterPlant(self,kind)->bool: 
        if self.isUsed==False:
            self.pantKind=kind
            self.pantingDate=datetime.now().strftime("%d-%m-%Y")
            self.isUsed=True
            return True

        return False
    
    def harvestPlant(self)->bool:
        if self.isUsed == True:
            if self.checkHarvesable():
                self.pantKind=None
                self.pantingDate=None
                self.isUsed=False
                return True
        return False
            
    def removePlant(self):
        self.pantKind=None
        self.pantingDate=None
        self.isUsed=False
        return True

    def checkHarvesable(self):
        if self.isUsed == False: return False
        diff=abs(datetime.strptime(self.pantingDate,"%d-%m-%Y")-datetime.now())
        return diff.days>=Plant.growTimeByKind(self.pantKind)