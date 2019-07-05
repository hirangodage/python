convert qt ui into py file
python -m PyQt5.uic.pyuic -x form.ui -o test.py

use pyinstaller to create executable
pyinstaller --onefile --windowed --icon=favicon.ico main.py