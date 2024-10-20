"""
    配置了 SimNow 常用的四个环境
    可以使用监控平台 http://openctp.cn 查看前置服务是否正常
"""

# 也可以按需配置其他的支持 ctp官方ctpapi库的柜台
# 注意需要同时修改相应的 user/password/broker_id/authcode/appid 等信息

# SimNow 提供的四个环境
fronts = {
    "7x24": {
        "td": "tcp://118.190.175.212:40500",
        "md": "tcp://118.190.175.212:40501",
    }
}

# 投资者ID / 密码
# user = "226485"
# password = "sWJedore20@$0807"
# user = "058762"
# password = "Jt14235678"
user = "100"
password = "100"
# user = "510100005510"
# password = "ie9560"
# user = "00030736"
# password = "61449185"

# 以下为连接 SimNow 环境的固定值
broker_id = ""
authcode = "ecbf8f06469eba63"
appid = "yd_dev_1.0"
