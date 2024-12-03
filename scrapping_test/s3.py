import boto3

key = "DecisionAdapterDLQ-uat.fifo/None/2024-01-11T07:00:34.475633-05:00.txt"
# tag = "correlation_id=PATSTPA-{p_Date}-{p_VuserID}{p_VuserID}{p_VuserID}{p_VuserID}-265c-d2eefgg4{p_RandomNumber}IDLBCA&x-aws-region=us-east-1"
# tag = "correlation_id=PATSTPA-{p_Date}-IDLBCA&x-aws-region=us-east-1"
tag = "correlation_id=PATSTPA-IDLBCA&x-aws-region=us-east-1"
data = {"eventVersion": "1.2", "eventId": "6136f816-55c9-4111-a19c-c739d0923e46", "eventTime": "2024-01-31T10:50:36", "eventName": "CreditApplications:Saved", "eventSource": "fni:Deals", "eventType": "fni:CreditApplications", "eventIdentityId": "6136f816-55c9-4111-a19c-c739d0923e46", "eventEntityId": "1154708", "eventTransactionId": "01HNFJ2QXA3JX9Q4T3XM7M0BPJ", "payloadSchemaHref": "", "eventKeyData": {"leadRefIdFD": "0", "dealJacketId": "510200000698438463", "dealerCode": "1154708", "partnerCode": "", "sourcePartnerId": "DXR", "sourcePartnerDealerId": "100025", "dealRefIdDR": "01HNFJ2QXA3JX9Q4T3XM7M0BPJ", "appRefIdFD": "0", "dealerId": "100025"}, "payload": {"status": "AppSaved", "approvedAmount": None, "approvedRate": None, "approvedTerm": None, "lenderId": None, "lenderName": "", "tier": None, "dealerMessage": "<p><strong><span style='font-size: large'>Thank you for your application</span></strong><strong><span style='font-size: large'>. </span></strong></p><p>Please contact us as we need some additional information to be able to decision your credit application and seek financing for you. </p><p>We look forward to hearing from you. </p>", "fromEmailAddress": "noreply@dealertrack.com", "stipulations": None, "lenderMoneyFactor": None, "customerMoneyFactor": None, "downPayment": None, "monthlyPayment": None, "financeMethod": "", "dealerDiscount": None, "dealUpdate": None, "fundedAmount": None, "rateVariance": None, "eContractEligible": None, "maxAmtToFinance": None, "resubmitReturnedEcontract": None, "lenderApplicationId": None, "message": None, "alternativeDealsGroupId": None}}

s3_client = boto3.client("s3", region_name="us-east-1")
try:
    s3_client.put_object(
                    Body=str(data),
                    Bucket="awscoxautolabs18-reprocessing-garage-us-east-1-lab",
                    Key=key,
                    Tagging=tag,
                    ContentType="txt",
                )
    print("success")
except Exception as e:
    print(str(e))
