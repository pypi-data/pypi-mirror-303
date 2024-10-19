# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BI.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x42I.proto\x12\x02\x42I\"f\n\x1bValidateSessionTokenRequest\x12\x1d\n\x15\x65ncryptedSessionToken\x18\x01 \x01(\x0c\x12\x1c\n\x14returnMcEnterpiseIds\x18\x02 \x01(\x08\x12\n\n\x02ip\x18\x03 \x01(\t\"\xda\x02\n\x1cValidateSessionTokenResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\x18\n\x10\x65nterpriseUserId\x18\x03 \x01(\x03\x12\x37\n\x06status\x18\x04 \x01(\x0e\x32\'.BI.ValidateSessionTokenResponse.Status\x12\x15\n\rstatusMessage\x18\x05 \x01(\t\x12\x17\n\x0fmcEnterpriseIds\x18\x06 \x03(\x05\x12\x18\n\x10hasMSPPermission\x18\x07 \x01(\x08\x12\x1e\n\x16\x64\x65letedMcEnterpriseIds\x18\x08 \x03(\x05\"[\n\x06Status\x12\t\n\x05VALID\x10\x00\x12\r\n\tNOT_VALID\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02\x12\x0e\n\nIP_BLOCKED\x10\x03\x12\x1a\n\x16INVALID_CLIENT_VERSION\x10\x04\"\x1b\n\x19SubscriptionStatusRequest\"\xaf\x02\n\x1aSubscriptionStatusResponse\x12$\n\x0b\x61utoRenewal\x18\x01 \x01(\x0b\x32\x0f.BI.AutoRenewal\x12/\n\x14\x63urrentPaymentMethod\x18\x02 \x01(\x0b\x32\x11.BI.PaymentMethod\x12\x14\n\x0c\x63heckoutLink\x18\x03 \x01(\t\x12\x19\n\x11licenseCreateDate\x18\x04 \x01(\x03\x12\x15\n\risDistributor\x18\x05 \x01(\x08\x12\x13\n\x0bisLegacyMsp\x18\x06 \x01(\x08\x12&\n\x0clicenseStats\x18\x08 \x03(\x0b\x32\x10.BI.LicenseStats\x12\x35\n\x0egradientStatus\x18\t \x01(\x0e\x32\x1d.BI.GradientIntegrationStatus\"\xd7\x01\n\x0cLicenseStats\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.BI.LicenseStats.Type\x12\x11\n\tavailable\x18\x02 \x01(\x05\x12\x0c\n\x04used\x18\x03 \x01(\x05\"\x80\x01\n\x04Type\x12\x18\n\x14LICENSE_STAT_UNKNOWN\x10\x00\x12\x0c\n\x08MSP_BASE\x10\x01\x12\x0f\n\x0bMC_BUSINESS\x10\x02\x12\x14\n\x10MC_BUSINESS_PLUS\x10\x03\x12\x11\n\rMC_ENTERPRISE\x10\x04\x12\x16\n\x12MC_ENTERPRISE_PLUS\x10\x05\"@\n\x0b\x41utoRenewal\x12\x0e\n\x06nextOn\x18\x01 \x01(\x03\x12\x10\n\x08\x64\x61ysLeft\x18\x02 \x01(\x05\x12\x0f\n\x07isTrial\x18\x03 \x01(\x08\"\x84\x04\n\rPaymentMethod\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.BI.PaymentMethod.Type\x12$\n\x04\x63\x61rd\x18\x02 \x01(\x0b\x32\x16.BI.PaymentMethod.Card\x12$\n\x04sepa\x18\x03 \x01(\x0b\x32\x16.BI.PaymentMethod.Sepa\x12(\n\x06paypal\x18\x04 \x01(\x0b\x32\x18.BI.PaymentMethod.Paypal\x12\x15\n\rfailedBilling\x18\x05 \x01(\x08\x12(\n\x06vendor\x18\x06 \x01(\x0b\x32\x18.BI.PaymentMethod.Vendor\x12\x36\n\rpurchaseOrder\x18\x07 \x01(\x0b\x32\x1f.BI.PaymentMethod.PurchaseOrder\x1a$\n\x04\x43\x61rd\x12\r\n\x05last4\x18\x01 \x01(\t\x12\r\n\x05\x62rand\x18\x02 \x01(\t\x1a&\n\x04Sepa\x12\r\n\x05last4\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x1a\x08\n\x06Paypal\x1a\x16\n\x06Vendor\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x1d\n\rPurchaseOrder\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x04Type\x12\x08\n\x04\x43\x41RD\x10\x00\x12\x08\n\x04SEPA\x10\x01\x12\n\n\x06PAYPAL\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\n\n\x06VENDOR\x10\x04\x12\x11\n\rPURCHASEORDER\x10\x05\"\x1f\n\x1dSubscriptionMspPricingRequest\"\\\n\x1eSubscriptionMspPricingResponse\x12\x19\n\x06\x61\x64\x64ons\x18\x02 \x03(\x0b\x32\t.BI.Addon\x12\x1f\n\tfilePlans\x18\x03 \x03(\x0b\x32\x0c.BI.FilePlan\"\x1e\n\x1cSubscriptionMcPricingRequest\"|\n\x1dSubscriptionMcPricingResponse\x12\x1f\n\tbasePlans\x18\x01 \x03(\x0b\x32\x0c.BI.BasePlan\x12\x19\n\x06\x61\x64\x64ons\x18\x02 \x03(\x0b\x32\t.BI.Addon\x12\x1f\n\tfilePlans\x18\x03 \x03(\x0b\x32\x0c.BI.FilePlan\".\n\x08\x42\x61sePlan\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x08.BI.Cost\"C\n\x05\x41\x64\x64on\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x08.BI.Cost\x12\x16\n\x0e\x61mountConsumed\x18\x03 \x01(\x03\".\n\x08\x46ilePlan\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x08.BI.Cost\"\xab\x01\n\x04\x43ost\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\x12%\n\tamountPer\x18\x04 \x01(\x0e\x32\x12.BI.Cost.AmountPer\x12\x1e\n\x08\x63urrency\x18\x05 \x01(\x0e\x32\x0c.BI.Currency\"L\n\tAmountPer\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05MONTH\x10\x01\x12\x0e\n\nUSER_MONTH\x10\x02\x12\x17\n\x13USER_CONSUMED_MONTH\x10\x03\"=\n\x14InvoiceSearchRequest\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x17\n\x0fstartingAfterId\x18\x02 \x01(\x05\"6\n\x15InvoiceSearchResponse\x12\x1d\n\x08invoices\x18\x01 \x03(\x0b\x32\x0b.BI.Invoice\"\xbe\x02\n\x07Invoice\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rinvoiceNumber\x18\x02 \x01(\t\x12\x13\n\x0binvoiceDate\x18\x03 \x01(\x03\x12\x14\n\x0clicenseCount\x18\x04 \x01(\x05\x12#\n\ttotalCost\x18\x05 \x01(\x0b\x32\x10.BI.Invoice.Cost\x12%\n\x0binvoiceType\x18\x06 \x01(\x0e\x32\x10.BI.Invoice.Type\x1a\x36\n\x04\x43ost\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x01\x12\x1e\n\x08\x63urrency\x18\x02 \x01(\x0e\x32\x0c.BI.Currency\"a\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x0b\n\x07RENEWAL\x10\x02\x12\x0b\n\x07UPGRADE\x10\x03\x12\x0b\n\x07RESTORE\x10\x04\x12\x0f\n\x0b\x41SSOCIATION\x10\x05\x12\x0b\n\x07OVERAGE\x10\x06\"/\n\x16InvoiceDownloadRequest\x12\x15\n\rinvoiceNumber\x18\x01 \x01(\t\"9\n\x17InvoiceDownloadResponse\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\"<\n\x1dReportingDailySnapshotRequest\x12\r\n\x05month\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x05\"v\n\x1eReportingDailySnapshotResponse\x12#\n\x07records\x18\x01 \x03(\x0b\x32\x12.BI.SnapshotRecord\x12/\n\rmcEnterprises\x18\x02 \x03(\x0b\x32\x18.BI.SnapshotMcEnterprise\"\xd7\x01\n\x0eSnapshotRecord\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\x03\x12\x16\n\x0emcEnterpriseId\x18\x02 \x01(\x05\x12\x17\n\x0fmaxLicenseCount\x18\x04 \x01(\x05\x12\x19\n\x11maxFilePlanTypeId\x18\x05 \x01(\x05\x12\x15\n\rmaxBasePlanId\x18\x06 \x01(\x05\x12(\n\x06\x61\x64\x64ons\x18\x07 \x03(\x0b\x32\x18.BI.SnapshotRecord.Addon\x1a*\n\x05\x41\x64\x64on\x12\x12\n\nmaxAddonId\x18\x01 \x01(\x05\x12\r\n\x05units\x18\x02 \x01(\x03\"0\n\x14SnapshotMcEnterprise\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x16\n\x14MappingAddonsRequest\"\\\n\x15MappingAddonsResponse\x12\x1f\n\x06\x61\x64\x64ons\x18\x01 \x03(\x0b\x32\x0f.BI.MappingItem\x12\"\n\tfilePlans\x18\x02 \x03(\x0b\x32\x0f.BI.MappingItem\"\'\n\x0bMappingItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"1\n\x1aGradientValidateKeyRequest\x12\x13\n\x0bgradientKey\x18\x01 \x01(\t\"?\n\x1bGradientValidateKeyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"E\n\x19GradientAddServiceRequest\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x13\n\x0bserviceDesc\x18\x02 \x01(\t\">\n\x1aGradientAddServiceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"D\n\x13GradientSaveRequest\x12\x13\n\x0bgradientKey\x18\x01 \x01(\t\x12\x18\n\x10\x65nterpriseUserId\x18\x02 \x01(\x03\"g\n\x14GradientSaveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12-\n\x06status\x18\x02 \x01(\x0e\x32\x1d.BI.GradientIntegrationStatus\x12\x0f\n\x07message\x18\x03 \x01(\t\"1\n\x15GradientRemoveRequest\x12\x18\n\x10\x65nterpriseUserId\x18\x01 \x01(\x03\":\n\x16GradientRemoveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"/\n\x13GradientSyncRequest\x12\x18\n\x10\x65nterpriseUserId\x18\x01 \x01(\x03\"g\n\x14GradientSyncResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12-\n\x06status\x18\x02 \x01(\x0e\x32\x1d.BI.GradientIntegrationStatus\x12\x0f\n\x07message\x18\x03 \x01(\t*D\n\x08\x43urrency\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03USD\x10\x01\x12\x07\n\x03GBP\x10\x02\x12\x07\n\x03JPY\x10\x03\x12\x07\n\x03\x45UR\x10\x04\x12\x07\n\x03\x41UD\x10\x05*S\n\x19GradientIntegrationStatus\x12\x10\n\x0cNOTCONNECTED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tCONNECTED\x10\x02\x12\x08\n\x04NONE\x10\x03\x42\x1e\n\x18\x63om.keepersecurity.protoB\x02\x42Ib\x06proto3')

