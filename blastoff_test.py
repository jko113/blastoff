from blastoff import blast
        
while True:
        
    counter = input("Time to countdown!\nEnter a number <= 20: ")
    try:
        counter = int(counter)
    except:
        print("not a valid integer")
        continue
    
    if counter > 20:
        print("too large. enter something smaller")
    elif counter < 1:
        print("too small. enter something bigger")
    else:
        break
    
blast(counter)