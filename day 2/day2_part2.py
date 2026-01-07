with open ("id.txt", "r") as file:
    som = 0
    for ranges in file:
        ranges = ranges.split(",")
        for parts in ranges:
            numbers = parts.split("-")
            start = int(numbers[0])
            end = int(numbers[1])
            for i in range(start, end + 1):
                s = str(i)
                if len(s) % 2 == 0:
                    midpoint = len(s) // 2
                    first_half = s[:midpoint]
                    second_half = s[midpoint:]
                    if first_half == second_half:
                        som += i
                 elif len(s) % 2 != 0:
                    som += 0
                    if s == s[0] * len(s):
                        som += i
    print(som)
