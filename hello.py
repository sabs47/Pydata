import yaml,csv

in_file  = open('test_pydata.csv', "r")
out_file = open('yaml_texts.yaml', "w")
items = []

def convert_to_yaml(line, counter):
    item = {
        'suppresion groupe ldap': line[8],
        'Ajout groupe ldap': line[7],
        'mot de passe': line[6],
        'service': line[5],
        'nom': line[4],
        'prenom': line[3],
        'email': line[2],
        'identifiant': line[1],
        'type': line[0]
        
    }
    items.append(item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)
    out_file.write(yaml.dump(items, default_flow_style=False) )

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