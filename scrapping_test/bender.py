# from jsonbender import bend, OptionalS, S
#
# source = {'does': {'exist': 23}}
#
# MAPPING_1 = {'val': S('does', 'exist')}
# ret = bend(MAPPING_1, source)
# print(ret)
# # assert ret == {'val': None}
#
# MAPPING_2 = {'val': OptionalS('does', 'exist', default=27)}
# ret = bend(MAPPING_2, source)
# print(ret)
# # assert ret == {'val': 27}
import ast
import json

from jsonbender import bend, K, S, OptionalS, F


# MAPPING = {
#     'firstName': S('customer', 'first_name'),
#     'age': K(10),
#     'gender': OptionalS('customer', 'gender', default='male'),
#     'fullName': (S('customer', 'first_name') +
#                  K(' ') +
#                  S('customer', 'last_name')),
#     'city': S('address', 'city'),
# }
# def return_age(payload):
#     # import pdb; pdb.set_trace()
#     if payload.get("customer").get("Age") and str(payload.get("customer").get("Age")).isnumeric():
#         # age = payload.get("Age")
#         print(1)
#         age = ast.literal_eval(str(payload.get("customer").get("Age")))
#     elif payload.get("customer").get("age") and str(payload.get("customer").get("age")).isnumeric():
#         print(2)
#         age = ast.literal_eval(str(payload.get("customer").get("age")))
#     else:
#         print(3)
#         age = None
#     return age


# MAPPING = {
#     "age": F(return_age)
# }

source = {
    'customer': {
        'first_name': 'Inigo',
        'last_name': 'Montoya',
        'age': 10
    },
    'address': {
        'city': 'Sicily',
        'country': 'Florin',
    },
}

