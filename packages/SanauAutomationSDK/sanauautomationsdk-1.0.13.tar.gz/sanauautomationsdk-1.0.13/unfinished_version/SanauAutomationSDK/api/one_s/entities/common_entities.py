from .ODataEntity import ODataEntity


class AdvanceReport(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "АвансовыйОтчет"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class BuyersPaymentByPaymentCard(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ОплатаОтПокупателяПлатежнойКартой"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class BuyersReturnOfGoods(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ВозвратТоваровОтПокупателя"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class Declaration(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ЗаявлениеОВвозеТоваровИУплатеКосвенныхНалогов"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class ElectronicInvoice(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ЭСФ"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class FixedAssetsTransfer(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПередачаОС"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class IdentityDocumentType(ODataEntity):
    PREFIX_NAME = "Catalog"
    OBJECT_CONFIG_NAME = "ДокументыУдостоверяющиеЛичность"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class IncomingCashOrder(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПриходныйКассовыйОрдер"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class IntangibleAssetsTransfer(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПередачаНМА"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class ReceivedInvoice(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "СчетФактураПолученный"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class IPNType(ODataEntity):
    PREFIX_NAME = "Catalog"
    OBJECT_CONFIG_NAME = "ВычетыИПН"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class IssuedInvoice(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "СчетФактураВыданный"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class IssuedInvoiceBasedDocument(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "СчетФактураВыданный_ДокументыОснования"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class OutgoingCashOrder(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "РасходныйКассовыйОрдер"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class PaymentOrderReceiptOfFund(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПлатежныйОрдерПоступлениеДенежныхСредств"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class PaymentOrderWithdrawalOfFund(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПлатежныйОрдерСписаниеДенежныхСредств"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class PurchaseOfAdditionalExpense(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПоступлениеДопРасходов"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class PurchaseOfGoodAndService(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ПоступлениеТоваровУслуг"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class RefundOfGoodAndService(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "ВозвратТоваровОтПокупателя"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class SaleOfGoodAndService(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "РеализацияТоваровУслуг"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class SaleProduct(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "РеализацияТоваровУслуг_Товары"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class SaleService(ODataEntity):
    PREFIX_NAME = "Document"
    OBJECT_CONFIG_NAME = "РеализацияТоваровУслуг_Услуги"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class TaxAccountingPolicy(ODataEntity):
    PREFIX_NAME = "InformationRegister"
    OBJECT_CONFIG_NAME = "УчетнаяПолитикаНалоговыйУчет"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class TaxAccountingType(ODataEntity):
    PREFIX_NAME = "Catalog"
    OBJECT_CONFIG_NAME = "ВидыУчетаНУ"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class TaxingChartOfAccount(ODataEntity):
    PREFIX_NAME = "ChartOfAccounts"
    OBJECT_CONFIG_NAME = "Налоговый"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)


class VatRate(ODataEntity):
    PREFIX_NAME = "Catalog"
    OBJECT_CONFIG_NAME = "СтавкиНДС"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)

