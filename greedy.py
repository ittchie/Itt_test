def greedy(n, k, works):
    works = sorted(works, key=lambda work: work['size'], reverse=True)
    rooms = [list() for i in range(k)]
    for work in works:
        min_room_index = min(range(len(rooms)), key=lambda i: len(rooms[i]))
        rooms[min_room_index].append(work)
    return rooms
n = 5
k = 3
works = [{'size': 10}, {'size': 15}, {'size': 5}, {'size': 7}, {'size': 8}]
result = greedy(n, k, works)
for i, room in enumerate(result):
    print(f'ห้อง {i + 1}: {room}')
