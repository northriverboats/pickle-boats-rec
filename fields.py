#!/usr/bin/env python

# [0] title, [1] column, [2] row, [3] default
topSection = [
    ["BOAT MODEL", 1, 1, ""],
    ["OVERHEAD BOAT", 3, 5, ""],
    ["RETAIL BOAT", 2, 6, ""],
    ["OVERHEAD MOTOR AND TRAILER", 3, 7, "0"],
    ["RETAIL MOTOR AND TRAILER", 2, 8, "0"],
]    

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

# [0] title, [1] column, [2] row, [3] default
startSections = [
    [" CONSUMABLES", 1, -1, "0"],
    [" LABOR RATE", 3, -1, "0"],
]

# [0] title, [1] column, [2] row, [3] default
startSectionsSize = [
    [" HOURS", 10, -1, "0"]
]

# [0] title, [1] column, [2] row, [3] default
endSections = [
    [" 18 SUBTOTAL ALL", 13, 0, "0"],
    [" 19 SUBTOTAL ALL", 17, 0, "0"],
    [" 20 SUBTOTAL ALL", 21, 0, "0"],
    [" 21 SUBTOTAL ALL", 25, 0, "0"],
    [" 22 SUBTOTAL ALL", 29, 0, "0"],
    [" 23 SUBTOTAL ALL", 33, 0, "0"],
    [" 24 SUBTOTAL ALL", 37, 0, "0"],
    [" 25 SUBTOTAL ALL", 41, 0, "0"],
    [" 26 SUBTOTAL ALL", 45, 0, "0"],
    [" 27 SUBTOTAL ALL", 49, 0, "0"],
    [" 28 SUBTOTAL ALL", 53, 0, "0"],
    [" 29 SUBTOTAL ALL", 57, 0, "0"],
    [" 30 SUBTOTAL ALL", 61, 0, "0"],
    [" 31 SUBTOTAL ALL", 65, 0, "0"],
    [" 32 SUBTOTAL ALL", 69, 0, "0"],
    [" 33 SUBTOTAL ALL", 73, 0, "0"],
    [" 34 SUBTOTAL ALL", 77, 0, "0"],
    [" 35 SUBTOTAL ALL", 81, 0, "0"],
    [" 36 SUBTOTAL ALL", 85, 0, "0"],
    [" 37 SUBTOTAL ALL", 89, 0, "0"],

    [" 18 CONSUMABLES", 13, 1, "0"],
    [" 19 CONSUMABLES", 17, 1, "0"],
    [" 20 CONSUMABLES", 21, 1, "0"],
    [" 21 CONSUMABLES", 25, 1, "0"],
    [" 22 CONSUMABLES", 29, 1, "0"],
    [" 23 CONSUMABLES", 33, 1, "0"],
    [" 24 CONSUMABLES", 37, 1, "0"],
    [" 25 CONSUMABLES", 41, 1, "0"],
    [" 26 CONSUMABLES", 45, 1, "0"],
    [" 27 CONSUMABLES", 49, 1, "0"],
    [" 28 CONSUMABLES", 53, 1, "0"],
    [" 29 CONSUMABLES", 57, 1, "0"],
    [" 30 CONSUMABLES", 61, 1, "0"],
    [" 31 CONSUMABLES", 65, 1, "0"],
    [" 32 CONSUMABLES", 69, 1, "0"],
    [" 33 CONSUMABLES", 73, 1, "0"],
    [" 34 CONSUMABLES", 77, 1, "0"],
    [" 35 CONSUMABLES", 81, 1, "0"],
    [" 36 CONSUMABLES", 85, 1, "0"],
    [" 37 CONSUMABLES", 89, 1, "0"],

    [" 18 TOTAL", 13, 2, "0"],
    [" 19 TOTAL", 17, 2, "0"],
    [" 20 TOTAL", 21, 2, "0"],
    [" 21 TOTAL", 25, 2, "0"],
    [" 22 TOTAL", 29, 2, "0"],
    [" 23 TOTAL", 33, 2, "0"],
    [" 24 TOTAL", 37, 2, "0"],
    [" 25 TOTAL", 41, 2, "0"],
    [" 26 TOTAL", 45, 2, "0"],
    [" 27 TOTAL", 49, 2, "0"],
    [" 28 TOTAL", 53, 2, "0"],
    [" 29 TOTAL", 57, 2, "0"],
    [" 30 TOTAL", 61, 2, "0"],
    [" 31 TOTAL", 65, 2, "0"],
    [" 32 TOTAL", 69, 2, "0"],
    [" 33 TOTAL", 73, 2, "0"],
    [" 34 TOTAL", 77, 2, "0"],
    [" 35 TOTAL", 81, 2, "0"],
    [" 36 TOTAL", 85, 2, "0"],
    [" 37 TOTAL", 89, 2, "0"],
]


