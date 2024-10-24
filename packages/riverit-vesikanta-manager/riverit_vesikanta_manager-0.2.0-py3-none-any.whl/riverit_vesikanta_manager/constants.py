# Config
WATER_FORM_CONFIG = "vesihuollon_lomakkeet_config"
BILLING_CONFIG = "kulutusweb-vesikanta_config"

# Vesikanta main window
MAIN_WND = 'class:"Gupta:AccFrame" and regex:"Jämsän Vesi Liikelaitos*"'
MAIN_NAVBAR = 'automationid:"4097"'
OK_BTN = 'class:"Button" and name:"OK"'

# Vesikanta login window
# NOTE: The login window is separate from the main window, and has no title (=window-name) -attribute. The login window is identified by its main class element.
LOGIN_WND = 'class:"Gupta:AccFrame"'
USERNAME_FLD = 'class:"Edit" and name:"Käyttäjätunnus "'
PASSWORD_FLD = 'class:"Edit" and name:"Salasana "'
DATABASE_DIALOG = 'control:"WindowControl" and name:"Tietokanta"'
DB_DIALOG_CANCEL_BUTTON = 'class:"Button" and name:"Cancel"'

# Lukemien tuonti -window
LUKEMATIEDOT_WND = 'class:"Gupta:AccFrame" and name:" Lukematiedot tietokantaan"'
VESIKANTA_INPUT_FILE_FLD = 'class:"Edit" and name:"Valittu tiedosto: "'
LUE_LUKEMAT_SISAAN_BTN = 'class:"Button" and name:"Lue lukemat sisään"'
LUKEMIEN_SIIRTO_DLG = 'class:"#32770" and name:"Lukemien siirto"'
DONT_UPDATE_YEARLY_CONSUMPTION_CHECKBOX = (
    'class:"Gupta:GPCheck" and name:"Vuosikulutusarviota ei päivitetä!"'
)

# Exception dialog class with variable name
LUKEMIEN_TUONTI_DLG = 'class:"#32770" and name:" Lukemien tuonti Vesikantaan"'
REPORT_TO_FILE_BTN = 'class:"Button" and name:"Raportti tiedostoon"'
SAVE_CSV_WND = 'class:"#32770" and name:"Tiedoston tallennus"'
SAVE_CSV_NAME_FLD = 'class:"Edit" and name:"Tiedostonimi:"'
SAVE_CSV_FILE_BTN = 'class:"Button" and name:"Tallenna"'
SAVE_CSV_CONFIRM_DLG = 'class:"#32770" and name:"Tiedoston tallennus"'
SQL_ERROR_DLG = 'class:"#32770" and name:"SQLWindows"'

# Print report -window
PRINT_REPORT_BTN = 'class:"Button" and name:"Tulosta raportti"'
TULOSTUS_WND = 'class:"Gupta:AccFrame" and name:"TULOSTUS"'
FOLDER_BTN = 'class:"Button" and automationid:"4106"'
PRINT_BTN = 'class:"Button" and name:"Tulosta"'
REPORT_BUILDER_WND = 'class:"AfxFrameOrView110u" and regex:".*Gupta Report Builder*."'
WIN32_PRINT_WND = 'class:"ApplicationFrameWindow" and name:"Tulostetaan Win32-sovelluksesta. – tulosta"'
WIN32_PRINTER_LST = 'class:"ComboBox" and name:"Tulostin"'
PDF_PRINTER = 'name:"Microsoft Print to PDF"'
WIN32_PRINT_BTN = 'class:"Button" and name:"Tulosta"'
SAVE_PDF_WND = 'class:"#32770" and name:"Tallenna tuloste nimellä"'
SAVE_PDF_NAME_FLD = 'class:"Edit" and name:"Tiedostonimi:"'
SAVE_PDF_FILE_BTN = 'class:"Button" and name:"Tallenna"'

# File Explorer -window
FILE_EXPLORER_WND = 'class:"CabinetWClass" and regex:"V:*"'

