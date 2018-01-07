from setuptools import setup


setup(
    name="Flask-Validates",
    version="0.3.0",
    url="https://github.com/tjpnz/flask-validates",
    license="MIT",
    author="Thomas Prebble",
    author_email="thomas.prebble@gmail.com",
    description="Form validation with view decorators",
    long_description="",
    packages=["flask_validates"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    setup_requires=[
        "pytest-runner"
    ],
    install_requires=[
        "Flask",
        "WTForms"
    ],
    tests_require=[
        "Flask-WTF",
        "pytest"
    ],
    test_suite="tests",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
