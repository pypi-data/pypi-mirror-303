# /usr/bin/env python
import uuid
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

def get_requirements(source):
    try:
        install_reqs = parse_requirements(source, session=uuid.uuid1())
    except TypeError:
        # Older version of pip.
        install_reqs = parse_requirements(source)
    required = sorted(set([str(ir.requirement) for ir in install_reqs]))
    return list(required)


setup(
    name="django-polyencode",
    version="2.1",
    description="Geo data database structure for the Django web framework.",
    author="Urtzi Odriozola (Code Syntax http://codesyntax.com)",
    author_email="uodriozola@codesyntax.com",
    url="https://github.com/codesyntax/django-geodata",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.10',
                 'Programming Language :: Python :: 3.11',
                 'Topic :: Utilities'],
    install_requires=get_requirements('requirements.txt'),
)
