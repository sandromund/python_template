# python_template
Template with my most used setup.

## Run
````shell
python source/main.py run --config configs/default.yaml
````

## Install
````shell
pip install --upgrade pip
pip install pylint pytest pyinstaller
pip install -r requirements.txt
````
```shell
pylint $(git ls-files '*.py')
```