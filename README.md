# PyEntityshape
Python library to lookup Wikidata items in the entityshape API.

This is the alpha software. Please open an issue if you have any ideas or suggestions or bugs to report.  

# Features
It can be used programmatically to get the results of one validation at a time.

# Installation
Get it from pypi

`$ pip install pyentityshape`

# Usage
```
e = EntityShape(eid="E1", lang="en", qid="Q1")
result = e.get_result()
print(result)
```

# Caveat
It does not currently make any 
attempt to parse the result JSON object 
from the API.

# License
GPLv3+
