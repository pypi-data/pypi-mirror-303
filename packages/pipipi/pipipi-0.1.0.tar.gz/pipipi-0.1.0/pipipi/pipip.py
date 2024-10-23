import os
import sys
import subprocess
import argparse
from pathlib import Path
from typing import TypedDict, NotRequired, Optional, Iterable

class PackageInfo(TypedDict):
    package: str
    index_url: NotRequired[str]

class NotFoundError(Exception):
    pass

def parse_package_name(package: str) -> PackageInfo:
    if "@index=" in package:
        package, index_url = package.split("@index=")
        return {"package": package, "index_url": index_url}
    return {"package": package}

def install_packages_from_same_index(packages: list[str], index_url: Optional[str], pip_args: list[str] = [], *, dry: bool = False) -> Optional[set[str]]:
    """
    (Dry) Installs the requested packages and any dependencies from the same index_url

    If dry, returns a set of packages that would be installed
    """

    command = [sys.executable, "-m", "pip", "install"] + pip_args + packages
    if dry:
        command += ["--dry-run"]
    if index_url:
        command += ["--index-url", index_url]

    print("Running", *command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    packages: set[str] = set()

    # Read stdout and stderr in real time
    for line in iter(process.stdout.readline, ""):
        if dry:
            line = line.strip()
            if line.startswith("Would install"):
                packages.add(line.removeprefix("Would install "))
        else:
            print(line, end='')  # Print to console

    for errline in iter(process.stderr.readline, ""):
        print(errline, end='', file=sys.stderr)  # Print to console

    process.stdout.close()
    process.stderr.close()
    process.wait()

    return packages if dry else None

def install_packages(packages: list[str], pip_args: list[str] = [], validate: bool = True, ask: bool = True):
    packages_info = [parse_package_name(package) for package in packages]

    packages: set[Path] = set()

    # Separate packages by index_url
    index_url_to_packages = {}
    for package_info in packages_info:
        index_url = package_info.get("index_url")
        if index_url not in index_url_to_packages:
            index_url_to_packages[index_url] = []
        index_url_to_packages[index_url].append(package_info["package"])

    # Dry install packages from the same index
    if validate:
        print("Checking packages to install...")
        for index_url, pkgs in index_url_to_packages.items():
            new_pkgs = install_packages_from_same_index(pkgs, index_url, pip_args, dry=True)
            packages.update(new_pkgs)

        if not packages:
            print("Nothing to install")
            sys.exit(0)

        # Ask user to confirm installation
        if ask:
            print("The following packages will be installed:", *packages)
            if input("Proceed? [Y/n] ").lower() == "n":
                print("Installation aborted")
                sys.exit(1)

    # Run real install
    for index_url, pkgs in index_url_to_packages.items():
        install_packages_from_same_index(pkgs, index_url, pip_args)

    return

def install_requirements(requirements: list[str], pip_args: list[str] = [], validate: bool = True, ask: bool = True):
    for requirement in requirements:
        with open(requirement, 'r') as f:
            packages = [line.strip() for line in f.readlines()]
            install_packages(packages, pip_args, validate, ask)

def main():
    __VERSION__ = "Pipip 0.1.0"
    parser = argparse.ArgumentParser(description="Pipip - A minimal extension to pip")
    parser.add_argument("-v", "--version", action="version", version=__VERSION__)
    parser.add_argument("packages", type=str, nargs='*', help="Packages to install") # Can be empty (if -r is set)
    parser.add_argument("-r", "--requirements", type=str, nargs='+', help="Read from requirements file") # If present, must have 1+
    parser.add_argument("--no-validation", action="store_true", help="Do not perform a dry run to validate packages, can speed up installation")
    parser.add_argument("-y", "--yes", action="store_true", help="Automatically confirm installation")
    parser.add_argument('pip_args', nargs=argparse.REMAINDER, help='Any additional arguments to pass to pip') # Pass through to pip

    args = parser.parse_args()
        

    # Check if packages xor requirements are provided
    if not args.packages and not args.requirements:
        parser.print_help()
        sys.exit(1)
    
    if args.packages and args.requirements:
        parser.error("Cannot specify both packages and requirements file")
        sys.exit(1)

    print("DISCLAIMER: Pipip enables you to install packages from custom indexes. Be cautious of the packages you install.")

    # Perform installation
    # Remove --index-url from pip_args if present
    pip_args = args.pip_args.copy()
    if "--index-url" in pip_args:
        index_url_index = pip_args.index("--index-url")
        del pip_args[index_url_index:index_url_index+2]
    if args.packages:
        install_packages(args.packages, pip_args, not args.yes)
    else:
        install_requirements(args.requirements, pip_args, not args.yes)

if __name__ == "__main__":
    main()