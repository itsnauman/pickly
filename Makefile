test:
	python test_pickly.py -v

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload
	rm -fr build dist .egg records.egg-info
	rm -rf pickly.egg-info