_CURRENCY = DESCRIPTOR.enum_types_by_name['Currency']
Currency = enum_type_wrapper.EnumTypeWrapper(_CURRENCY)
_GRADIENTINTEGRATIONSTATUS = DESCRIPTOR.enum_types_by_name['GradientIntegrationStatus']
GradientIntegrationStatus = enum_type_wrapper.EnumTypeWrapper(_GRADIENTINTEGRATIONSTATUS)
UNKNOWN = 0
USD = 1
GBP = 2
JPY = 3
EUR = 4
AUD = 5
NOTCONNECTED = 0
PENDING = 1
CONNECTED = 2
NONE = 3


_VALIDATESESSIONTOKENREQUEST = DESCRIPTOR.message_types_by_name['ValidateSessionTokenRequest']
_VALIDATESESSIONTOKENRESPONSE = DESCRIPTOR.message_types_by_name['ValidateSessionTokenResponse']
_SUBSCRIPTIONSTATUSREQUEST = DESCRIPTOR.message_types_by_name['SubscriptionStatusRequest']
_SUBSCRIPTIONSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['SubscriptionStatusResponse']
_LICENSESTATS = DESCRIPTOR.message_types_by_name['LicenseStats']
_AUTORENEWAL = DESCRIPTOR.message_types_by_name['AutoRenewal']
_PAYMENTMETHOD = DESCRIPTOR.message_types_by_name['PaymentMethod']
_PAYMENTMETHOD_CARD = _PAYMENTMETHOD.nested_types_by_name['Card']
_PAYMENTMETHOD_SEPA = _PAYMENTMETHOD.nested_types_by_name['Sepa']
_PAYMENTMETHOD_PAYPAL = _PAYMENTMETHOD.nested_types_by_name['Paypal']
_PAYMENTMETHOD_VENDOR = _PAYMENTMETHOD.nested_types_by_name['Vendor']
_PAYMENTMETHOD_PURCHASEORDER = _PAYMENTMETHOD.nested_types_by_name['PurchaseOrder']
_SUBSCRIPTIONMSPPRICINGREQUEST = DESCRIPTOR.message_types_by_name['SubscriptionMspPricingRequest']
_SUBSCRIPTIONMSPPRICINGRESPONSE = DESCRIPTOR.message_types_by_name['SubscriptionMspPricingResponse']
_SUBSCRIPTIONMCPRICINGREQUEST = DESCRIPTOR.message_types_by_name['SubscriptionMcPricingRequest']
_SUBSCRIPTIONMCPRICINGRESPONSE = DESCRIPTOR.message_types_by_name['SubscriptionMcPricingResponse']
_BASEPLAN = DESCRIPTOR.message_types_by_name['BasePlan']
_ADDON = DESCRIPTOR.message_types_by_name['Addon']
_FILEPLAN = DESCRIPTOR.message_types_by_name['FilePlan']
_COST = DESCRIPTOR.message_types_by_name['Cost']
_INVOICESEARCHREQUEST = DESCRIPTOR.message_types_by_name['InvoiceSearchRequest']
_INVOICESEARCHRESPONSE = DESCRIPTOR.message_types_by_name['InvoiceSearchResponse']
_INVOICE = DESCRIPTOR.message_types_by_name['Invoice']
_INVOICE_COST = _INVOICE.nested_types_by_name['Cost']
_INVOICEDOWNLOADREQUEST = DESCRIPTOR.message_types_by_name['InvoiceDownloadRequest']
_INVOICEDOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name['InvoiceDownloadResponse']
_REPORTINGDAILYSNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name['ReportingDailySnapshotRequest']
_REPORTINGDAILYSNAPSHOTRESPONSE = DESCRIPTOR.message_types_by_name['ReportingDailySnapshotResponse']
_SNAPSHOTRECORD = DESCRIPTOR.message_types_by_name['SnapshotRecord']
_SNAPSHOTRECORD_ADDON = _SNAPSHOTRECORD.nested_types_by_name['Addon']
_SNAPSHOTMCENTERPRISE = DESCRIPTOR.message_types_by_name['SnapshotMcEnterprise']
_MAPPINGADDONSREQUEST = DESCRIPTOR.message_types_by_name['MappingAddonsRequest']
_MAPPINGADDONSRESPONSE = DESCRIPTOR.message_types_by_name['MappingAddonsResponse']
_MAPPINGITEM = DESCRIPTOR.message_types_by_name['MappingItem']
_GRADIENTVALIDATEKEYREQUEST = DESCRIPTOR.message_types_by_name['GradientValidateKeyRequest']
_GRADIENTVALIDATEKEYRESPONSE = DESCRIPTOR.message_types_by_name['GradientValidateKeyResponse']
_GRADIENTADDSERVICEREQUEST = DESCRIPTOR.message_types_by_name['GradientAddServiceRequest']
_GRADIENTADDSERVICERESPONSE = DESCRIPTOR.message_types_by_name['GradientAddServiceResponse']
_GRADIENTSAVEREQUEST = DESCRIPTOR.message_types_by_name['GradientSaveRequest']
_GRADIENTSAVERESPONSE = DESCRIPTOR.message_types_by_name['GradientSaveResponse']
_GRADIENTREMOVEREQUEST = DESCRIPTOR.message_types_by_name['GradientRemoveRequest']
_GRADIENTREMOVERESPONSE = DESCRIPTOR.message_types_by_name['GradientRemoveResponse']
_GRADIENTSYNCREQUEST = DESCRIPTOR.message_types_by_name['GradientSyncRequest']
_GRADIENTSYNCRESPONSE = DESCRIPTOR.message_types_by_name['GradientSyncResponse']
_VALIDATESESSIONTOKENRESPONSE_STATUS = _VALIDATESESSIONTOKENRESPONSE.enum_types_by_name['Status']
_LICENSESTATS_TYPE = _LICENSESTATS.enum_types_by_name['Type']
_PAYMENTMETHOD_TYPE = _PAYMENTMETHOD.enum_types_by_name['Type']
_COST_AMOUNTPER = _COST.enum_types_by_name['AmountPer']
_INVOICE_TYPE = _INVOICE.enum_types_by_name['Type']
ValidateSessionTokenRequest = _reflection.GeneratedProtocolMessageType('ValidateSessionTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATESESSIONTOKENREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ValidateSessionTokenRequest)
  })
