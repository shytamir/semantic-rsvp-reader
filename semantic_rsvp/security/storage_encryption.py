from __future__ import annotations

import platform
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class StorageEncryptionStatus:
    status: str
    message: str

    @property
    def warning(self) -> str | None:
        if self.status == "encrypted":
            return None
        return self.message


def check_storage_encryption(path: Path) -> StorageEncryptionStatus:
    system = platform.system().lower()
    if system == "windows":
        return _check_windows_bitlocker(path)
    if system == "darwin":
        return _check_macos_filevault()
    if system == "linux":
        return _check_linux_luks(path)
    return StorageEncryptionStatus(
        "unknown",
        "Storage encryption status could not be checked on this platform.",
    )


def _check_windows_bitlocker(path: Path) -> StorageEncryptionStatus:
    drive = _existing_path(path).resolve().drive
    if not drive:
        return StorageEncryptionStatus(
            "unknown",
            "Storage encryption status could not be checked because no drive was found.",
        )

    result = _run_fixed_command(["manage-bde", "-status", drive])
    if result is None:
        return StorageEncryptionStatus(
            "unknown",
            "BitLocker status could not be checked; manage-bde is unavailable or timed out.",
        )

    output = result.stdout.lower()
    if "protection status" in output and "protection on" in output:
        return StorageEncryptionStatus("encrypted", "BitLocker protection is enabled.")
    if "protection status" in output and "protection off" in output:
        return StorageEncryptionStatus(
            "unencrypted",
            "BitLocker protection appears to be off for the defect report storage drive.",
        )
    return StorageEncryptionStatus(
        "unknown",
        "BitLocker status output did not clearly confirm encrypted storage.",
    )


def _check_macos_filevault() -> StorageEncryptionStatus:
    result = _run_fixed_command(["fdesetup", "status"])
    if result is None:
        return StorageEncryptionStatus(
            "unknown",
            "FileVault status could not be checked; fdesetup is unavailable or timed out.",
        )

    output = result.stdout.lower()
    if "filevault is on" in output:
        return StorageEncryptionStatus("encrypted", "FileVault is enabled.")
    if "filevault is off" in output:
        return StorageEncryptionStatus(
            "unencrypted",
            "FileVault appears to be off for local defect report storage.",
        )
    return StorageEncryptionStatus(
        "unknown",
        "FileVault status output did not clearly confirm encrypted storage.",
    )


def _check_linux_luks(path: Path) -> StorageEncryptionStatus:
    findmnt = _run_fixed_command(
        ["findmnt", "-no", "SOURCE", "--target", str(_existing_path(path).resolve())]
    )
    if findmnt is None or findmnt.returncode != 0 or not findmnt.stdout.strip():
        return StorageEncryptionStatus(
            "unknown",
            "Linux storage encryption status could not be checked; findmnt failed.",
        )

    source = findmnt.stdout.strip().splitlines()[0]
    lsblk = _run_fixed_command(["lsblk", "-no", "TYPE,FSTYPE", source])
    if lsblk is None:
        return StorageEncryptionStatus(
            "unknown",
            "Linux storage encryption status could not be checked; lsblk failed.",
        )

    output = lsblk.stdout.lower()
    if "crypt" in output or "crypto_luks" in output:
        return StorageEncryptionStatus("encrypted", "LUKS encrypted storage was detected.")
    return StorageEncryptionStatus(
        "unknown",
        "Linux storage encryption could not be confirmed for the defect report path.",
    )


def _run_fixed_command(command: list[str]) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=3,
            shell=False,
            check=False,
        )
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
        return None


def _existing_path(path: Path) -> Path:
    current = path
    while not current.exists() and current != current.parent:
        current = current.parent
    return current
