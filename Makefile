#
# JSONDB project Makefile
#
# $Id$
#

# Make us OS-independent ... at least for MacOS and Linux
OS := $(shell uname -s)
ifeq (Linux, ${OS})
    DATE := $(shell date --iso-8601)
else
    DATE := $(shell date "+%Y-%m-%d")
endif

# Python version
PYTHON := python3
# PYTHON := python2

DIRS = "."
DIRPATH = "~/projects/p/python/stibitz/"

.PHONY: help
help:
	cat Makefile
	echo "OS: " ${OS}
	echo "DATE: " ${DATE}

PYTHON_SOURCE = \
	jsondb_editor.py \
	jsondb_loader.py \
	trace_debug.py

SOURCE = \
	 ${PYTHON_SOURCE} \
	 Makefile \
	 sample_1.jdb \
	 sample_2.jdb \
	 .gitattributes \
	 .gitignore \
	 README.md

.PHONY: clean pylint listings test lint ci

FILES = \
	${SOURCE} \
	pylintrc

clean:
	- rm *.ps *.pdf

ci:
	ci -l ${FILES}

pylint:
	- pylint trace_debug.py

lint: pylint

test:
	${PYTHON} jsondb_editor.py sample_1.jdb

listings:\
	listing-trace_debug.pdf
	mv $^ ~/tmp

listing-%.ps: %.py
	enscript -G $< -p $@

listing-Makefile.ps: Makefile
	enscript -G $< -p $@

%.pdf: %.ps
	ps2pdf $< $@
	rm $<

# GIT operations

diff: .gitattributes
	git diff

status: ${FORCE}
	git status

# this brings the remote copy into sync with the local one
commit: .gitattributes
	git commit ${FILES}
	git push -u origin main

# This brings the local copy into sync with the remote (main)
pull: .gitattributes
	git pull origin main

log: .gitattributes
	git log --pretty=oneline
