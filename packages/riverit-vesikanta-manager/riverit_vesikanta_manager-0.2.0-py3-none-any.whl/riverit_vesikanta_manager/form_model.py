from datetime import date, datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    ValidationInfo,
    field_validator,
    model_validator,
)


class PreserveEmailMixin:
    # Custom validator to prevent email from being converted to uppercase
    @field_validator("email")
    @classmethod
    def preserve_email_case(cls, v: str) -> str:
        return v.lower() if v is not None else v


class Customer(BaseModel, PreserveEmailMixin):
    model_config = ConfigDict(str_to_upper=True)
    first_name: str
    last_name: str
    phone: str = None
    id: str = None
    address: str = None
    mail_number: int = None
    mail_address: str = None
    email: EmailStr = None
    bank_account: str = None

    @property
    def name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    @field_validator("*")
    @classmethod
    def check_not_empty(cls, v: str, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError(f"The field '{info.field_name}' cannot be empty")
        return v


class Company(BaseModel, PreserveEmailMixin):
    model_config = ConfigDict(str_to_upper=True)
    id: str
    name: str
    mailing_address: str
    mailing_address_city: str
    mailing_address_postal_code: int
    physical_address: str = None
    physical_address_city: str = None
    physical_address_postal_code: int = None
    email: EmailStr = None
    phone: str = None
    intermediator: str = None
    intermediator_id: str = None
    online_invoice_address: str = None
    bank_account: str = None

    @field_validator("*")
    @classmethod
    def check_not_empty(cls, v: str, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError(f"The field '{info.field_name}' cannot be empty")
        return v


class RealEstate(BaseModel):
    model_config = ConfigDict(str_to_upper=True)
    address: str
    mail_number: int
    mail_address: str
    consumption_point_number: int = None
    meter_number: int = None

    @field_validator("*")
    @classmethod
    def check_not_empty(cls, v: str, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError(f"The field '{info.field_name}' cannot be empty")
        return v


class Form(BaseModel):
    transfer_date: date
    meter_reading: int
    consumption_estimate: int
    real_estate: RealEstate
    former_owner: Customer | Company
    new_owner: Customer | Company
    additional_owners: list[Customer | None]

    @field_validator("transfer_date", mode="before")
    @classmethod
    def parse_transfer_date(cls, v: str) -> date:
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Invalid date format. Please use 'dd.mm.yyyy'.")
        return v

    @field_validator("*")
    @classmethod
    def check_not_empty(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, date):
            return v.strftime("%d.%m.%Y")
        if v is None or v == "":
            raise ValueError(f"The field '{info.field_name}' cannot be empty")
        return v

    @model_validator(mode="after")
    def validate_new_owner_finnish_id(self):
        new_owner = self.new_owner

        # Validate only if the new_owner is a Customer and not a Company
        if isinstance(new_owner, Customer):
            id = new_owner.id

            if not isinstance(id, str) or len(id) != 11:
                raise ValueError(f"Finnish ID must be in format YYMMDD-XXXC: {id}")

            # Remove the separator and calculate the check digit
            id_without_separator = id[:6] + id[7:10]
            try:
                id_number = int(id_without_separator)
            except ValueError:
                raise ValueError(f"Invalid Finnish ID number: {id}")

            remainder = id_number % 31
            revision = "0123456789ABCDEFHJKLMNPRSTUVWXY"
            expected_check_digit = revision[remainder]
            actual_check_digit = str(id[10]).upper()

            if actual_check_digit != expected_check_digit:
                raise ValueError(
                    f"Invalid Finnish ID: {id}. Expected check digit '{expected_check_digit}', "
                    f"but got '{actual_check_digit}'."
                )

        return self
