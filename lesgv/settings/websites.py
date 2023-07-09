domains = [
  'gvois.in',
  'gvcoop.org',
  'gvcoop.com',
  'coopgv.org',
  'coopgv.com',
  'l-g-v.com',
  'lesgrandsvoisins.com',
  'lesgrandsvoisins.fr',
]

def allowed_hosts():
  output = []
  for domain in domains:
    output += [domain]
    output += ["www.{}".format(domain)]
  return output
  
def csrf_trusted_origins():
  output = []
  for domain in domains:
    output += ["https://{}".format(domain)]
    output += ["https://www.{}".format(domain)]
  return output