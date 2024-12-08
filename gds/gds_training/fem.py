import logging
import sys

import gdsfactory as gf
import matplotlib.pyplot as plt
from femwell.maxwell.waveguide import compute_modes
from femwell.visualization import plot_domains
from gdsfactory.generic_tech import LAYER_STACK, get_generic_pdk
from gdsfactory.technology import LayerStack
from gplugins.gmsh import get_mesh
from rich.logging import RichHandler
from skfem import Basis, ElementTriP0
from skfem.io.meshio import from_meshio

gf.config.rich_output()
PDK = get_generic_pdk()
PDK.activate()

logger = logging.getLogger()
logger.removeHandler(sys.stderr)
logging.basicConfig(level="WARNING", datefmt="[%X]", handlers=[RichHandler()])