_sym_db.RegisterMessage(ValidateSessionTokenRequest)

ValidateSessionTokenResponse = _reflection.GeneratedProtocolMessageType('ValidateSessionTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATESESSIONTOKENRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ValidateSessionTokenResponse)
  })
_sym_db.RegisterMessage(ValidateSessionTokenResponse)

SubscriptionStatusRequest = _reflection.GeneratedProtocolMessageType('SubscriptionStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONSTATUSREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionStatusRequest)
  })
_sym_db.RegisterMessage(SubscriptionStatusRequest)

SubscriptionStatusResponse = _reflection.GeneratedProtocolMessageType('SubscriptionStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONSTATUSRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionStatusResponse)
  })
_sym_db.RegisterMessage(SubscriptionStatusResponse)

LicenseStats = _reflection.GeneratedProtocolMessageType('LicenseStats', (_message.Message,), {
  'DESCRIPTOR' : _LICENSESTATS,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.LicenseStats)
  })
_sym_db.RegisterMessage(LicenseStats)

AutoRenewal = _reflection.GeneratedProtocolMessageType('AutoRenewal', (_message.Message,), {
  'DESCRIPTOR' : _AUTORENEWAL,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.AutoRenewal)
  })
_sym_db.RegisterMessage(AutoRenewal)

