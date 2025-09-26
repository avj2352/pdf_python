help:
	@echo 'Available UI commands:'
	@echo 'clean: Cleanup files section'
	@echo 'pdf: Execute PDF script'

tree:
	@echo 'Show App structure...'
	tree -L 3 -I __pycache__
	
clean:
	@echo 'Cleanup files folder...'
	rm -rf files
	mkdir files


compress:
	@echo 'Execute PDF compress script...'
	uv run compress.py

pdf:
	@echo 'Execute PDF script...'
	uv run main.py
