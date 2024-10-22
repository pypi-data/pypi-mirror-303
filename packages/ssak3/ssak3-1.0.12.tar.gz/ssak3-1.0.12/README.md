# ssak3

pip install apify loguru
pip install setuptools
pip install wheel twine

(.venv) $python setup.py sdist bdist_wheel
(.venv) $twine upload dist/*