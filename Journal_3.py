#define function
def f(x):                
    return x**3 + 8      

#defining the integer
def main():              
    x = 9              
    print("f(x) = x**3 + 8\n\nWhen x =",x,", f(x) =",f(x))
    
#final results
    if f(x) > 27:
        print("\nYAY!")        
    else:
        print("\nOh No!") 

if __name__ == "__main__":
    main()
