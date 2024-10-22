import ROOT
from array import array

def _array2hist_1d(nbins, areas, th1, errors=None):
    for bin_index in range(nbins):
        th1.SetBinContent(bin_index+1, areas[bin_index])
        if errors is not None:
            th1.SetBinError(bin_index+1, errors[bin_index])

def to_th1(name, binedges, areas, nbins, errors=None):
    th1 = ROOT.TH1D(name, name, len(binedges)-1, array('d', [b for b in binedges]))
    _array2hist_1d(nbins, areas, th1, errors=errors)
    return th1

def _array2hist_2d(nbins, areas, th2, errors=None):
    nbins_x, nbins_y = nbins
    for bin_index_x in range(nbins_x):
        for bin_index_y in range(nbins_y):
            th2.SetBinContent(bin_index_x+1, bin_index_y+1, areas[bin_index_x, bin_index_y])
            if errors is not None:
                th2.SetBinError(bin_index_x+1, bin_index_y+1, errors[bin_index_x, bin_index_y])

def to_th2(name, binedges, areas, nbins, errors=None):
    th2 = ROOT.TH2D(name, name, len(binedges[0])-1, array('d', [b for b in binedges[0]]), len(binedges[1])-1, array('d', [b for b in binedges[1]]))
    _array2hist_2d(nbins, areas, th2, errors=errors)
    return th2
