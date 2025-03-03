.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
run_api : 
	uvicorn src.api:app --reload
run_tests: 
	pytest -v  tests/test_api.py 