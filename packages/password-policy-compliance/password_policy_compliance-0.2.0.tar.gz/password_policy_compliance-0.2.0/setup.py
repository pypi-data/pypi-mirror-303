from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="password_policy_compliance",
    version="0.2.0",
    author="Bassem Abidi",
    author_email="abidi.bassem@me.com",
    description="A Python library for enforcing password policies and compliance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bassemabidi/password_policy_compliance",
    packages=find_packages(include=['password_policy_compliance', 'password_policy_compliance.*', 'examples']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1,<3.0.0",
        "zxcvbn>=4.4.28,<5.0.0",
        "flask>=2.0.0,<3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
        ],
    },
    package_data={
        "password_policy_compliance": ["LICENSE", "README.md"],
    },
    include_package_data=True,
    license="MIT",
)
