# from urllib.parse import urlsplit, urlunsplit
# URL_MAPPING = {"apic.dev-east.unifinp.dealertrack.com": "fni-api.dvi1.dealertrack.com",
#                "apic.uat-east.unifipp.dealertrack.com": "fni-api.uat1.dealertrack.com"}
# url = list(urlsplit("https://apic.uat-east.unifipp.dealertrack.com/sfni/uat1/dr-decisions/v1/responses/310300000011568525/lenders/DT6"))
# print(url)
# url[1] = URL_MAPPING[url[1]]
# new_url = urlunsplit(url)
# print(new_url)

def get_markup_value(settings, lender_id):
    try:
        lender_markup_list = settings["consumerDecisions"]["lenderBuyRateMarkup"]
        if len(lender_markup_list) > 0:
            markup = None
            for lender in lender_markup_list:
                if lender["lenderId"] == lender_id:
                    markup = lender["buyRateMarkup"]
            if markup is None:
                markup = settings["buyRateMarkup"]
        else:
            markup = settings["buyRateMarkup"]
        return markup
    except Exception as exe:
        raise exe

settings = {
            "sendDetailedInfo": "Summary",
            "subfeature_custom_key": "SETTINGS.DEALER.410001169.DECISION",
            "feature": "FSDEALER",
            "custom_value": "SETTINGS.DEALER.DECISION",
            "buyRateMarkup": 1.2,
            "consumerDecisions": {
                "tradeIn": "Yes",
                "lenderBuyRateMarkup": [
                ],
                "dealType": "Retail",
                "vehicleType": "Used"
            }
        }
x = get_markup_value(settings, "DTS")
print(x)
