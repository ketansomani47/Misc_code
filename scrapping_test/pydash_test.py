import pydash
import json

with open("FLD.json") as fld_data:
    data1 = fld_data.read()
F_data = json.loads(data1)

with open("DXG_1.json") as dealxg_data:
    data2 = dealxg_data.read()
D_data = json.loads(data2)
# postal_code = pydash.get(F_data, "dt_application.deal_data.applicant_data.applicant[0].address_data.address[0].zip_code")
# print(postal_code)
postal_code = pydash.get(D_data, "dealStructure.financialDetails.feeDetails.fees")
print(postal_code)
# pydash.set_(D_data, "dealStructure.participants.buyer.postalCode", 4321)
# print(pydash.get(D_data, "dealStructure.participants.buyer.postalCode"))
# print(data["dt_application"]["deal_data"]["applicant_data"]["applicant"][0])
# postal_code = pydash.get(data, "dt_application.deal_data.applicant_data.applicant[0].address_data.address[0].zip_code")
# print(postal_code)


