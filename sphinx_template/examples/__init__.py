"""
This is the Example module, 

It contains various function, plotting graphs and containing information useful
to see how Sphinx, and Sphinx-Gallery behave when you deploy documentation.
"""



# we provide version_info as a tuple, because on Major version bump, 
# alphabetical ordering may be wrong !
# '10.0.0' < '9.0.0'

version_info = (0, 0, 5)
__version__ = '.'.join([str(x) for x in version_info])



def add_with_saturation_bad(a, b, c=10):
    """
    add_with_saturation add with saturation
    """
    return min(a+b, c)



