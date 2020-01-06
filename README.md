# NRB PICKLE BOATS
## To Edit Source Code and Work with GIT
1. Use Git Bash
2. `cd ../../Development`
2. `git clone https://github.com/northriverboats/nrb-pickle-boats.git`
2. `cd nrb-pickle-boats`
3. `\Python37\python -m venv .`
4. `Scripts\activate`
5. Download `PyQt4-4.11.4-cp37-cp37m-win_amd64.whl` from https://www.lfd.uci.edu/~gohlke/pythonlibs/
6. `pip install <path-to-folder>\PyQt4-4.11.4-cp37-cp37m-win_amd64.whl`
7. `pip install -r requirements.txt`
8. Remember to Create New Branch Before Doing Any Work

## Generate UI
1. Ues QT Creator
2. MainWindow.ui
3. `Lib\site-packages\PyQt4\pyuic4 MainWindow.ui  -o MainWindow.py`
4. PreferencesDialog.ui
5. `Lib\site-packages\PyQt4\pyuic4 PreferencesDialog.ui  -o PreferencesDialog.py`

## Build Executable
`Scripts\pyinstaller.exe --onefile --windowed --icon options.ico  --name "Excel Options Search and Replace" "Excel Options Search and Replace FWW.spec" main.py`


## Possible pyinstall patches
[Loran425/pyinstaller](https://github.com/Loran425/pyinstaller/commit/14b6e65642e4b07a4358bab278019a48dedf7460)  
