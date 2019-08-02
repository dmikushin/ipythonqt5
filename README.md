# Embedding IPython into Qt 5 Application

A demo based on [StackOverflow example](https://stackoverflow.com/questions/11513132/embedding-ipython-qt-console-in-a-pyqt-application).

![screenshot](screenshot.png)

## Prerequisites

Prepare the virtual environment:

```
sudo apt-get install python3-venv
python3 -m venv .
source bin/activate
```

Install Python dependencies:

```
pip install wheel
pip install ipykernel==4.6.1 qtconsole
pip install sip PyQt5
```

## Deployment

Additionally, install matplotlib, which we will use for illustration:

```
pip install matplotlib
```

Launch the IPython Qt application example:

```
python ./example.py
```

## Standalone executable

A standalone executable could be created with Nuitka:

```
pip install nuitka
python -m nuitka --standalone --recurse-all --show-progress --show-modules --plugin-enable=qt-plugins --include-package=pygments.lexers --include-package=pygments.styles --include-package=ipykernel.datapub --include-package=zmq.utils --include-package=pip --include-package=wheel --output-dir=x86_64-linux-python-3.6 example.py
```
