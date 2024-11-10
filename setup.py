import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()   
    
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Sha0ndeep"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "shaondeepmandal@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python project for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    pacakages = setuptools.find_packages(where="src")
)