PaymentMethod = _reflection.GeneratedProtocolMessageType('PaymentMethod', (_message.Message,), {

  'Card' : _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_CARD,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Card)
    })
  ,

  'Sepa' : _reflection.GeneratedProtocolMessageType('Sepa', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_SEPA,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Sepa)
    })
  ,

  'Paypal' : _reflection.GeneratedProtocolMessageType('Paypal', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_PAYPAL,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Paypal)
    })
  ,

  'Vendor' : _reflection.GeneratedProtocolMessageType('Vendor', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_VENDOR,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Vendor)
    })
  ,

  'PurchaseOrder' : _reflection.GeneratedProtocolMessageType('PurchaseOrder', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_PURCHASEORDER,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.PurchaseOrder)
    })
  ,
  'DESCRIPTOR' : _PAYMENTMETHOD,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.PaymentMethod)
  })
_sym_db.RegisterMessage(PaymentMethod)
_sym_db.RegisterMessage(PaymentMethod.Card)
_sym_db.RegisterMessage(PaymentMethod.Sepa)
_sym_db.RegisterMessage(PaymentMethod.Paypal)
_sym_db.RegisterMessage(PaymentMethod.Vendor)
_sym_db.RegisterMessage(PaymentMethod.PurchaseOrder)

SubscriptionMspPricingRequest = _reflection.GeneratedProtocolMessageType('SubscriptionMspPricingRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMSPPRICINGREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMspPricingRequest)
  })