# result = bend(MAPPING, source)
# print(json.dumps(result))
# x = 10
# print({"age": ast.literal_eval(str(x))})
# x = """{
# 	"dt_application": {
# 		"dtversion": "2.0",
# 		"active": "yes",
# 		"status": "new",
# 		"key_data": {
# 			"optout": "no",
# 			"dealer_code": 1089761,
# 			"legacy_dealer_id": 104334,
# 			"dealer_state": "",
# 			"dealer_address": {
# 				"address_line_1": "3400 New Hyde Park Rd",
# 				"city": "New Hyde Park",
# 				"postal_code": "11042",
# 				"state_code": "NY"
# 			},
# 			"is_resubmit": false,
# 			"partner_correlation_id": "71b1e9b0-734d-11ee-8df3-0242ac110003",
# 			"datapower_timestamp": "",
# 			"datapower_url": "http://dp.dev-east.unifinp.dealertrack.com:8021/CreditAppSubmit/",
# 			"datapower_url_no_prefix": "dp.dev-east.unifinp.dealertrack.com:8021/CreditAppSubmit/",
# 			"prime_id": "",
# 			"subprime_id": "",
# 			"subvented_id": "",
# 			"server_name": "",
# 			"enterprise_code": "",
# 			"source": "FD",
# 			"original_partner_source": null,
# 			"partner_reference_id": "510000000001248992",
# 			"document_id": "",
# 			"company_code": "",
# 			"partner_name": "",
# 			"dealer_name": "Test DealerTrack DMS Regression",
# 			"dealer_legal_name": "Test DealerTrack Dms Regression",
# 			"adapter_subscribed": false,
# 			"extra_data": {
# 				"lender_specific_data": null
# 			},
# 			"end_point": "",
# 			"authorization": "",
# 			"partner_dealer_code": "3081184307",
# 			"party_id": "BOA",
# 			"partner_id": 113430155,
# 			"dealer_logon_id": "",
# 			"orchestration_code": "",
# 			"time_stamp": "",
# 			"lender_app_id": "",
# 			"lender_account_id": "",
# 			"is_automation_deal": false,
# 			"is_unifi_credit_connection_application": false,
# 			"is_address_lines_in_xml_enabled": false,
# 			"is_zipcode_nine_digital_enabled": true,
# 			"remove_app_opt_program": true,
# 			"dealer_selected_ads_id": "",
# 			"is_aud_address_line_enabled": true,
# 			"app_submitted_user_name": "Mark Clatterbuck",
# 			"app_submitted_user_id": "",
# 			"app_submitted_date_time": "2023-10-25T15:44:55.299195",
# 			"str_deal_jacket_id": "310200000246648131",
# 			"dtservices_url": "http://dtservices.fni-dev-east.cmnsvc:6100/api/decisions/creditapp/"
# 		},
# 		"deal_data": {
# 			"credit_type": {
# 				"type": "individual"
# 			},
# 			"app_type": {
# 				"type": "personal"
# 			},
# 			"product_type": {
# 				"type": "retail",
# 				"paymentcall": false
# 			},
# 			"vehicle_type": {
# 				"type": "new",
# 				"certified": false,
# 				"trade": false
# 			},
# 			"cust_credit_type": {
# 				"type": ""
# 			},
# 			"loan_type": {
# 				"type": "auto"
# 			},
# 			"is_invisible": false,
# 			"deal_jacket_id": 310200000246648131,
# 			"deal_id": 310200000246648134,
# 			"applicant_data": {
# 				"applicant": [
# 					{
# 						"type": "primary",
# 						"address_data": {
# 							"address": [
# 								{
# 									"type": "current",
# 									"address_line_1": "78 Palace Court",
# 									"address_line_2": "",
# 									"city": "Castle Hayne",
# 									"state": "NC",
# 									"street_name": "Palace",
# 									"street_no": "78",
# 									"street_type": "CT",
# 									"street_type_desc": "Court",
# 									"zip_code": "28429",
# 									"po_box_no": "",
# 									"apt_no": "",
# 									"rural_route": "",
# 									"months_at_address": 5,
# 									"years_at_address": 10,
# 									"county": ""
# 								}
# 							]
# 						},
# 						"employment_data": {
# 							"employment": [
# 								{
# 									"type": "current",
# 									"emp_status": {
# 										"type_code": "Y",
# 										"type_desc": "employed"
# 									},
# 									"employed_by": "Nagarro",
# 									"months_employed": 5,
# 									"occupation": "Construction",
# 									"salary": {
# 										"type_code": "W",
# 										"type_desc": "weekly",
# 										"text": 2814
# 									},
# 									"work_phone_no": "5169697934",
# 									"years_employed": 16
# 								}
# 							]
# 						},
# 						"first_name": "Ketan",
# 						"last_name": "Somani",
# 						"citizenship": "",
# 						"mi": "",
# 						"home_phone_no": {
# 							"text": "3368566633",
# 							"type": "HOME"
# 						},
# 						"other_phone_no": {
# 							"text": "3369865379",
# 							"type": "CELL"
# 						},
# 						"email_address": "hazeltestco@email.com",
# 						"email_not_provided": "N",
# 						"housing_status": {
# 							"type_code": "N",
# 							"type_desc": "own outright"
# 						},
# 						"marital_status": {
# 							"type_code": "",
# 							"type_desc": ""
# 						},
# 						"dob": "1963-06-18",
# 						"ssn": "555385250",
# 						"driver_license_no": "9070GRXZWINP909",
# 						"driver_license_state": "VT",
# 						"business_name": "",
# 						"business_tax_id": "",
# 						"business_phone_no": "",
# 						"signer_first_name": "",
# 						"signer_middle_name": "",
# 						"signer_last_name": "",
# 						"signer_suffix": "",
# 						"signer_title": "",
# 						"add_ssn_business_fields": true,
# 						"business_established_date": "",
# 						"state_of_incorporation": "",
# 						"business_type_code": "",
# 						"number_of_employees": "",
# 						"financial_statement": "",
# 						"bank_name": "",
# 						"bank_account_no": "",
# 						"bank_contact_name": "",
# 						"bank_contact_phone_no": "",
# 						"years_in_business": "",
# 						"applicant_age": "60",
# 						"mortgage_rent": 0,
# 						"other_income": 118,
# 						"relationship": {
# 							"type_code": "",
# 							"type_desc": ""
# 						},
# 						"source_other_income": "Insurance Settlement",
# 						"suffix": "",
# 						"spouse": null,
# 						"customer_references": {
# 							"reference": []
# 						},
# 						"credit_score": null,
# 						"full_name": "Ketan Somani",
# 						"new_primary_customer": false,
# 						"cc_id": 310200000246648130,
# 						"old_cc_id": "FNI701910618"
# 					}
# 				]
# 			},
# 			"product_data": {
# 				"hold_deposit": "",
# 				"interest_deferment_ind": "",
# 				"interest_deferment_start_date": "",
# 				"acc_health_insurance": "",
# 				"acc_health_insurance_desc": null,
# 				"app_opt_program": null,
# 				"cash_down": "",
# 				"cash_selling_price": 20000,
# 				"trade_in_sales_tax": "",
# 				"creditlife": "",
# 				"creditlife_insurance_cost": null,
# 				"creditlife_insurance_reserve": null,
# 				"creditlife_insurance_desc": null,
# 				"creditlife_who": null,
# 				"credit_disability_who": null,
# 				"involuntary_insurance_beneficiary": null,
# 				"contract_term": 44,
# 				"contract_term_period": null,
# 				"initial_payment": "",
# 				"last_month_payment": "",
# 				"refunded_trade": "",
# 				"insurance_data": [],
# 				"last_payment_date": "",
# 				"deferred_down_payment": "",
# 				"deferred_down_payment_date": "",
# 				"form_no": "",
# 				"first_payment_date": null,
# 				"amount_due_at_delivery": "",
# 				"days_to_first_payment": "",
# 				"est_amt_financed": 21070,
# 				"est_payment": "",
# 				"gap": "",
# 				"gap_term": null,
# 				"gap_insurance_company": null,
# 				"gap_cost": null,
# 				"gap_reserve": null,
# 				"finance_charge": "",
# 				"rate_program": "",
# 				"finance_reserve": "",
# 				"amount_due_at_start": "",
# 				"demo_invoice_amount": null,
# 				"invoice_amount": 400,
# 				"msrp": null,
# 				"front_end_fee_amount": 70,
# 				"back_end_fee_amount": "",
# 				"rebate": "",
# 				"manufacturer_rebate": "",
# 				"requested_apr": 1.99,
# 				"apr": null,
# 				"amount_financed": "",
# 				"total_amount_financed": "",
# 				"sales_pgm_code": "",
# 				"sales_tax": 800,
# 				"term_months": 44,
# 				"ttl_estimate": 200,
# 				"unpaid_balance": 21070,
# 				"warranty": "",
# 				"cap_cost": 20000,
# 				"acq_fee": "",
# 				"wholesale_value": null,
# 				"wholesale_source": null,
# 				"wholesale_veh_condition": "na",
# 				"wholesale_veh_type": "na",
# 				"wholesale_book_frequency": null,
# 				"wholesale_book_date": null,
# 				"retail_value": null,
# 				"retail_source": null,
# 				"retail_veh_condition": "na",
# 				"retail_book_frequency": null,
# 				"retail_book_date": null,
# 				"dealer_comments": null,
# 				"net_trade": "",
# 				"balloon_payment": "",
# 				"lender_program": "",
# 				"vci_bulletin": "",
# 				"marketing_code": "",
# 				"lender_prog": "",
# 				"rate_protection_date": "",
# 				"coupon_code": "",
# 				"tax_data": {
# 					"taxes": [
# 						{
# 							"tax_type": "sales",
# 							"amount": 800.0,
# 							"payment_method": null,
# 							"category": "",
# 							"paid_to": "",
# 							"paid_to_other": ""
# 						}
# 					],
# 					"sales": 800.0,
# 					"use_tax": null,
# 					"use_tax_input": null,
# 					"use_tax_percent": null,
# 					"total_use_tax": null,
# 					"total_tax_credit": "",
# 					"fed_lux": null,
# 					"inventory": null,
# 					"lieu": null,
# 					"property_tax": null,
# 					"DOD_state_adj": null,
# 					"generalexcisetax_DOD": null,
# 					"generalexcisetax_CC": null,
# 					"rental_tax": null,
# 					"acquisition2": null,
# 					"tradein_salestax_credit": null,
# 					"non_taxable_part_cash_price": null,
# 					"state_upfront_tax": null,
# 					"total_tax_fees": null,
# 					"document_stamp_tax": null,
# 					"other_taxes": null,
# 					"motor_vehicle_tax": null,
# 					"dealer_inventory": null,
# 					"tire_tax": null,
# 					"business_and_occupation": null,
# 					"local_upfront_tax": null,
# 					"taxes_additional": null,
# 					"taxes_not_in_cash_price": null,
# 					"sales_tax_exemp": null,
# 					"taxable_part_cash_price": null,
# 					"other_taxable_cash_price_amount": [],
# 					"purchase_and_use_tax": null,
# 					"tax_rate": null,
# 					"monthly_sales_tax": null,
# 					"other_charges": [],
# 					"warranty_tax": null,
# 					"svccontract_sales": null,
# 					"maintenance_sales": null,
# 					"dealfee_sales_tax_percentage": null,
# 					"government_taxes_not_included_in_cash_price": null,
# 					"other_tax_amount_description": null
# 				},
# 				"fee_data": {
# 					"fees": null,
# 					"electronic_registration": null,
# 					"deputy_service": null,
# 					"convenience": null,
# 					"documentation": null,
# 					"notary": null,
# 					"fl_doc_stamps": null,
# 					"other_public_official": null,
# 					"driveway_permit": null,
# 					"emission_inspection": null,
# 					"smog": null,
# 					"state_smog": null,
# 					"service": "",
# 					"title_transfer": null,
# 					"transfer": null,
# 					"temporary_tag": null,
# 					"registration": null,
# 					"license_registration": null,
# 					"license_title_registration": null,
# 					"smog_certification": null,
# 					"lic_title_reg_over_term": null,
# 					"filing": null,
# 					"government": [],
# 					"vehicle_inspection": null,
# 					"dps_handling": null,
# 					"temp_license": null,
# 					"postage": null,
# 					"registration_fee": null,
# 					"electronic_filing": null,
# 					"ucc_filing": "",
# 					"loan_origination_fee": null,
# 					"state_emissions_fee": "",
# 					"plate_fee": null,
# 					"delivery_handling": null,
# 					"accessory_and_install_charges": null,
# 					"accessory_charge": null,
# 					"accessory_charge_2": null,
# 					"accessory_charge_3": null,
# 					"accessory_charge_4": null,
# 					"accessory_charge_5": null,
# 					"de_doc_fee": null,
# 					"trade_in_credit_agreement": null,
# 					"payment_protection_insurance": null,
# 					"road_safety_surcharge": null,
# 					"transportation_improvement": null,
# 					"cancellation": null,
# 					"dmv_electronic": null,
# 					"documentation_processing": null,
# 					"duplicate_card": null,
# 					"duplicate_title": null,
# 					"electric_vehicle_charging": null,
# 					"encumbrance": null,
# 					"gross_vehicle_weight_rating": null,
# 					"lemon_law": null,
# 					"lien": null,
# 					"recording": null,
# 					"waste_tire": null,
# 					"weight": null,
# 					"surface_protection_charge": null,
# 					"theft_deterrent_charge": null,
# 					"total_additional_fees": null,
# 					"license": null,
# 					"dealer_administration": null,
# 					"supplement_title": null,
# 					"tire": null,
# 					"title": null,
# 					"prior_lease_or_loan_balance": null
# 				},
# 				"note_date": "",
# 				"credit_disability_amount": null,
# 				"owing_amount": "",
# 				"total_others_amount": "",
# 				"total_credit_insurance": "",
# 				"comments_to_analyst": "",
# 				"net_tradein_allowance": "",
# 				"total_cash_price": "",
# 				"monthly_payment": "",
# 				"total_tax_credit": "",
# 				"flex_cash_data": [],
# 				"hard_adds": [],
# 				"amount_in_cash_paid": "",
# 				"trade_gross_amount1": "",
# 				"trade_actual_cash_value": "",
# 				"simple_interest": "",
# 				"amount_paid_at_signing": "",
# 				"annual_miles": "",
# 				"real_annual_miles": "",
# 				"days_to_cancellation": "",
# 				"other_down_payment1_amount": "",
# 				"other_down_payment2_amount": "",
# 				"other_down_payment3_amount": "",
# 				"trade_vehicle_ownership_ind": null,
# 				"adjusted_msrp": "",
# 				"prior_lease_payments": "",
# 				"additional_money_factor": "",
# 				"total_rebate": "",
# 				"total_cash_down": "",
# 				"other_down_payment_desc": null,
# 				"other_down_payment1_desc": "",
# 				"other_down_payment2_desc": "",
# 				"limited_right_to_cancel": "",
# 				"total_other_charge_amount": "",
# 				"total_of_payments": "",
# 				"total_down_payment": "",
# 				"total_sale_price": "",
# 				"other_down_payment_amount": 0,
# 				"total_cash_down_amount": "",
# 				"total_cash_down_payment": "",
# 				"federal_ev_tax_credit": "",
# 				"vehicle_insurance": {
# 					"insurance_type": "physical_damage"
# 				},
# 				"dlr_markup_share_percent": null,
# 				"lender_data": null
# 			},
# 			"vehicle_data": {
# 				"certified_used": false,
# 				"usage_type": "",
# 				"business_principal_name1": "",
# 				"stock_no": "932YCHY7",
# 				"vin": null,
# 				"book_year": "",
# 				"book_make": "",
# 				"book_model": "",
# 				"book_trim": "",
# 				"model_number": "",
# 				"chrome_year": "",
# 				"chrome_make": "",
# 				"chrome_model": "",
# 				"chrome_style_id": null,
# 				"chrome_trim": "",
# 				"odometer": 34,
# 				"other_year": 2013,
# 				"other_make": "Ford",
# 				"other_model": "Escape",
# 				"other_trim": "FWD 4dr Limited",
# 				"options": {},
# 				"bookout_options": "",
# 				"chrome_options": {
# 					"options": []
# 				},
# 				"ros_number": null,
# 				"prior_use": "",
# 				"input_gross_weight_num": "",
# 				"trim": "",
# 				"model": ""
# 			},
# 			"tradein_vehicle_data": null,
# 			"type": "newapplication",
# 			"spot": {
# 				"indicator": false
# 			},
# 			"regb": false,
# 			"comu_state": false,
# 			"swap": false,
# 			"cosigner_intent": "",
# 			"program_routing_ind": "none",
# 			"credit_app_request_id": 310300000002117077,
# 			"dt_app_id": "BCJ2439119",
# 			"beneficial_owners": null,
# 			"custom_tags": null
# 		},
# 		"decision_data": {
# 			"model_number": "",
# 			"lender_app_id": "BCJ2439122DTCOM",
# 			"comments_only": "",
# 			"analyst_comments": {
# 				"comment": [
# 					{
# 						"type": "credit",
# 						"comments_date": "",
# 						"comments_text": "Application is complete."
# 					},
# 					{
# 						"type": "credit",
# 						"comments_date": "",
# 						"comments_text": "Loan has been given for the amount requested."
# 					}
# 				]
# 			},
# 			"analyst_data": {
# 				"analyst_fax": "8002271087",
# 				"analyst_name": "Bernard Patel",
# 				"analyst_phone": "7189723903",
# 				"analyst_email": "abc@xyzbank.com",
# 				"lender_contact_email": "customerservice@abc.com",
# 				"lender_contact_no": "8001759237"
# 			},
# 			"app_status": {
# 				"contract": "no",
# 				"text": "Generic Credit Decision"
# 			},
# 			"approved_loan_amt": 21070,
# 			"term_months": 44,
# 			"buy_rate": 2.33,
# 			"co_decline_reasons": [
# 				{
# 					"line": "",
# 					"text": "15% MINIMUM CASH DOWN REQUIREMENT NOT MET"
# 				},
# 				{
# 					"line": "",
# 					"text": "CREDIT SCORE HAS DECREASED BY MORE THAN 100 POINTS"
# 				}
# 			],
# 			"contract_rate": "",
# 			"cust_rate": 1.99,
# 			"lender_money_factor": 0.11,
# 			"cust_money_factor": 0.3456,
# 			"dealer_participation": 10,
# 			"dealer_reserve_amt": 120,
# 			"dealer_bonus_amt": 130.42,
# 			"net_proceeds_amt": 400,
# 			"disbursed_amt": 21070,
# 			"payment_call_amt": 300,
# 			"balloon_payment": 400.45,
# 			"dealupdate": {
# 				"eligible": true
# 			},
# 			"alternatedealstructure": {
# 				"eligible": true,
# 				"id": "d290f1ee-6c54-4b01-90e6-d701748f8888"
# 			},
# 			"decision_code": "APPROVAL",
# 			"decision_date": "2023-10-25T15:51:56",
# 			"dec_expiration_date": "2023-11-24T15:51:56",
# 			"fund_date": "",
# 			"partner_sponsor_reference_code": "",
# 			"fico_score": 650,
# 			"ltv_ratio": "1.5",
# 			"monthly_payment": "",
# 			"program_id": "",
# 			"program_code": "",
# 			"stipulations": {
# 				"stipulation": [
# 					{
# 						"text": "Proof of Income",
# 						"is_redflag": false,
# 						"status": "Pending",
# 						"accepted_docs": [
# 							{
# 								"person_type": "app",
# 								"doc_type": "W2"
# 							},
# 							{
# 								"person_type": "coapp",
# 								"doc_type": "gap"
# 							}
# 						]
# 					},
# 					{
# 						"line": "",
# 						"text": "***APPROVED - VERIFY RATE***"
# 					}
# 				]
# 			},
# 			"modifiers": "If ACQ FEE WAIVER FOR VEHICLE then Add 0.000550 to Program Rate|If ACQ FEE WAIVER FOR VEHICLE then = 0.000000 Acquisition Fee|If VEHICLE LOYALTY then Subtract 0.000100 from Program Rate|If NO SEC DEP WITH RATE ADJUSTMENT then Add 0.000100 to Program Rate|",
# 			"eligibilities": "",
# 			"tier_level": "SUPER",
# 			"customer_standing": "",
# 			"payment_call_amount": 450,
# 			"veh_subvented": {
# 				"indicator": "N"
# 			},
# 			"econtract": {
# 				"eligible": "Y"
# 			},
# 			"deferred_payment": {
# 				"indicator": "N"
# 			},
# 			"pass_thru": 1,
# 			"max_amt_to_finance": "27400.00",
# 			"max_pti": "16.3",
# 			"ach_indicator": {
# 				"completed": "N"
# 			},
# 			"max_ltv_apr": 12.37,
# 			"low_ltv": "Upto 90%",
# 			"low_ltv_apr": 5.68,
# 			"veh_class": "Class One",
# 			"total_monthly_income": 4300.0,
# 			"verified_income": 3400.0,
# 			"pti_ratio": 7.8,
# 			"dti_ratio": 7.5,
# 			"special_price": 2.4,
# 			"special_price_apr": 1.2,
# 			"special_price_fee": 200.0,
# 			"funded_amount": 20150.0,
# 			"rate_variance": "This loan qualifies for Auto Advantage Rates",
# 			"disbursal_info": [
# 				{
# 					"paid_to": "Acme Dealer",
# 					"amt": 23580,
# 					"mode": "ACH"
# 				},
# 				{
# 					"paid_to": "ETCFC Holdback",
# 					"amt": 500,
# 					"mode": "Check"
# 				},
# 				{
# 					"paid_to": "ETCFC First Pay Deduct",
# 					"amt": 670,
# 					"mode": "Check"
# 				},
# 				{
# 					"paid_to": "State of Florida",
# 					"amt": 200,
# 					"mode": "Check"
# 				}
# 			],
# 			"trade_allowance": 500.0,
# 			"comaker_counter": "X",
# 			"stamps_fee": 12.0,
# 			"title_fee": 5.0,
# 			"service_contract_amt": 230.0,
# 			"smog_fee": 35.0,
# 			"resubmit_returned_econtract": {
# 				"indicator": "N"
# 			},
# 			"over_warranty_deduct": 25,
# 			"dealer_admin_fee": 20,
# 			"lien_fee": 34,
# 			"dealer_income": 300,
# 			"fund_hotline_num": "8003451278",
# 			"fund_fax_num": "8003451278",
# 			"dealer_service_fee": 42.5,
# 			"dealer_service_charge": 23.8,
# 			"misc_deduction": 24.9,
# 			"wholesale_offset": 39.9,
# 			"wholesale_balance_due": 28,
# 			"lien_holder_name": "Abc bank",
# 			"gap_cost": [
# 				{
# 					"type": "regular",
# 					"dealer": "125.00",
# 					"max_retail": "175.00"
# 				},
# 				{
# 					"type": "premier",
# 					"dealer": "500.00",
# 					"max_retail": "600.00"
# 				}
# 			],
# 			"max_front_end": "115% (up to 120% with $195 fee)",
# 			"lender_cash_down": "",
# 			"app_received_date": "2023-10-25T15:44:55.299195",
# 			"book_date": "2015-06-01T11:27:48.507402",
# 			"doc_received_date": "2015-06-01T11:27:48.507402",
# 			"cap_cost": 20000,
# 			"residual_value": 100,
# 			"security_deposit": 123,
# 			"official_fees": 34.56,
# 			"acq_fee": "",
# 			"gap": "",
# 			"first_pay_deduct": 123,
# 			"dealer_subvention": 123,
# 			"pending_docs": {
# 				"doc": ""
# 			},
# 			"max_monthly_payment": "12345",
# 			"min_down_payment": "123",
# 			"participation_points": "1",
# 			"ltv_options": {
# 				"option": 1
# 			},
# 			"range": "4.56",
# 			"apr_buy_rate": "45673",
# 			"price": 20000,
# 			"update_ltv_options": "N",
# 			"apr_buy_down": "456789",
# 			"last_update": "2015-06-01T11:27:48.507402",
# 			"dealer_fee": 123.45,
# 			"mileage_fee": 123,
# 			"marketing_fee": 123,
# 			"processing_fee": 1234,
# 			"assignment_fee": 123,
# 			"dealer_net_fee": 12345,
# 			"max_ltv": "34.54",
# 			"addl_acq_fee": 12,
# 			"dealer_incentive": 123,
# 			"term_fee": 12,
# 			"buy_down": 123,
# 			"dealer_discount": 12,
# 			"applicant_final_income": 12345,
# 			"coapplicant_final_income": 12345,
# 			"program_text": {
# 				"line": ""
# 			},
# 			"price_label": "testlabel",
# 			"lender_score": 123,
# 			"p_lender_apr": 321,
# 			"p_total_pmts": 123,
# 			"p_finance_charge": 90,
# 			"second_pay_deduct": 88,
# 			"third_pay_deduct": 99,
# 			"late_charge_fee": 123,
# 			"fl_stamp_tax": 111,
# 			"down_payment_fee": 1010,
# 			"amt_financed_fee": 21070,
# 			"dti_fee": 22,
# 			"pti_fee": 33,
# 			"other_fee": 11,
# 			"over_advance_deduct": 1,
# 			"veh_val_fee": 17,
# 			"ltv_fee": 99,
# 			"advance_percentage": 10,
# 			"cost_center": "223456",
# 			"veh_collateral": "we23456",
# 			"rate_sheet": "2345",
# 			"rate_sheet_date": "2015-06-01T11:27:48.507402",
# 			"sales_message": [
# 				{
# 					"Text": "1Buy Rate and/or fee will increase for back end % >= 15.01% of vehicle use."
# 				},
# 				{
# 					"Text": "2Test Message"
# 				},
# 				{
# 					"Text": "3TestOn123"
# 				}
# 			],
# 			"contract_type": "Paper",
# 			"auth_user_id": "12345",
# 			"auth_user_name": "test_user",
# 			"auth_cert_pwd": "test",
# 			"total_income": 90909,
# 			"total_down_pmt": 900,
# 			"backend_products": "",
# 			"other_backend_products": 1,
# 			"term_ext_fee": 11,
# 			"doc_fee": 555,
# 			"total_fee": 19999,
# 			"approved_product": {
# 				"type": "retail"
# 			},
# 			"approved_term": 12,
# 			"approved_apr": 1234,
# 			"bank_rate": 12,
# 			"maximum_rate": 15,
# 			"collateral_value": 12345,
# 			"price_class": "Price Class",
# 			"funding_address": {
# 				"line1": "line",
# 				"line2": "test"
# 			},
# 			"blackbook_fee": 123,
# 			"veh_ltv_options": {
# 				"veh_option": {
# 					"label": "Advance"
# 				},
# 				"opt_val": "12346"
# 			},
# 			"decision_type": "auto",
# 			"contact_address": {
# 				"address_type": "Insurance Loss Payee Address",
# 				"addess_title": "title",
# 				"line1": "456, test",
# 				"line2": "US",
# 				"city": "NC",
# 				"state": "NC",
# 				"zip": "10001"
# 			},
# 			"buying_center_contact_info": {
# 				"contact_phone_no": "7189113903",
# 				"contact": {
# 					"name": "First Last",
# 					"extension": 341
# 				},
# 				"contact_fax": "8002271087"
# 			},
# 			"back_end_percentage": 6.7,
# 			"plan_mileage": 101,
# 			"max_term": 48,
# 			"vendor_si_ins_amt": 444,
# 			"total_backend_percent": 1.9,
# 			"total_frontend_percent": 1.7,
# 			"frontend_amt": 70,
# 			"callback_title": "title",
# 			"frontend_options": {
# 				"fe_range": {
# 					"be_range": {
# 						"apr_buy_rate": "91",
# 						"acq_fee": "456"
# 					}
# 				}
# 			},
# 			"doc_ids": {
# 				"doc_id": "8902345678"
# 			},
# 			"payment_frequency": 12345,
# 			"url": "http://google.com",
# 			"tci_value": "4.50",
# 			"first_payment_date": "2015-06-01T11:27:48.507402",
# 			"est_net_proceeds": 2323,
# 			"lo_location": "location",
# 			"drm_name": "Patel",
# 			"drm_phone": "8003451278",
# 			"drm_location": "newyork",
# 			"fe_ratio": "1.10",
# 			"options_data": {
# 				"ltv_option": {
# 					"ranges": "4.50"
# 				}
# 			},
# 			"addl_pending_docs": "",
# 			"dlr_reserve_type": "",
# 			"unpaid_balance": 21070,
# 			"rebate_amt": "",
# 			"ttl": 200,
# 			"credit_life": "",
# 			"msrp": null,
# 			"residence_time": "2015-06-01T11:27:48.507402",
# 			"job_time": "15-06",
# 			"dealer_check": 123.45,
# 			"min_cash_down": 123,
# 			"dlr_reserve_bonus_amt": 12,
# 			"sell_rate": 12.3,
# 			"flat_incentive": 123,
# 			"certified_used_tf": "N"
# 		}
# 	}
# }"""
# print(type(x))
# print("@"*100)
# y = json.loads(x)
# print(y["dt_application"].get("decision_data", {}))


