import itertools

def tsp(cities, distances):
    shortest_distance = float('inf')
    shortest_route = None

    routes = itertools.permutations(cities)
    for route in routes:
        total_distance = 0

        for i in range(len(route)-1):
            current_city = route[i]
            next_city = route[i+1]
            total_distance += distances[current_city][next_city]

        
        total_distance += distances[route[-1]][route[0]]
        route = route + (route[0], )
        
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_route = route

    return shortest_route, shortest_distance

cities = ['C1', 'C2', 'C3', 'C4']
distances = {
    'C1': {'C2': 2, 'C3': 5, 'C4': 7},
    'C2': {'C1': 2, 'C3': 8, 'C4': 3},
    'C3': {'C1': 5, 'C2': 8, 'C4': 1},
    'C4': {'C1': 7, 'C2': 3, 'C3': 1},
}

tour, shortest_distance = tsp(cities, distances)
print(f"The shortest tour is {tour} with a total distance of {shortest_distance}.")
