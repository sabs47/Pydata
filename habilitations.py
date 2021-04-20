import yaml,csv
import base64, sys, hashlib
import random
import string
import os.path
from os import path
import subprocess
in_file  = open('test_pydata.csv', "r")
out_file = open('yaml_texts.yaml', "w")
items = []
getites = []
texts ="ddf"
  
      

def convert_to_yaml(line, counter):
    # print(gen_password())
    text = string.ascii_lowercase
    text = bytes(''.join(random.choice(text) for i in range(10)), 'utf-8')
    auth = hashlib.md5(text).digest()
    mdp = base64.b64encode(auth)
   
    item = {
        'suppresion groupe ldap': line[8],
        'Ajout groupe ldap': line[7],
        'mot de passe': mdp.decode(),
        'service': line[5],
        'nom': line[4],
        'prenom': line[3],
        'email': line[2],
        'identifiant': line[1],
        'type': line[0]
        
    }
    items.append(item)
    for i in range(len(items)):
          # print(items[i]["Ajout groupe ldap"].split(',') )
          for car in items[i]["Ajout groupe ldap"].split(','):
                #print("car",car)
                if(car== "gkib_ied_bddf_a2800_abc" ):
                     # print("ext",car)
                      car = "kib_bddf_a5080ied"
                      items[i]["Ajout groupe ldap"] = car
                      #print(items[i])
                      getites.append(items[i])
          
    a =  path.exists("data.yml")
    new_matricule =line[0]
    new_password = mdp.decode(),
    new_usermaisl = line[2]
    if ((new_matricule == "X")):
          new_usermaisl = 'NON'  
    

           

     
''' 
          if (items[i]["Ajout groupe ldap"] == "gkib_ied_bddf_a2800_abc"  ) :
                for car in items[i]["Ajout groupe ldap"].split(','):
                      items[i]["Ajout groupe ldap"] = "kib_bddf_a5080ied"
                      if car == "gkib_ied_bddf_a2800_abc":
                            items[i]["Ajout groupe ldap"] = "kib_bddf_a5080ied"
                            getites.append(items[i])
                            print(getites) '''

                
                
try:
   
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)
    out_file.write(yaml.dump(getites, default_flow_style=False) )

finally:
    in_file.close()
    out_file.close()
""" 
with open('custInfo.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) """

""" csvfile = open('custInfo.csv', 'r')
datareader = csv.reader(csvfile, delimiter=",", quotechar='"')
result = list()
type_index = -1
child_fields_index = -1

for row_index, row in enumerate(datareader):
  if row_index == 0:
    # let's do this once here
    data_headings = list()
    for heading_index, heading in enumerate(row):
      fixed_heading = heading.lower().replace(" ", "_").replace("-", "")
      data_headings.append(fixed_heading)
      if fixed_heading == "type":
        type_index = heading_index
      elif fixed_heading == "childfields":
        child_fields_index = heading_index
  else:
    content = dict()
    is_array = False
    for cell_index, cell in enumerate(row):
      if cell_index == child_fields_index:
        content[data_headings[cell_index]] = [{
            "username" : "fra:" + value.capitalize(),
            "destination" : value,
            "type" : "string",
            "childfields" : "null"
          } for value in cell.split(",")]
      else:
        content[data_headings[cell_index]] = cell
        is_array = (cell_index == type_index) and (cell == "array")
    result.append(content)
    print (yaml.dump(result))
 """
