import os
from importlib.metadata import version


def check_package_version_requirements(working_dir: str, requirements_file: str, exit_on_fail: bool = True):
    with open(os.path.join(working_dir, requirements_file)) as f:
        requirements = f.readlines()

    for requirement in requirements:
        if requirement.startswith("#") or requirement == "\n" or requirement == "" or "==" not in requirement:
            continue

        package_name, package_version = requirement.split("==")
        package_version = package_version.strip()

        try:
            installed_version = version(package_name)

            if installed_version != package_version:
                print(f"Package '{package_name}' is not at the required version! Should be: '{package_version}' but is '{installed_version}'.")
                if exit_on_fail:
                    exit(1)

        except Exception as e:
            print(e)
            print(f"Package {package_name} is not installed.")
            if exit_on_fail:
                exit(1)
