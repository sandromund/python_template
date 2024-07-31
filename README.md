# python_template
Template with my most used setup.

## Run
````shell
python source/main.py run --config configs/default.yaml
````

## Install
````shell
pip install --upgrade pip
pip install pylint black pyinstaller
pip install -r requirements.txt
````
## Style check
```shell
pylint $(git ls-files '*.py')
```
## Test
````shell
pytest
````

## Format 
````shell
black source 
black tests
````

## Create an Exe
````shell
pyinstaller --onefile source/main.py --name=app
````
## Run the Exe 
````shell
dist/app.exe run --config configs/default.yaml
````