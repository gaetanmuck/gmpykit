.DEFAULT_GOAL := infos

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

publish-patch: clean build-patch upload
publish-minor: clean build-minor upload
publish-major: clean build-major upload