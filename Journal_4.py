#define main program
def main():     
#Classification/Parameter                 
    BlueWhale = {                       
        "name"      :    "BlueWhale",
        "arm_L"     :    65.7,     #inches
        "leg_L"     :    0.0,   #inches
        "eyes"      :    2,
        "tail"      :    True,    
        "furry"     :    False     
    }

#prints 
    print("Favorite animal:",BlueWhale["name"])
    print("\nArm length (in):",BlueWhale["arm_L"])
    print("Leg length (in):",BlueWhale["leg_L"])
    print("Number of eyes:",BlueWhale["eyes"])
    print("Has tail:",BlueWhale["tail"])
    print("Is furry:",BlueWhale["furry"])


#final main function run
if __name__ == "__main__":
    main()
