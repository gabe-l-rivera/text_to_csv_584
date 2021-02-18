# text_to_csv_584
In my VLSI class I needed a solution to processing data in excel from a raw text file containing output data, so I wrote this script to save me time. It turns any text file of 2 column data into a csv with 2 segregated columns instead of throwing both values in the same column with a space in between.


Steps to utilize this program:

1) run simulation with "spectre +l sim.log *name_of_spectre_file*.sp:" then access data with "vim *name_of_spectre_file*.print"

2) highlight the raw data, numbers only, copy and paste into a text file

3) save text file to your preferred location

4) edit this program accordingly to your data file's path and the path where you would like to save the output csv file as well

