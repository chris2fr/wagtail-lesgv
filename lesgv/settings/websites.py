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
  "manncoach.gvois.in",
  "wagtail.gvois.in",
  "resdigitacom.gvois.in",
  "distractivescom.gvois.in",
  "whowhatetccom.gvois.in",
  "voisandcom.gvois.in",
  "coopgvcom.gvois.in",
  "voisandorg.gvois.in",
  "lesgvcom.gvois.in",
  "popuposcom.gvois.in",
  "grandsvoisinscom.gvois.in",
  "forumgrandsvoisinscom.gvois.in",
  "baldridgegvoisorg.gvois.in",
  "discourselesgvcom.gvois.in",
  "iriviorg.gvois.in",
  "ooolesgrandsvoisinscom.gvois.in",
  "hyperattentioncom.gvois.in",
  "forumgdvoisinscom.gvois.in",
  "forumgrandsvoisinscom.gvois.in",
  "agoodvillagecom.gvois.in",
  "lgvcoop.gvois.in",
  "configmagiccom.gvois.in",
  "caplancitycom.gvois.in",
  "quiquoietccom.gvois.in",
  "lesartsvoisinscom.gvois.in",
  "maelanccom.gvois.in",
  "manncity.gvois.in",
  "focusplexcom.gvois.in",
  "gvoisorg.gvois.in",
  "vlgorg.gvois.in",
  "oldlesgrandsvoisinscom.gvois.in",
  "cooptellgv.gvois.in",
  "howwownowcom.gvois.in",
  "aaalesgrandsvoisinscom.gvois.in",
  "oldmanndigital.gvois.in",
  "resolvactivecom.gvois.in",
  "gvcity.gvois.in",
  "toutdouxlissecom.gvois.in",
  "iciwowcom.gvois.in",
  "mann.fr"
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