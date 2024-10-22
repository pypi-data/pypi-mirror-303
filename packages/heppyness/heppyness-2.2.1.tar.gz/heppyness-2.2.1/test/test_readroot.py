# Auxiliary modules
import numpy as np
from numpy.testing import assert_almost_equal as assert_approx
from os.path import join, dirname
import ROOT
import sys

# Module to be tested
sys.path.append(join(dirname(__file__), '..'))
import heppy


#
# Set up
#
testfile = join(dirname(__file__), 'example.root')
hist1d_path = 'root_histogram_1d_name'
hist2d_path = 'root_histogram_2d_name'
areas2d = np.array([[1., 5.],
       				[2., 6.],
       				[3., 7.],
       				[4., 8.]])
# Reference 2D ROOT histogram
reference_th2 = ROOT.TH2F('reference_th2', 'reference_th2', 4, -1.0, 1.0, 2, -1.0, 1.0)
# The zero padding is for the under-/overflows
reference_areas = np.transpose(np.array([
	[0., 0., 0., 0., 0., 0.],
	[0., 1., 2., 3., 4., 0.],
	[0., 5., 6., 7., 8., 0.],
	[0., 0., 0., 0., 0., 0.],]))
reference_area_errors = np.transpose(np.array([
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
	[0.0, 0.4, 0.3, 0.2, 0.1, 0.0],
	[0.0, 0.8, 0.7, 0.6, 0.5, 0.0],
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],]))
reference_th2.SetBinContent(1, 1, 1.0)
reference_th2.SetBinContent(2, 1, 2.0)
reference_th2.SetBinContent(3, 1, 3.0)
reference_th2.SetBinContent(4, 1, 4.0)
reference_th2.SetBinContent(1, 2, 5.0)
reference_th2.SetBinContent(2, 2, 6.0)
reference_th2.SetBinContent(3, 2, 7.0)
reference_th2.SetBinContent(4, 2, 8.0)
reference_th2.SetBinError(1, 1, 0.4)
reference_th2.SetBinError(2, 1, 0.3)
reference_th2.SetBinError(3, 1, 0.2)
reference_th2.SetBinError(4, 1, 0.1)
reference_th2.SetBinError(1, 2, 0.8)
reference_th2.SetBinError(2, 2, 0.7)
reference_th2.SetBinError(3, 2, 0.6)
reference_th2.SetBinError(4, 2, 0.5)


def test_read_histogram_1d():
	'''
	Test reading a ROOT TH1F and creating a Heppy histogram from it
	'''
	h = heppy.readroot(testfile, hist1d_path)
	assert isinstance(h, heppy.histogram1d)
	np.testing.assert_array_almost_equal( h.areas, [1.1, 4.3, 9.5, 16.7] )
	np.testing.assert_array_almost_equal( h.binsizes, [0.5, 0.5, 0.5, 0.5] )
	np.testing.assert_array_almost_equal( h.heights, h.areas / 0.5 )
	np.testing.assert_array_almost_equal( h.uncorr_variations['Statistical__1up'], [1.3, 4.9, 10.5, 18.1] )
	np.testing.assert_array_almost_equal( h.uncorr_variations['Statistical__1down'], [0.9, 3.7, 8.5, 15.3] )


def test_read_histogram_2d():
	'''
	Test reading a ROOT TH2F and creating a Heppy histogram from it
	'''
	h = heppy.readroot(testfile, hist2d_path)
	assert isinstance(h, heppy.histogram2d)
	np.testing.assert_array_almost_equal( h.areas, areas2d )
	np.testing.assert_array_almost_equal( h.binsizes, np.ones_like(areas2d) * 0.5 )
	np.testing.assert_array_almost_equal( h.heights, areas2d / 0.5 )
	statistical__1up = (reference_areas + reference_area_errors)[1:-1,1:-1]
	np.testing.assert_array_almost_equal( h.uncorr_variations['Statistical__1up'], statistical__1up )
	statistical__1down = (reference_areas - reference_area_errors)[1:-1,1:-1]
	np.testing.assert_array_almost_equal( h.uncorr_variations['Statistical__1down'], statistical__1down )
