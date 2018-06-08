CONFIG_DIR = /etc/yum/pluginconf.d
PLUGIN_DIR = /usr/lib/yum-plugins

all:

install:
	install -m 0644 -t "$(PLUGIN_DIR)" monit.py
	install -m 0644 -t "$(CONFIG_DIR)" monit.conf

uninstall:
	-rm -f "$(PLUGIN_DIR)/monit.py" "$(PLUGIN_DIR)/monit.pyc" "$(PLUGIN_DIR)/monit.pyo"
	-rm -f "$(CONFIG_DIR)/monit.conf"

.PHONY: install uninstall
