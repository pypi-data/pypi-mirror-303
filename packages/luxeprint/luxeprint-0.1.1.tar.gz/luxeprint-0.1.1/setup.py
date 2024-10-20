from setuptools import setup
from setuptools_rust import RustExtension, Binding

setup(
    name="luxeprint",
    version="0.1.1",
    description="A Rust-based library for styled printing, tables, and emojis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Roman Tezikov",
    license="MIT",
    rust_extensions=[RustExtension("luxeprint.luxeprint", path="Cargo.toml", binding=Binding.PyO3)],
    packages=["luxeprint"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    url="https://github.com/TezRomacH/luxeprint",
    options={
        'egg_base': '.',
    },
)
