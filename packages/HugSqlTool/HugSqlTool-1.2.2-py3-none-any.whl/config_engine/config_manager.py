# encoding=utf-8

class TemplateConfig(object):

    def __init__(self):
        return self
    
    @property
    # 离线标签 / 准实时
    def tag_type(self):
        return self.tag_type
    
    # （小微/消费/经营/其他/迁移）
    def tag_belong(self):
        return self.tag_belong

    # 自定义 Name
    def tag_name(self):
        return self.tag_name
    
    # tag_code，非空
    def tag_code(self):
        return self.tag_code
    
    # 自定义版本号， 默认使用1.0.0
    def tag_version(self):
        if isinstance(self.tag_version, str) and self.tag_version != '':
            return self.tag_version
        else:
            return "1.0.0"
    
    # 标签优先级
    def tag_priority(self):
        return self.tag_priority
    
    # 数据层级
    def tag_data_level(self):
        return self.tag_data_level
    
    # 数据依赖项
    def tag_dependencies(self):
        return self.tag_dependencies
    
    # 实体类型，依赖子类实现
    def tag_entity_type(self):
        raise RuntimeError("未在子类指定存储目标地址")

    # 存储目的地
    def tag_destination(self):
        raise RuntimeError("未在子类指定存储目标地址")
