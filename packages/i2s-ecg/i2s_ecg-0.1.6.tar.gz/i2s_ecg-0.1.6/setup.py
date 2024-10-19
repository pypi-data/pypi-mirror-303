import setuptools
import os
import io

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# 确定README文件的路径
readme_path = os.path.join('ecgi2s123', 'README.md')


# 从requirements.txt文件读取依赖
if os.path.exists("requirements.txt"):
    with io.open("requirements.txt", encoding="utf-8") as f:
        install_requires = [line.strip() for line in f if line.strip()]
else:
    install_requires = []

setuptools.setup(
    name="i2s-ecg",
    version="0.1.6",
    author="zou linzhuang",
    license='MIT License',  
    author_email="zoulinzhuang2204@hnu.edu.cn",
    description="the package for ECG signal processing",
    long_description=long_description,
    long_description_content_type="text/markdown",  # 使用Markdown格式
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
    # include_package_data=True,  # 自动打包文件夹内所有数据
    # 如果需要包含多个文件可以单独配置 MANIFEST.in
    
    # 如果需要支持脚本方法运行，可以配置入口点
)