data = """
{
    "applicant": {
        "currentEmployment": {
            "employerName": "Walmart",
            "occupation": "Construction",
            "status": "Employed",
            "totalMonthsEmployed": 197,
            "workPhone": "5169697934",
            "employerAddress": {}
        },
        "housingStatus": "OwnOutright",
        "mortgageOrRentAmount": 1657,
        "otherMonthlyIncome": 118,
        "previousEmployment": {
            "employerAddress": {}
        },
        "lastName": "Somani",
        "spouse": {
            "address": {}
        },
        "email": "ketansomani@email.com",
        "firstName": "Ketan",
        "otherPhone": "3369865379",
        "otherMonthlyIncomeSource": "Insurance Settlement",
        "phone": "3368566631",
        "relationship": "Self",
        "income": 2814,
        "address": {
            "city": "Castle Hayne",
            "line1": "78 Palace Court",
            "postalCode": "28429",
            "state": "NC"
        },
        "monthsAtCurrentAddress": 125,
        "incomeFrequency": "Weekly"
    },
    "targetPlatforms": [
        {
            "partyId": "1043340",
            "id": "DTC"
        }
    ],
    "customerType": "Individual",
    "sourcePartnerId": "DWR",
    "financeMethod": "Finance",
    "extraData": [
        {
            "name": "OTDXDCMB01",
            "value": "CustomValue-SOJCD165"
        },
        {
            "name": "OTDXDCMB02",
            "value": "CustomValue-SOJCD165"
        }
    ],
    "financeSummary": {
        "vehicleSellingPrice": 20000,
        "amountFinanced": 19000,
        "invoiceAmount": 400,
        "mileage": 34,
        "requestedAPR": 1.99,
        "term": 44,
        "governmentFees": 200,
        "salesTax": 800
    },
    "vehicle": {
        "otherYear": 2013,
        "inventoryVehicleCondition": "New",
        "odometerType": "Miles",
        "odometerReading": 34,
        "stockNumber": "932YCHY7",
        "otherModel": "Escape",
        "otherMake": "Ford",
        "otherTrim": "FWD 4dr Limited"
    }
}
"""
import ast
import re