# Seurantatiedot -window
SEURANTATIEDOT_WND = 'class:"Gupta:AccFrame" and name:"Seurantatietojen keruu"'
TRACKING_GRP_START_FLD = 'class:"Edit" and automationid:"4105"'
TRACKING_GRP_END_FLD = 'class:"Edit" and automationid:"4106"'
PERFORM_BTN = 'class:"Button" and name:"Suorita"'
CONFIMATION_DLG = 'class:"#32770" and name:"Seurantatietojen keruu"'
DATA_COLL_DONE_DLG_TXT = 'class:"Static" and name:"Seurantatietojen keruu suoritettu"'

# Kulutuspiste -window
KULUTUSPISTE_WND = 'class:"Gupta:AccFrame" and regex:"Kulutuspiste*"'
CONSUMPTION_POINT_CODE_FLD = 'class:"Edit" and name:"Kulutuspiste"'
PROPERTY_PROCESSING_BTN = 'class:"Button" and name:"Kiinteistönkäsittely"'
OWNER_INFO_TBL = 'class:"Gupta:ChildTable" and automationid:"4114"'
YEARLY_CONSUMPTION_FIELD = 'class:"Edit" and name:"Vuosikulutusarvio (m3)"'
CONSUMPTION_SAVE_BUTTON = 'class:"Button" and id:"24583"'

# Vesilaitoksen tulot -window
VESILAITOKSEN_TULOT_WND = 'class:"Gupta:AccFrame" and name:"Vesilaitoksen tulot"'
REVENUE_GRP_START_FLD = 'class:"Edit" and automationid:"4098"'
REVENUE_GRP_END_FLD = 'class:"Edit" and automationid:"4100"'
REVENUE_REPORT_TO_CSV_BTN = 'class:"Button" and name:"Tiedostoon "'

# Laskutusraportti laskutetuista -window
LASKUTETUT_WND = 'class:"Gupta:AccFrame" and name:"Laskutusraportti laskutetuista"'
BILLED_GRP_START_FLD = 'class:"Edit" and automationid:"4111"'
BILLED_GRP_END_FLD = 'class:"Edit" and automationid:"4113"'
DATE_OF_ENTRY_START_FLD = 'class:"Edit" and automationid:"4121"'
DATE_OF_ENTRY_END_FLD = 'class:"Edit" and automationid:"4123"'
BILLED_REPORT_TO_CSV_BTN = 'class:"Button" and name:"Tiedostoon "'
BILLED_SAVE_CSV_CONFIRM_DLG = 'class:"#32770" and name:"Laskutusraportit"'
BILLED_YES_BTN = 'class:"Button" and name:"Yes"'
CREATING_FILE_WND = 'class:"Gupta:Dialog" and name:" Siirretään tiedostoon"'

# Web aineisto -window
WEB_AINEISTO_WND = (
    'class:"Gupta:AccFrame" and name:"Tietojen siirto Internet - palveluun"'
)
TRANSFER_BTN = 'class:"Button" and name:"Siirto"'
TRANSFER_DLG = 'class:"#32770" and name:"Tietojen siirto Internet - palveluun"'
TRANFER_DONE_DLG_TXT = 'class:"Static" and name:"Tietojen siirto suoritettu"'

# Asiakastietojen selailu -window
ASIAKASTIETOJEN_SELAILU_WND = (
    'class:"Gupta:AccFrame" and name:"Asiakastietojen selailu"'
)
AS_NAME_FLD = 'class:"Edit" and name:"Nimi"'
AS_ADDRESS_FLD = 'class:"Edit" and name:"Osoite"'
ADD_LIM_CMB = 'class:"ComboBox" and automationid:"4110"'
AS_SEARCH_BTN = 'class:"Button" and name:"Hae"'
AS_SEARCH_RESULTS_TXT = 'control:"TextControl" and regex:"Haettuja rivejä on*"'
AS_SEARCH_RESULTS_TBL = 'class:"Gupta:ChildTable" and automationid:"4097"'
AS_SELECT_BTN = 'class:"Button" and name:"Valinta"'

