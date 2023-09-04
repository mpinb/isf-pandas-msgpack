*   Tag commit

        git tag -a x.x.x -m 'Version x.x.x'

*   and push to github

        git push origin master --tags

*  Upload to PyPI

        git clean -xfd
        python setup.py register sdist --formats=gztar
        twine upload dist/*

*  Do a pull-request to the feedstock on `pandas-msgpack-feedstock <https://github.com/conda-forge/pandas-msgpack-feedstock/>`__

        update the version
        update the SHA256 (retrieve from PyPI)


* register has been deprecated, Uploading also to PyPI testing  (UPDATED 31.08.2023)

        git clean -xfd
        python setup.py sdist --formats=gztar  bdist_wheel
        python -m twine check dist/*
        python -m twine upload dist/* --verbose --repository-url https://test.pypi.org/legacy/
        twine upload dist/*

* using .pypirc not passwords will be requested

        git clean -xfd
        python setup.py sdist --formats=gztar  bdist_wheel
        python -m twine check dist/*
        twine upload --repository testpypi dist/* --verbose
        twine upload dist/* --verbose