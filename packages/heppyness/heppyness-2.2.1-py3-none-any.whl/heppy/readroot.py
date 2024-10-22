#!/usr/bin/env python3

import uproot
from .histogram import histogram1d, histogram2d

def readroot(rootfile, histpath, variation_paths={}, ignore_missing_variations=False, **kwargs):
    """Reads a histogram (possibly with systematic variations) from a ROOT file.

    :param rootfile: path to ROOT file
    :type rootfile: ``str``
    :param histopath: path of the histogram inside the file
    :type histopath: ``str``
    :param variation_paths: optional dictionary of variation names (keys) and
        paths to the variation histograms inside the same ROOT file (values).
        NOTE: we can easily add the ability to read variation histograms also
        from other ROOT files than the nominal, get in touch if you want that.
    :type variation_paths: ``dict`` of ``str : str``
    :param **kwargs: get passed on to histogram constructor. An important one is
        ``areas=False`` if retrieving ratios (e.g. efficiencies).
    """

    # TODO add this:
    #
    # The variation paths may contain the following wildcards:
    # - "@" will be interpreted as a numerical index starting at 0 and continuing until no more histograms are found
    # - "#" is the same as "@", but starting at 1
    # - Arbitrary Unix-style wildcards (see Python module fnmatch). These may not be combined with the above
    # custom wildcards. Note: including Unix-style wildcards may be very slow.

    file = uproot.open(rootfile)
    urhist = file[histpath]

    if not any(['TH1' in urhist.classname, 'TH2' in urhist.classname]):
        raise TypeError('Can only read ROOT.TH1 and ROOT.TH2 objects, but '
            f'found {urhist.classname} object in {rootfile} at {histpath}')

    binedges = tuple([axis.edges() for axis in urhist.axes])
    if len(binedges) == 1:
        binedges = binedges[0]
    corr_variations = {}
    for name, path in variation_paths.items():
        try:
            corr_variations[name] = file[path].values()
        except (ReferenceError, uproot.exceptions.KeyInFileError):
            if not ignore_missing_variations:
                raise ValueError('While reading variation histograms, could '
                    f'not read object object in {rootfile} at {path}')
    attributes = {
        'name' : urhist.name,
        'title' : urhist.title,
        'provenance' : f'{rootfile}:{histpath}'
    }
    histclass = histogram1d if 'TH1' in urhist.classname else histogram2d
    kwargs['areas'] = kwargs.get('areas', True)
    return histclass(binedges, urhist.values(),
        uncorr_variations={'Statistical__1up' : urhist.values() + urhist.errors(),
        'Statistical__1down' : urhist.values() - urhist.errors()},
        corr_variations=corr_variations, attributes=attributes,
        plot_attributes={'label' : kwargs.get('name', urhist.name)}, **kwargs)
