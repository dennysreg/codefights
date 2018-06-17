import re
def variableName(name):
  return re.match(r'^([A-Za-z_])+([A-Za-z_0-9])*$',name) !=None