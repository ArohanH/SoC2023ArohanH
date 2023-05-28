import numpy as np
Capital=10
def gameA():
    toss=np.random.randint(0,1000)
    if toss<=504 and toss>=0:
        return -1;
    else:
        return 1;
def gameB():
    if Capital%3==0:
        chance=np.random.randint(0,10)
        if chance<=8 and chance>=0:
            return -1
        else:
            return 1;
    else:
        chance=np.random.randint(0,4)
        if chance<=2 and chance>=0:
            return 1
        else:
            return -1;
if __name__ == "__main__":
    for i in range(10):
            print(" Current Capital: ", Capital)
            choice = input("Enter A for Game A and B for Game B: ")
            if choice == 'A' or choice == 'a':
                Capital += gameA()
            elif choice == 'B' or choice == 'b':
                Capital += gameB()
            else:
                print("Invalid choice")
                break
    print("Final Capital: ", Capital)
    
