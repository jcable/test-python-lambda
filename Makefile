package:
	mkdir package
	pip3 install --target ./package requests
	zip -r test-python-requests.zip lambda_function.py  package
