from pathlib import Path

from pydantic import BaseModel, EmailStr, ValidationInfo, field_validator


class Config(BaseModel):
    vesikanta_path: Path
    vesikanta_creds: str
    reading_report_files_path: Path = None
    reading_report_files_archive_path: Path = None
    tracking_report_files_path: Path = None
    tracking_report_files_archive_path: Path = None
    ufile_path: Path = None
    customer_group_start: int | str = None
    customer_group_end: int | str = None
    email_creds: str
    email_sender: EmailStr
    email_recipients: list[EmailStr]
    email_subject: str = None
    email_body: str = None
    column_p_regex_list: list[str] = None
    date_format: str
    update_yearly_consumption_estimate: bool
    signature: str = None
    form_report_folder: str = None

    # Validators for string-based fields
    @field_validator("*")
    @classmethod
    def check_not_empty(cls, v: str, info: ValidationInfo) -> str:
        # Specific check for Path objects
        if isinstance(v, Path) and str(v) == ".":  # empty Path obj is "."
            raise ValueError(f"The field '{info.field_name}' cannot be an empty Path!")
        # Check rest are not empty
        elif v is None or v == "":
            raise ValueError(f'The field "{info.field_name}" cannot be empty.')

        return v

    @field_validator("email_recipients", "column_p_regex_list")
    @classmethod
    def check_lists_are_not_empty(cls, v: list, info: ValidationInfo) -> str:
        if len(v) == 0:
            raise ValueError(f"The field '{info.field_name}' cannot be an empty list!")
        # Check for empty strings within the list
        if any(isinstance(item, str) and item == "" for item in v):
            raise ValueError(
                f"The field '{info.field_name}' cannot contain empty strings!"
            )
        return v
