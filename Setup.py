from setuptools import setup

setup(
    name="pasgen",
    version="1.1",
    description="Targeted Password Wordlist Generator",
    author="Azan Chishiua",
    author_email="Azan.Chishiya@gmail.com",
    url="https://github.com/yourusername/pasgen",
    py_modules=["pasgen"],                     # because it's a single module
    entry_points={
        "console_scripts": [
            "pasgen = pasgen:main",            # creates a command 'pasgen'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
