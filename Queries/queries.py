import pyvo as vo
from astropy.coordinates import SkyCoord

import warnings
warnings.filterwarnings('ignore', module="astropy.io.votable.*")

archives = vo.regsearch(servicetype='image', waveband='x-ray')
pos = SkyCoord.from_name('Bellatrix')
len(archives) 


print(archives)