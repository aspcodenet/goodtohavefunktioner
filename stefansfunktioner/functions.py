def getInputBetween(startval: int,endval: int)->int:
    while True:
        try:
            val=int(input("Mata in:"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except:
            print("Ange ett tal tack!")

def getBestPlayer()->str:
    return "Mats Sundin"

if __name__ == "__main__":
    x = getInputBetween(100,200)            
    print(x)