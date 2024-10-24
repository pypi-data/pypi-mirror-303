import base64
import calendar
import csv
import faulthandler
import fnmatch
import io
import os
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd
import pyautogui
from psutil import process_iter
from robocorp import log, vault, windows
from robocorp.windows import ActionNotPossible, ElementNotFound, WindowElement
from robocorp.workitems import ApplicationException, BusinessException

from riverit_vesikanta_manager import constants as const

from .config_model import Config
from .form_model import Company, Customer, Form


class VesikantaManager:
    """Manages the Vesikanta application session, navigation and activities."""

    def __init__(self, config: Config) -> None:
        self.config = config
        self.desktop = windows.Desktop()
        self.vesikanta_window = None
        self.readings_window = None
        self.search_customers_window = None
        self.change_payer_window = None
        self.payer_info_window = None
        self.consumption_point_window = None
        self.property_window = None
        self.agreements_window = None
        self.browse_customers_window = None
        self.consumption_readings_window = None
        self.print_window = None

    def __enter__(self) -> "VesikantaManager":
        self._login_with_tracking()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        if exc_type:
            self.error_screenshot()
        self.close()

    def login(self) -> None:
        """
        Launch Vesikanta and login.

        This function performs the login process for Vesikanta. It opens the Vesikanta application,
        fills in the username and password fields, and clicks the OK button to log in.

        Raises:
            `ApplicationException`: If the login process fails.
        """
        vesikanta_creds = vault.get_secret(self.config.vesikanta_creds)

        try:
            self.desktop.windows_run(str(self.config.vesikanta_path))
            login_window = windows.find_window(const.LOGIN_WND, timeout=30)
            login_window.send_keys(
                vesikanta_creds["username"], locator=const.USERNAME_FLD
            )
            login_window.send_keys(
                vesikanta_creds["password"], locator=const.PASSWORD_FLD
            )
            login_window.click(const.OK_BTN)
            windows.find_window(const.MAIN_WND, timeout=60)
        except (ElementNotFound, ActionNotPossible) as e:
            raise ApplicationException(
                f"Failed to login: {e}", code="CRITICAL_LOGIN_FAILED"
            ) from e

    def close(self) -> None:
        """
        Closes the Vesikanta window.

        This method checks if the Vesikanta window is running and attempts to close it.
        If the window cannot be closed normally, it terminates the associated process.
        """
        self.vesikanta_window = self._get_main_window()
        if not self.vesikanta_window.is_running():
            return
        try:
            self.vesikanta_window.close_window()
        except Exception as e:
            log.warn(f"Failed to close Vesikanta normally: {e}")
            for proc in process_iter("name"):
                if proc.name == "vkawin.exe":
                    log.warn(f"Terminating {proc.name} process.")
                    proc.kill()

    def track_execution_time(func):
        """
        Decorator to log the execution time of a function.

        Args:
            func (callable): The function to be wrapped.

        Returns:
            callable: A wrapper function that logs the execution time.
        """

        def wrapper(*args, **kwargs):
            start_time = time.time()  # Start time
            result = func(*args, **kwargs)  # Execute the function
            end_time = time.time()  # End time
            execution_time = end_time - start_time  # Calculate execution time
            log.info(
                f"VesikantaManager '{func.__name__}' executed in {execution_time:.1f} seconds"
            )
            return result

        return wrapper

    @track_execution_time
    def _login_with_tracking(self):
        """Calls login function with excecution time wrapper, to display time taken in log.html"""
        self.login()

    def _get_main_window(self) -> WindowElement:
        """Get the Vesikanta application main window element.

        Returns:
            `WindowElement`: The main window element.

        Raises:
            `ApplicationException`: If failed to get the main window.
        """
        if self.vesikanta_window is None:
            try:
                self.vesikanta_window = windows.find_window(const.MAIN_WND, timeout=60)
            except ElementNotFound as e:
                raise ApplicationException(
                    f"Failed to get the main window: {e}",
                    code="CRITICAL_GET_WND_FAILED",
                ) from e
        return self.vesikanta_window

    def _close_window(self, window: WindowElement) -> None:
        """
        Closes the specified window.

        Args:
            `window` (WindowElement): The window to be closed.
        """
        max_attempts = 5
        delay_between_attempts = 1  # Seconds
        attempts = 0

        while not window.is_disposed() and attempts < max_attempts:
            try:
                window.set_focus()
                with pyautogui.hold("alt"):
                    pyautogui.press("p")
                time.sleep(
                    delay_between_attempts
                )  # Give some time for the window to process the close command
                attempts += 1
            except Exception as e:
                raise ApplicationException(
                    f"An error occurred while attempting to close the window: {e}",
                    code="WARN_CLOSE_WND_FAILED",
                ) from e

    def _find_child_window_without_logging(
        self, parent: WindowElement, locator: str, timeout: float
    ) -> WindowElement | None:
        """
        ### SEE ISSUE https://github.com/robocorp/robocorp/issues/283
        `Temporary` wrapper for `find_child_window()` to prevent excessive logging when
        the child window is not found. This is done by disabling faulthandler and then
        enabling it after search is done.

        Args:
            parent (WindowElement): The window element whose child window is to be found.
            locator (str): The locator used to find the child window.
            timeout (float): The timeout duration in seconds.

        Returns:
            WindowElement | None: The found child window, or `None` if no window is found.

        Related Issues:
            - https://github.com/robocorp/robocorp/issues/283
        """
        faulthandler.disable()
        child_window = parent.find_child_window(
            locator=locator, timeout=timeout, raise_error=False
        )
        faulthandler.enable()
        return child_window

    def error_screenshot(self) -> None:
        """screenshot to log.html in case of Exception"""
        log.critical("Exception detected! Taking a screenshot:")
        self.desktop.log_screenshot("ERROR")

    def screenshot_with_pyautogui(self) -> None:
        """Alternative way of getting screenshots for debugging"""
        # Take screenshot using pyautogui and store it in memory buffer
        image = pyautogui.screenshot()
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")

        # Get the binary data from the buffer
        image_data = buffer.getvalue()

        # Convert the image data to a base64 string
        image_base64 = base64.b64encode(image_data).decode("utf-8")

        # Embed the image in the HTML log
        log.html(f'<img src="data:image/png;base64,{image_base64}"/>')

    def open_lukematietojen_haku(self) -> None:
        """Opens the 'Lukematietojen haku' window in the Vesikanta application.

        Raises:
            `ApplicationException`: If the 'Lukematietojen haku' window fails to open.
        """
        self.vesikanta_window = self._get_main_window()
        pyautogui.press("alt", interval=0.5)
        pyautogui.press("p", interval=0.5)  # Perustiedot
        self.vesikanta_window.send_keys(
            "{ä}", locator=const.MAIN_NAVBAR, wait_time=0.5
        )  # Liittymät.
        pyautogui.press(
            "t", interval=0.5
        )  # Kulutustietorajapinta (Web ja etäluettavat mittarit)
        pyautogui.press("l", interval=0.5)  # Lukematietojen haku ja siirto...
        pyautogui.press("enter", interval=0.5)

        try:
            self.readings_window = self.vesikanta_window.find_child_window(
                const.LUKEMATIEDOT_WND
            )
        except ElementNotFound as e:
            raise ApplicationException(
                f"Failed to open Lukematietojen haku: {e}", code="CRITICAL_OPEN_FAILED"
            ) from e

    def read_lukematiedot_in(self, report_files_path: Path) -> bool:
        """
        Reads the lukematiedot (reading data) from a specified report folder.

        Args:
            `report_folder` (str): The path to the report folder.

        Returns:
            `bool`: True if the lukematiedot is successfully read, False otherwise.

        Raises:
            `BusinessException`: If the DFILE is not found in the report folder.
        """

        self.readings_window.send_keys(
            str(report_files_path / "DFILE.ZIP"),
            locator=const.VESIKANTA_INPUT_FILE_FLD,
        )

        # Check if yearly consumption estimate should be updated or not.
        if not self.config.update_yearly_consumption_estimate:
            self.readings_window.click(const.DONT_UPDATE_YEARLY_CONSUMPTION_CHECKBOX)

        self.readings_window.click(const.LUE_LUKEMAT_SISAAN_BTN)
        if self.desktop.find_window(
            const.LUKEMIEN_TUONTI_DLG, timeout=5, raise_error=False
        ):
            self.readings_window.click(const.OK_BTN)
            log.critical("DFILE not found found. Cannot read file in.")
            raise BusinessException("DFILE not found found. Cannot read file in.")

        lukemien_siirto_dialog = self.readings_window.find_child_window(
            const.LUKEMIEN_SIIRTO_DLG
        )
        dialog_text: str = self._get_dialog_text(lukemien_siirto_dialog)

        # Check if reading file in was success and handle subsequent dialogs.
        try:
            if "Luetaanko tiedosto" in dialog_text:
                lukemien_siirto_dialog.click(const.OK_BTN)
                lukemien_siirto_dialog = self.readings_window.find_child_window(
                    const.LUKEMIEN_SIIRTO_DLG
                )
                dialog_text = self._get_dialog_text(lukemien_siirto_dialog)
                if "Jatketaan lukemien tarkastuksella..." in dialog_text:
                    lukemien_siirto_dialog.click(const.OK_BTN)
                    lukemien_siirto_dialog = self.readings_window.find_child_window(
                        const.LUKEMIEN_SIIRTO_DLG
                    )
                    dialog_text = self._get_dialog_text(lukemien_siirto_dialog)
                    if "Lukemien siirto suoritettu !" in dialog_text:
                        lukemien_siirto_dialog.click(const.OK_BTN)
                    return True
        except ElementNotFound as e:
            raise BusinessException(
                f"Failed to read Lukematiedot in: {e}",
                code="CRITICAL_READING_IN_FAILED",
            ) from e

    def _get_dialog_text(self, lukemien_siirto_dialog: WindowElement):
        """
        Get the dialog text from the given WindowElement.

        Args:
            `lukemien_siirto_dialog` (WindowElement): The WindowElement representing the dialog.

        Returns:
            `dialog_text` (str): The dialog text.
        """
        dialog_text_length = 16  # The default max length of the dialog text. Longer texts indicate possible error messages.
        ls_children = lukemien_siirto_dialog.iter_children()
        for child in ls_children:
            if len(child.name) > dialog_text_length:
                dialog_text = child.name
        return dialog_text

    def save_report_csv(self, report_files_path: str) -> str:
        """
        Saves the report as a CSV file.

        Args:
            `report_files_path` (str): The folder where the report CSV file will be saved.

        Returns:
            `report_csv_file` (str): The path to the saved report CSV file.

        Raises:
            `BusinessException`: If the report CSV file could not be saved.
        """
        try:
            self.readings_window.click(const.REPORT_TO_FILE_BTN)
            save_csv_file_window = self.readings_window.find_child_window(
                const.SAVE_CSV_WND
            )

            # Get the default name of the report CSV and set the path to the file.
            report_csv_file = "report.csv"
            report_csv_file = os.path.join(report_files_path, report_csv_file)
            save_csv_file_window.send_keys(
                report_csv_file, locator=const.SAVE_CSV_NAME_FLD
            )

            # Save report and wait 3 seconds to prevent issues with confirmation window.
            with pyautogui.hold("alt"):
                pyautogui.press("a")
            time.sleep(3)

            self.screenshot_with_pyautogui()  # debugging screenshot

            save_report_confirm_dialog = self.readings_window.find_child_window(
                const.SAVE_CSV_CONFIRM_DLG
            )
            save_report_confirm_dialog.click(const.OK_BTN)

        except ElementNotFound as e:
            raise BusinessException(
                f"Failed to save the report CSV file: {e}",
                code="CRITICAL_SAVE_CSV_FAILED",
            ) from e
        return report_csv_file

    def print_report_pdf(self, report_files_path: Path) -> None:
        """
        Prints the report as a PDF file.

        Args:
            `report_files_path` (str): The folder where the PDF report file will be saved.
        """
        try:
            self.vesikanta_window = self._get_main_window()
            datetime_now = datetime.now().strftime(self.config.date_format)
            self.vesikanta_window.click(const.PRINT_REPORT_BTN)
            self.print_window = self._find_child_window_without_logging(
                self.vesikanta_window, const.TULOSTUS_WND, 20
            )

            # Click the folder button to avoid SQL error. Close the folder window when it opens.
            self.print_window.click(const.FOLDER_BTN)
            self._close_folder_window()
            self.print_window.click(const.PRINT_BTN)

            # Report Builder -window
            report_builder_window = self.desktop.find_window(const.REPORT_BUILDER_WND)
            with pyautogui.hold("alt"):
                pyautogui.press("p", interval=0.5)  # Print
                pyautogui.press(
                    "p", interval=0.5
                )  # Print (to open Win32 print -window)

            # Win32 printing window
            win32_print_window = self.desktop.find_window(const.WIN32_PRINT_WND)

            # Open the printer list and select the PDF printer
            win32_print_window.click(const.WIN32_PRINTER_LST)
            win32_print_window.find(const.WIN32_PRINTER_LST).click(const.PDF_PRINTER)
            win32_print_window.click(const.WIN32_PRINT_BTN)

            # Save file window
            report_file_name = f"Lukemaraportti_{datetime_now}.pdf"
            report_file_path = report_files_path / report_file_name
            save_file_window = report_builder_window.find_child_window(
                const.SAVE_PDF_WND
            )
            save_file_window.find(const.SAVE_PDF_NAME_FLD).set_value(report_file_path)
            save_file_window.click(const.SAVE_PDF_FILE_BTN)

            # Wait for the report file to be created before continuing
            file_size_zero = 0
            while os.path.getsize(report_file_path) == file_size_zero:
                time.sleep(1)

            # Close the printing windows
            if not report_builder_window.is_disposed():
                with pyautogui.hold("alt"):
                    pyautogui.press("f", interval=0.5)  # File
                    pyautogui.press("c", interval=0.5)  # Close
        except Exception as e:
            raise ApplicationException(
                f"Failed to print the PDF file!",
                code="CRITICAL_PDF_PRINT_FAILED",
            ) from e

    def _close_folder_window(self):
        """
        Closes the folder window if it is open.

        This function attempts to find the folder window using the `desktop.find_window` method
        and closes it by sending the key combination "{CTRL}w". If an error occurs during the process,
        a critical log message is generated.

        Raises:
            Exception: If an error occurs while trying to close the folder window.
        """
        try:
            folder_window = self.desktop.find_window(const.FILE_EXPLORER_WND)
            if not folder_window.is_disposed():
                folder_window.send_keys("{CTRL}w")
        except ElementNotFound as e:
            raise ApplicationException(
                f"An error occurred while trying to close the folder window: {e}"
            ) from e

    def check_report(self, report_csv_file: str) -> bool:
        """
        Checks the report CSV file for notifications.

        Args:
            `report_csv_file` (str): The path to the report CSV file.

        Returns:
            `bool`: True if notifications are found, False otherwise.
        """
        file_path = Path(report_csv_file)

        if not file_path.is_file():
            raise ApplicationException(
                f"Report CSV file '{report_csv_file}' could not be read or does not exist.",
                code="CRITICAL_CSV_READ_FAILED",
            )

        try:
            with file_path.open("r") as file:
                csv_report = csv.DictReader(file, delimiter=";")
                for row in csv_report:
                    if row.get("Selite", "").strip() != "KulutusWeb":
                        log.info(f"Notification found in row: {row}")
                        return True

        except Exception as e:
            raise ApplicationException(
                f"Error reading CSV file: {e}", code="CSV_READ_ERROR"
            )

        return False

    def open_seurantatietojen_keruu_window(self) -> None:
        """NOTE: NOT IN USE
        Opens the Seurantatietojen keruu window.

        Raises:
            ApplicationException: If the Seurantatietojen keruu window cannot be opened.

        """
        self.vesikanta_window = self._get_main_window()
        self.vesikanta_window.foreground_window()
        pyautogui.press("alt", interval=0.5)
        pyautogui.press("p", interval=0.5)  # Perustiedot
        pyautogui.press("i", interval=0.5)  # Tietokanta
        pyautogui.press("e", interval=0.5)  # Seurantatietojen keruu

        try:
            self.vesikanta_window.find(const.SEURANTATIEDOT_WND)
        except ElementNotFound as e:
            raise ApplicationException(
                f"Failed to open Seurantatietojen keruu: {e}",
                code="CRITICAL_OPEN_FAILED",
            ) from e

    def set_customer_group_interval(
        self, customer_group_start: int | str, customer_group_end: int | str
    ) -> None:
        """NOTE: NOT IN USE
        Sets the customer group interval in the Vesikanta Manager.

        Args:
            `customer_group_start` (int | str): The starting value of the customer group.
            `customer_group_end` (int | str): The ending value of the customer group.
        """
        self.vesikanta_window = self._get_main_window()
        tracking_data_window = self.vesikanta_window.find_child_window(
            const.SEURANTATIEDOT_WND
        )
        tracking_data_window.set_value(
            value=str(customer_group_start), locator=const.TRACKING_GRP_START_FLD
        )
        tracking_data_window.set_value(
            value=str(customer_group_end), locator=const.TRACKING_GRP_END_FLD
        )

    def activate_data_collection(self) -> None:
        """NOTE: NOT IN USE
        Activates the data collection process.

        Raises:
            `BusinessException`: If the data collection fails.
        """
        self.vesikanta_window = self._get_main_window()
        tracking_data_window = self.vesikanta_window.find_child_window(
            const.SEURANTATIEDOT_WND
        )
        tracking_data_window.click(const.PERFORM_BTN)

        # Confirmation of the data collection start
        confirmation_dialog = self.vesikanta_window.find_child_window(
            const.CONFIMATION_DLG, raise_error=False
        )
        if confirmation_dialog:
            confirmation_dialog.click(const.OK_BTN)

        # Confirmation that the data collection is done
        try:
            done_dialog_text = self.vesikanta_window.find(const.DATA_COLL_DONE_DLG_TXT)
            if done_dialog_text:
                self.vesikanta_window.click(const.OK_BTN)
        except ElementNotFound as e:
            raise BusinessException(
                f"Data collection failed: {e}", code="CRITICAL_DATA_COLLECTION_FAILED"
            )

        # Close the Seurantatietojen keruu -window
        self._close_window(tracking_data_window)

    def open_vesilaitoksen_tulot_window(self) -> None:
        """NOTE: NOT IN USE
        Opens the Vesilaitoksen tulot -window in Vesikanta by hotkeys.

        Raises:
            `ApplicationException`: If the Vesilaitoksen tulot -window fails to open.
        """
        self.vesikanta_window = self._get_main_window()
        self.vesikanta_window.foreground_window()
        pyautogui.press("alt", interval=0.5)  # Perustiedot
        for _ in range(5):
            pyautogui.press(
                "right", interval=0.5
            )  # NOTE: in Vesikanta main window "t" hotkey is reserved for both Työmääräin and Tulosteet menu items. Työmääräin is disabled, and "alt+t" won't activate Tulosteet, hence navigating the menu via arrow keys.
        pyautogui.press("enter", interval=0.5)  # Tulosteet
        pyautogui.press("v", interval=0.5)  # Vesilaitoksen tulot...

        try:
            self.vesikanta_window.find(const.VESILAITOKSEN_TULOT_WND)
        except ElementNotFound as e:
            raise ApplicationException(
                f"Failed to open Vesilaitoksen tulot: {e}",
                code="CRITICAL_OPEN_FAILED",
            ) from e

    def set_revenue_report_interval(
        self, customer_group_start: int | str, customer_group_end: int | str
    ) -> None:
        """NOTE: NOT IN USE
        Set the revenue report interval for a given customer group.

        Args:
            `customer_group_start` (int | str): The starting value of the customer group.
            `customer_group_end` (int | str): The ending value of the customer group.
        """
        self.vesikanta_window = self._get_main_window()
        revenue_report_window = self.vesikanta_window.find_child_window(
            const.VESILAITOKSEN_TULOT_WND
        )
        revenue_report_window.set_value(
            str(customer_group_start), locator=const.REVENUE_GRP_START_FLD
        )
        revenue_report_window.set_value(
            str(customer_group_end), locator=const.REVENUE_GRP_END_FLD
        )

    def save_revenue_report_to_csv(self, report_folder: str) -> str:
        """NOTE: NOT IN USE
        Prints the revenue report to a CSV file.

        Args:
            `report_folder` (str): The folder where the report CSV file will be saved.

        Returns:
            `revenue_report_csv_file` (str): The path to the saved report CSV file.
        """
        self.vesikanta_window = self._get_main_window()
        date_time_now = datetime.now().strftime(self.config.date_format)
        revenue_report_window = self.vesikanta_window.find_child_window(
            const.VESILAITOKSEN_TULOT_WND
        )
        try:
            self.vesikanta_window.click(const.REVENUE_REPORT_TO_CSV_BTN)
            save_csv_file_window = self.vesikanta_window.find_child_window(
                const.SAVE_CSV_WND
            )

            revenue_report_csv_file = Path(
                "Vesilaitoksen_tulot_" + date_time_now + ".csv"
            )
            revenue_report_csv_file = report_folder / revenue_report_csv_file
            save_csv_file_window.set_value(
                value=revenue_report_csv_file, locator=const.SAVE_CSV_NAME_FLD
            )

            save_csv_file_window.click(const.SAVE_CSV_FILE_BTN)
            save_report_confirm_dialog = self.vesikanta_window.find_child_window(
                const.SAVE_CSV_CONFIRM_DLG
            )
            save_report_confirm_dialog.click(const.OK_BTN)
        except (ElementNotFound, ValueError, ActionNotPossible) as e:
            raise BusinessException(
                f"Failed to save the report CSV file: {e}",
                code="CRITICAL_SAVE_CSV_FAILED",
            )

        self._close_window(revenue_report_window)
        return revenue_report_csv_file

    def csv_contains_rows_requiring_actions(
        csv_path: str, allowed_p_patterns: list
    ) -> bool:
        """NOTE: NOT IN USE
        Checks the CSV file for rows that match specified logic, indicating actions are needed.

        Args:
            `csv_path` (str): Path to the CSV file to be checked.
            `allowed_p_patterns` (list): List of regex patterns COLUMN_P is allowed to contain.

        Returns:
            `bool`: `True` if actions are needed, `False` otherwise.

        Raises:
            `FileNotFoundError`: If the specified CSV file is not found.
            `Exception`: For any other unexpected errors during validation.
        """
        try:
            with log.suppress_variables():
                df = pd.read_csv(
                    csv_path, delimiter=";", encoding="latin-1", skiprows=1
                )

                # Check for rows where COLUMN_O contains COLUMN_O_REGEX
                o_matches = df[const.COLUMN_O].str.contains(
                    const.OTHER_PAYMENTS, regex=True
                )
                # and COLUMN_P does not match any pattern in COLUMN_P_REGEX list
                p_not_matches = ~df[const.COLUMN_P].str.contains(
                    "|".join(allowed_p_patterns), regex=True
                )

                filtered_rows = df[o_matches & p_not_matches]
                if filtered_rows.empty:
                    return False
                log.warn("Combinations requiring actions found!")
                log.warn(filtered_rows[[const.COLUMN_O, const.COLUMN_P]])
                return True

        except FileNotFoundError as fe:
            raise FileNotFoundError(f"csv not found: {fe}")
        except Exception as e:
            raise Exception(f"Couldn't validate csv: {e}")

    def filter_customers_and_dates_from_csv(csv_path: str) -> dict:
        """NOTE: NOT IN USE
        Reads a CSV, filters records based on conditions, and extracts
        first and last dates for each unique customer group with non-zero other payments.
        Returns a dictionary mapping group identifiers to formatted start and end dates.

        Args:
        - `csv_path` (str): Path to CSV.

        Returns:
        - `dict`: Mapping of group identifiers to lists of 'DD.MM.YYYY' dates.

        Raises:
        - `FileNotFoundError`: If the specified CSV file is not found.
        - `Exception`: If an error occurs during CSV processing or data extraction.

        Note:
        - Uses ';' delimiter and 'latin-1' encoding.
        - Requires `const.MONTH_MAPPING` for month abbreviation to number conversion.
        - logging supressed when handling customer information
        """
        final_dict = {}
        try:
            with log.suppress_variables():
                df = pd.read_csv(csv_path, delimiter=";", encoding="latin-1")
                find_other_payments = df[const.OTHER_PAYMENTS] != const.ZERO_FORMAT
                found_o_p = df[find_other_payments]

                # Pick the customer number preceeding hyphen
                unique_values = found_o_p[const.COL_CUSTOMER].unique()
                unique_values_dict = {
                    val: re.match(const.CUST_NUM_REGX, val).group(1)
                    for val in unique_values
                    if re.match(const.CUST_NUM_REGX, val)
                }

                for key in unique_values_dict:
                    month_numbers = []

                    for index, row in found_o_p.iterrows():
                        if (
                            row[const.COL_CUSTOMER] == key
                            and row[const.COL_MONTH] in const.MONTH_MAPPING
                        ):
                            month_num = const.MONTH_MAPPING[row[const.COL_MONTH]]
                            year = row["Vuosi"]
                            month_numbers.append((month_num, year))

                    if month_numbers:
                        # Sort the list of tuples by year (item[1]) and then by month (item[0])
                        month_numbers_sorted = sorted(
                            month_numbers, key=lambda x: (x[1], x[0])
                        )

                        # Extract first and last dates
                        first_month = month_numbers_sorted[0]
                        last_month = month_numbers_sorted[-1]

                        # Format first and last dates
                        first_day = f"01.{first_month[0]:02d}.{first_month[1]}"
                        last_day = calendar.monthrange(last_month[1], last_month[0])[1]
                        last_date = (
                            f"{last_day:02d}.{last_month[0]:02d}.{last_month[1]}"
                        )

                        final_dict[unique_values_dict[key]] = [first_day, last_date]

            return final_dict

        except FileNotFoundError as fe:
            raise FileNotFoundError(f"csv not found: {fe}")

    def open_raportti_laskutetuista_window(self) -> None:
        """NOTE: NOT IN USE
        Opens the Raportti laskutetuista -window in Vesikanta by hotkeys.
        """
        self.vesikanta_window = self._get_main_window()
        self.vesikanta_window.foreground_window()
        pyautogui.press("alt")
        pyautogui.press("l", interval=0.5)  # Laskutus
        pyautogui.press("a", interval=0.5)  # Raportti laskutetuista...

        try:
            self.vesikanta_window.find(const.LASKUTETUT_WND)
        except ElementNotFound as e:
            raise ApplicationException(
                f"Failed to open Raportti laskutetuista: {e}",
                code="CRITICAL_OPEN_FAILED",
            )

    def set_raportti_laskutetuista_interval(
        self, group: str, date_start: str, date_end: str
    ) -> None:
        """NOTE: NOT IN USE
        Sets the interval for the billed report.

        Args:
            `group` (str): The starting (and ending) value of the customer group.
            `date_start` (str): The starting date of the entry.
            `date_end` (str): The ending date of the entry.
        """
        self.vesikanta_window = self._get_main_window()
        report_billed_window = self.vesikanta_window.find_child_window(
            const.LASKUTETUT_WND
        )
        report_billed_window.set_value(value=group, locator=const.BILLED_GRP_START_FLD)
        report_billed_window.set_value(value=group, locator=const.BILLED_GRP_END_FLD)
        report_billed_window.set_value(
            date_start, locator=const.DATE_OF_ENTRY_START_FLD
        )
        report_billed_window.set_value(date_end, locator=const.DATE_OF_ENTRY_END_FLD)

    def save_billed_report_to_csv(
        self, report_files_path: str, group: str, date_start: str, date_end: str
    ) -> str:
        """NOTE: NOT IN USE
        Saves a billed report to a CSV file.

        Args:
            `report_files_path` (str): The folder where the CSV file will be saved.
            `group` (str): The group name for the report.
            `date_start` (str): The start date for the report.
            `date_end` (str): The end date for the report.

        Returns:
            `billed_report_csv_file` (str): The path to the saved CSV file.
        """
        self.vesikanta_window = self._get_main_window()
        report_billed_window = self.vesikanta_window.find_child_window(
            const.LASKUTETUT_WND
        )
        try:
            self.vesikanta_window.click(const.BILLED_REPORT_TO_CSV_BTN)
            save_report_confirm_dialog = self.vesikanta_window.find_child_window(
                const.BILLED_SAVE_CSV_CONFIRM_DLG
            )
            save_report_confirm_dialog.click(const.BILLED_YES_BTN)
            save_csv_file_window = self.vesikanta_window.find_child_window(
                const.SAVE_CSV_WND
            )

            # Get the default name of the report CSV and set the path to the file.
            billed_report_csv_file: str = (
                "Raportti_laskutetuista_"
                + group
                + "_"
                + date_start
                + "-"
                + date_end
                + ".csv"
            )
            billed_report_csv_file: str = os.path.join(
                report_files_path, billed_report_csv_file
            )
            save_csv_file_window.set_value(
                billed_report_csv_file, locator=const.SAVE_CSV_NAME_FLD
            )

            save_csv_file_window.click(const.SAVE_CSV_FILE_BTN)

            # Printing files can take a while, so waiting for a few minutes.
            save_report_confirm_dialog = self.vesikanta_window.find_child_window(
                const.SAVE_CSV_CONFIRM_DLG, timeout=360
            )
            save_report_confirm_dialog.click(const.OK_BTN)
        except (ActionNotPossible, ValueError, ElementNotFound) as e:
            raise BusinessException(
                f"Failed to save the report CSV file: {e}",
                code="CRITICAL_SAVE_CSV_FAILED",
            )

        # Close the Raportti laskutetuista -window
        self._close_window(report_billed_window)
        return billed_report_csv_file

    def check_report_for_notifications(
        self, report_files_path: str, allowed_p_patterns
    ) -> bool:
        """NOTE: NOT IN USE
        Check the reports in the specified folder for notifications.

        Args:
            `report_folder` (str): The path to the folder containing the reports.
            `allowed_p_patterns`: A list of allowed patterns for the reports.

        Returns:
            `Tuple[bool, List[str]]`: A tuple containing a boolean value indicating whether an email should be sent,
            and a list of files that have notifications.
        """
        files_w_notifications = []
        for file in os.listdir(report_files_path):
            report_file = os.path.join(report_files_path, file)
        if fnmatch.fnmatch(file, const.PATTERN):
            actions_required = self.csv_contains_rows_requiring_actions(
                report_file, allowed_p_patterns
            )
            if actions_required:
                send_email = True
                files_w_notifications.append(file)
        return send_email, files_w_notifications

    def open_web_aineiston_muodostaminen(self) -> None:
        """
        Opens the Tietojen siirto Internet - palveluun -window in Vesikanta by hotkeys.
        """
        self.vesikanta_window = self._get_main_window()
        self.vesikanta_window.foreground_window()
        pyautogui.press("alt", interval=0.5)
        pyautogui.press("p", interval=0.5)  # Perustiedot
        self.vesikanta_window.send_keys(
            "{ä}", locator=const.MAIN_NAVBAR, wait_time=0.5
        )  # Liittymät.
        pyautogui.press(
            "t", interval=0.5
        )  # Kulutustietorajapinta (Web ja etäluettavat mittarit)
        pyautogui.press("w", interval=0.5)  # Web aineiston muodostaminen...

        try:
            self.vesikanta_window.find(const.WEB_AINEISTO_WND)
        except ElementNotFound as e:
            raise ApplicationException(
                f"Failed to open Web aineiston muodostaminen: {e}",
                code="CRITICAL_OPEN_FAILED",
            ) from e

    def activate_data_transfer(self) -> None:
        """
        Activates the data transfer process to the Web aineiston muodostaminen -window.
        """
        self.vesikanta_window = self._get_main_window()
        web_material_window = self.vesikanta_window.find_child_window(
            const.WEB_AINEISTO_WND
        )
        web_material_window.click(const.TRANSFER_BTN)
        web_material_window.click(const.OK_BTN)

    def check_data_transfer_state(self) -> None:
        """
        Check the state of data transfer.

        Raises:
            `BusinessException`: If the data transfer fails.
        """
        self.vesikanta_window = self._get_main_window()
        web_aineisto_window = self.vesikanta_window.find_child_window(
            const.WEB_AINEISTO_WND
        )
        transfer_dialog = self.vesikanta_window.find_child_window(const.TRANSFER_DLG)
        dialog_text = self._get_dialog_text(transfer_dialog)

        if "Tiedot siirretty tiedostoon" in dialog_text:
            transfer_dialog.click(const.OK_BTN)
            log.info("Data transfer successful.")
        else:
            raise BusinessException(
                "Data transfer failed.", code="CRITICAL_DATA_TRANSFER_FAILED"
            )

        # Close Tietojen siirto Internet - palveluun -window
        self._close_window(web_aineisto_window)

    # TODO
    # Form functions from this point onwards
    # TODO

    def open_browse_customers_window(self) -> None:
        """
        Opens the Asiakastietojen selailu -window. as `self.browse_customers_window`

        Raises:
            `ApplicationException`: If the customer browsing window fails to open within the specified timeout.
        """
        self.vesikanta_window = self._get_main_window()
        with pyautogui.hold("alt"):
            pyautogui.press("a", interval=0.5)  # Asiakastiedot
        pyautogui.press("a", interval=0.5)  # Asiakkaiden selailu ...

        try:
            self.browse_customers_window = windows.find_window(
                const.ASIAKASTIETOJEN_SELAILU_WND
            )
        except ElementNotFound as e:
            raise ApplicationException(
                "Failed to open the Asiakastietojen selailu -window",
                code="CRITICAL_OPEN_FAILED",
            ) from e

    def search_for_customer(self, form: Form) -> None:
        """
        Searches for a customer (consumption point) in the Vesikanta application using name and address.

        Args:
            form (Form): Form object containing the owner's information.

        Raises:
            BusinessException: If no customer is found or if multiple customers are found.
        """
        try:
            self._enter_search_criteria(form)
            search_results_count = self._get_search_results_count()
            self._handle_search_results(search_results_count)
        finally:
            self._close_window(self.browse_customers_window)

    def _enter_search_criteria(self, form: Form) -> None:
        """Fills in the search criteria fields in the customer browsing window."""
        name = form.former_owner.name
        address = form.real_estate.address
        meter_id = "Mittaritunnus"

        self.browse_customers_window.send_keys(name, locator=const.AS_NAME_FLD)
        self.browse_customers_window.send_keys(address, locator=const.AS_ADDRESS_FLD)
        self.browse_customers_window.select(meter_id, locator=const.ADD_LIM_CMB)

    def _get_search_results_count(self) -> int:
        """Clicks Hae -button to update the lower text control and extracts the number of search results."""
        self.browse_customers_window.click(const.AS_SEARCH_BTN)
        search_results_count = self.browse_customers_window.find(
            const.AS_SEARCH_RESULTS_TXT
        ).name

        # Find the count of search results
        number_regex = r"\d+"
        number_match = re.search(number_regex, search_results_count)
        if not number_match:
            raise BusinessException(
                "Failed to retrieve search results.", code="CRITICAL_SEARCHING_FAILED"
            )
        return int(number_match.group())

    def _handle_search_results(self, count: int) -> None:
        """Handles the logic based on the number of search results found."""
        if count == 0:
            raise BusinessException(
                "Customer not found.", code="CRITICAL_CUSTOMER_NOT_FOUND"
            )
        elif count == 1:
            self._select_found_customer()
        elif count > 1:
            raise BusinessException(
                "Multiple customers found!", code="CRITICAL_TOO_MANY_CUSTOMERS"
            )
        else:
            raise BusinessException(
                "Unexpected error in searching for the customer.",
                code="CRITICAL_UNDEFINED_ERROR",
            )

    def _select_found_customer(self) -> None:
        """Selects the customer from the search results."""
        search_results_table = self.browse_customers_window.find(
            const.AS_SEARCH_RESULTS_TBL
        )
        search_results_table.set_focus()
        search_results_table.send_keys("{down}")
        search_results_table.double_click()

    def open_payer_change_window(self) -> None:
        """
        Opens the Maksajan vaihto -window in the Vesikanta application.

        Raises:
            `ApplicationException`: If the Maksajan vaihto -window fails to open.
        """
        self.vesikanta_window = self._get_main_window()
        with pyautogui.hold("alt"):
            pyautogui.press("a", interval=0.5)  # Asiakastiedot
        pyautogui.press("v", interval=0.5)  # Visuaalinen yhteenveto (laitos) skipped
        pyautogui.press("v", interval=0.5)  # Maksajan vaihto ...
        pyautogui.press("enter", interval=0.5)

        try:
            self.change_payer_window = windows.find_window(const.MAKSAJAN_VAIHTO_WND)
        except ElementNotFound as e:
            raise ApplicationException(
                f"Failed to open the Maksajan vaihto -window: {e}",
                code="CRITICAL_OPEN_FAILED",
            ) from e

    def update_current_owner_address(self, form: Form) -> None:
        """Sets the current payer address in the Vesikanta application."""
        self.change_payer_window.find(const.CURRENT_PAYER_ADDRESS_FLD).mouse_hover()
        # change_payer_window.set_value(
        #     form.former_owner.address,
        #     locator=const.CURRENT_PAYER_ADDRESS_FLD,
        # )

    def move_current_payer_to_history_if_eligible(self) -> None:
        """Moves the payer to history if only one active contract exists."""
        self._open_current_payer_info_window()
        if self._has_single_active_contract():
            self._move_payer_to_history()
        # self._close_window(self.payer_info_window)

    def _open_current_payer_info_window(self) -> None:
        self.change_payer_window.click(const.CURRENT_PAYER_INFO_BTN)
        self.payer_info_window = windows.find_window(const.MAKSAJATIEDOT_WND)

    def _has_single_active_contract(self) -> bool:
        """Checks if there is only one active contract."""
        consumption_points = self.payer_info_window.click(
            const.CONSUMPTION_POINT_DROPDWN
        )
        contracts_list = consumption_points.find_many(const.CONSUMPTION_LIST_ITEM)
        log.info(f"Number of active contracts: {len(contracts_list)}")
        return len(contracts_list) == 1

    def _move_payer_to_history(self) -> None:
        """Moves the payer to the history group."""
        self.payer_info_window.double_click(const.CUSTOMER_GRP_BTN)
        customer_groups_window = self.payer_info_window.find_child_window(
            const.ASIAKASRYHMAT_WND
        )

        delineation_field = customer_groups_window.find(const.DELINEATION_FLD)
        delineation_field.send_keys("historia")
        customer_groups_window.send_keys("{tab}")
        customer_groups_window.send_keys("{down}")
        # test
        # customer_groups_window.click(const.AR_SAVE_BTN)
        # self._close_window(customer_groups_window)

    def new_owner_found_from_database(self, form: Form) -> bool:
        # TEST
        self.change_payer_window = windows.find_window(const.MAKSAJAN_VAIHTO_WND)
        """
        Searches for the new property owner from the Vesikanta customers.
        Returns:
            bool: `True` if exactly one customer is found and selected,
            `False` if no customers are found.
        """
        self._open_search_customer_window()
        self._fill_customer_search_form(form)
        customers_count = self._perform_customer_search_and_get_count()

        if self._no_customers_found(customers_count):
            return False

        self._handle_multiple_customer_matches(customers_count)
        self._select_single_customer_from_results()
        return True

    def _perform_customer_search_and_get_count(self) -> int:
        """Executes the customer search and returns the count of matches"""
        self.search_customers_window.click(const.AH_SEARCH_BTN)
        search_results_element = self.search_customers_window.find(
            const.AH_SEARCH_RESULTS_TXT
        )

        # Find the count of search results
        number_regex = r"\d+"
        customers_count = re.search(number_regex, search_results_element.name)
        return int(customers_count.group()) if customers_count else 0

    def _select_single_customer_from_results(self) -> None:
        """Selects the customer from the search results and closes the search"""
        search_results_table = self.search_customers_window.find(
            const.AH_SEARCH_RESULTS_TBL
        )
        search_results_table.set_focus()
        search_results_table.send_keys("{down}")
        search_results_table.double_click()
        self._close_window(self.search_customers_window)

    def _fill_customer_search_form(self, form: Form) -> None:
        """Fills out the customer search form with provided data"""
        search_fields = {
            const.AH_NAME_FLD: form.new_owner.name,
            const.AH_ADDRESS_FLD: form.real_estate.address,
        }
        for locator, value in search_fields.items():
            self.search_customers_window.send_keys(value, locator=locator)

    def _open_search_customer_window(self) -> None:
        self.change_payer_window.click(const.SEARCH_CUSTOMER_BTN)
        self.search_customers_window = self.change_payer_window.find_child_window(
            const.ASIAKKAIDEN_HAKU_WND
        )

    def _no_customers_found(self, customers_count: int) -> bool:
        """Returns `True` if no customers were found."""
        if customers_count == 0:
            self._close_window(self.search_customers_window)
            return True
        return False

    def _handle_multiple_customer_matches(self, customers_count: int) -> None:
        if customers_count > 1:
            raise BusinessException(
                message=f"Many matches found: {customers_count}",
                code="CRITICAL_CUSTOMER_MATCHES",
            )

    def create_new_owner(self, form: Form) -> None:
        """
        Add a new customer to the Vesikanta application.
        TODO: Company logic
        """
        self._open_new_payer_info_window()

        # Set the new customer info
        owner_info = {
            const.PAYER_INFO_NAME_FLD: form.new_owner.name,
            const.PAYER_INFO_ID_FIELD: form.new_owner.id,
            const.PAYER_INFO_ADDRESS_FLD: form.new_owner.address,
            const.PAYER_INFO_POSTAL_CODE_FLD: form.new_owner.mail_number,
            const.PAYER_INFO_PHONE_FLD: form.new_owner.phone,
            const.PAYER_INFO_EMAIL_FLD: form.new_owner.email,
        }

        for field, value in owner_info.items():
            self.payer_info_window.set_value(value, locator=field)

        customer_type = self._determine_customer_type(form.new_owner)
        self.payer_info_window.set_value(customer_type, locator=const.CUSTOMER_TYPE_FLD)

        self._save_and_close_payer_info()

    def _open_new_payer_info_window(self) -> None:
        self.change_payer_window.click(const.OPEN_MAKSAJATIEDOT_BTN)
        self.payer_info_window = windows.find_window(const.MAKSAJATIEDOT_WND)
        self.payer_info_window.click(const.PAYER_INFO_NEW_BTN)

    def _determine_customer_type(self, new_owner: Customer | Company):
        return const.CUSTOMER if isinstance(new_owner, Customer) else const.COMPANY

    def _save_and_close_payer_info(self) -> None:
        # test
        pass
        # self.payer_info_window.click(const.PAYER_INFO_SAVE_BTN)
        # self._close_window(self.payer_info_window)

    def set_payer_change_info(self, form: Form) -> None:
        """
        Sets the payer change information in the Vesikanta application.

        Args:
            form (Form): Form object containing the necessary data for the payer change.
        """
        self._set_transfer_date(form)
        self._set_final_reading_details(form)

    def _set_transfer_date(self, form: Form) -> None:
        # TEST
        self.change_payer_window = windows.find_window(const.MAKSAJAN_VAIHTO_WND)
        """Sets the final invoice details in the payer change window."""
        date_field = self.change_payer_window.set_focus(const.FINAL_INVOICE_DATE_FLD)
        date_field.send_keys(form.transfer_date)

    def _set_final_reading_details(self, form: Form) -> None:
        """Sets the final reading details in the Vesikanta application."""
        self._open_readings_window()
        self._handle_missing_estimate_popup()
        self._handle_missing_meter_popup()

        # Set transfer type as "Omistajanvaihto"
        self._set_transfer_type()
        self._validate_and_set_reading(form.meter_reading)
        self._save_and_close_reading_window()

    def _open_readings_window(self) -> None:
        """Opens the consumption readings window."""
        self.change_payer_window.click(const.FINAL_READING_BTN)
        self.consumption_readings_window = windows.find_window(const.KULUTUSLUKEMAT_WND)

    def _handle_missing_estimate_popup(self) -> None:
        """Handles the 'estimate missing' popup if it appears."""
        missing_estimate_popup = self._find_child_window_without_logging(
            self.consumption_readings_window, const.ESTIMATE_MISSING_POPUP, timeout=2
        )
        if missing_estimate_popup:
            missing_estimate_popup.click(const.OK_BTN)

    def _handle_missing_meter_popup(self) -> None:
        """Handles the 'meter missing' popup and raises an exception if necessary."""
        meter_missing_popup = self._find_child_window_without_logging(
            self.consumption_readings_window, const.METER_MISSING_POPUP, timeout=2
        )
        if meter_missing_popup:
            with pyautogui.hold("alt"):
                pyautogui.press("n")
            raise BusinessException(
                message="Water meter not found!",
                code="CRITICAL_METER_MISSING",
            )

    def _set_transfer_type(self) -> None:
        """Sets the transfer type in the readings window."""
        self.consumption_readings_window.send_keys(
            "1", locator=const.READING_EXPLANATION_FIELD
        )

    def _validate_and_set_reading(self, meter_reading: int) -> None:
        """Validates the former reading and sets the new meter reading."""
        reading = self.consumption_readings_window.get_value(const.FORMER_READING_FIELD)

        # Check that the reading is a valid digit and smaller than the current meter reading
        if reading.isdigit() and int(reading) <= meter_reading:
            self.consumption_readings_window.set_value(
                meter_reading, locator=const.READING_FLD
            )
        else:
            raise BusinessException(
                message="Former reading not present, or is greater than current reading!",
                code="CRITICAL_READING_ISSUE",
            )

    def _save_and_close_reading_window(self) -> None:
        """Saves the done changes and closes the readings window."""
        # test
        # consumption_readings_window.click(const.KL_SAVE_BTN)
        # self._close_window(self.consumption_readings_window)

    def create_invoice(self) -> None:
        # TODO
        """Creates an invoice in the Vesikanta application."""
        # Tee laskurivit
        # test
        # self.change_payer_window.click(const.CREATE_INVOICE_LINES_BTN)
        billing_lines_popup = self.change_payer_window.find('name:"Perusmaksurivit"')
        billing_lines_popup.click('class:"Button" and name:"Ok"')
        equalization_fee_popup = self.change_payer_window.find('name:"Tasausmaksut"')
        equalization_fee_popup.click('class:"Button" and name:"Ok"')
        billing_report_window = self.change_payer_window.find_child_window(
            'name:"Laskutusraportti"'
        )
        due_date_field = billing_report_window.find('class:"Edit"')
        due_date_field.send_keys("due_date")  # TODO HOW TO DETERMINE!?!
        billing_report_window.click('class:"Button" and name:"Tulosta"')
        billing_print_window = billing_report_window.find_child_window(
            'name:"TULOSTUS"'
        )
        billing_print_window.click('class:"Button" and name:"Tulosta"')
        self.desktop.find_window('regex:"Gupta Report Builder"')
        with pyautogui.hold("alt"):
            pyautogui.press("p", interval=0.5)  # Print
            pyautogui.press("p", interval=0.5)  # Print (to open Win32 print -window)
        win_print_window = None  # TODO finalize printing
        self._close_window(billing_report_window)

        # Tee lasku
        # test
        # self.change_payer_window.click(const.CREATE_INVOICE_BTN)
        billing_window = self.change_payer_window.find_child_window('name:"Laskutus"')
        due_date_field = billing_window.find('class:"Edit" and name:"Eräpäivä"')
        due_date_field.send_keys("due_date")  # TODO HOW TO DETERMINE!?!
        billing_window.click('class:"Button" and name:"Laskutuserä_btn"')
        billing_batch_window = billing_window.find_child_window('name:"Laskutuserä"')
        billing_batch_window  # TODO set latest batch NOTE how to create new batch?
        billing_batch_window.click('class:"Button" and name:"Suorita"')
        create_zip_file_popup = billing_batch_window.find_child_window(
            'name:"Tulostus"'
        )
        create_zip_file_popup.click('class:"Button" and name:"Yes"')
        remove_xml_popup = billing_batch_window.find_child_window('name:"Zip"')
        remove_xml_popup.click('class:"Button" and name:"Yes"')
        printing_popup = billing_batch_window.find_child_window('name:"Tulostus"')
        printing_popup.click('class:"Button" and name:"OK"')
        self._close_window(billing_batch_window)

    def perform_customer_change(self) -> None:
        # TODO
        """Performs the join change removal in the Vesikanta application."""
        # test
        # self.change_payer_window.click(const.JOIN_CHANGE_REMOVE_BTN)
        payer_change_confirmation_popup = self.change_payer_window.find_child_window(
            'name:"Maksajan vaihto kulutuspisteelle"'
        )
        payer_change_confirmation_popup.click('class:"Button" and name:"Yes"')
        change_email_and_phone_popup = self.change_payer_window.find_child_window(
            'name:"Tietokanta"'
        )
        change_email_and_phone_popup.click('class:"Button" and name:"Yes"')
        reset_id_popup = self.change_payer_window.find_child_window('name:"Tietokanta"')
        reset_id_popup.click('class:"Button" and name:"Yes"')
        change_name_popup = self.change_payer_window.find_child_window(
            'name:"Tietokanta"'
        )
        change_name_popup.click('class:"Button" and name:"Yes"')
        contract_termination_window = self.change_payer_window.find_child_window(
            'name:"Sopimuksen päättäminen"'
        )
        termination_date_field = contract_termination_window.find('class:"Edit"')
        termination_date_field.send_keys("termination_date")
        contract_termination_window.click('class:"Button" and name:"Kyllä"')
        self._close_window(self.change_payer_window)

    def open_kulutuspiste_window(self) -> None:
        """
        Opens the Kulutuspiste -window in the Vesikanta application.

        Raises:
            `Exception`: If the Kulutuspiste -window fails to open.
        """
        self.vesikanta_window = self._get_main_window()
        with pyautogui.hold("alt"):
            pyautogui.press("a", interval=0.5)  # Asiakastiedot
        pyautogui.press(
            "enter", interval=0.5
        )  # Kulutuspiste ... (NOTE: the first item in the sub-menu)

        try:
            self.consumption_point_window = windows.find_window(const.KULUTUSPISTE_WND)
        except ElementNotFound as e:
            raise ApplicationException(
                "Failed to open the Kulutuspiste -window",
                code="CRITICAL_OPEN_FAILED",
            ) from e

    # Placeholder comment for JPH development TODO

    def set_yearly_consumption_estimate(self, form: Form) -> None:
        """Opens Laskutustiedot -tab and fills in the yearly water consumption estimate"""
        with pyautogui.hold("alt"):
            pyautogui.press("l")

        self.consumption_point_window.send_keys(
            str(form.consumption_estimate), locator=const.YEARLY_CONSUMPTION_FIELD
        )
        # test
        # self.consumption_point_window.click(const.CONSUMPTION_SAVE_BUTTON)

    def open_property_processing(self) -> None:
        """Opens the property processing window in the Vesikanta application."""
        with pyautogui.hold("alt"):
            pyautogui.press("r")
        self.consumption_point_window.click(const.PROPERTY_PROCESSING_BTN)
        self.property_window = self.consumption_point_window.find_child_window(
            const.PROPERTY_WINDOW
        )

    def change_owner_name(self, form: Form) -> None:
        """Update the property owner's name by interacting with the UI.

        This method locates a clickable element in the property owner table
        that is not directly accessible through automation, simulates a mouse hover and click,
        and updates the owner name field with the new owner's full name from the form.

        Args:
            form (Form): The form containing the new owner's details
        """
        # Move mouse and locate clickable element that automation can't see
        self.property_window.find(const.PROPERTY_OWNER_TABLE).mouse_hover()
        pyautogui.move(-110, -120)
        pyautogui.click()

        # This field becomes visible after clicking
        name_field = self.property_window.find(const.OWNER_NAME_FIELD)
        name_field.set_value("")
        name_field.send_keys(form.new_owner.name)

        # test
        # self.property_window.click(const.PROPERTY_SAVE_BUTTON)

    def edit_property_owners(self, form: Form) -> None:
        self.property_window = self.consumption_point_window.find_child_window(
            const.PROPERTY_WINDOW
        )
        """This method opens the property owners window, deletes the current owner 
        if applicable, and adds a new owner by entering the full name from the form. 
        It handles interaction with UI elements that are not directly accessible 
        via automation by simulating mouse hovers and clicks.

        Args:
            form (Form): The form containing the new owner's details."""
        self.property_window.click(const.PROPERTY_OWNERS_BUTTON)
        property_owners_window = self.property_window.find_child_window(
            const.PROPERTY_OWNERS_WINDOW
        )
        # Move mouse and locate clickable element that automation can't see
        property_owners_window.find(const.PROPERTY_ID).mouse_hover()
        pyautogui.move(-60, 50)
        pyautogui.click()

        # test
        # property_owners_window.click(const.DELETE_BUTTON)

        confirm_delete_popup = property_owners_window.find_child_window(
            const.CONFIRM_DELETE_POPUP
        )

        # test
        # confirm_delete_popup.click(const.CONFIRM_DELETE_YES_BUTTON)

        property_owners_window.click(const.NEW_OWNER_BUTTON)
        property_owners_window.send_keys(form.new_owner.name)

        # test
        # property_owners_window.click(const.SAVE_PROPERTY_OWNERS)

        self._close_window(property_owners_window)

    def handle_property_registry_info(self) -> None:
        self.property_window = self.consumption_point_window.find_child_window(
            const.PROPERTY_WINDOW
        )
        """
        Handle property registry information by interacting with the registry 
        processing window and importing new or changed property and building data.

        This method navigates through various windows related to property registry 
        processing, retrieves updated registry data, and configures the import 
        settings for properties and buildings.

        It handles the following steps:
        1. Opens the registry processing window.
        2. Imports property data.
        3. Imports building data with specific filters applied (e.g., project buildings, only new).
        4. Closes the registry processing window.
        """
        self.property_window.click(const.REGISTRY_PROCESSING_BUTTON)
        registry_processing_window = self.property_window.find_child_window(
            const.REGISTRY_PROCESSING_WINDOW
        )
        registry_processing_window.click(const.REGISTRY_PROPERTIES_BUTTON)
        import_properties_window = registry_processing_window.find_child_window(
            const.IMPORT_PROPERTIES_WINDOW, timeout=60
        )
        self._fetch_new_and_changed_registry_data(import_properties_window)
        import_properties_window.click(const.RETURN_BUTTON)

        registry_processing_window.click(const.REGISTRY_BUILDINGS_BUTTON)
        buildings_to_property_window = registry_processing_window.find_child_window(
            const.BUILDINGS_TO_PROPERTY_WINDOW, timeout=60
        )
        self._fetch_new_and_changed_registry_data(buildings_to_property_window)
        buildings_to_property_window.click(const.PROJECT_BUILDINGS_RADIO)
        buildings_to_property_window.click(const.ONLY_NEW_RADIO)
        self._fetch_new_and_changed_registry_data(buildings_to_property_window)
        buildings_to_property_window.click(const.RETURN_BUTTON)

        self._close_window(registry_processing_window)

    def _fetch_new_and_changed_registry_data(self, window: WindowElement) -> None:
        """
        Fetch new and changed registry data by interacting with the given window.

        This method triggers the data fetching process twice: first for the selected data,
        and then for data marked as changed. It clicks the appropriate UI elements and moves
        data within the window.

        Args:
            window (WindowElement): The window containing the registry data fetching options.
        """
        self._fetch_chosen_and_move(window)
        window.click(const.ONLY_CHANGED_RADIO)
        self._fetch_chosen_and_move(window)

    def _fetch_chosen_and_move(self, window: WindowElement) -> None:
        """
        Fetch selected registry data, transfer it, and save the changes.

        This method interacts with the window by:
        1. Clicking the 'Fetch Chosen' button to fetch the selected data.
        2. Clicking the 'Transfer' button to move the data.
        3. Clicking the 'Save' button to save the registry changes.

        Delays are introduced between actions to ensure UI responsiveness.

        Args:
            window (WindowElement): The window where the data fetching, transferring,
                                    and saving actions are performed.
        """
        window.click(const.FETCH_CHOSEN)
        time.sleep(0.5)  # sleep

        # window.click(const.TRANSFER_BUTTON)
        time.sleep(0.5)  # sleep

        # window.click(const.REGISTRY_SAVE_BUTTON)
        time.sleep(0.5)  # sleep

    def handle_connection_application(self, form: Form, config: Config) -> None:
        self.property_window = self.consumption_point_window.find_child_window(
            const.PROPERTY_WINDOW
        )
        """TODO"""
        self.property_window.click(const.CONNECTION_POINT_BTN)
        connection_point_window = self.property_window.find_child_window(
            const.JOINING_POINT_WINDOW
        )

        # connection_point_window.click(const.JOINING_POINT_OWNER_COMBOBOX)
        # connection_point_window.select(
        #     form.new_owner.name, locator=const.JOINING_POINT_OWNER_COMBOBOX
        # )
        # # test hover
        # connection_point_window.find(const.JOINING_POINT_SAVE_BUTTON).mouse_hover()
        # # connection_point_window.click(const.JOINING_POINT_SAVE_BUTTON)

        connection_point_window.click(const.CONNECTION_APPLICATION_BTN)

        application_window = connection_point_window.find_child_window(
            const.LIITTYMISHAKEMUS_WND
        )
        """# test hover
        application_window.find(const.LH_NEW_BTN).mouse_hover()
        # application_window.click(const.LH_NEW_BTN)

        application_window.click(const.LH_OWNERS_CMB)
        application_window.select(form.new_owner.name, locator=const.LH_OWNERS_CMB)
        application_window.click(const.EXISTING_BUILDING_CHK)"""

        # test
        # application_window.click(const.CONNECTION_APPLICATION_SAVE_BUTTON)

        application_window.click(const.AGREEMENTS_BTN)

        agreements_window = application_window.find_child_window(
            const.AGREEMENTS_WINDOW
        )
        agreements_window.click(const.CUSTOMER_BUTTON)
        agreements_customer_window = agreements_window.find_child_window(
            const.AGREEMENTS_CUSTOMER_WINDOW
        )
        agreements_customer_window.send_keys(
            form.new_owner.name, locator=const.AGREEMENTS_CUSTOMER_NAME_FIELD
        )

        search_results_table = agreements_customer_window.find(
            const.AGREEMENTS_CUSTOMER_SEARCH_RESULTS
        )
        search_results_table.set_focus()
        search_results_table.send_keys("{down}")
        search_results_table.send_keys("{space}")

        agreements_customer_window.click(const.CHOOSE_SEARCH_RESULTS_BUTTON)

        application_window.click(const.ADDITIONAL_INFO_BOX)
        application_window.send_keys(
            const.OWNER_CHANGE, locator=const.ADDITIONAL_INFO_BOX
        )

        application_window.click(const.TAX_CHECKBOX)

        # set signature
        # combo = application_window.click(const.LKS_SIGNATURE_NAME_CMB)
        application_window.set_value(
            config.signature, locator=const.LKS_SIGNATURE_NAME_CMB
        )

        signature_date_field = application_window.find(const.LKS_SIGNATURE_DATE_FLD)
        signature_date_field.send_keys(form.transfer_date)
        customer_signature_date_field = application_window.find(
            const.CUSTOMER_SIGNATURE_DATE
        )
        customer_signature_date_field.send_keys(form.transfer_date)

        self._set_attachments()

        buildings_count = 1
        if buildings_count > 1:
            # TODO Implementation of adding info about additional buildings
            pass

        # test
        # application_window.click(const.CONTRACT_SAVE_BUTTON)

        # test
        # application_window.click(const.FILL_CONSUMPTION_POINT_INFO_BUTTON)

        # test
        # application_window.click(const.CONTRACT_SAVE_BUTTON)

    def print_contract(self) -> None:
        # TODO
        self.consumption_point_window = windows.find_window(const.KULUTUSPISTE_WND)
        self.property_window = self.consumption_point_window.find_child_window(
            const.PROPERTY_WINDOW
        )
        connection_point_window = self.property_window.find_child_window(
            const.JOINING_POINT_WINDOW
        )
        application_window = connection_point_window.find_child_window(
            const.LIITTYMISHAKEMUS_WND
        )
        self.agreements_window = application_window.find_child_window(
            const.AGREEMENTS_WINDOW
        )
        """TODO"""
        datetime_now = datetime.now().strftime(self.config.date_format)
        self.agreements_window.click(const.LKS_PRINT_BTN)
        print_window = self.agreements_window.find_child_window(const.LKS_PRINT_WND)
        # print_window.click(const.LKS_PW_PRINT_BTN)

        # Define the path where the report will be saved
        report_path = self.config.form_report_folder
        path = Path(report_path)

        # Click the folder button to avoid SQL error. Close the folder window when it opens.
        print_window.click(const.FOLDER_BTN)
        self._close_folder_window()
        print_window.click(const.PRINT_BTN)

        # Report Builder -window
        report_builder_window = self.desktop.find_window(const.REPORT_BUILDER_WND)
        with pyautogui.hold("alt"):
            pyautogui.press("p", interval=0.5)  # Print
            pyautogui.press("p", interval=0.5)  # Print (to open Win32 print -window)

        # Win32 printing window
        win32_print_window = self.desktop.find_window(const.WIN32_PRINT_WND)

        # Open the printer list and select the PDF printer
        win32_print_window.click(const.WIN32_PRINTER_LST)
        win32_print_window.find(const.WIN32_PRINTER_LST).click(const.PDF_PRINTER)
        win32_print_window.click(const.WIN32_PRINT_BTN)

        # Save file window
        report_file_name = "Omistajanvaihdos_" + datetime_now + ".pdf"
        report_file_path = path / report_file_name
        save_file_window = report_builder_window.find_child_window(const.SAVE_PDF_WND)
        with pyautogui.hold("alt"):
            pyautogui.press("up", 10, 0.3)

        save_file_window.click('id:"1001" and regex:"Osoite:*"')
        save_file_window.find("id:41477").send_keys(report_path, send_enter=True)
        save_file_window.find(const.SAVE_PDF_NAME_FLD).set_value(report_file_name)
        save_file_window.click(const.SAVE_PDF_FILE_BTN)

        # Wait for the report file to be created before continuing
        file_size_zero = 0
        while os.path.getsize(report_file_path) == file_size_zero:
            time.sleep(1)

        # Close the printing windows
        if not report_builder_window.is_disposed():
            with pyautogui.hold("alt"):
                pyautogui.press("f", interval=0.5)  # File
                pyautogui.press("c", interval=0.5)  # Close

        self._close_window(print_window)

    def _set_attachments(self) -> None:
        """Sets the attachments in the Vesikanta application."""
        self.agreements_window.click(const.ATTACHMENTS_BTN)
        attachments_window = self.agreements_window.find_child_window(
            const.LIITTEET_WND
        )
        attachments_window.click(const.LKS_TERMS_CHK)
        attachments_window.click(const.LKS_PAYMENT_OR_PRICE_CHK)
        attachments_window.click(const.LKS_GENERAL_TERMS_CHK)
        # test
        # attachments_window.click(const.ATTACHMENTS_SAVE_BUTTON)
        # self._close_window(attachments_window)
