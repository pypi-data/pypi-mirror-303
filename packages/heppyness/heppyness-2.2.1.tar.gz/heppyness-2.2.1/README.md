# Heppy

Heppy provides pythonic data structures and a few high-level tools for high-energy physics. In particular, it provides very useful histogram classes that neatly integrate systematic variations (which, to my knowledge, no other histogram class that's widely used in HEP does) and support common operations such as addition, division, rebinning, slicing, projecting, integrating. It also provides flexible matplotlib-based plotting.

The documentation can be found [here](https://heppy.readthedocs.io).

This package also provides object conversion from and to ROOT histograms. Reading from ROOT is handled by [uproot](https://github.com/scikit-hep/uproot) and therefore doesn't depend on ROOT per se (i.e., you don't need to have [Py]ROOT installed). Converting to ROOT, however, is still done in PyROOT and thus requires a ROOT installation. This could also be ported to uproot at some point, get in touch if you need that.
