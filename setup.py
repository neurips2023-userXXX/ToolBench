from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Action Generation Evaluation Suite"
LONG_DESCRIPTION = "A package that makes it easy to evaluate LLM pipelines on real world action generation tasks."

REQUIRED = [
    "farm-haystack==1.15.1",
    "manifest-ml==0.1.2",
    "faiss-cpu==1.7.2",
    "numpy==1.22.4",
    "scipy==1.10.1",
    "shapely==2.0.1",
    "astunparse==1.6.3",
    "pygments==2.15.0",
    "pybullet==3.2.5",
    "gdown==4.7.1",
    "moviepy==1.0.3",
    "gspread==5.8.0",
    "gspread_dataframe==3.3.0",
    "gspread_formatting==1.1.2",
    "black==23.3.0",
]

setup(
    name="actgen-eval",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Qiantong Xu",
    author_email="xqt0904@gmail.com",
    license="MIT",
    python_requires=">=3.8.0",
    packages=find_packages(exclude=["tests", "scripts", "data", "api"]),
    install_requires=REQUIRED,
    keywords="action generation evaluation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
