from setuptools import find_packages, setup


setup(
    name="docassemble.VTCertificateOfServiceGeneral",
    version="0.0.1",
    description="General Certificate of Service form 600-00264.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Legal Services Vermont and Lemma Legal",
    packages=find_packages(),
    namespace_packages=["docassemble"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "docassemble",
    ],
)
