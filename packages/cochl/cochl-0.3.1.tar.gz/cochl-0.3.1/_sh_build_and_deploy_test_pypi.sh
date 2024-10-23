#!/bin/sh

sudo apt install python3.8
sudo apt install python3.8-venv

python3.8 --version
python3.8 -m pip install --upgrade pip
python3.8 -m pip install --upgrade build

rm -rf .github
rm -rf .idea
rm -rf .pytest_cache
rm -rf dist
mkdir dist
rm -rf samples
rm -rf tests
rm -rf .gitignore
rm -rf README_hglim.md
rm -rf README_HOME_dot_pypirc.txt

python3.8 -m build
git reset --hard

python3.8 -m pip install --upgrade twine

cp -f ~/.test_pypirc ~/.pypirc
python3.8 -m twine upload dist/* --verbose --repository testpypi
rm -rf ~/.pypirc

# python3.8 -m pip install --index-url https://test.pypi.org/simple/ --no-deps cochl
# python3.8 -c 'import cochl.sense; print(cochl.sense.APIConfig())'
