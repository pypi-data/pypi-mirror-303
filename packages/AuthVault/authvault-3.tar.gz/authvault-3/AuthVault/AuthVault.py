import os
import requests
import platform
import hashlib
import subprocess
import ctypes
from pathlib import Path


class AuthVault:
    is_initialized = False

    @staticmethod
    def error(message):
        print(f"Error: {message}")
        ctypes.windll.user32.MessageBoxW(0, message, "Error", 0)
        exit(1)

    @staticmethod
    def get_username():
        return os.getlogin()

    @staticmethod
    def check_initialization():
        if not AuthVault.is_initialized:
            AuthVault.error("AuthVault is not initialized! Call AuthVault.setup() before any other function.")

    @staticmethod
    def create_appdata_folder():
        appdata_path = Path(f"C:/Users/{AuthVault.get_username()}/AppData/Roaming/authvault")
        if not appdata_path.exists():
            try:
                appdata_path.mkdir(parents=True, exist_ok=True)
                print(f"Created AppData folder at {appdata_path}")
            except Exception as e:
                AuthVault.error(f"Failed to create AppData folder: {e}")

    @staticmethod
    def get_hwid():
        if platform.system() == "Windows":
            try:
                # Get CPU ID
                cpu_id_cmd = "wmic csproduct get uuid"
                cpu_id = subprocess.check_output(cpu_id_cmd, shell=True).decode().split("\n")[1].strip()

                # Get Disk Volume Serial Number
                vol_cmd = "vol C:"
                vol_serial = subprocess.check_output(vol_cmd, shell=True).decode().split()[-1]

                hwid_combined = cpu_id + vol_serial

                # Hash HWID for uniqueness
                hwid_hashed = hashlib.sha256(hwid_combined.encode()).hexdigest()
                return hwid_hashed
            except Exception as e:
                AuthVault.error(f"Error generating HWID: {e}")
        else:
            AuthVault.error("HWID generation is supported only on Windows.")

    @staticmethod
    def is_online():
        try:
            response = requests.get("https://8.8.8.8", timeout=3)  # Google DNS
            return True
        except requests.ConnectionError:
            return False

    @staticmethod
    def validate_license_key(license_key, application_id, secret):
        AuthVault.check_initialization()

        if not AuthVault.is_online():
            AuthVault.error("No stable internet connection detected.")

        hwid = AuthVault.get_hwid()
        url = f"https://authvault-api-3.tiiny.io/?license_key={license_key}&application_id={application_id}&secret={secret}&hwid={hwid}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "valid":
                    print("License is valid.")
                    return True
                else:
                    print("License is invalid.")
                    return False
            else:
                AuthVault.error(f"Failed to validate license key. HTTP Status: {response.status_code}")
        except Exception as e:
            AuthVault.error(f"An error occurred during license validation: {e}")

    @staticmethod
    def setup():
        print("Initializing AuthVault...")
        AuthVault.create_appdata_folder()
        AuthVault.is_initialized = True
        print("AuthVault initialized successfully.")
