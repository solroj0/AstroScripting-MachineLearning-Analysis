from astropy import table
from pyvo import registry

QUERY = "SELECT TOP 1 s_ra, s_dec from ivoa.obscore"

results = []
for svc_rec in registry.search(
          datamodel="obscore", servicetype="tap"):
      print("Querying {}".format(svc_rec.res_title))
      try:
          svc = svc_rec.get_service("tap")
          results.append(
              svc.run_sync(QUERY).to_table())
      except KeyboardInterrupt:
          # someone lost their patience with a service.  Query next.
          pass
      except Exception as msg:
          # some service is broken; you *should* complain, but
          print("  Broken: {} ({}).  Complain to {}.\n".format(
              svc_rec.ivoid, msg, svc_rec.get_contact()))

total_result = table.vstack(results)
print(total_result)