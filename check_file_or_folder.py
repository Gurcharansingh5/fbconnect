import dropbox
import csv

dbx = dropbox.Dropbox('HXbs__9V2IEAAAAAAAAAAUT_tdP51a21_yiGysC-MixwNyxqrWHqO1AajNbdO1lV')
a = dbx.files_list_folder('/testing')
print(a.has_more)