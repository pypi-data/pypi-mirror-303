import os
from setuptools import setup, find_packages
from al78tools.pysetup.tools import get_file_content, get_file_content_as_list


pwd = os.path.dirname(__file__)

packages = find_packages()
VERSION = get_file_content(os.path.join(pwd, "VERSION"))
README_MD = get_file_content(os.path.join(pwd, "README.md"))
requirements = get_file_content_as_list(os.path.join(pwd, "requirements.txt"))


print(f"packages: {packages}")
print(f"requirements: {requirements}")

setup(
    name="al78tools",
    version=VERSION,
    license='MIT',
    author='Ales Adamek',
    author_email='alda78@seznam.cz',
    description='Tools for PySetup etc.',
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/alda78/al78tools",
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,  # MANIFEST.in
    zip_safe=False,  # aby se spravne vycitala statika pridana pomoci MANIFEST.in
)
