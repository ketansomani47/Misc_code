from box import Box

with open("FLD.json") as fld_data:
    data = Box(fld_data)

print(data)
print(type(data))
print(data.deal_data.applicant_data.applicant[0].address_data.address[0].zip_code)
