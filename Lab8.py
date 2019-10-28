#Jonathan Kelly, Jonathan.kelly2@marist.edu
# Get temps and adds to cooling or heating degree days 

def main():
    
    x = int(input("How many days do you want to enter:"))
    degree = [0] * x
    
    heating = 0
    cooling = 0
    
    for i in range(x):
        degree[i] = int(input("Enter next degree day: "))
        
    for i in degree:
        if(i < 60):
            heating = heating + (60 - i)
        
        elif(i > 80):
            cooling = cooling + (i - 80)
            
    print("Cooling degree days:", cooling, "Heating degree days:", heating)
    
main()