# Maksajan vaihto -window
MAKSAJAN_VAIHTO_WND = 'class:"Gupta:AccFrame" and name:"Maksajan vaihto "'
CURRENT_PAYER_ADDRESS_FLD = 'class:"Edit" and automationid:"4128"'
CURRENT_PAYER_INFO_BTN = 'class:"Button" and automationid:"4122"'
FINAL_INVOICE_DATE_FLD = 'class:"Edit" and name:"Lopetuspvm"'
FINAL_READING_BTN = 'class:"Button" and name:"Loppulukema..."'
SEARCH_CUSTOMER_BTN = 'class:"Button" and automationid:"4139"'
OPEN_MAKSAJATIEDOT_BTN = 'class:"Button" and automationid:"4140"'
CREATE_INVOICE_LINES_BTN = 'class:"Button" and name:"Tee laskurivit"'
CREATE_INVOICE_BTN = 'class:"Button" and name:"Tee lasku"'
JOIN_CHANGE_REMOVE_BTN = 'class:"Button" and name:"Tee liitos/vaihto/poisto"'

# Asiakkaiden haku -window
ASIAKKAIDEN_HAKU_WND = 'class:"Gupta:AccFrame" and name:"Asiakkaiden haku"'
AH_NAME_FLD = 'class:"Edit" and automationid:"4098"'
AH_ADDRESS_FLD = 'class:"Edit" and automationid:"4102"'
AH_SEARCH_BTN = 'class:"Button" and name:"Hae"'
AH_SEARCH_RESULTS_TXT = 'control:"TextControl" and regex:"Haettuja rivejä on*"'
AH_SEARCH_RESULTS_TBL = 'class:"Gupta:ChildTable" and automationid:"4111"'

# Maksajatiedot -window
MAKSAJATIEDOT_WND = 'class:"Gupta:AccFrame" and regex:"Maksajatiedot*"'
CONSUMPTION_POINT_DROPDWN = 'id:"4172" and class:"ComboBox"'
CONSUMPTION_LIST_ITEM = "path:1 > control:ListItemControl"
CUSTOMER_GRP_BTN = 'class:"Button" and automationid:"4147"'
ASIAKASRYHMAT_WND = 'class:"Gupta:AccFrame" and name:"Asiakasryhmät"'
DELINEATION_FLD = 'class:"Edit" and name:"Rajaus selitteellä:"'
PAYER_INFO_SAVE_BTN = 'class:"Button" and name:"Tallenna"'
PAYER_INFO_NEW_BTN = 'class:"Button" and name:"Uusi"'
PAYER_INFO_NAME_FLD = 'class:"Edit" and name:"Nimi"'
PAYER_INFO_ID_FIELD = 'class:"Edit" and name:"Hetu/Y-tunnus"'
PAYER_INFO_ADDRESS_FLD = 'class:"Edit" and name:"Osoite"'
PAYER_INFO_POSTAL_CODE_FLD = 'class:"Edit" and name:"Postiosoite"'
PAYER_INFO_PHONE_FLD = 'class:"Edit" and name:"GSM"'
PAYER_INFO_EMAIL_FLD = 'class:"Edit" and name:"Sähköpostiosoite"'
CUSTOMER_TYPE_FLD = 'class:"ComboBox" and name:"Laskutuksen asiakastyyppi"'
CUSTOMER = "0 - Yksityinen - Henkilö"
COMPANY = "2 - Yksityinen - Yritys"

# Asiakasryhmät -window
AR_SAVE_BTN = 'class:"Button" and name:"Tallenna" and automationid:"24579"'

# Kulutuslukemat -window
KULUTUSLUKEMAT_WND = 'class:"Gupta:AccFrame" and regex:"Kulutuslukemat*"'
DATE_OF_READING_FLD = 'class:"Edit" and name:"Luentapäivä"'
READING_FLD = 'class:"Edit" and name:"Vesi"'
READING_EXPLANATION_BTN = 'class:"Button" and automationid:"4122"'
KL_SAVE_BTN = 'class:"Button" and name:"Tallenna" and automationid:"4123"'
FORMER_READING_FIELD = 'class:"Edit" and id:"4136"'
ESTIMATE_MISSING_POPUP = 'class:"#32770" and name:"Kulutuslukemat"'
METER_MISSING_POPUP = 'class:"#32770" and name:"Mittarit"'
READING_EXPLANATION_FIELD = 'class:"Edit" and name:"Lukeman selite"'

# Lukeman selitteet -window
LUKEMAN_SELITTEET_WND = 'class:"Gupta:AccFrame" and name:"Lukeman selitteet"'
BOUNDARY_FLD = 'class:"Edit" and name:"Rajausehto:"'
LS_SAVE_BTN = 'class:"Button" and name:"Tallenna" and automationid:"24577"'

