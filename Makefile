APP:=bmg
SRC:=src/cli.py

help:
	@echo Please see README.md for valid targets
	
binary:
	@rm -rf build dist $(APP).spec
	pyinstaller -F -n $(APP) $(SRC)

tests:
	cd src; ./run_tests

