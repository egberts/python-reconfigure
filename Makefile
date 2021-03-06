PYTHON=`which python`
DESTDIR=/
BUILDIR=$(CURDIR)/debian/reconfigure
RPMTOPDIR=$(CURDIR)/build
PROJECT=reconfigure
DEBPROJECT=python-reconfigure
VERSION=`python -c "from reconfigure import __version__; print __version__"`
PREFIX=/usr
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
DOCBUILDDIR   = docs/build
DOCSOURCEDIR   = docs/source
ALLSPHINXOPTS   = -d $(DOCBUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(DOCSOURCEDIR)

all:

build:

doc:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(DOCBUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

cdoc:
	rm -rf $(DOCBUILDDIR)/*
	make doc

install:
	$(PYTHON) setup.py install --root $(DESTDIR) $(COMPILE) --prefix $(PREFIX)

rpm: build tgz
	rm -rf dist/*.rpm

	cat dist/$(PROJECT).spec.in | sed s/__VERSION__/$(VERSION)/g > $(PROJECT).spec

	mkdir -p build/SOURCES || true
	cp dist/$(PROJECT)*.tar.gz build/SOURCES

	rpmbuild --define '_topdir $(RPMTOPDIR)' -bb $(PROJECT).spec

	mv build/RPMS/noarch/$(PROJECT)*.rpm dist

	rm $(PROJECT).spec

deb: build tgz
	rm -rf dist/*.deb

	cat debian/changelog.in | sed s/__VERSION__/$(VERSION)/g | sed "s/__DATE__/$(DATE)/g" > debian/changelog

	cp dist/$(PROJECT)*.tar.gz ..
	rename -f 's/$(PROJECT)-(.*)\.tar\.gz/$(DEBPROJECT)_$$1\.orig\.tar\.gz/' ../*
	dpkg-buildpackage -b -rfakeroot -us -uc

	mv ../$(DEBPROJECT)*.deb dist/

	rm ../$(DEBPROJECT)*.orig.tar.gz
	rm ../$(DEBPROJECT)*.changes
	rm debian/changelog

upload-deb: deb
	scp dist/*.deb root@ajenti.org:/srv/repo/ng/debian
	ssh root@ajenti.org /srv/repo/rebuild-debian.sh

upload-rpm: rpm
	scp dist/*.rpm root@ajenti.org:/srv/repo/ng/centos/6
	ssh root@ajenti.org /srv/repo/rebuild-centos.sh

upload-rpm7: rpm
	scp dist/*.rpm root@ajenti.org:/srv/repo/ng/centos/7
	ssh root@ajenti.org /srv/repo/rebuild-centos7.sh

upload-tgz: tgz
	$(PYTHON) setup.py sdist bdist_wheel upload

tgz: build
	rm dist/*.tar.gz || true
	$(PYTHON) setup.py sdist


distclean: clean
	rm -rf .pytest_cache/
	find src -name "__pycache__" -exec rm -rf {} \;
	rm -rf dist/docs
	rm -rf dist/reconfigure-2.0.0-py*
	rm -rf htmlcov

clean:
	$(PYTHON) setup.py clean
	rm -rf $(DOCBUILDDIR)/*
	rm -rf build/ debian/$(PROJECT)* debian/*stamp* debian/files MANIFEST *.egg-info
	find . -name '*.pyc' -delete


test:
	nosetests -v
