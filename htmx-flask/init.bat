pip3 install pipenv
python3 -m venv .venv
# Set-ExecutionPolicy RemoteSigned
.\.venv\Scripts\activate.bat
pipenv install

# tailwindcss -i ./static/src/input.css -o ./static/css/main.css --watch
