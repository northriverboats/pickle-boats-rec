#!/usr/bin/env python

"""
Notes:
  * Page is divide into 3 typos of bands: top, bottom, and section(s)
  * If a column is CALCULATED it is column + (index into boatSection * 4)
  * If a row is OFFSET it is offset + row
  * These are done with sections[], boatSizes[] start[], end[]
    * sections[] the order the sections are to be found in on the sheet
    * boatSizes[] the boat lengths are integers found in Row 1
    * start[] of each section where "QTY" found in Column A (1)
    * end[] of each section where "SUBTOTAL " found in Column J (10)
  * To process a sheet the a dictionary entry is made with the key being
    the name of boat model and the value is another dictionary.
  * Examples use the Seahawk Outboard for Boat Model:
    * Top/Bottom directly addressed: ['Seahawk Outboard']['OVERHEAD BOAT']
    * Section top/bottom directly addressed: ['Seahawk Outboard']['TRAILER LABOR RATE']
    * Section parts list is an array found in: ['Seahawk Outboard']['TRAILER PARTS']
    * Section parts are referenced by index: ['Seahawk Outboard']['TRAILER PARTS'][0]
    * Parts details are addresed: ['Seahawk Outboard']['TRAILER PARTS'][0]['UOM']
"""

# order of sections corresponds with order of starts and ends
sections = ["TRAILER", "ENGINE & JET", "FABRICATION", "CANVAS", "PAINT", "OUTFITTING"]


##  TOP BAND        #########################################################

# top of sheet, absolute row, absolute column
# [0] title, [1] column, [2] row, [3] default
topSection = [
    ["BOAT MODEL", 1, 1, ""],
    ["OVERHEAD BOAT", 3, 5, ""],
    ["RETAIL BOAT", 2, 6, ""],
    ["OVERHEAD MOTOR AND TRAILER", 3, 7, "0"],
    ["RETAIL MOTOR AND TRAILER", 2, 8, "0"],
]    

# top of sheet, calculated column, absolute row
# [0] title, [1] column, [2] row, [3] default
costSummary = [
    [" LABOR TOTAL", 11, 2, "0"],
    [" MATERIAL TOTAL", 11, 3, "0"],
    [" TRAILER / ENGINE & JET", 11, 4, "0"],
    [" TOTAL COST", 11, 5, "0"],
	[" RETAIL BASE BOAT", 11, 6, "0"],
	[" RETAIL MOTOR / TRAILER", 11, 7, "0"],
	[" CALCULATED RETAIL TOTAL", 11, 8, "0"],
	[" CALCULATED DEALER INVOICE", 11, 9, "0"],
	[" CALCULATED CM", 11, 10, "0"],
	[" ADVERTISED RETAIL TOTAL", 11, 12, "0"],
	[" ADVERTISED DEALER INVOICE", 11, 13, "0"],
	[" ADVERTISED CM", 11, 14, "0"],
]


##  BOTTOM BAND    ##########################################################

# bottom section - max(end) + 5, absolute column, offest row
# [0] title, [1] column, [2] row, [3] default
bottomSection = [
]


##  SECTION BANDS  ##########################################################

# top of section, absolute column, offset row
# [0] title, [1] column, [2] row, [3] default
startSections = [
    [" CONSUMABLES", 1, -1, "0"],
    [" LABOR RATE", 3, -1, "0"],
]

# top of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
startSectionsSize = [
    [" HOURS", 10, -1, "0"]
]

# bottom of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
endSections = [
    [" SUBTOTAL ALL", 11, 0, "0"],
    [" CONSUMABLES", 11, 1, "0"],
    [" TOTAL", 11, 2, "0"],
]

# 1/2 body of section, absolute column, offset row
# [0] title, [1] column, [2] row, [3] default
partSection = [
    ["PART NUMBER", 1, 1, ""],
    ["DESCRIPTION", 2, 1, ""],
    ["UOM", 3, 1, ""],
    ["PRICE", 4, 1, "0"],
    ["VENDOR", 5, 1, ""],
    ["VENDOR PART", 6, 1, ""],
    ["RRS", 7, 1, ""], 
]

# 2/2 body of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
partSectionByModel = [
    [" QTY", 8, 1, "0"],
    [" TOTAL", 11, 1, "0"],
]