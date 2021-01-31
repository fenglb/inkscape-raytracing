"""
Module to describe and interact with a scene composed of various optical
objects
"""


import inkex


class World(object):
    """Stores a scene and computes the interaction with a ray"""

    def __init__(self, list_=None):
        if list_ is None:
            list_ = []
        self._objects = list(list_)

    def add_object(self, obj):
        self._objects.append(obj)

    def __iter__(self):
        return iter(self._objects)
        
    @property
    def num_objects(self):
        return len(self._objects)

    def propagate_beam(self, beam_seed):
        """Computes the propagation of a beam in the system

        :param beam_seed: The initial beam from which the light is produced.
        :type beam_seed: Ray
        :return: List of all the beam paths generated by this seed.
            It is stored as
            [path0[(Ray0, t0), (Ray1, t1), ...], path1[...], ...].
            Each path is a list of successive rays having each traveled by
            an amount :math:`t` before hitting an object.
        :rtype: list of list of tuple(Ray, float)
        """

        for object_ in self:
            inkex.utils.debug(object_.geometry.hit(beam_seed))
