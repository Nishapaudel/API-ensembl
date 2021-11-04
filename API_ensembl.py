# http://rest.ensembl.org/ 
import requests, sys
 
server = "http://rest.ensembl.org"
ext = "/sequence/id/ENSG00000157764?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
 
print(r.text)
