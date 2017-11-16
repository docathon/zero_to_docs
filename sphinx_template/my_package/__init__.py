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

__all__ = ['plot_random_dots', 'trapezoid_integrate']

from .viz import plot_random_dots
from .trapezoid import trapzf as trapezoid_integrate



def export(function):
    global __all__
    __all__.append(function.__name__)
    return function


@export
def add_with_saturation_bad(a, b, c=10):
    """add_with_saturation add with saturation as 25 to avoid bug. Otherwise it does not work and crash later.
    """
    if c < 0:
        raise Exception('No.')
    return min(a+b, c)


@export
def add_with_saturation(a:int, b:int, *, high_water_mark:int=256):
    """Addition with a maximum threshold

    Parameters
    ----------

    a:int
    b:int
        number to add together

    high_water_mark:int[default to 256]
        Maximum value returned by the addition

    Returns
    -------

        Sum of ``a`` and ``b`` if lower than ``high_water_mark``.

    Raise
    -----
        ValueError or high_water_mark lower than ``10``

    See Also
    --------

        :func:`add_with_saturation_bad`

    """

    if high_water_mark < 0:
        raise ValueError('High water mark too low')
    return min(a+b, high_water_mark)

