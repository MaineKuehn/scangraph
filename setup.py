#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

repo_base_dir = os.path.abspath(os.path.dirname(__file__))
# pull in the packages metadata
package_about = {}
with open(os.path.join(repo_base_dir, "scangraph", "__about__.py")) as f:
    exec(f.read(), package_about)

with open(os.path.join(repo_base_dir, "README.rest"), "r") as README:
    long_description = README.read()

# other modules/packages required
dependencies = ["graphi"]
if sys.version_info < (3, 3):
    dependencies.append("backports.range")

if __name__ == "__main__":
    setup(
        name=package_about["__title__"],
        version=package_about["__version__"],
        description=package_about["__summary__"],
        long_description=long_description.strip(),

        author=package_about["__author__"],
        author_email=package_about["__email__"],
        url=package_about['__url__'],
        license='MIT',
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Science/Research",
            # Versions/Interpreters we support
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            # We probably support others as well, need to check
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Clustering",
        ],
        keywords=package_about["__keywords__"],
        # what we provide               V but not any of these
        packages=find_packages(exclude=("scangraph_*",)),
        # what we need
        install_requires=dependencies,
        # what we need for special things
        extras_require={
            # "feature": ["package", "package"], "feature": []
        },
        # unit tests
        # test_suite="scangraph_unittests",
        # use unittest backport to have subTests etc.
        tests_require=["unittest2"] if sys.version < (3, 4) else [],
    )
