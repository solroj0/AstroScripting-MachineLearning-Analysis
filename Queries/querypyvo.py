import pyvo as vo

for service in vo.regsearch(datamodel="obscore"):
    print(service['ivoid'])