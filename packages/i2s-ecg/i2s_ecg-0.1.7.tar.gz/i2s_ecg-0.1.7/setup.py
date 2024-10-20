import setuptools
import os
import io

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Determine the path of the README file
readme_path = os.path.join('ecgi2s123', 'README.md')

# Read dependencies from the requirements.txt file
if os.path.exists("requirements.txt"):
    with io.open("requirements.txt", encoding="utf-8") as f:
        install_requires = [line.strip() for line in f if line.strip()]
else:
    install_requires = []

setuptools.setup(
    name="i2s-ecg",
    version="0.1.7",
    author="zou linzhuang",
    license='MIT License',  
    author_email="zoulinzhuang2204@hnu.edu.cn",
    description="the package for ECG signal processing",
    long_description=long_description,
    long_description_content_type="text/markdown",  # use Markdown for README.md
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    package_data={
        'i2s_ecg': ['data/Heart_Disease_Prediction_using_ECG.pkl', 'data/PCA_ECG.pkl'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
