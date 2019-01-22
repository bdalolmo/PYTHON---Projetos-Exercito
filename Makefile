PLUGIN_NAME = testPlugin
PY_FILES = __init__.py plugin.py
EXTRAS = icon.png metadata.txt
RESOURCE_FILES = resources.py

default: deploy

compile: $(RESOURCE_FILES)

%.py : %.qrc
	export PATH="/Applications/QGIS.app/Contents/MacOS/bin:$PATH"; export PYTHONPATH="/Applications/QGIS.app/Contents/Resources/python"; pyrcc4 -o $@ $<

deploy: compile
	mkdir ~p $(HOME)/home/breno/.qgis2/python/plugins/$(PLUGIN_NAME)
	cp ~vf $(PY_FILES) $(HOME)/home/breno/.qgis2/python/plugins/$(PLUGIN_NAME)
	cp ~vf $(RESOURCE_FILES) $(HOME)/home/breno/.qgis2/python/plugins/$(PLUGIN_NAME)
	cp ~vf $(EXTRAS) $(HOME)/home/breno/.qgis2/python/plugins/$(PLUGIN_NAME)

clean:
	rm $(RESOURCE_FILES)

