# Update package resources to account for version changes.
import importlib, pkg_resources
importlib.reload(pkg_resources)

import tensorflow as tf
import tensorflow_quantum as tfq

import cirq
import sympy
import numpy as np

# visualization tools
%matplotlib inline
import matplotlib.pyplot as plt
from cirq.contrib.svg import SVGCircuit
