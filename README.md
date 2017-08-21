# markdocs
Extract markdown from Python source file comments and outputs structured documentation &amp; README file.

# Python documentation

I'm enjoying writing functional documentation using __Markdown__ in __Rustlang__, so I'll do experiments to have the same functionality in Python.  Take a look at [rustdoc](https://doc.rust-lang.org/book/first-edition/documentation.html) and [here an example](https://doc.rust-lang.org/rand/rand/index.html) of documentation site generated for a Rust crate using [markdown comments](https://doc.rust-lang.org/rand/src/rand/lib.rs.html#11-1288).

Information is extracted using `python -m tokenize file.py` https://docs.python.org/3.5/library/tokenize.html#examples

[Markdown](http://commonmark.org/help/)

## How it works

> NOTE: this is just an early stage idea, not implemented yet! if you like please comment.

The _Markdocs_ extracts documentation from all _.py_ files and outputs in a well organized documentation _html_ site which can use the mkdocs.org to expose and deploy.

```bash
markdocs /path/to/project
```

If you dont want to generate full documentation you can easily generate a readme file for your repo

```bash
markdocs /path/project --readme README.md -k 'filter-oly-some-files-and-objects'
```

With the above a `README.md` is generated including only the filtered files and objects documentation, but you can also generate a single README for your whole project.


All `.py` files on that folder will be parsed for documentation blocks which are Python multiline comments starting in `!` example:

> NOTE: if you don't like mixing code and documentation, you can use a `mymodule.md` to document `mymodule.py` and the `.md` should be located in the same folder or in `mdocs` folder of the project. You can also write separated object files like in `mymodule.myclass.mymethod.md` which will be linked only to the `mymethod` of `MyClass`.

```python
    """!
    # this is a documentation written in markdown
    As it has only one `!` at the top, it is considered the module documentation
    I can include module documentation along the file and will be merged in to the top level documentation
    """
    
    from foo import bar
    
    """!!
    # This is an object documentation, can be used for any object but most for functions and classes
    It is defined before the object and not on the `__doc__` docstring, as markdocs does not conflicts with it.
    
    ## What are the advantages
    - Markdown is easy to learn
    - More people will contribute to documentation because they already know the format
    - With simple commands like `markdocs /path --readme README.md` the readme for your repo is generated from markdocs
    - Markdocs will generate the output for http://www.mkdocs.org/
    - You can write bare `.md` files in a `mdocs` folder and they will be added to you documentation as well
    
    [[params
      # X is the single param of this function
      x: int | default 0
      # The return is a string with the x interpolated.
    ]] result: str
    """
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
        def method(self, x):
            """This is the regular docstring for method"""
            a = x
            """!!!!
            ## Here we increase the nesting level
            Markdown is amazing!
            """
            def inner_function(..):
                pass
```     
 
As you can see the `!!` can be also used, in fact you can use as many `!!!!!` you want to define nesting.

Parser options are:

- https://github.com/miyuchina/mistletoe/
- https://github.com/lepture/mistune#lexers

Website output formats

- mkdocs.org
- https://github.com/rocadocs/rocadocs

more on https://gist.github.com/rochacbruno/1689c849f3ef54086772c410d77a82de
