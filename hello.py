print("hello")
class person:
    __name = ''
    __year = 0
    __age = 0

    def __init__(self,name,year):
        self.__name = name
        self.__year = year

    def getName(self):
        return self.__name

    def getYear(self):
        return self.__year

    def getAge(self):
        return self.__year+1

p = person('lujun',20)
print(p.getName())
print(p.getYear())
print(p.getAge())