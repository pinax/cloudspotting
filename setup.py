import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    name="cloudspotting",
    long_description=read("README.md"),
    packages=find_packages(),
    package_data={
        "cloudspotting": []
    },
    test_suite="runtests.runtests",
    tests_require=[
        "django-test-plus>=1.0.11",
    ],
    install_requires=[
        "django-user-accounts>=1.3.1",
        "pinax-images>=0.2.0",
        "pinax-likes>=1.3.1",
        "pinax-eventlog==1.1.1",
        "pinax-theme-bootstrap>=7.7.0",
        "pinax-webanalytics>=2.0.1",
    ],
    zip_safe=False
)
