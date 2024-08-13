input_data = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11",
]

worker_hours_map = {}

for record in input_data:
    name, hours = record.rsplit(" ", 1)
    hours = int(hours)
    
    if name in worker_hours_map:
        worker_hours_map[name].append(hours)
    else:
        worker_hours_map[name] = [hours]

for name, hours in worker_hours_map.items():
    total_hours = sum(hours)
    hours = ", ".join(map(str, hours))
    print(f"{name}: {hours}; sum: {total_hours}")
