import heapq
from collections import defaultdict

class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = {} 
    
    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance

def a_star_search(start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic[start][goal]

    while open_list:
        _, current = heapq.heappop(open_list)

        # If goal is reached, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        # Explore neighbors
        for neighbor, distance in current.neighbors.items():
            tentative_g_score = g_score[current] + distance

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor][goal]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

            # Debug output
            print(f"Exploring {current.name} -> {neighbor.name}, "
                  f"g(n): {tentative_g_score}, "
                  f"h(n): {heuristic[neighbor][goal]}, "
                  f"f(n): {f_score[neighbor]}")

    return None  # No path found

# Example usage:
station_A = Station("A")
station_B = Station("B")
station_C = Station("C")
station_D = Station("D")

# Define connections
station_A.add_neighbor(station_B, 5)
station_A.add_neighbor(station_D, 7)
station_B.add_neighbor(station_C, 3)
station_D.add_neighbor(station_C, 2)

# Define heuristic values
heuristic = {
    station_A: {station_C: 6, station_B: 5, station_D: 7},
    station_B: {station_C: 3, station_A: 5},
    station_D: {station_C: 2, station_A: 7},
    station_C: {station_C: 0}
}

# Find path from station_A to station_C
path = a_star_search(station_A, station_C, heuristic)
if path:
    print("Path found:", " -> ".join([station.name for station in path]))
else:
    print("No path found")
