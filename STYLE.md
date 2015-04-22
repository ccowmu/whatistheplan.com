WhatIsThePLAN.com Style Guide
=============================
Developing in a group project is easier and simpler if everybody can agree on a simple and consistent convention
for coding standards. Because of its wide acceptance in the python community and good documentation, we have
decided to follow the PEP8 standard. To that end we use a python module named pylint that will scan the code
repository and determine if there are any PEP8 violations. Certain lines and files may be ignored by pylint if and
only if the violation is directly caused by a django convention or standard.

Running Pylint
--------------
A make target named `lint` has been set up to make running pylint simple and easy. Simply run the command:
```
make lint
```
Any violations should be explained by the output of pylint. Any confusing messages can be looked up in the
[pylint docs](http://docs.pylint.org/features.html).

Team Preferences
----------------
Aside from the PEP8 conventions, any
other coding style preferences follow here.

### Line Length
Pylint will not fail a line unless it is above 100 characters, however we prefer to keep lines shorter than 80
characters where possible.

###Long Argument Lists
Long argument lists that cause lines to be long can be broken into multiple lines. If that is the case we prefer
that the following form be used

```python
function_name(
    argument1,
    argument2,
    argument3,
    {
        "key1": "value1",
        "key2": "value2"
    }
)
```
