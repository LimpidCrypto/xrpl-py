#!/bin/bash

# install pyenv
curl https://pyenv.run | bash
export PATH="$HOME/.pyenv/bin:$PATH"

# install poetry
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry completions bash >> ~/.bash_completion

~/.pyenv/bin/pyenv install 3.12
~/.pyenv/bin/pyenv local 3.12
poetry env use $HOME/.pyenv/versions/3.12.3/bin/python
poetry install

sudo npm install -g @angular/cli