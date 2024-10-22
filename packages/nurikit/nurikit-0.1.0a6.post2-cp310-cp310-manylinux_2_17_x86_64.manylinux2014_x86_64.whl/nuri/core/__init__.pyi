"""

The core module of NuriKit.

This module contains the core classes of NuriKit. The core module is not
very useful by itself, but is a dependency of many other modules. Chemical
data structures, such as elements, isotopes, and molecules, and also the
graph structure and algorithms, are defined in this module.
"""
from __future__ import annotations
from nuri.core._core import Atom
from nuri.core._core import AtomData
from nuri.core._core import Bond
from nuri.core._core import BondData
from nuri.core._core import BondOrder
from nuri.core._core import Element
from nuri.core._core import Hyb
from nuri.core._core import Isotope
from nuri.core._core import Molecule
from nuri.core._core import Mutator
from nuri.core._core import Neighbor
from nuri.core._core import PeriodicTable
from nuri.core._core import ProxySubAtom
from nuri.core._core import ProxySubBond
from nuri.core._core import ProxySubNeighbor
from nuri.core._core import ProxySubstructure
from nuri.core._core import SubAtom
from nuri.core._core import SubBond
from nuri.core._core import SubNeighbor
from nuri.core._core import Substructure
from nuri.core._core import SubstructureCategory
from nuri.core._core import SubstructureContainer
from . import _core
__all__: list = ['Molecule', 'Mutator', 'Atom', 'Bond', 'Neighbor', 'SubstructureContainer', 'Substructure', 'SubAtom', 'SubBond', 'SubNeighbor', 'Element', 'Isotope', 'PeriodicTable', 'Hyb', 'BondOrder', 'SubstructureCategory', 'AtomData', 'BondData']
periodic_table: _core.PeriodicTable  # value = <nuri.core._core.PeriodicTable object>
