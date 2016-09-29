# college-eight-lookup
Flask application to display mentions of 'college eight' in a selected wcms subdomain

[gist of python script to strip duplicates and wrong extensions from your csv file](https://gist.github.com/pguther/955d323cc5622ec1434a1d53eb465059)

example file structure:

    subdomain1, /this/is/a/site/path.html
    subdomain1, /also/a/site/path.html
    subdomain2, /a/text/file.txt
    subdomain3, /this/will/be/removed.jpg

If your csv file has extra columns after the subdomain andpath columns, they will be ignored

## Installation

#### to install without virtualenv
    pip install -r requirements.txt

#### to install with virtualenv
In the college-eight-lookup directory

    virtualenv flask
    . flask/bin/activate
    pip install -r requirements.txt

#### to run
    chmod +x run.py
    ./run.py
or

    python run.py

##### to quit the virtualenv
    deactivate

##### to remove the virtualenv
    rm -r flask