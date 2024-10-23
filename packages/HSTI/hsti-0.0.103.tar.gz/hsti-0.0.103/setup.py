import setuptools

## Have not been able to make automatic data file inclusion to work
## Not sure if it helps adding the function to __init__.py
# import os
# def package_files(directory):
#     paths = []
#     for (path, directories, filenames) in os.walk(directory):
#         for filename in filenames:
#             paths.append(os.path.join('..', path, filename))
#     return paths
# extra_files = package_files('hsti-analysis/HSTI/data_files')


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HSTI",
    version="0.0.103",
    author="Mads Nibe et. al.",
    author_email="mani@newtec.dk",
    description="The NEWTEC HSTI package contains fundamental functions for the data analysis of hyperspectral thermal images (HSTI).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # packages=setuptools.find_namespace_packages(where="hsti-analysis"),
    packages=setuptools.find_packages(where="hsti-analysis"),
    package_dir={"": "hsti-analysis"},
    include_package_data = False,
    # package_data={
    # "HSTI.HSTI_data_files-main": ["*.txt","*.pkl"],
    # "HSTI.HSTI_data_files-main.NUC.10_10_200_22": ["*.npy"],
    # "HSTI.HSTI_data_files-main.NUC.10_10_200_191": ["*.npy"],
    # "HSTI.HSTI_data_files-main.Temperature_conversions.10_10_200_22": ["*.npy"],
    # "HSTI.HSTI_data_files-main.Temperature_conversions.10_10_200_191": ["*.npy"]
    # },
    python_requires=">=3.6",
    install_requires=[
        "BaselineRemoval>= 0.1.4",
        "fast-histogram>=0.10",
        "fnnls>=1.0.0",
        "ipython>=7.25.0",
        "jupyter",
        "matplotlib>=3.4.2",
        "natsort>=7.1.1",
        "notebook>=6.4.0",
        "numpy>=1.19.5",
        "opencv-python>=4.5.2.54",
        "Pillow>=8.4.0",
        "scikit-learn>=0.24.2",
        "scipy>=1.7.0",
        "Screeninfo>=0.8",
        "RangeSlider>=2021.7.4",
        "tk>=0.1.0"
    ]
)
