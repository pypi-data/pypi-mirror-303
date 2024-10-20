from setuptools import setup, find_packages

setup(
    name="zarinpal-python-sdk",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    include_package_data=True,
    description="Zarinpal Payment Gateway SDK for Python",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author="Mohammad Hossein",
    author_email="mohamd.qorbani383@gmail.com",
    url="https://github.com/MohamadHusein/zarinpal-python-sdk",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="zarinpal, payment, sdk, python",
)
