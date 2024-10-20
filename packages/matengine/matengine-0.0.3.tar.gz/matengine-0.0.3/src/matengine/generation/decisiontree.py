import numpy as np

class decision_tree:
    def __init__(self):
        self.tree = None
    
    def build_tree(self, instructions):
        nodes = {}
        for node_id, details in instructions.items():
            if details['type'] == 'decision':
                nodes[node_id] = self.DecisionNode(
                    func=details['func'],
                    args=details['args']
                )
            elif details['type'] == 'leaf':
                nodes[node_id] = self.LeafNode(details['action'])
        for node_id, details in instructions.items():
            if details['type'] == 'decision':
                nodes[node_id].yes_branch = nodes.get(details.get('yes_branch'))
                nodes[node_id].no_branch = nodes.get(details.get('no_branch'))
        self.tree = nodes['root']  # Assuming 'root' is the entry point defined in your instructions

    def decide(self, data):
        if self.tree:
            return self.tree.decide(data)
        else:
            raise ValueError("The decision tree has not been built yet.")

    class DecisionNode:
        def __init__(self, func, args, yes_branch=None, no_branch=None):
            self.func = func
            self.args = args
            self.yes_branch = yes_branch
            self.no_branch = no_branch

        def decide(self, data):
            if self.func(data, **self.args):
                return self.yes_branch.decide(data) if self.yes_branch else None
            else:
                return self.no_branch.decide(data) if self.no_branch else None

    class LeafNode:
        def __init__(self, action):
            self.action = action

        def decide(self, data):
            return self.action

def less_than(data, key, threshold):
    return data[key] <= threshold

def greater_than(data, key, threshold):
    return data[key] > threshold

def linear(data, key1, key2, m, c):
    return data[key2] - m*data[key1] - c >= 0

def ellipse(data, key1, key2, cx, cy, sx, sy, angle=0):
    # Convert angle to radians
    angle_rad = np.radians(angle)
    
    # Extract point coordinates and center them
    x = data[key1] - cx
    y = data[key2] - cy
    
    # Apply rotation
    x_rot = x * np.cos(angle_rad) + y * np.sin(angle_rad)
    y_rot = -x * np.sin(angle_rad) + y * np.cos(angle_rad)
    
    # Check ellipse condition with rotated coordinates
    return (x_rot / sx) ** 2 + (y_rot / sy) ** 2 <= 1

def ellipsoid(data, key1, key2, key3, cx, cy, cz, sx, sy, sz):
    return ((data[key1]-cx)/sx)**2 + ((data[key2]-cy)/sy)**2 + ((data[key3]-cz)/sz)**2 <= 1
