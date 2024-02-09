from astropy import table
from astropy.coordinates import SkyCoord
from pyvo import registry


my_obj = SkyCoord.from_name("Bellatrix")
for res in registry.search(waveband="infrared", servicetype="spectrum"):
    print(res.service.search(pos=my_obj, size=0.001))
