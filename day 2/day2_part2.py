total_invalid_sum = 0  #Counter

with open("id.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",") #strip to avoid unwanted spaces, and split to have ranges for ID
        for r in ranges:
            parts = r.split("-") #split in to the start and end of the range to we need 
            start = int(parts[0])
            end = int(parts[1])
            for i in range(start, end + 1):
                id_str = str(i) #convert number into string so we can use built in function len()
                total_len = len(id_str)
                is_invalid = False
                for chunk_len in range(1, (total_len // 2) + 1):
                    if total_len % chunk_len == 0:
                        pattern = id_str[:chunk_len]
                        num_repeats = total_len // chunk_len
                        if pattern * num_repeats == id_str:
                            is_invalid = True
                            break
                if is_invalid:
                    total_invalid_sum += i

print(total_invalid_sum)