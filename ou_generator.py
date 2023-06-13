import csv
import random

def random_word():
    """Choose a random word from a list of Cyrillic words."""
    with open("wordlist_full.txt", "r", encoding="utf-8") as f:
        words = f.readlines()
    return random.choice(words).strip()


class OrganizationalUnit:
    def __init__(self, name, depth, max_depth, parent=None):
        self.name = name
        self.parent = parent
        self.depth = depth
        self.max_depth = max_depth
        self.children = []

        # Recursively generate children with decreasing probability for each depth level
        if depth < max_depth - 1 and random.random() < 0.7:
            num_children = random.randint(1, 2)
            for i in range(num_children):
                child = OrganizationalUnit(random_word(), depth + 1, max_depth, parent=self)
                self.children.append(child)

    def flatten(self):
        """Return a flattened version of this OrganizationalUnit as a dictionary."""
        flattened = {"Name": self.name}

        # Add parent names for up to max_depth levels
        for i in range(1, self.max_depth):
            if i < len(self.ancestors) + 1:
                flattened[f"Parent {i}"] = self.ancestors[-i].name
            else:
                flattened[f"Parent {i}"] = ""

        return flattened

    @property
    def ancestors(self):
        """Return a list of ancestors of this OrganizationalUnit up to the root node."""
        ancestors = []
        if self.parent:
            ancestors.extend(self.parent.ancestors)
            ancestors.append(self.parent)
        return ancestors


def generate_organization_structure(root_name, num_children, max_depth, current_depth=0):
    """Generate a random organizational unit structure."""
    root = OrganizationalUnit(root_name, current_depth, max_depth)
    open_nodes = [root]

    # Generate up to num_children children per node until max_depth is reached
    while current_depth < max_depth:
        next_depth = []
        for node in open_nodes:
            num_children = random.randint(1, num_children)
            for i in range(num_children):
                child = OrganizationalUnit(random_word(), current_depth + 1, max_depth, parent=node)
                node.children.append(child)
                next_depth.append(child)
        current_depth += 1
        open_nodes = next_depth

    return root


def write_csv(filename, root):
    """Write the organizational unit structure to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Name"] + [f"Parent {i}" for i in range(1, root.max_depth)]
        writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
        writer.writeheader()

        # Flatten all nodes and write as CSV rows
        open_nodes = [root]
        while open_nodes:
            node = open_nodes.pop(0)
            writer.writerow(node.flatten())
            open_nodes.extend(node.children)


if __name__ == "__main__":
    num_children = 3
    max_depth = 5
    structure = generate_organization_structure("ROOT", num_children, max_depth)
    write_csv("ou_structure.csv", structure)