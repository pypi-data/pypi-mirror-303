# encoding=utf-8

from constants_engine.constants import Constants
from utils_engine import core_utils as CoreUtils

kRepeatTipContent = '输入内容不符合要求，请重新输入:'
kMultipleTipContent = '是否继续输入(Y/N):'
kMultipleTipOptions = ['Y','N']

class TagConstants(Constants):
    def __init__(self):
        return self

class TagConstantsTips(TagConstants):

    def __init__(self, 
                 tag_tip, 
                 tag_tip_name,
                 tag_options=[], 
                 tag_nullable=False, 
                 tag_multilpeable=False,
                 tag_defalut_rs='',
                 tag_complete_flag='Y',
                 tag_duplicate_check=False,
                 tag_repeat_tip=kRepeatTipContent):
        
        self.tag_tip = tag_tip
        self.tag_nullable = tag_nullable
        self.tag_options = CoreUtils.safe_list(tag_options)
        self.tag_repeat_tip = tag_repeat_tip
        self.tag_multilpeable = tag_multilpeable
        self.tag_tip_name = tag_tip_name
        self.tag_complete_flag = tag_complete_flag
        self.tag_defalut_rs = tag_defalut_rs
        self.tag_duplicate_check = tag_duplicate_check
    
# 多次录入提醒
class TagMultipleConstantsTips(Constants):

    def __init__(self, 
                 tag_constants, 
                 tag_tip_name, 
                 tag_complete,
                 tag_duplicate_check=False
                 ):
        
        self.tag_constants = CoreUtils.safe_list(tag_constants)
        self.tag_complete = CoreUtils.obj_null_filter(tag_complete, TagConstantsTips)
        self.tag_tip_name = tag_tip_name
        self.tag_duplicate_check = tag_duplicate_check
