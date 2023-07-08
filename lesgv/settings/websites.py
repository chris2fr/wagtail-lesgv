domains = [
  'gvois.in',
  'gvcoop.org',
  'gvcoop.com',
  'coopgv.org',
  'coopgv.com',
  'l-g-v.com',
]

def allowed_hosts():
  output = []
  for dom in domains:
    output += [domains]
    output += ["www.{}".format(dom)]
  return output
  
def csrf_trusted_origins():
  output = []
  for domain in domains:
    output += ["https://{}".format(domain)]
    output += ["https://www.{}".format(domain)]
  return output