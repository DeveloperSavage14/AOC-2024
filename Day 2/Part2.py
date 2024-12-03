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

print(ans)
