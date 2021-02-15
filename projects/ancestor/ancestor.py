from util import Stack

def earliest_ancestor(ancestors, starting_node):
    """
    Finds the earliest ancestor of a node
    """
    parent = -1
    relatives = Stack()
    visited = set()

    for pair in ancestors:
        if pair[1] == starting_node:
            if pair not in visited:
                relatives.push(pair)

    while relatives.size() > 0:
        current_pair = relatives.pop()
        parent = current_pair[0]

        for pair in ancestors:
            if pair not in visited:
                if pair[1] == parent:
                    relatives.push(pair)
                    visited.add(pair)

    return parent