partSection = [
    ["PART NUMBER", 2, 1, ""],
    ["DESCRIPTION", 3, 1, ""],
    ["UOM", 4, 1, ""],
    ["PRICE", 5, 1, "0"],
    ["VENDOR", 8, 1, ""],
    ["VENDOR PART", 9, 1, ""],

    ["18 QTY", 10, 1, "0"],
    ["19 QTY", 14, 1, "0"],
    ["20 QTY", 18, 1, "0"],
    ["21 QTY", 22, 1, "0"],
    ["22 QTY", 26, 1, "0"],
    ["23 QTY", 30, 1, "0"],
    ["24 QTY", 34, 1, "0"],
    ["25 QTY", 38, 1, "0"],
    ["26 QTY", 44, 1, "0"],
    ["27 QTY", 46, 1, "0"],
    ["28 QTY", 50, 1, "0"],
    ["29 QTY", 54, 1, "0"],
    ["30 QTY", 58, 1, "0"],
    ["31 QTY", 62, 1, "0"],
    ["32 QTY", 66, 1, "0"],
    ["33 QTY", 70, 1, "0"],
    ["34 QTY", 74, 1, "0"],
    ["35 QTY", 78, 1, "0"],
    ["36 QTY", 82, 1, "0"],
    ["37 QTY", 86, 1, "0"],

    ["18 TOTAL", 13, 1, "0"],
    ["19 TOTAL", 17, 1, "0"],
    ["20 TOTAL", 21, 1, "0"],
    ["21 TOTAL", 25, 1, "0"],
    ["22 TOTAL", 29, 1, "0"],
    ["23 TOTAL", 33, 1, "0"],
    ["24 TOTAL", 37, 1, "0"],
    ["25 TOTAL", 41, 1, "0"],
    ["26 TOTAL", 45, 1, "0"],
    ["27 TOTAL", 49, 1, "0"],
    ["28 TOTAL", 53, 1, "0"],
    ["29 TOTAL", 57, 1, "0"],
    ["30 TOTAL", 61, 1, "0"],
    ["31 TOTAL", 65, 1, "0"],
    ["32 TOTAL", 69, 1, "0"],
    ["33 TOTAL", 73, 1, "0"],
    ["34 TOTAL", 77, 1, "0"],
    ["35 TOTAL", 81, 1, "0"],
    ["36 TOTAL", 85, 1, "0"],
    ["37 TOTAL", 89, 1, "0"],
]

# [0] title, [1] column, [2] row, [3] default
bottomSection = [
  ["EOS QUANTITY", 1, 1, ""],
  ["EOS LOCATION SELECTION", 2, 1, ""],
  ["EOS NOTES FIELD", 3, 1, ""],
  ["E71	EOS CANVAS COLOR", 4, 1, ""],

  ["EOS 1 PAINT COLOR", 1, 3, ""],
  ["EOS 2 PAINT COLOR", 2, 3, ""],
  ["EOS ZOLATONE", 3, 3, ""],
  ["EOS 1 VINYL", 4, 3, ""],
  ["EOS 2 VINYL", 5, 3, ""],

  ["SSOB", 2, 6, ""],
  ["SSOB CODE", 4, 6, ""],
  
  ["LSOB", 2, 7, ""],
  ["LSOB CODE", 4, 7, ""],
  
  ["SHHT", 2, 8, ""],
  ["SHHT CODE", 4, 8, ""],
  
  ["23OS", 2, 9, ""],
  ["23OS CODE", 4, 9, ""],
  
  ["SO", 2, 10, ""],
  ["SO CODE", 4, 10, ""],
  
  ["WXL", 2, 11, ""],
  ["WXL CODE", 4, 11, ""],
  
  ["WASO", 2, 12, ""],
  ["WASO CODE", 4, 12, ""],
  
  ["DV", 2, 13, ""],
  ["DV CODE", 4, 13, ""],
  
  ["C", 2, 14, ""],
  ["C CODE", 4, 14, ""],
  
  ["OSP", 2, 15, ""],
  ["OSP CODE", 4, 15, ""],
  
  ["S", 2, 16, ""],
  ["S CODE", 4, 16, ""],
  
  ["EOS DEPARTMENT", 1, 19, ""],
]
