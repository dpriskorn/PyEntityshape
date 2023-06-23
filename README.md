# PyEntityshape
Python library to lookup Wikidata items in the entityshape API.

This is the alpha software. Please open an issue if you have any ideas or suggestions or bugs to report.  

# Features
* validate one item at a time (the API has no batch support).
* determine whether an item is valid according to a certain schema or not

# Installation
Get it from pypi

`$ pip install pyentityshape`

# Usage
Example:
```
e = EntityShape(eid="E1", lang="en", qid="Q1")
result = e.get_result()
result.is_valid
False|True
result.required_properties_that_are_missing
["P1", "P2"]
```

## Validation
The is_valid method on the Result object mimics all red warnings displayed by https://www.wikidata.org/wiki/User:Teester/EntityShape.js 

It currently checks these five conditions that all have to be false for the item to be valid:
1.  properties with too many statements found
2.   incorrect statements found
3.   some required properties are missing
4.   properties without enough correct statements found
5.   statements with properties that are not allowed found

# License
GPLv3+
