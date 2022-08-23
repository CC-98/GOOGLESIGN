# GOOGLESIGN
>### 处理AAB上架谷歌商店所需的签名

>工具功能描述

&emsp;&emsp;当有新游戏需要上线，或者谷歌后台秘钥需要修改，使用本工具生成上传谷歌后台的新秘钥，
>材料准备

&emsp;&emsp;新游戏的签名文件
&emsp;&emsp;谷歌后台提供的encryptionkey
&emsp;&emsp;配置config.ini

>执行命令

&emsp;&emsp;Python creat_privatepepk.py

>产出内容

&emsp;&emsp;在GOOGLESIGN/根目录下生成xxxx_private.pepk文件

>常见错误及解决方法

&emsp;&emsp;出现：error:Nnoe output： creat private_key success!  
&emsp;&emsp;说明：已成功创建秘钥

&emsp;&emsp;出现：Error: Unable to export or encrypt the private key  
&emsp;&emsp;原因：java.lang.IllegalArgumentException:  
&emsp;&emsp;处理：config.ini中最后一行的占位符不能删掉