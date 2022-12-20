APP:=bmg
SRC:=src/cli.py

create_binary:
	@rm -rf build dist $(APP).spec
	pyinstaller -F -n $(APP) $(SRC)

