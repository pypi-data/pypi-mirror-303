import networkx as nx
from typing import Dict, Union, List, Tuple
from modeltasks.log import logger


def get_root_nodes(graph: Union[nx.DiGraph, nx.MultiDiGraph]) -> List[str]:
    """
    Finds and returns the root nodes of a graph
    """
    return [n for n, d in graph.out_degree() if d == 0]


def get_end_leafes(graph: Union[nx.DiGraph, nx.MultiDiGraph]) -> List[str]:
    """
    Finds and returns the end_leaf nodes of a graph
    """
    return [n for n, d in graph.in_degree() if d == 0]


def get_node_neighbors(graph: Union[nx.DiGraph, nx.MultiDiGraph], node: str) -> List[str]:
    """
    Returns all neighbors of a graph node
    """
    return [n for n in graph.neighbors(node)]


def get_direct_node_predecessors(graph: Union[nx.DiGraph, nx.MultiDiGraph], node: str) -> List[Tuple[str, str]]:
    """
    Returns all inbound predecessor nodes for a given node
    """
    return graph.in_edges(node)


def get_direct_node_successors(graph: Union[nx.DiGraph, nx.MultiDiGraph], node: str) -> List[Tuple[str, str]]:
    """
    Returns all outbound predecessor nodes for a given node
    """
    return graph.out_edges(node)


def is_start_node(graph: Union[nx.DiGraph, nx.MultiDiGraph], node: str) -> bool:
    """
    Returns `True`if a node has no predecessors.
    """
    return len(get_direct_node_predecessors(graph, node)) == 0


def is_end_node(graph: Union[nx.DiGraph, nx.MultiDiGraph], node: str) -> bool:
    """
    Returns `True`if a node has no predecessors.
    """
    return len(get_direct_node_successors(graph, node)) == 0


def sort_topologically_parallel(graph: Union[nx.DiGraph]) -> List[List]:
    graph_copy = graph.copy()
    sequence = []
    while graph_copy:
        zero_in = [v for v, d in graph_copy.in_degree() if d == 0]
        sequence.append(zero_in)
        graph_copy.remove_nodes_from(zero_in)
    return sequence


def sort_topologically(graph: Union[nx.DiGraph, nx.MultiDiGraph]) -> List:
    """
    Returns a flat topologically sorted list of graph nodes
    """
    try:
        return list(nx.topological_sort(graph))
    except nx.NetworkXError:
        logger.error(f'Cannot sort graph topologically (Graph not directed)')


def hierarchical_position(
    graph: nx.DiGraph,
    root: str,
    levels: Dict = None,
    width: float = 1.0,
    height: float = 1.0
):
    """
    Calculates a hierarchical tree-like positioning for a given graph node in a directed graph
    """

    total = "total"
    current = "current"

    graph = graph.reverse()

    def make_levels(
        levels,
        node: str = root,
        current_level: int = 0,
        parent_node: str = None
    ):
        # Get number of nodes at each hierarchy level
        if current_level not in levels:
            levels[current_level] = {total: 0, current: 0}
        levels[current_level][total] += 1
        neighbors = [n for n in graph.neighbors(node)]
        for neighbor in [n for n in neighbors if n != parent_node]:
            levels = make_levels(
                levels,
                node=neighbor,
                current_level=current_level + 1,
                parent_node=node
            )
        return levels

    def make_position(
        position,
        node: str = root,
        current_level: int = 0,
        parent_node: str = None,
        vertical_location: int = 0
    ):
        dx = 1 / levels[current_level][total]
        left = dx / 2
        position[node] = ((left + dx * levels[current_level][current]) * width, vertical_location)
        levels[current_level][current] += 1
        neighbors = [n for n in graph.neighbors(node)]
        for neighbor in [n for n in neighbors if n != parent_node]:
            position = make_position(
                position,
                node=neighbor,
                current_level=current_level + 1,
                parent_node=node,
                vertical_location=vertical_location-vertical_gap
            )
        return position

    if levels is None:
        levels = make_levels({})
    else:
        levels = {l: {total: levels[l], current: 0} for l in levels}

    vertical_gap = height / (max([l for l in levels]) + 1)

    return make_position({})
