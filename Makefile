clean:
	rm -rf ./build ./dist ./htmlcov/

coverage_report: test_coverage
	coverage report -m
	coverage html

init:
	pip install -r requirements.txt -U

test:
	python manage.py test smsish

test_coverage:
	coverage run --source=smsish manage.py test smsish

build:
	python setup.py sdist bdist_wheel

release: build
	twine upload dist/*
