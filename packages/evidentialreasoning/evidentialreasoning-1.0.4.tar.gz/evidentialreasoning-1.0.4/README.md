Python implementations evidential reasoning (ER) approach

## Installation:
### Using pip: 
```shell
pip install evidentialreasoning
```
##Example:
```shell

import numpy as np
from evidentialreasoning.ER import *

input = np.array([[0,0,0.2,0.2,0.6,0],[0,0,0.2,0.4,0.4,0],[0,0,0.2,0.8,0,0],[0,0,0.4,0.2,0.4,0]])
weights = np.array([0.25,0.25,0.25,0.25])
a = ER_Aggregation(input,weights)
print(a)
b = ER_Normaliation(a)
print(b)

```
*To be updated*
