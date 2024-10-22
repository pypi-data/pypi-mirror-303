from setuptools import setup, find_namespace_packages
import os


# Function to read the version from version.py
def get_version():
    version_file = os.path.join("zinley", "version.py")
    try:
        with open(version_file) as f:
            code = compile(f.read(), version_file, "exec")
            version_ns = {}
            exec(code, version_ns)
            return version_ns["__version__"]
    except FileNotFoundError:
        raise RuntimeError("version.py not found in zinley package")


# Attempt to read requirements.txt
try:
    with open("requirements.txt") as f:
        required = f.read().splitlines()
except FileNotFoundError:
    required = []
    print("requirements.txt not found, proceeding without external dependencies")


setup(
    name="zinley-cli",
    version=get_version(),
    packages=find_namespace_packages(include=["zinley", "zinley.*"]),
    include_package_data=True,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "zinley = zinley.__main__:main",  # Ensure __main__.py has a main() function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
