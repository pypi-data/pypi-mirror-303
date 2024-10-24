#!/usr/bin/env python3 -B
# coding=utf-8

"""
Copyright (C) 2022-2024 Plato Mavropoulos
"""

import os
import subprocess

from typing import Final

from biosutilities.common.externals import szip_path, tiano_path
from biosutilities.common.paths import is_dir, is_empty_dir
from biosutilities.common.system import printer

# 7-Zip switches to auto rename, ignore passwords, ignore prompts, ignore wildcards,
# eliminate root duplication, set UTF-8 charset, suppress stdout, suppress stderr,
# suppress progress, disable headers, disable progress, disable output logs
SZIP_COMMON: Final[list[str]] = ['-aou', '-p', '-y', '-spd', '-spe', '-sccUTF-8',
                                 '-bso0', '-bse0', '-bsp0', '-ba', '-bd', '-bb0']

# Success exit codes (0 = OK, 1 = Warnings)
SZIP_SUCCESS: Final[list[int]] = [0, 1]


def szip_code_assert(exit_code: int) -> None:
    """ Check 7-Zip bad exit codes (0 OK, 1 Warning) """

    if exit_code not in SZIP_SUCCESS:
        raise ValueError(f'Bad exit code: {exit_code}')


def szip_switches(in_switches: list[str]) -> list[str]:
    """ Generate 7-Zip command line switches """

    common_switches: list[str] = SZIP_COMMON

    for in_switch in in_switches:
        for sw_pattern in ('-p', '-ao', '-bs', '-bb', '-scc'):
            if in_switch.startswith(sw_pattern):
                common_switches = [sw for sw in common_switches if not sw.startswith(sw_pattern)]

                break

    return [*set(common_switches + in_switches), '--']


def is_szip_supported(in_path: str, padding: int = 0, args: list | None = None, silent: bool = True) -> bool:
    """ Check if file is 7-Zip supported """

    try:
        if args is None:
            args = []

        szip_c: list[str] = [szip_path(), 't', *szip_switches(in_switches=[*args]), in_path]

        szip_t: subprocess.CompletedProcess[bytes] = subprocess.run(szip_c, check=False)

        szip_code_assert(exit_code=szip_t.returncode)
    except Exception as error:  # pylint: disable=broad-except
        if not silent:
            printer(message=f'Error: 7-Zip could not check support for file {in_path}: {error}!', padding=padding)

        return False

    return True


def szip_decompress(in_path: str, out_path: str, in_name: str = 'archive', padding: int = 0, args: list | None = None,
                    check: bool = False, silent: bool = False) -> bool:
    """ Archive decompression via 7-Zip """

    try:
        if args is None:
            args = []

        szip_c: list[str] = [szip_path(), 'x', *szip_switches(in_switches=[*args, f'-o{out_path}']), in_path]

        szip_x: subprocess.CompletedProcess[bytes] = subprocess.run(szip_c, check=False)

        if check:
            szip_code_assert(exit_code=szip_x.returncode)

        if not (is_dir(in_path=out_path) and not is_empty_dir(in_path=out_path)):
            raise OSError(f'Extraction directory is empty or missing: {out_path}')
    except Exception as error:  # pylint: disable=broad-except
        if not silent:
            printer(message=f'Error: 7-Zip could not extract {in_name} file {in_path}: {error}!', padding=padding)

        return False

    if not silent:
        printer(message=f'Successful {in_name} decompression via 7-Zip!', padding=padding)

    return True


def efi_compress_sizes(data: bytes | bytearray) -> tuple[int, int]:
    """ Get EFI compression sizes """

    size_compress: int = int.from_bytes(data[0x0:0x4], byteorder='little')

    size_original: int = int.from_bytes(data[0x4:0x8], byteorder='little')

    return size_compress, size_original


def is_efi_compressed(data: bytes | bytearray, strict: bool = True) -> bool:
    """ Check if data is EFI compressed, controlling EOF padding """

    size_comp, size_orig = efi_compress_sizes(data=data)

    check_diff: bool = size_comp < size_orig

    if strict:
        check_size: bool = size_comp + 0x8 == len(data)
    else:
        check_size = size_comp + 0x8 <= len(data)

    return check_diff and check_size


def efi_decompress(in_path: str, out_path: str, padding: int = 0, silent: bool = False,
                   comp_type: str = '--uefi') -> bool:
    """ EFI/Tiano Decompression via TianoCompress """

    try:
        subprocess.run([tiano_path(), '-d', in_path, '-o', out_path, '-q', comp_type],
                       check=True, stdout=subprocess.DEVNULL)

        with open(in_path, 'rb') as file:
            _, size_orig = efi_compress_sizes(data=file.read())

        if os.path.getsize(out_path) != size_orig:
            raise OSError('EFI decompressed file & header size mismatch!')
    except Exception as error:  # pylint: disable=broad-except
        if not silent:
            printer(message=f'Error: TianoCompress could not extract file {in_path}: {error}!', padding=padding)

        return False

    if not silent:
        printer(message='Successful EFI decompression via TianoCompress!', padding=padding)

    return True
