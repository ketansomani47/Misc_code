import requests
import json

url = "https://apic.dev-east.unifinp.dealertrack.com/sfni/devint/dr-decisions/v1/responses/310300000004638131/lenders/113430065/"
# url = "https://apic.dev-east.unifinp.dealertrack.com/sfni/devint/dr-decisions/v1/responses/310300000004638131/lenders/ALY/"

payload = {}
headers = {
  'dealer_code': '1089761',
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer AAIkMjFmODBhMjctOTdkMS00M2VhLWJjZjgtYzJkNjRjMjBkOTFi7tJNyC6P6J8EnRrqNU1Ohg55I3x7d2AU_WBDiTF7mVWEAfA33D8Vx68xrRGePWfzFMKmuEaxMaV8FpwAHC3CArvZblz7bDO1EBx8TcHBLCGHthpqLZ3y1inUAwKfI7qsU0dVfN2PolNiBtJ4pg3Q0JBQ8X2xTM5C7kzg7b_HJ5E'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response)
print(response.status_code)
print(response.text)
if response.text is None:
    print("None")
else:
    print(response.text)
if not response or response.status_code == 404:
    print("no data")
else:
    print("forbidden")
