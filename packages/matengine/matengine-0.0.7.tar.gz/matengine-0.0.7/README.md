# MatEngine

MatEngine is a Python library designed for the engineering and scientific community focused on materials science. When fully developed, it will facilitate material discovery through micro to macrostructural generation and characterisation through simulation.

# Features:
- Material Generation: Tools to generate material structures at various scales
  - random field generation
  - plurigaussian simulation
  - plotting functionality

*NB: MatEngine is currently in development, and as such, the feature list will continue to be updated*

# Quick Start

Below is an example of how to generate a discrete two-phase structure with plurigaussian simulation

```python
from matengine.generation.generators import random_field, create_covariance_model
from matengine.generation.decisiontree import decision_tree, ellipse
from matengine.generation.plurigaussian import plurigaussian_simulation
from matengine.utils.plotting import array_to_vtk

dim = [50,50]
ls=5
var=1
kernel = 'gau'
seed1 = 123
seed2 = 1234
mdl = create_covariance_model(kernel, dim, var, ls)
z1 = random_field(mdl, dim, seed=seed1)
z2 = random_field(mdl, dim, seed=seed2)
fields = [z1, z2]

Config = {
    'root': {
        'type': 'decision',
        'func': ellipse,
        'args': {
            'key1': 'Z1',
            'key2': 'Z2',
            'cx': 0,
            'cy': 0,
            'sx': 2.6,
            'sy': 0.3
        },
        'yes_branch': 'phase1',
        'no_branch': 'phase0'
    },
    'phase0': {
        'type': 'leaf',
        'action': 0
    },
    'phase1': {
        'type': 'leaf',
        'action': 1
    },
}

tree_config = Config

tree = decision_tree()
tree.build_tree(tree_config)

L, P = plurigaussian_simulation(dim, tree, fields, ldim=500)

array_to_vtk(L, 'L')
array_to_vtk(P, 'P')
```

# Documentation
Coming soon ...

# License
MatEngine is made available under the MIT License, allowing for liberal reuse and modification for both academic and commercial purposes.

# Contact
For support, feedback, or inquiries, please contact via email: rickettse1@cardiff.ac.uk