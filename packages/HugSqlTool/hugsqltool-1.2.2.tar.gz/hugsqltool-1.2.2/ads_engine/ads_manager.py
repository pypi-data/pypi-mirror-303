from ads_config import AdsTagConfig

def prepare_tag_config(dict:dict):
    print('ads tag config info %s'%(dict))
    tag_config = AdsTagConfig()
    # 归属
    tag_config.tagt_data_level = 'ads'
    # 业务归属
    tag_config.tag_belong = dict['tag_belong']
    # 标签Code
    tag_config.tag_code = dict['tag_code']
    # 标签Name
    tag_config.tag_name = dict['tag_name']
    # 优先级
    tag_config.tag_priority = dict['tag_priority']
    # 实体类型
    tag_config.tag_priority = dict['tag_entity']
    # 数据依赖
    tag_config.tag_dependencies = dict['tag_dependencies']