from setuptools import setup, find_packages

setup(
    name="ResolutionSystemesLineaireEtNon",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],  # Dépendances à installer
    description="Description de mon package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Leo leo",
    author_email="hocomi3722@exeneli.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
