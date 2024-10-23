import subprocess
import asyncio
from py2docfx import PACKAGE_ROOT

PYPI = "pypi"

pip_install_common_options = [
    # "--no-cache-dir", # to reduce install duration after switching to each venv
    "--quiet",
    "--no-compile",
    "--no-warn-conflicts",
    "--disable-pip-version-check",
    "--verbose",
]


def download(package_name, path, extra_index_url=None, prefer_source_distribution=True):
    # Downloads a package from PyPI to the specified path using pip.
    download_param = ["pip", "download", "--dest", path, "--no-deps", package_name]
    if extra_index_url:
        download_param.append("--extra-index-url")
        download_param.append(extra_index_url)
    if prefer_source_distribution:
        download_param.append("--no-binary=:all:")
    else:
        download_param.append("--prefer-binary")
    subprocess.run(download_param, check=True, cwd=PACKAGE_ROOT)


def install(package_name, options):
    # Installs a package from PyPI using pip.
    install_param = "pip install {} {}".format(
        " ".join(pip_install_common_options + options), package_name
    ).split(" ")
    subprocess.run(install_param, check=True, cwd=PACKAGE_ROOT)


def install_in_exe(exe_path, package_name, options):
    # Installs a package from PyPI using pip.
    install_param = [exe_path] + "-m pip install {} {}".format(
        " ".join(pip_install_common_options + options), package_name
    ).split(" ")
    subprocess.run(install_param, check=True, cwd=PACKAGE_ROOT)

async def install_in_exe_async(exe_path, package_name, options):
    pip_cmd = ["-m", "pip", "install"]+ pip_install_common_options + options + [package_name]
    await(await asyncio.create_subprocess_exec(exe_path, *pip_cmd)).wait()