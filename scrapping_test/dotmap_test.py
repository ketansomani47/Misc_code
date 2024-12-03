from dotmap import DotMap

with open("FLD.json") as fld_data:
    data = fld_data.read()
print(data)
data = DotMap(data)

print(data)
print(type(data))
print(data.deal_data.applicant_data.applicant[0].address_data.address[0].zip_code)
