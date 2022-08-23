from genericpath import exists
import os
import re
from powershell import *


# 当前目录
P_curposition = os.getcwd()
P_SIGN_CONFIG = P_curposition+"/config.ini"

# 执行命令创建谷歌私钥
def F_creat_private_key():
    File_readConfig = open(P_SIGN_CONFIG,"r",encoding="utf-8")
    for eachline in File_readConfig:
        if(re.search("keystore",eachline)):
            keystorepath = eachline.split("=")[1][:-1]
        if(re.match("alias=",eachline)):
            aliasName = eachline.split("=")[1][:-1]
        if(re.match("pswd",eachline)):
            pswd = eachline.split("=")[1][:-1]
        if(re.search("aliaspswd",eachline)):
            aliaspswd = eachline.split("=")[1][:-1]
        if(re.search("encryptionkey",eachline)):
            encryptionkey = eachline.split("=")[1][:-1]
    with PowerShell('GBK') as ps:
        outs, errs = ps.run('java -jar pepk.jar --keystore='+keystorepath+' --keystore-pass='+pswd+' --alias='+aliasName+' --key-pass='+aliaspswd+' --encryptionkey='+encryptionkey+' --output='+keystorepath[:-9]+'_private.pepk')
    print('error:', os.linesep, errs)
    print('output:', os.linesep, outs)
    print("creat private_key seccess!")

F_creat_private_key()