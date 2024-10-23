from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="msc-mumu",
    version="0.0.2",
    description="截图工具-mumu",
    author="KateTseng",
    author_email="Kate.TsengK@outlook.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="Auto Script Testing",
    project_urls={},
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=['opencv-python', 'adbutils', 'loguru','mmumu','msc-base'],
    python_requires=">=3",
)
