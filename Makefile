pack:
	mkdir -p package
	pip install --target ./package requests
	zip -r test-python-requests.zip lambda_function.py  package
