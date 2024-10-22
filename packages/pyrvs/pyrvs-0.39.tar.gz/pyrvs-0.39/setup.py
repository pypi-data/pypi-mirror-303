from setuptools import setup, find_packages
import os
import platform

base_folder = "pyrvs"

# Path to the compiled .pyd/.so file
def get_shared_lib_file():
    ext = '.pyd' if platform.system() == 'Windows' else '.so'
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(ext):
                return os.path.join(root, file)
    raise FileNotFoundError(f"Shared library file not found.")

shared_lib_file = get_shared_lib_file()

def make_init():
    only_file = os.path.basename(shared_lib_file)
    with open(f"./{base_folder}/__init__.py", "w") as f:
        f.write("def __bootstrap__():\n")
        f.write("   global __bootstrap__, __loader__, __file__\n")
        f.write("   import sys, pkg_resources, imp\n")
        f.write(f"   __file__ = pkg_resources.resource_filename(__name__,'{only_file}')\n")
        f.write("   __loader__ = None; del __bootstrap__, __loader__\n")
        f.write("   imp.load_dynamic(__name__,__file__)\n")
        f.write("__bootstrap__()\n")

make_init()

setup(
    name="pyrvs",
    version="0.39",
    author="Daniele Bonatto, Sarah Fachada",
    author_email="daniele.bonatto@ulb.be",
    description="Reference View Synthesizer (RVS) python package.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mpeg-i-visual/rvs",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False,
    install_requires=[
        'pybind11>=2.6.0',
        'numpy',
        'opencv-python'
    ],
    packages=find_packages(include=["pyrvs"]),
    include_package_data=True,
    package_data={
        '': [shared_lib_file],  # Include the precompiled .pyd file
    },
)