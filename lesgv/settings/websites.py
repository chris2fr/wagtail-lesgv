domains = [
  'gvois.in',
  'gvcoop.org',
  'gvcoop.com',
  'coopgv.org',
  'coopgv.com',
  'l-g-v.com',
  'lesgrandsvoisins.com',
  'lesgrandsvoisins.fr',
  'resdigita.com',
  'resdigita.org',
  'avmeet.com',
  "gvoisin.org",
  "meet.lesgrandsvoisins.com",
  "app.lesgrandsvoisins.com",
  "auth.lesgrandsvoisins.com",
  "biz.lesgrandsvoisins.com",
  "forum.lesgrandsvoisins.com",
  "mail.lesgrandsvoisins.com",
  "wiki.lesgrandsvoisins.com",
  "www.gvoisins.org",
  "meet.gvoisins.org",
  "meet.gvoisins.com",
  "gvoisins.org",
  "www.gvoisins.com",
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