# Kiinteistöt -window
PROPERTY_WINDOW = 'class:"Gupta:AccFrame" and name:"Kiinteistöt"'
PROPERTY_OWNER_TABLE = 'class:"Gupta:ChildTable" and automationid:"4114"'
OWNER_NAME_FIELD = 'class:"Edit" and id:"32773"'
PROPERTY_SAVE_BUTTON = 'class:"Button" and id:"24581"'
PROPERTY_OWNERS_BUTTON = 'class:"Button" and name:"Omistajat"'
PROPERTY_OWNERS_WINDOW = 'class:"Gupta:AccFrame" and name:"Kiinteistön omistajat"'
PROPERTY_ID = 'class:"Static" and name:"Kiinteistötunnus"'
DELETE_BUTTON = 'class:"Button" and id:"24578"'
CONFIRM_DELETE_POPUP = 'name:"Vahvista"'
CONFIRM_DELETE_YES_BUTTON = 'class:"Button" and name:"Yes"'
NEW_OWNER_BUTTON = 'class:"Button" and name:"Uusi"'
SAVE_PROPERTY_OWNERS = 'class:"Button" and id:"24580"'
REGISTRY_PROCESSING_BUTTON = 'class:"Button" and name:"Rekisteritietojen käsittely"'
REGISTRY_PROCESSING_WINDOW = (
    'class:"Gupta:AccFrame" and name:"Rekisteritietojen käsittely"'
)
REGISTRY_PROPERTIES_BUTTON = 'class:"Button" and id:"4102"'
IMPORT_PROPERTIES_WINDOW = 'class:"Gupta:AccFrame" and regex:"Kiinteistöjen tuonti*"'
ONLY_CHANGED_RADIO = 'class:"Gupta:GPRadio" and name:"Vain muuttuneet"'
REGISTRY_SAVE_BUTTON = 'class:"Button" and name:"Tallenna"'

FETCH_CHOSEN = 'class:"Button" and name:"Hae valitut"'
TRANSFER_BUTTON = 'class:"Button" and name:"Siirto >> "'

REGISTRY_BUILDINGS_BUTTON = 'class:"Button" and id:"4103"'
BUILDINGS_TO_PROPERTY_WINDOW = (
    'class:"Gupta:AccFrame" and regex:"Rakennukset kiinteistövalinnalle*"'
)
PROJECT_BUILDINGS_RADIO = 'class:"Gupta:GPRadio" and name:"RHR - hankerakennukset"'
ONLY_NEW_RADIO = 'class:"Gupta:GPRadio" and name:"Vain uudet"'
RETURN_BUTTON = 'class:"Button" and name:"Paluu"'

CONNECTION_POINT_BTN = 'class:"Button" and name:"Liittämiskohta"'

# Rekisteritietojen käsittely -window
REGISTERS_PROCESSING_WND = (
    'class:"Gupta:AccFrame" and name:"Rekisteritietojen käsittely"'
)
PROPERTIES_BTN = 'class:"Button" and name:"Kiinteistöt"'

# Liittämiskohta -window
JOINING_POINT_WINDOW = 'class:"Gupta:AccFrame" and name:"Liittämiskohta"'
JOINING_POINT_OWNER_COMBOBOX = 'class:"ComboBox" and automationid:"4103"'
JOINING_POINT_SAVE_BUTTON = 'class:"Button" and id:"24577"'

CONNECTION_APPLICATION_BTN = (
    'class:"Button" and name:"Liittymishakemus" and automationid:"4211"'
)

