from typing import List
from collections import defaultdict
import pandas as pd


def find_connected_components(pairs: List[tuple | list] | pd.DataFrame):
    """From a list of pairs, find all links. Uses the Depth-First Search algorithm."""

    # if the given pairs are in format of a dataframe, change it
    if isinstance(pairs, pd.DataFrame):
        pairs = pairs.values.tolist()

    # Create a graph using a dictionary
    graph = defaultdict(list)

    # Add edges to the graph
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = []

    # Helper function for DFS traversal
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    # Find all components
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components
