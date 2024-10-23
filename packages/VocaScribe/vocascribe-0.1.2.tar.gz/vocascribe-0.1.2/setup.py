from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="VocaScribe",
    version="0.1.2",
    py_modules=["vocascribe"],
    packages=find_packages(),
    install_requires=[
        "build ~= 1.2.2.post1",
        "SpeechRecognition ~= 3.11.0",
        "gTTS ~= 2.5.3",
        "pydub ~= 0.25.1",
        "ffmpeg ~= 1.4",
        "installer ~= 0.7.0",
    ],  # Add any other dependencies here
    entry_points={
        "console_scripts": [
            "vscribe=src.vocascribe_package_ofalltrades.vocascribe:main",
        ],
    },
    author="Jake Johnson",
    author_email="",  # Omitted for privacy
    description="A very simple tool to transcribe audio files to text.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ofalltrades/VocaScribe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={
        "Issues": "https://github.com/ofalltrades/VocaScribe/issues",
    },
)