_sym_db.RegisterMessage(SubscriptionMspPricingRequest)

SubscriptionMspPricingResponse = _reflection.GeneratedProtocolMessageType('SubscriptionMspPricingResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMSPPRICINGRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMspPricingResponse)
  })
_sym_db.RegisterMessage(SubscriptionMspPricingResponse)

SubscriptionMcPricingRequest = _reflection.GeneratedProtocolMessageType('SubscriptionMcPricingRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMCPRICINGREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMcPricingRequest)
  })
_sym_db.RegisterMessage(SubscriptionMcPricingRequest)

SubscriptionMcPricingResponse = _reflection.GeneratedProtocolMessageType('SubscriptionMcPricingResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMCPRICINGRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMcPricingResponse)
  })
_sym_db.RegisterMessage(SubscriptionMcPricingResponse)

BasePlan = _reflection.GeneratedProtocolMessageType('BasePlan', (_message.Message,), {
  'DESCRIPTOR' : _BASEPLAN,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.BasePlan)
  })
_sym_db.RegisterMessage(BasePlan)

Addon = _reflection.GeneratedProtocolMessageType('Addon', (_message.Message,), {
  'DESCRIPTOR' : _ADDON,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.Addon)
  })
_sym_db.RegisterMessage(Addon)

FilePlan = _reflection.GeneratedProtocolMessageType('FilePlan', (_message.Message,), {
  'DESCRIPTOR' : _FILEPLAN,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.FilePlan)
  })
