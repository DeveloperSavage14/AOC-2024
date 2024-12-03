with open('Day2.txt', 'r') as f:
    total = 0
    dec = False
    rise = False
    for line in f:
        arr1 = line.strip()
        arr1 = [int(num) for num in line.strip().split()]
        looptime = 0
        failed = False
        for i in range(len(arr1)):
            looptime += 1    
            if arr1[0] == arr1[1]:
                failed = True
            if int(arr1[0]) < int(arr1[1]):
                rise = True
            elif int(arr1[0]) > int(arr1[1]):
                dec = True
            else:
                break
            if looptime < len(arr1) and failed == False:
                if rise == True: 
                    x = int(arr1[i+1]) - int(arr1[i])
                    if x < 1 or x > 3:
                        rise = False
                        failed = True
                        
                if dec == True:
                    x = int(arr1[i]) - int(arr1[i+1])
                    if x < 1 or x > 3:
                        dec = False
                        failed = True
                if x == 0:
                    failed = True
        if failed == False:
            total = total + 1
            print(arr1)
            rise = False
            dec = False
    print(total)



