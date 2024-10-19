"""
3x3 Ring - Geometry
===================
"""

from FiberFusing import Geometry, BackGround
from FiberFusing.fiber.catalogue import load_fiber, get_silica_index
from FiberFusing.configuration.ring import FusedProfile_03x03 as FusedProfile

wavelength = 1.55e-6

air = BackGround(index=1.0)

clad = FusedProfile(
    fiber_radius=62.5e-6,
    fusion_degree=0.5,
    index=get_silica_index(wavelength=wavelength)
)

fibers = [
    load_fiber('SMF28', wavelength=wavelength, position=core) for core in clad.cores
]

geometry = Geometry(
    background=air,
    additional_structure_list=[clad],
    x_bounds='centering',
    y_bounds='centering',
    resolution=350
)

_ = geometry.add_fiber(*fibers)

geometry.plot()

# -
