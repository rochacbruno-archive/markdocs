#! /usr/bin/python
"""This is the regular module __doc__"""

"""!
# this is a documentation written in markdown
As it has only one `!` at the top, it is considered the module documentation
I can include module documentation along the file and will be merged in to the
top level documentation
"""

from os import path  # this comment is ignored

"""!!
# This is an object documentation
can be used for any object but most for functions and classes
It is defined before the object and not on the `__doc__` docstring, as markdocs
does not conflicts with it.

## What are the advantages
- Markdown is easy to learn
- More people will contribute to documentation because they already know the
  format
- With simple commands like `markdocs /path --readme README.md` the readme for
  your repo is generated from markdocs
- Markdocs will generate the output for http://www.mkdocs.org/
- You can write bare `.md` files in a `mdocs` folder and they will be added to
  you documentation as well

[[params
  # x is the single param of this function
  x: int | default 0
  # The return is a string with the x interpolated.
]] result: str
"""
@foo_bar  # this decorator is listed as part of function in docs (maybe linked)
def a_function(x=0):
    """This regular docstring does not conflicts with the above markdoc"""
    return f'Hello {x}'

"""!!
# This is a class documentation
We can also define runnable and highlighted blocks of code.
```run
obj = MyClass()
```
"""
class MyClass:
    """the class docstring is not affected"""
    attr = 'foo'
    """!!!
    # this is a method documentation
    [[params
      x: str
    ]]
    """
    @bla_bla_bla
    def method(self, x):
        """This is the regular docstring for method"""
        a = x
        """!!!!
        ## Here we increase the nesting level
        Markdown is amazing!
        """
        def inner_function(..):
            pass

    # This comment is ognored

"""!
> This is also the module documentation, will be included as a foot note
"""
