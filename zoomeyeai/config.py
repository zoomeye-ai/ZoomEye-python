#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
* Filename: config.py
* Description: command tool config
* Time: 2024.12.05
*/
"""
from zoomeyeai import __version__, __site__

# save api key file and json web token file path 保存API密钥文件和json web令牌文件路径
ZOOMEYE_CONFIG_PATH = "~/.config/zoomeyeai/setting"

# print data max length 打印数据
STRING_MAX_LENGTH = 2

# cache file name缓存文件名
FILE_NAME = "/{}_{}.json"

RADIUS = 7

CHARACTER = "# "

BLANK = "  "

COLOR_TABLE = ["\x1b[90m", "\x1b[91m", "\x1b[92m", "\x1b[93m", "\x1b[94m", "\x1b[95m", "\x1b[96m", "\x1b[97m",
               "\x1b[91m", "\x1b[92m"]

COLOR_RESET = "\x1b[0m"

BANNER = """\033[01;33m
         ,----,                                                                 
       .'   .`|                            ____      ,---,.                     
    .'   .'   ;                          ,'  , `.  ,'  .' |                     
  ,---, '    .' ,---.     ,---.       ,-+-,.' _ |,---.'   |                     
  |   :     ./ '   ,'\   '   ,'\   ,-+-. ;   , |||   |   .'                     
  ;   | .'  / /   /   | /   /   | ,--.'|'   |  ||:   :  |-,      .--,   ,---.    \033[01;37m{%s }\033[01;33m
  `---' /  ; .   ; ,. :.   ; ,. :|   |  ,', |  |,:   |  ;/|    /_ ./|  /     \  
    /  ;  /  '   | |: :'   | |: :|   | /  | |--' |   :   .' , ' , ' : /    /  | 
   ;  /  /--,'   | .; :'   | .; :|   : |  | ,    |   |  |-,/___/ \: |.    ' / | 
  /  /  / .`||   :    ||   :    ||   : |  |/     '   :  ;/| .  \  ' |'   ;   /|  
./__;       : \   \  /  \   \  / |   | |`-'      |   |    \  \  ;   :'   |  / | 
|   :     .'   `----'    `----'  |   ;/          |   :   .'   \  \  ;|   :    |  
;   |  .'                        '---'           |   | ,'      :  \  \\   \  /  \033[01;37m %s \033[01;33m
`---'                                            `----'         \  ' ; `----'   
                                                                 `--`           \033[0m\033[4;37m\033[0m

""" % (__version__, __site__)
