.DEFAULT_GOAL := infos
a := helloworlllld

infos:
	@echo "Current version:"
	@tail version

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf /gmpykit.egg-info

build-major:
	python3 setup.py sdist bdist_wheel major

build-minor:
	python3 setup.py sdist bdist_wheel minor

build-patch:
	python3 setup.py sdist bdist_wheel patch

upload:
	twine upload dist/*

git-upload:
	version=$(shell cat version.txt)
	git add .
	git commit -m "v$$(cat version.txt)"
	git push origin main

publish-patch: clean build-patch upload git-upload
publish-minor: clean build-minor upload git-upload
publish-major: clean build-major upload git-upload