_sym_db.RegisterMessage(FilePlan)

Cost = _reflection.GeneratedProtocolMessageType('Cost', (_message.Message,), {
  'DESCRIPTOR' : _COST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.Cost)
  })
_sym_db.RegisterMessage(Cost)

InvoiceSearchRequest = _reflection.GeneratedProtocolMessageType('InvoiceSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOICESEARCHREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceSearchRequest)
  })
_sym_db.RegisterMessage(InvoiceSearchRequest)

InvoiceSearchResponse = _reflection.GeneratedProtocolMessageType('InvoiceSearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOICESEARCHRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceSearchResponse)
  })
_sym_db.RegisterMessage(InvoiceSearchResponse)

Invoice = _reflection.GeneratedProtocolMessageType('Invoice', (_message.Message,), {

  'Cost' : _reflection.GeneratedProtocolMessageType('Cost', (_message.Message,), {
    'DESCRIPTOR' : _INVOICE_COST,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.Invoice.Cost)
    })
  ,
  'DESCRIPTOR' : _INVOICE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.Invoice)
  })
_sym_db.RegisterMessage(Invoice)
_sym_db.RegisterMessage(Invoice.Cost)

InvoiceDownloadRequest = _reflection.GeneratedProtocolMessageType('InvoiceDownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEDOWNLOADREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceDownloadRequest)
  })
_sym_db.RegisterMessage(InvoiceDownloadRequest)

InvoiceDownloadResponse = _reflection.GeneratedProtocolMessageType('InvoiceDownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEDOWNLOADRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceDownloadResponse)
  })
_sym_db.RegisterMessage(InvoiceDownloadResponse)

ReportingDailySnapshotRequest = _reflection.GeneratedProtocolMessageType('ReportingDailySnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTINGDAILYSNAPSHOTREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ReportingDailySnapshotRequest)
  })
_sym_db.RegisterMessage(ReportingDailySnapshotRequest)

ReportingDailySnapshotResponse = _reflection.GeneratedProtocolMessageType('ReportingDailySnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTINGDAILYSNAPSHOTRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ReportingDailySnapshotResponse)
  })
_sym_db.RegisterMessage(ReportingDailySnapshotResponse)

SnapshotRecord = _reflection.GeneratedProtocolMessageType('SnapshotRecord', (_message.Message,), {

  'Addon' : _reflection.GeneratedProtocolMessageType('Addon', (_message.Message,), {
    'DESCRIPTOR' : _SNAPSHOTRECORD_ADDON,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.SnapshotRecord.Addon)
    })
  ,
  'DESCRIPTOR' : _SNAPSHOTRECORD,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SnapshotRecord)
  })
_sym_db.RegisterMessage(SnapshotRecord)
_sym_db.RegisterMessage(SnapshotRecord.Addon)

SnapshotMcEnterprise = _reflection.GeneratedProtocolMessageType('SnapshotMcEnterprise', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTMCENTERPRISE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SnapshotMcEnterprise)
  })
_sym_db.RegisterMessage(SnapshotMcEnterprise)

MappingAddonsRequest = _reflection.GeneratedProtocolMessageType('MappingAddonsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAPPINGADDONSREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.MappingAddonsRequest)
  })
_sym_db.RegisterMessage(MappingAddonsRequest)

MappingAddonsResponse = _reflection.GeneratedProtocolMessageType('MappingAddonsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAPPINGADDONSRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.MappingAddonsResponse)
  })
_sym_db.RegisterMessage(MappingAddonsResponse)

MappingItem = _reflection.GeneratedProtocolMessageType('MappingItem', (_message.Message,), {
  'DESCRIPTOR' : _MAPPINGITEM,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.MappingItem)
  })
_sym_db.RegisterMessage(MappingItem)

GradientValidateKeyRequest = _reflection.GeneratedProtocolMessageType('GradientValidateKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTVALIDATEKEYREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientValidateKeyRequest)
  })
_sym_db.RegisterMessage(GradientValidateKeyRequest)

GradientValidateKeyResponse = _reflection.GeneratedProtocolMessageType('GradientValidateKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTVALIDATEKEYRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientValidateKeyResponse)
  })
_sym_db.RegisterMessage(GradientValidateKeyResponse)

