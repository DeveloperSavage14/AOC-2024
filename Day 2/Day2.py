with open('Day2.txt', 'r') as f:
    # Part 1
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


# Part 2
def is_safe_report(report):
    if len(report) < 2:
        return False  # A single-level report cannot be evaluated

    is_increasing = True
    is_decreasing = True

    for i in range(len(report) - 1):
        current_level = report[i]
        next_level = report[i + 1]
        difference = next_level - current_level

        if abs(difference) < 1 or abs(difference) > 3:
            return False

        if difference > 0:
            is_decreasing = False
        elif difference < 0:
            is_increasing = False
        else:
            return False

    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    
    return False

ans = 0

with open('Day2.txt', 'r') as f:
    for line in f:
        arr1 = [int(num) for num in line.strip().split()]
        
        if is_safe_with_dampener(arr1):
            ans += 1

print(f"Total safe reports with Problem Dampener: {ans}")
