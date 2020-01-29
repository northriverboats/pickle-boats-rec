# NRB PICKLE BOATS
## To Edit Source Code and Work with GIT
1. Use Git Bash
2. `cd ../../Development`
2. `git clone https://github.com/northriverboats/nrb-pickle-boats.git`
2. `cd nrb-pickle-boats`
2. Use windows shell
2. `cd \Development\nrb-pickle-boats`
3. `\Python37\python -m venv .venv`
4. `.venv\Scripts\activate`
5. `python -m pip install pip --upgrade`
5. Download `PyQt4-4.11.4-cp37-cp37m-win_amd64.whl` from https://www.lfd.uci.edu/~gohlke/pythonlibs/
6. `pip install <path-to-folder>\PyQt4-4.11.4-cp37-cp37m-win_amd64.whl`
7. `pip install -r requirements.txt`
8. Remember to Create New Branch Before Doing Any Work

## Generate UI
1. Ues QT Creator
2. '.venv\Lib\site-packages\PyQt4\Designer.exe`
3. MainWindow.ui
4. `.venv\Lib\site-packages\PyQt4\pyuic4 MainWindow.ui  -o MainWindow.py`
5. PreferencesDialog.ui
6. `.venv\Lib\site-packages\PyQt4\pyuic4 PreferencesDialog.ui  -o PreferencesDialog.py`

## Build Executable
`.venv\Scripts\pyinstaller.exe --onefile --windowed --icon options.ico  --name "Excel Pickle Boats" "NRB Pickle Boats FWW.spec" main.py`

## Methodology for extracting values from Spreadsheet
1. A sheet is vertically divided into top, bottom and sections
	* top is absolutely positioned at row 1.
	* section `start` is found by looking in column A/1 for all cells that have the value `QTY`.
	* section `end` is found by looking in column J/10 for all cells that have the value `SUBTOTAL`.
	* bottom is computed as `max(end)+ 5`
2. A sheet horizontally divided into an absolute positioned and relative positioned `boatSizes`.
	* the leftmost column A/1 is absolutely positioned.
	* `boatSizes` is the text of any cell that is an integer value as determined by `.isidigit()`.
	* the column position of `boatSizes` is computed by J/11 with `11 + (4 * i)` with `i` being the current index into `enumerate(boatSizes)`.
3. The file `fields.py` holds the different **bands** on the page. Each **band** has entries for individual values that will be captured
	* **name** of the dictionary entry we are saving for that value
	* **column** either absolute or relative of the value to be captured
	* **row** either absolute or relative of the value to be captured
	* **default** a default value such as "0", "0.0" or "" in case the cell is empty so nulls are not being stored.
4. Non Section **bands** are processed once
	* `topSection` has absolute columns and absolute rows
	* `costSummary` has columns found calculated by 11 + 4 * index into `boatSizes` and absolute rows.
	* `bottomSection` has absolute columns and rows that are offset from `max(end) + 5`
5. Section **bands** are processed once for each item in the `section[]` list.
	* `startSections` has absolute columns and rows offset from `start[i]` and occur before the `partSection` in each **section**.
	* `startSectionsSize` has columns found calculated by 11 + 4 * index into `boatSizes` and rows offset from `start[i]` and occur before the `partSection` in each **section**.
	* `endSections` has columns found calculated by 11 + 4 * index into `boatSizes` and rows offset from `end[i]` and occur after the `partSection` in each **section**.
	* `partSection` needs to be divided it has both absolute columns at the start **and** `boatSizes[]` calculated columns.