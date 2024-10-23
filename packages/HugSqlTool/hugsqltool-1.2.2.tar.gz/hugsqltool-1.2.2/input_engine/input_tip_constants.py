
from constants_engine.constants import Constants

class InputTipConstants(Constants):
    @property
    def tip_name(self):
        return self.tip_name
    
    def tip_options(self):
        return self.tip_options
    

class InputRepeatTipConstants(InputTipConstants):
    @property
    def tip_name(self):
        return "请重新输入："

    def tip_options(self):
        return super().tip_options()