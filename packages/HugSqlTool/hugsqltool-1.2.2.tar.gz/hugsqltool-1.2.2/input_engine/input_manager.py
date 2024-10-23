# encoding=utf-8

from utils_engine import core_utils as CoreUtils
from tag_template_cons.tag_template_constants import TagConstants, TagConstantsTips, TagMultipleConstantsTips

# 本地输入提醒
def start_input_tips(tip_config, err_repeat=False):

    if isinstance(tip_config, TagConstantsTips):

        tag_tip = tip_config.tag_tip
        tag_options = tip_config.tag_options

        if isinstance(tag_tip, str) == False:
            raise RuntimeError('传入配置tag_tip错误，请排查源码~，Info:%s'%(tag_tip))
        
        if isinstance(tag_options, list) == False:
            raise RuntimeError('传入配置tag_options错误，请排查源码~, Info:%s'%(tag_tip))

        input_rs = ''

        if err_repeat == True:
            tag_tip = tip_config.tag_repeat_tip

        if CoreUtils.is_python3():
            input_rs = input(tag_tip)

        if CoreUtils.is_python2():
            input_rs = raw_input(tag_tip)

        if input_rs in tag_options or len(tag_options) == 0:

            if isinstance(input_rs, str):
                if len(input_rs) > 0:
                    return input_rs
                elif tip_config.tag_nullable :
                    return tip_config.tag_defalut_rs
            
        return start_input_tips(tip_config, True)

    # 需要录入多个数据，春初结果是数组
    if isinstance(tip_config, TagMultipleConstantsTips):
        rs = []
        input_complete = False
        while input_complete == False:
            item_dict = {}
            for item_config in tip_config.tag_constants:
                item_rs = start_input_tips(item_config)
                item_dict[item_config.tag_tip_name]=item_rs
            rs.append(item_dict)

            complet_rs = start_input_tips(tip_config.tag_complete)
            if complet_rs.upper() == tip_config.tag_complete.tag_complete_flag:
                input_complete = True

        return rs
    
    RuntimeError("不支持的对象类型，请检查代码")

