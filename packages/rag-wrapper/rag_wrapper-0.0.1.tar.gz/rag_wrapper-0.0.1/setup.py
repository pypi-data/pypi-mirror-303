from setuptools import setup, find_packages
import pkg_resources


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.1"
REPO_NAME = "LLMOps"
PKG_NAME= "rag-wrapper"
AUTHOR_USER_NAME = "keshavkmr48"
AUTHOR_EMAIL = "keshavkmr076@gmail.com"


def get_installed_packages():
    """
    Get a list of installed packages and their versions.
    Returns a list of formatted strings that can be used in a setup.py dependencies list.
    """
    installed_packages = pkg_resources.working_set
    dependencies = []
    
    for package in installed_packages:
        package_name = package.key
        version = package.version
        dependencies.append(f"{package_name}=={version}")
    
    return dependencies

dependencies = get_installed_packages()
    



setup(
    name=PKG_NAME,  # The name of your package
    version=__version__,  # Initial version
    packages=find_packages(where="src"),  # Automatically find all the packages in the directory
    package_dir={"": "src"},
    install_requires=dependencies,
    include_package_data=True,  # To include any non-Python files specified in MANIFEST.in
    description="A package for LLMOps related tasks",  # Short description
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author="keshav Kumar",  # Your name or the team's name
    author_email=AUTHOR_EMAIL,  # Your contact email
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the project repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3",  # Specify Python versions supported
        "License :: OSI Approved :: Apache Software License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Python version compatibility
)
