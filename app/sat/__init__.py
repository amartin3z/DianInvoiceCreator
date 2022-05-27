"""

Main Tables:
	sat_lco
	sat_lrfc



create sat_lco_2020_02_10 -- Use the year, month and day. If there is already a table with that name use and increment (_counter)
mv sat_lco to sat_lco_2020_02_10_bkp
mv sat_lco_2020_02_10 sat_lco

create sat_lco_2020_02_11
mv sat_lco to sat_lco_2020_02_11_bkp
mv sat_lco_2020_02_11 sat_lco

create sat_lco_2020_02_11_7
mv sat_lco to sat_lco_2020_02_11_7_bkp
mv sat_lco_2020_02_11_7 sat_lco

At the end we will have as many tables as the number of import commands we call
"""



