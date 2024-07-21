VERSION := $(shell cat VERSION)

distribute:
	conda run -n papnt python setup.py install
