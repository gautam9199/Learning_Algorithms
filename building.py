
def main():
    building = [3,5,4,6,8,2]

    AreaList =[]

    for x , y in enumerate (building):
        counterLeft = 0
        counterRight =0
        
        if x == 0:
          counterRight =  CountRight(x, building,counterRight)
          
        elif x == len(building) -1:
            counterLeft = CountLeft(x, building,counterLeft)
        
        else:
             
            counterRight = CountRight(x, building,counterRight)
           
            counterLeft = CountLeft(x, building,counterLeft)
       
        AreaList.append(y * (counterLeft + counterRight + 1))
   
    print(AreaList)   
    print(max(AreaList))
    
    return max(AreaList)



def CountLeft(x, building, countL):
    
    current = building[x]

    
    while x > 0 :
        nextPos = x-1
        if x != 0 and current <= building[nextPos]  :
            countL = countL+ 1
            x = x-1
            
        else:
            return countL
    return countL
   

def CountRight(x, building, countR):
    
    current = building[x]
    
    while x < len(building) -1:
        nextPos = x+1
        if x != len(building) and current <= building[nextPos]:
            countR = countR + 1
            x +=1
            
        else:
            return countR
    return countR
    

main()