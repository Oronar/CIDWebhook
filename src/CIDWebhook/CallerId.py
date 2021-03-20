class CallerId:
    __instance__ = None

    def __init__(self):
        if CallerId.__instance__ is None:
            CallerId.__instance__ = self
        else:
            raise Exception("This class is singleton")
        
        self.Date = None
        self.Time = None
        self.Number = None
        self.Name = None

    @staticmethod
    def getInstance():
        if not CallerId.__instance__:
            CallerId()
        return CallerId.__instance__

    def getId(self):
        return f"{self.Name} - {self.Number}"