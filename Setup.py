from setuptools import setup, find_packages

setup(
    name="pasgen",
    version="1.1",
    description="Targeted Password Wordlist Generator",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/pasgen",
    py_modules=["pasgen"],
    entry_points={
        "console_scripts": [
            "pasgen = pasgen:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