# Liittymishakemus -window
LIITTYMISHAKEMUS_WND = 'class:"Gupta:AccFrame" and name:"Liittymishakemus"'
LH_NEW_BTN = 'class:"Button" and name:"Uusi" and automationid:"24578"'
LH_OWNERS_CMB = 'class:"ComboBox" and name:"Omistajat" and automationid:"4102"'
EXISTING_BUILDING_CHK = 'class:"Gupta:GPCheck" and name:"Olemassa oleva  rakennus"'
CONNECTION_APPLICATION_SAVE_BUTTON = 'class:"Button" and id:"24577"'
AGREEMENTS_BTN = 'class:"Button" and name:"Sopimukset"'
AGREEMENTS_WINDOW = 'class:"Gupta:AccFrame" and name:"Liittymis- ja käyttösopimukset"'
CUSTOMER_BUTTON = 'class:"Button" and id:"4128"'
AGREEMENTS_CUSTOMER_WINDOW = 'class:"Gupta:AccFrame" and name:"Asiakkaiden haku"'
AGREEMENTS_CUSTOMER_NAME_FIELD = 'class:"Edit" and id:"4098"'
AGREEMENTS_CUSTOMER_SEARCH_RESULTS = 'id:"4111" and class:"Gupta:ChildTable"'
CHOOSE_SEARCH_RESULTS_BUTTON = 'class:"Button" and name:"Valinta"'
AGREEMENTS_CUSTOMER_RETURN_BUTTON = 'class:"Button" and id:"26625"'
ADDITIONAL_INFO_BOX = 'class:"Edit" and name:"Lisätieto"'
OWNER_CHANGE = "OMISTAJANVAIHTO"
TAX_CHECKBOX = 'id:"4194" and class:"Gupta:GPCheck"'


# Liittymis- ja käyttösopimukset -window
SOPIMUKSET_WND = 'class:"Gupta:AccFrame" and name:"Liittymis- ja käyttösopimukset"'
LKS_NAME_FLD = 'class:"Edit" and name:"Nimi" and automationid:"4131"'
LKS_ADDRESS_FLD = 'class:"Edit" and name:"Lähiosoite" and automationid:"4135"'
LKS_POSTAL_CODE_FLD = 'class:"Edit" and name:"Postinro" and automationid:"4137"'
LKS_DISTRICT_FLD = 'class:"Edit" and name:"Postitoimipaikka" and automationid:"4139"'
LKS_PHONE_FLD = 'class:"Edit" and name:"Puhelin" and automationid:"4141"'
LKS_EMAIL_FLD = 'class:"Edit" and name:"S-Posti" and automationid:"4143"'
LKS_PIC_FLD = 'class:"Edit" and name:"Hetu/Y-tunnus" and automationid:"4145"'
LKS_CONTRACT_DATE_FLD = 'class:"Edit" and name:"Pvm" and automationid:"4110"'
PM_YKSIKKO_ALV_CHK_1 = 'class:"Gupta:GPCheck" and name:"Alv" and automationid:"4194"'
PM_YKSIKKO_ALV_CHK_2 = 'class:"Gupta:GPCheck" and name:"Alv" and automationid:"4196"'
PERUSMAKSU_ALV_CHK_1 = 'class:"Gupta:GPCheck" and name:"Alv" and automationid:"4201"'
PERUSMAKSU_ALV_CHK_2 = 'class:"Gupta:GPCheck" and name:"Alv" and automationid:"4203"'
LKS_SIGNATURE_NAME_CMB = 'class:"ComboBox" and name:"Allekirjoitus: Laitos/Pvm"'
LKS_SIGNATURE_DATE_FLD = 'class:"Edit" and id:"4246"'
CUSTOMER_SIGNATURE_FIELD = 'class:"Edit" and name:"Liittyjä/Pvm"'
CUSTOMER_SIGNATURE_DATE = 'class:"Edit" and id:"4248"'
CONTRACT_SAVE_BUTTON = 'class:"Button" and id:"24578"'
FILL_CONSUMPTION_POINT_INFO_BUTTON = (
    'class:"Button" and name:"Täydennä kulutuspisteen tiedot"'
)

ATTACHMENTS_SAVE_BUTTON = 'class:"Button" and id:"24578"'
ATTACHMENTS_BTN = 'class:"Button" and name:"Liitteet"'
LKS_PRINT_BTN = 'class:"Button" and name:"Tulosta" and automationid:"24581"'
LKS_PRINT_WND = 'class:"Gupta:AccFrame" and name:"TULOSTUS"'
LKS_PW_PRINT_BTN = 'class:"Button" and name:"Tulosta" and automationid:"24577"'
USER_AGREEMENT_BTN = 'class:"Button" and name:"Käyttösopimus"'

