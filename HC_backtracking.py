import networkx as nx

def hamiltonian_circuits(graph, start_vertex):
    num_vertices = graph.number_of_nodes()
    all_hamiltonian_circuits = set()
    path = [None] * (num_vertices+1)

    def solve_hamiltonian_util(position):
        if position == num_vertices:
            if graph.has_edge(path[position - 1], path[0]):
                path[position] = path[0]
                all_hamiltonian_circuits.add(tuple(path))
            return

        for v in graph.nodes():
            if is_safe(v, position):
                path[position] = v
                solve_hamiltonian_util(position + 1)
                path[position] = None

    def is_safe(v, position):
        if not graph.has_edge(path[position - 1], v):
            return False

        if v in path[:position]:
            return False

        return True

    path[0] = start_vertex
    solve_hamiltonian_util(1)

    return list(all_hamiltonian_circuits)

g = nx.Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)

start_vertex = 0

all_circuits = hamiltonian_circuits(g, start_vertex)
if len(all_circuits):
    print("All Hamiltonian circuits found:")
    for circuit in sorted(all_circuits):
        print(circuit)
else:
    print("No Hamiltonian circuits found.")
