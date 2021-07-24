import dropbox
import os
dbx = dropbox.Dropbox('HXbs__9V2IEAAAAAAAAAAUT_tdP51a21_yiGysC-MixwNyxqrWHqO1AajNbdO1lV')
folder_path = os.getcwd().replace('\\','/')
print('1111111111111111111111')
print(folder_path+'/qr.zip')
print('1111111111111111111111')

dbx.files_download_zip_to_file(path='/superlucky/TRVa/READY',download_path=folder_path+'/qr.zip')