GradientAddServiceRequest = _reflection.GeneratedProtocolMessageType('GradientAddServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTADDSERVICEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientAddServiceRequest)
  })
_sym_db.RegisterMessage(GradientAddServiceRequest)

GradientAddServiceResponse = _reflection.GeneratedProtocolMessageType('GradientAddServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTADDSERVICERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientAddServiceResponse)
  })
_sym_db.RegisterMessage(GradientAddServiceResponse)

GradientSaveRequest = _reflection.GeneratedProtocolMessageType('GradientSaveRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSAVEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSaveRequest)
  })
_sym_db.RegisterMessage(GradientSaveRequest)

GradientSaveResponse = _reflection.GeneratedProtocolMessageType('GradientSaveResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSAVERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSaveResponse)
  })
_sym_db.RegisterMessage(GradientSaveResponse)

GradientRemoveRequest = _reflection.GeneratedProtocolMessageType('GradientRemoveRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTREMOVEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientRemoveRequest)
  })
_sym_db.RegisterMessage(GradientRemoveRequest)

GradientRemoveResponse = _reflection.GeneratedProtocolMessageType('GradientRemoveResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTREMOVERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientRemoveResponse)
  })
_sym_db.RegisterMessage(GradientRemoveResponse)

GradientSyncRequest = _reflection.GeneratedProtocolMessageType('GradientSyncRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSYNCREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSyncRequest)
  })
_sym_db.RegisterMessage(GradientSyncRequest)

GradientSyncResponse = _reflection.GeneratedProtocolMessageType('GradientSyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSYNCRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSyncResponse)
  })
