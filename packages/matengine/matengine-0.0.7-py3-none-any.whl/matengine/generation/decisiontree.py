import numpy as np

class decision_tree:
    """
    A class to represent a decision tree for making decisions based on user-defined criteria.
    """
    def __init__(self):
        """
        Initialize the decision tree with an empty structure.
        """
        self.tree = None
    
    def build_tree(self, instructions):
        """
        Build a decision tree based on the given instructions.

        Parameters:
            instructions: dict 
                A dictionary containing details about the nodes, including type, function, arguments, and branches.
        
        Notes:
            - Nodes can be either decision nodes or leaf nodes.
            - The 'root' node is assumed to be the starting point.
        """
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
        """
        Make a decision using the decision tree.

        Parameters:
            data: dict
                The input data used for making a decision.

        Returns:
            The action to be taken as per the leaf node reached.
        
        Raises:
            ValueError: If the decision tree has not been built yet.
        """
        if self.tree:
            return self.tree.decide(data)
        else:
            raise ValueError("The decision tree has not been built yet.")

    class DecisionNode:
        """
        A class to represent a decision node in the decision tree.
        """
        def __init__(self, func, args, yes_branch=None, no_branch=None):
            """
            Initialize a decision node.

            Parameters:
                func: function
                    The function used to evaluate the decision.
                args: dict
                    Arguments required by the function.
                yes_branch: DecisionNode or LeafNode, optional
                    The branch to follow if the decision is True.
                no_branch: DecisionNode or LeafNode, optional 
                    The branch to follow if the decision is False.
            """
            self.func = func
            self.args = args
            self.yes_branch = yes_branch
            self.no_branch = no_branch

        def decide(self, data):
            """
            Make a decision at this node based on the input data.

            Parameters:
                data: dict
                    The input data used for making a decision.

            Returns:
                The action or next node based on the function's evaluation.
            """
            if self.func(data, **self.args):
                return self.yes_branch.decide(data) if self.yes_branch else None
            else:
                return self.no_branch.decide(data) if self.no_branch else None

    class LeafNode:
        """
        A class to represent a leaf node in the decision tree.
        """
        def __init__(self, action):
            """
            Initialize a leaf node.

            Parameters:
                action: 
                    The action to be returned when this leaf node is reached.
            """
            self.action = action

        def decide(self, data):
            """
            Return the action associated with this leaf node.

            Parameters:
                data: dict 
                    The input data used for making a decision.

            Returns:
                The action stored in this leaf node.
            """
            return self.action

def less_than(data, key, threshold):
    """
    Determine if the value in the data is less than or equal to the threshold.

    Parameters:
        data: dict
            The input data.
        key: str
            The key whose value is being compared.
        threshold: numeric
            The threshold value.

    Returns:
        bool: 
            True if the value is less than or equal to the threshold, False otherwise.
    """
    return data[key] <= threshold

def greater_than(data, key, threshold):
    """
    Determine if the value in the data is greater than the threshold.

    Parameters:
        data: dict
            The input data.
        key: str
            The key whose value is being compared.
        threshold: numeric
            The threshold value.

    Returns:
        bool: 
            True if the value is greater than the threshold, False otherwise.
    """
    return data[key] > threshold

def linear(data, key1, key2, m, c):
    """
    Determine if the value lies on or above the line defined by the equation y = mx + c.

    Parameters:
        data: dict
            The input data.
        key1: str
            The key representing the x-value.
        key2: str` 
            The key representing the y-value.
        m: float 
            The slope of the line.
        c: float 
            The y-intercept of the line.

    Returns:
        bool: 
            True if the point is on or above the line, False otherwise.
    """
    return data[key2] - m*data[key1] - c >= 0

def ellipse(data, key1, key2, cx, cy, sx, sy, angle=0):
    """
    Determine if a point lies inside or on the boundary of an ellipse.

    Parameters:
        data: dict
            The input data.
        key1: str 
            The key representing the x-coordinate of the point.
        key2: str 
            The key representing the y-coordinate of the point.
        cx: float 
            The x-coordinate of the ellipse center.
        cy: float 
            The y-coordinate of the ellipse center.
        sx: float 
            The semi-axis length in the x-direction.
        sy: float 
            The semi-axis length in the y-direction.
        angle: float, optional
            The rotation angle of the ellipse in degrees. Default is 0.

    Returns:
        bool: 
            True if the point lies within or on the ellipse, False otherwise.
    """
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
    """
    Determine if a point lies inside or on the boundary of an ellipsoid.

    Parameters:
        data: dict
            The input data.
        key1: str 
            The key representing the x-coordinate of the point.
        key2: str 
            The key representing the y-coordinate of the point.
        key3: str 
            The key representing the z-coordinate of the point.
        cx: float 
            The x-coordinate of the ellipsoid center.
        cy: float 
            The y-coordinate of the ellipsoid center.
        cz: float 
            The z-coordinate of the ellipsoid center.
        sx: float 
            The semi-axis length in the x-direction.
        sy: float 
            The semi-axis length in the y-direction.
        sz: float 
            The semi-axis length in the z-direction.

    Returns:
        bool: 
            True if the point lies within or on the ellipsoid, False otherwise.
    """
    return ((data[key1]-cx)/sx)**2 + ((data[key2]-cy)/sy)**2 + ((data[key3]-cz)/sz)**2 <= 1
