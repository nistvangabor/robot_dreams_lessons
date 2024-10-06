playlist = ["I'm a barbie girl", "8 óra munka", "Autó egy szerpentinen", "Heavy is the crown"]

for id, song in enumerate(playlist):
    print(f"Playing {id+1}-{song}")
    #time.sleep(1)

print("--------------------------------------")
seating_chart = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Dexter", "Maria"],
    ["Grance", "Henry", "Harry"]            
]

for row_id, row in enumerate(seating_chart,1):
    for seat_id, guest in enumerate(row,1):
        print(f"{guest} sits in the {row_id}. row and the {seat_id}. seat")