_sym_db.RegisterMessage(GradientSyncResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.keepersecurity.protoB\002BI'
  _CURRENCY._serialized_start=4079
  _CURRENCY._serialized_end=4147
  _GRADIENTINTEGRATIONSTATUS._serialized_start=4149
  _GRADIENTINTEGRATIONSTATUS._serialized_end=4232
  _VALIDATESESSIONTOKENREQUEST._serialized_start=16
  _VALIDATESESSIONTOKENREQUEST._serialized_end=118
  _VALIDATESESSIONTOKENRESPONSE._serialized_start=121
  _VALIDATESESSIONTOKENRESPONSE._serialized_end=467
  _VALIDATESESSIONTOKENRESPONSE_STATUS._serialized_start=376
  _VALIDATESESSIONTOKENRESPONSE_STATUS._serialized_end=467
  _SUBSCRIPTIONSTATUSREQUEST._serialized_start=469
  _SUBSCRIPTIONSTATUSREQUEST._serialized_end=496
  _SUBSCRIPTIONSTATUSRESPONSE._serialized_start=499
  _SUBSCRIPTIONSTATUSRESPONSE._serialized_end=802
  _LICENSESTATS._serialized_start=805
  _LICENSESTATS._serialized_end=1020
  _LICENSESTATS_TYPE._serialized_start=892
  _LICENSESTATS_TYPE._serialized_end=1020
  _AUTORENEWAL._serialized_start=1022
  _AUTORENEWAL._serialized_end=1086
  _PAYMENTMETHOD._serialized_start=1089
  _PAYMENTMETHOD._serialized_end=1605
  _PAYMENTMETHOD_CARD._serialized_start=1383
  _PAYMENTMETHOD_CARD._serialized_end=1419
  _PAYMENTMETHOD_SEPA._serialized_start=1421
  _PAYMENTMETHOD_SEPA._serialized_end=1459
  _PAYMENTMETHOD_PAYPAL._serialized_start=1461
  _PAYMENTMETHOD_PAYPAL._serialized_end=1469
  _PAYMENTMETHOD_VENDOR._serialized_start=1471
  _PAYMENTMETHOD_VENDOR._serialized_end=1493
  _PAYMENTMETHOD_PURCHASEORDER._serialized_start=1495
  _PAYMENTMETHOD_PURCHASEORDER._serialized_end=1524
  _PAYMENTMETHOD_TYPE._serialized_start=1526
  _PAYMENTMETHOD_TYPE._serialized_end=1605
  _SUBSCRIPTIONMSPPRICINGREQUEST._serialized_start=1607
  _SUBSCRIPTIONMSPPRICINGREQUEST._serialized_end=1638
  _SUBSCRIPTIONMSPPRICINGRESPONSE._serialized_start=1640
  _SUBSCRIPTIONMSPPRICINGRESPONSE._serialized_end=1732
  _SUBSCRIPTIONMCPRICINGREQUEST._serialized_start=1734
  _SUBSCRIPTIONMCPRICINGREQUEST._serialized_end=1764
  _SUBSCRIPTIONMCPRICINGRESPONSE._serialized_start=1766
  _SUBSCRIPTIONMCPRICINGRESPONSE._serialized_end=1890
  _BASEPLAN._serialized_start=1892
  _BASEPLAN._serialized_end=1938
  _ADDON._serialized_start=1940
  _ADDON._serialized_end=2007
  _FILEPLAN._serialized_start=2009
  _FILEPLAN._serialized_end=2055
  _COST._serialized_start=2058
  _COST._serialized_end=2229
  _COST_AMOUNTPER._serialized_start=2153
  _COST_AMOUNTPER._serialized_end=2229
  _INVOICESEARCHREQUEST._serialized_start=2231
  _INVOICESEARCHREQUEST._serialized_end=2292
  _INVOICESEARCHRESPONSE._serialized_start=2294
  _INVOICESEARCHRESPONSE._serialized_end=2348
  _INVOICE._serialized_start=2351
  _INVOICE._serialized_end=2669
  _INVOICE_COST._serialized_start=2516
  _INVOICE_COST._serialized_end=2570
  _INVOICE_TYPE._serialized_start=2572
  _INVOICE_TYPE._serialized_end=2669
  _INVOICEDOWNLOADREQUEST._serialized_start=2671
  _INVOICEDOWNLOADREQUEST._serialized_end=2718
  _INVOICEDOWNLOADRESPONSE._serialized_start=2720
  _INVOICEDOWNLOADRESPONSE._serialized_end=2777
  _REPORTINGDAILYSNAPSHOTREQUEST._serialized_start=2779
  _REPORTINGDAILYSNAPSHOTREQUEST._serialized_end=2839
  _REPORTINGDAILYSNAPSHOTRESPONSE._serialized_start=2841
  _REPORTINGDAILYSNAPSHOTRESPONSE._serialized_end=2959
  _SNAPSHOTRECORD._serialized_start=2962
  _SNAPSHOTRECORD._serialized_end=3177
  _SNAPSHOTRECORD_ADDON._serialized_start=3135
  _SNAPSHOTRECORD_ADDON._serialized_end=3177
  _SNAPSHOTMCENTERPRISE._serialized_start=3179
  _SNAPSHOTMCENTERPRISE._serialized_end=3227
  _MAPPINGADDONSREQUEST._serialized_start=3229
  _MAPPINGADDONSREQUEST._serialized_end=3251
  _MAPPINGADDONSRESPONSE._serialized_start=3253
  _MAPPINGADDONSRESPONSE._serialized_end=3345
  _MAPPINGITEM._serialized_start=3347
  _MAPPINGITEM._serialized_end=3386
  _GRADIENTVALIDATEKEYREQUEST._serialized_start=3388
  _GRADIENTVALIDATEKEYREQUEST._serialized_end=3437
  _GRADIENTVALIDATEKEYRESPONSE._serialized_start=3439
  _GRADIENTVALIDATEKEYRESPONSE._serialized_end=3502
  _GRADIENTADDSERVICEREQUEST._serialized_start=3504
  _GRADIENTADDSERVICEREQUEST._serialized_end=3573
  _GRADIENTADDSERVICERESPONSE._serialized_start=3575
  _GRADIENTADDSERVICERESPONSE._serialized_end=3637
  _GRADIENTSAVEREQUEST._serialized_start=3639
  _GRADIENTSAVEREQUEST._serialized_end=3707
  _GRADIENTSAVERESPONSE._serialized_start=3709
  _GRADIENTSAVERESPONSE._serialized_end=3812
  _GRADIENTREMOVEREQUEST._serialized_start=3814
  _GRADIENTREMOVEREQUEST._serialized_end=3863
  _GRADIENTREMOVERESPONSE._serialized_start=3865
  _GRADIENTREMOVERESPONSE._serialized_end=3923
  _GRADIENTSYNCREQUEST._serialized_start=3925
  _GRADIENTSYNCREQUEST._serialized_end=3972
  _GRADIENTSYNCRESPONSE._serialized_start=3974
  _GRADIENTSYNCRESPONSE._serialized_end=4077
# @@protoc_insertion_point(module_scope)
