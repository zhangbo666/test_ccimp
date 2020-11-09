__author__ = "zhangbo"


from ccimp_systemSettings_app.models.WebConfigModels import WebConfig
import json


orderConfig = "OrderConfig"

# 调取默认配置表(configKey=OrderConfig)
webConfigs = WebConfig.objects.all()

for w1 in webConfigs:

    if (w1.keyConfig == orderConfig):

        dict_data = w1.valueConfig

        # src转dict
        w1 = json.loads(dict_data)

        orderon_limit_sum = int(w1["sum"])

        break

    else:

        orderon_limit_sum = 5