# Liitteet -window
LIITTEET_WND = 'class:"Gupta:AccFrame" and name:"Liitteet"'
LKS_TERMS_CHK = 'class:"Gupta:GPCheck" and name:"Sopimusehdot" and automationid:"4155"'
LKS_PAYMENT_OR_PRICE_CHK = (
    'class:"Gupta:GPCheck" and name:"VL:n maksu tai hinnasto" and automationid:"4157"'
)
LKS_GENERAL_TERMS_CHK = 'class:"Gupta:GPCheck" and name:"VL:n yleiset toimitusehdot" and automationid:"4156"'
KS_TERMS_CHK = 'class:"Gupta:GPCheck" and name:"Sopimusehdot" and automationid:"4162"'
KS_GENERAL_TERMS_CHK = 'class:"Gupta:GPCheck" and name:"VL:n yleiset toimitusehdot" and automationid:"4163"'
KS_PAYMENT_OR_PRICE_CHK = (
    'class:"Gupta:GPCheck" and name:"VL:n maksu tai hinnasto" and automationid:"4164"'
)
OTHER_CONDITIONS_BTN = 'class:"Button" and name:"Muut ehdot"'

# Liittymissopimuksen muut ehdot -window
MUUT_EHDOT_WND = 'class:"Gupta:AccFrame" and regex:"Liittymissopimuksen muut ehdot*"'
TXT_BOX = 'class:"Edit" and automationid:"4097"'
LME_SAVE_BTN = 'class:"Button" and name:"Tallenna" and automationid:"24577" and path:"1|1|1|1|3|1|2"'

# Käyttösopimuskäsittely -window
KAYTTOSOPIMUSKASITTELY_WND = 'class:"Gupta:AccFrame" and name:"Käyttösopimuskäsittely"'
KS_NEW_BTN = 'class:"Button" and name:"Uusi" and automationid:"24579"'
CONSENT_CHK = 'class:"Gupta:GPCheck" and name:"Suostumus"'
USAGE_CONTRACT_TXT_FLD = 'class:"Edit" and automationid:"4117" and path:"1|1|1|1|2|21"'
JOINING_FEES_PAID_CHK = 'class:"Gupta:GPCheck" and name:"Liittymismaksut maksettu"'
CHANGE_PAYER_BTN = 'class:"Button" and name:".." and automationid:"4144"'
KS_SIGNATURE_NAME_CMB = 'class:"ComboBox" and automationid:"4209"'
KS_SIGNATURE_DATE_FLD = 'class:"Edit" and automationid:"4111" and path:"1|1|1|1|1|15"'

# Käyttösopimuskäsittely -window
KAYTTOSOPIMUSKASITTELY_WINDOW = (
    'class:"Gupta:AccFrame" and name:"Käyttösopimuskäsittely"'
)
KS_NEW_BUTTON = 'class:"Button" and name:"Uusi" and automationid:"24579"'
CONSENT_CHECKBOX = 'class:"Gupta:GPCheck" and name:"Suostumus"'
USAGE_CONTRACT_TEXT_FIELD = (
    'class:"Edit" and automationid:"4117" and path:"1|1|1|1|2|21"'
)
JOINING_FEES_PAID_CHECKBOX = 'class:"Gupta:GPCheck" and name:"Liittymismaksut maksettu"'
CHANGE_PAYER_BUTTON = 'class:"Button" and name:".." and automationid:"4144"'
KS_SIGNATURE_NAME_COMBOBOX = 'class:"ComboBox" and automationid:"4209"'
KS_SIGNATURE_DATE_FIELD = 'class:"Edit" and automationid:"4111" and path:"1|1|1|1|1|15"'

# Check csv rows
COLUMN_O = "Selite"
COLUMN_P = "Maksu"
OTHER_PAYMENTS = "Muut maksut"
ZERO_FORMAT = "0,00"
COL_CUSTOMER = "As.ryhmä"
CUST_NUM_REGX = r"(\d+)-"
COL_MONTH = "kk"
PATTERN = "Raportti_laskutetuista*"
MONTH_MAPPING = {
    "Tammikuu": 1,
    "Helmikuu": 2,
    "Maaliskuu": 3,
    "Huhtikuu": 4,
    "Toukokuu": 5,
    "Kesäkuu": 6,
    "Heinäkuu": 7,
    "Elokuu": 8,
    "Syyskuu": 9,
    "Lokakuu": 10,
    "Marraskuu": 11,
    "Joulukuu": 12,
}
