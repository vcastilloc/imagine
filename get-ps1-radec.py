from astrometry.util.fits import *
import sys
import os
import argparse
from astrometry.libkd.spherematch import *

parser = argparse.ArgumentParser()
parser.add_argument('-r', dest='radius', type=float, help='Search radius in degrees',
                    default=1)
parser.add_argument('--all', '-a', action='store_true', help='Retrieve all within range; default: nearest',
                    default=False)
parser.add_argument('radec', nargs=2, type=float, help='RA,Dec coords to search')
args = parser.parse_args()

bands = 'grz'
T = fits_table('data/ps1skycells.fits')
T.cut(np.array([b in bands for b in T.filter]))

ra,dec = args.radec
radius = args.radius
closest = not args.all

print('Searching RA,Dec', ra,dec, 'with radius', radius, 'deg')

I,J,d = match_radec(np.array([ra]), np.array([dec]), T.ra, T.dec, radius, nearest=closest)
print('Matched', len(J), 'sky cells')

T.cut(J)

for cell,subcell,fn,band in zip(T.projcell, T.subcell, T.filename, T.filter):
    url = 'ps1images.stsci.edu' + fn.strip()
    outdir = os.path.join('data', 'ps1', 'skycells', '%04i'%cell)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    fn = 'ps1-%04i-%03i-%s.fits' % (cell, subcell, band)
    outfn = os.path.join(outdir, fn)
    if os.path.exists(outfn):
        print('File exists:', outfn)
        continue

    tmpoutfn = os.path.join(outdir, 'tmp-' + fn)
    cmd = 'wget -O %s "%s"' % (tmpoutfn, url)
    print(cmd)
    rtn = os.system(cmd)
    if rtn == 0:
        os.rename(tmpoutfn, outfn)
