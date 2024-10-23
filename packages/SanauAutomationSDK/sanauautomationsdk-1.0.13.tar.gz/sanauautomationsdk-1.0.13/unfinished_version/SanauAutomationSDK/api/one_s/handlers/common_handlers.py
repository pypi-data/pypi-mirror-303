from .ODataHandler import ODataHandler
from ..entities.common_entities import *
from ....classes.OneSApiCredentials import OneSApiCredentials


class AdvanceReportsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=AdvanceReport(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class BuyersPaymentByPaymentCardsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=BuyersPaymentByPaymentCard(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class BuyersReturnOfGoodsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=BuyersReturnOfGoods(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class DeclarationsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=Declaration(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class ElectronicInvoicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=ElectronicInvoice(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class FixedAssetsTransfersHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=FixedAssetsTransfer(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class IdentityDocumentTypesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=IdentityDocumentType(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class IncomingCashOrdersHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=IncomingCashOrder(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class IntangibleAssetsTransfersHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=IntangibleAssetsTransfer(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class ReceivedInvoicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=ReceivedInvoice(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class IPNTypesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=IPNType(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class IssuedInvoicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=IssuedInvoice(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class IssuedInvoiceBasedDocumentsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=IssuedInvoiceBasedDocument(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class OutgoingCashOrdersHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=OutgoingCashOrder(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class PaymentOrderReceiptOfFundsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=PaymentOrderReceiptOfFund(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class PaymentOrderWithdrawalOfFundsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=PaymentOrderWithdrawalOfFund(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class PurchaseOfAdditionalExpensesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=PurchaseOfAdditionalExpense(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class PurchaseOfGoodAndServicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=PurchaseOfGoodAndService(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class RefundOfGoodAndServicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=RefundOfGoodAndService(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class SaleOfGoodAndServicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=SaleOfGoodAndService(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class SaleProductsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=SaleProduct(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class SaleServicesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=SaleService(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class TaxAccountingPoliciesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=TaxAccountingPolicy(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class TaxAccountingTypesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=TaxAccountingType(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class TaxingChartOfAccountsHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=TaxingChartOfAccount(database_name, server), api_wrapper=api_wrapper, credentials=credentials)


class VatRatesHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=VatRate(database_name, server), api_wrapper=api_wrapper, credentials=credentials)
