
from dynamodb_json import json_util
x = """{
  "feature": {
    "S": "FT"
  },
  "subfeature_custom_key": {
    "S": "FIN.DLR.104334.SETTINGS"
  },
  ".DEALER_ID": {
    "S": "104334"
  },
  "aws:rep:deleting": {
    "BOOL": false
  },
  "aws:rep:updateregion": {
    "S": "us-east-1"
  },
  "aws:rep:updatetime": {
    "N": "1627476226.835001"
  },
  "dealerSettings": {
    "M": {
      "creditApplicationService": {
        "M": {
          "unhideDeals": {
            "BOOL": true
          }
        }
      },
      "preQualificationService": {
        "M": {
          "unhideDeals": {
            "BOOL": true
          }
        }
      }
    }
  },
  "_username": {
    "S": "Liavontsi.Khachuyeu@coxautoinc.com"
  }
}"""
y = """{
  "feature": {
    "S": "FT"
  },
  "subfeature_custom_key": {
    "S": "FIN.DLR.104334.SETTINGS"
  },
  ".DEALER_ID": {
    "S": "104334"
  },
  "aws:rep:deleting": {
    "BOOL": false
  },
  "aws:rep:updateregion": {
    "S": "us-east-1"
  },
  "aws:rep:updatetime": {
    "N": "1627476226.835001"
  },
  "dealerSettings": {
    "M": {
      "creditApplicationService": {
        "M": {
          "unhideDeals": {
            "BOOL": false
          }
        }
      },
      "preQualificationService": {
        "M": {
          "unhideDeals": {
            "BOOL": true
          }
        }
      }
    }
  },
  "_username": {
    "S": "Ketan.Somani@coxautoinc.com"
  }
}"""
old_settings = json_util.loads(x)
new_settings = json_util.loads(y)
print("old settings", old_settings)
print("new settings", new_settings)
from deepdiff import DeepDiff
diff = DeepDiff(old_settings, new_settings)
print("difference in settings : ", diff)

import flatdict
flat_data = flatdict.FlatDict(old_settings, delimiter=".")
print("flatten dict : ", flat_data)
