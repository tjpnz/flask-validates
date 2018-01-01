from setuptools import setup, find_packages


setup(
    name="Flask-Validates",
    version="0.1.0",
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
    install_requires=[
        "Flask",
        "WTForms"
    ],
    tests_require=[
        "Flask-WTF"
    ],
    test_suite="tests",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