def convert_str_to_number(value):
    """
    converts string value to corresponding literal value(integer or float ), else return value
    :param value: value to be processed
    :return: integer or float value
    """
    try:
        if value and isinstance(value, str):
            value = re.sub("[%$~]", "", value)
            value = "0" if re.match("^0*$", value) else value.lstrip("0")
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value


TEST_MAPPING = {
    "ketan": OptionalS("name")
}


DEAL_DATA_FIELDS_MAPPING = {
    "requestedAmountFinanced": OptionalS("amountFinanced") >> F(convert_str_to_number),
    "requestedAdjustedCapitalizedCost": OptionalS("adjustedCapitalizedCost") >> F(convert_str_to_number),
    "requestedTerm": OptionalS("term") >> F(convert_str_to_number),
    "requestedAPR": OptionalS("requestedAPR") >> F(convert_str_to_number),
    "requestedMonthlyPayment": OptionalS("estimatedPayment") >> F(convert_str_to_number),
    "financeDetails" if OptionalS("requestedAPR") == 1.98 else None: None,
    "data": TEST_MAPPING
}

result = bend(DEAL_DATA_FIELDS_MAPPING, ast.literal_eval(data).get("financeSummary"))
print(json.dumps(result))
#
# MAP = {
#     "dealType": OptionalS("type"),
#     "financeDetails" if str(OptionalS("type")) == "undecided" else None: None
# }
# res = bend(MAP, {"type": "undecided"})
# print(res)
