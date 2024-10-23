from setuptools import setup

try:
    with open("./README.md", "r") as f:
        readme = f.read()
except Exception as e:
    readme = ""


setup(
    name='django-stackstore-model-ooppyy',
    author="OoppyY",
    url="https://github.com/c2emarket-ooppyy/django-stackstore-model",
    description='Django stackstore model',
    long_description_content_type="text/markdown",
    long_description=readme,
    keywords=["django", "model", "versioning"],
    version='1.0',
    packages=['stackstore'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
