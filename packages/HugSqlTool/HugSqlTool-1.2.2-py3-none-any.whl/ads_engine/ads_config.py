from config_engine.config_manager import TemplateConfig

class AdsTagConfig(TemplateConfig):
    @property
    def tag_type(self):
        return super().tag_type
    
    # 业务自定义生成模板存储位置
    def tag_destination(self):
        destination_path = "/%s/tag"%(self.tag_data_level)
        append_dir_path = ''
        if self.tag_type == '离线':
            
            if self.tag_belong == '小微':
                append_dir_path = 'index_02_xiaowei'
            elif self.tag_belong == '消费':
                append_dir_path = 'index_01_consumption'
            elif self.tag_belong == '其他':
                append_dir_path = 'index_03_other'
            elif self.tag_belong == '经营':
                append_dir_path == 'index_04_bussiness_operation'
            elif self.tag_belong == '迁移':
                append_dir_path == 'index_05_history'
            else :
                RuntimeError('不支持的业务类型，请重试(%s)'%(self.tag_belong))
        
        elif self.tag_type == '准实时':
            append_dir_path = 'index_06_nrt'

        else:
            RuntimeError('不支持的标签类型（错误标签：%s）'%(self.tag_type))

        destination_path = destination_path + '/' + append_dir_path

        return destination_path

    def tag_data_level(self):
        return 'dw/ads'
    
    
    