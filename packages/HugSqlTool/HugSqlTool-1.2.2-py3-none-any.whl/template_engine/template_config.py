# encoding = utf-8

class TemplateConfig(object):
    def __init__(self, config_dict):
        self.config_dict = config_dict

class TagTemplateConfig(TemplateConfig):
    def __init__(self, config_dict):
        super().__init__(config_dict)