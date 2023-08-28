import shutil,os
import datetime
import re
from time import sleep
from tqdm import tqdm, trange

# ========= 讀取來源位置首頁檔案、資料夾名稱 =========
startPath = r"" + input("起始資料夾位置:")
goalPath = r"" + input("備份資料夾位置:")
#dir_path = "G:/" # 來源位置
all_file_name = os.listdir(startPath)
#↑讀取資料夾內所有檔案名稱然後放進all_file_name這個list裡

skip = 0 # 紀錄不用搬移檔案的數量
fileslist = [] # 存放搬移檔案名稱

# 篩選出不用搬移的檔案
for i in all_file_name:
    F = str(i)
    if re.search(r"found.", F, re.I):
        skip+=1
    elif re.search(r"RECYCLE.BIN", F, re.I):
        skip+=1
    elif re.search(r"System Volume Information", F, re.I):
        skip+=1
    else:
        #print(F)
        fileslist.append(F)

#  ========= 執行搬運檔案  =========
#print(fileslist) # 印出需要搬移的所有檔案名稱
#print(len(fileslist)) # 印出需要搬移的所有檔案名稱數量
times = 0 # 計時用，刷新進度條
progress = tqdm(total=100) # 進度條

while times < 100:
    for i in fileslist:
        files = startPath + i
        source = goalPath + i 
        #files = "G:/" + i # ===> 來源位置 (可以改，改G就好)
        #source = "I:/" + i # ===> 搬運目標 (可以改，改I就好)
        try:
            print("正在搬運:",i)
            shutil.copytree( files, source)
            progress.update(1)
            times += 1
            sleep(0.01)
        except:
            print("已經搬運過:",i)
            progress.update(1)
            times += 1
            sleep(0.01)
            continue
print("執行完畢")

