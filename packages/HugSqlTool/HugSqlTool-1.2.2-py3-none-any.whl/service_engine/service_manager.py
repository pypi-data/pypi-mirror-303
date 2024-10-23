# encoding=utf-8

import os,platform

from input_engine import input_manager as Input
from config_engine import config_manager as Config

from tag_template_cons.tag_template_constants import TagConstantsTips, TagMultipleConstantsTips

from template_engine import template_manager as TemplateManager

from utils_engine import git_utils

# 创建交互式配置
def interactive_tag_config():

    tag_configs = []
    
    tag_name_config = TagConstantsTips(
        tag_tip='请输入标签中文名:',
        tag_tip_name='tag_name'
    )
    tag_configs.append(tag_name_config)

    tag_code_config = TagConstantsTips(
        tag_tip='请输入标签Code:',
        tag_duplicate_check=True,
        tag_tip_name='tag_code'
    )
    tag_configs.append(tag_code_config)

    # 标签默认ADS层
    # tag_datalevel_config = TagConstantsTips(
    #     tag_tip="请输入数据层级(ads/ods/dws/dwd/dim):",
    #     tag_options=['ads','ods','dws','dwd','dim'],
    #     tag_tip_name='tag_data_level'
    # )
    # tag_configs.append(tag_datalevel_config)
    
    tag_belong_config = TagConstantsTips(
        tag_tip='请输入标签目录归属(1-消费[常规标签]/2-小微/3-其他经营[广告/生态/线下]/4-经营时机/5-历史标签[迁移]/6-准实时复算/7-消费宽表/8-业务自助加工/9-风控策略):',
        tag_options=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        tag_tip_name='tag_belong'
    )
    tag_configs.append(tag_belong_config)

    tag_version_config = TagConstantsTips(
        tag_tip='请输入标签版本信息(跳过默认使用1.0.0):',
        tag_nullable=True,
        tag_tip_name='tag_version',
        tag_defalut_rs='1.0.0'
    )
    tag_configs.append(tag_version_config)

    tag_entitytype_config = TagConstantsTips(
        tag_tip='请输入标签实体类型：[可选项:did/cmid/adjust_id](跳过默认使用did):',
        tag_nullable=True,
        tag_defalut_rs='did',
        tag_tip_name='tag_entity_type'
    )
    tag_configs.append(tag_entitytype_config)

    tag_staticize_config = TagConstantsTips(
        tag_tip='请输入是否要加工成静态变量：[可选项:false/true](跳过默认不入库：使用false):',
        tag_nullable=True,
        tag_tip_name='tag_staticize',
        tag_defalut_rs='false'
    )
    tag_configs.append(tag_staticize_config)

    # 加工的RCC组目前确定就会统一一个，去掉相关逻辑
    # tag_rccgroup_config = TagConstantsTips(
    #     tag_tip='请输入标签加工的RCC组：[可选项:fsg_rcc_loan_data_rd/fsg_rcc_loan_data_qualified_rd](跳过默认使用fsg_rcc_loan_data_rd):',
    #     tag_nullable=True,
    #     tag_tip_name='tag_rccgroup',
    #     tag_defalut_rs='fsg_rcc_loan_data_rd'
    # )
    # tag_configs.append(tag_rccgroup_config)

    # 标签的应用场景目前根据，优先级和消费宽表进行自助判断；后续场景变多在进行处理
    # tag_apply_scenario_config = TagConstantsTips(
    #     tag_tip='请输入标签应用场景：[可选项:fsg_rcc_loan_data_rd/fsg_rcc_loan_data_qualified_rd](跳过默认使用fsg_rcc_loan_data_rd):',
    #     tag_nullable=True,
    #     tag_tip_name='tag_rccgroup',
    #     tag_defalut_rs='fsg_rcc_loan_data_rd'
    # )
    # tag_configs.append(tag_apply_scenario_config)

    tag_priority_config = TagConstantsTips(
        tag_tip='是否为高优标签[高优使用P0](跳过默认使用P1)',
        tag_tip_name='tag_priority',
        tag_nullable=True,
        tag_defalut_rs='P1'
    )
    tag_configs.append(tag_priority_config)

    tag_dependencies_config = TagMultipleConstantsTips(
        tag_tip_name='tag_dependencies',
        tag_constants=[],
        tag_complete = TagConstantsTips(
            tag_tip='是否已完成依赖源输入(Y/N):',
            tag_options=['Y', 'N'],
            tag_tip_name='tag_dependencies_complete',
            tag_multilpeable = True,
            tag_complete_flag='Y'
        )
    )

    tag_dependtable_config = TagConstantsTips(
        tag_tip='请输入依赖数据源(dbname.tablename):',
        tag_tip_name='table'
    )
    tag_dependpartitions_config = TagConstantsTips(
        tag_tip='请输入依赖分区[{DATE-1}/{DATE2-1}/{DATE-1}23](跳过默认为{DATE-1}):',
        tag_tip_name='partitions',
        tag_nullable=True,
        tag_defalut_rs='{DATE-1}'
    )
    tag_dependpartitionsname_config = TagConstantsTips(
        tag_tip='请输入依赖分区[ads_day/dws_day/dwd_day/dim_day/ods_day/dwd_hour](跳过默认为dwd_day):',
        tag_tip_name='partitions_name',
        tag_nullable=True,
        tag_defalut_rs='dwd_day'
    )
    tag_dependencies_config.tag_constants.append(tag_dependtable_config)
    tag_dependencies_config.tag_constants.append(tag_dependpartitions_config)
    tag_dependencies_config.tag_constants.append(tag_dependpartitionsname_config)

    tag_configs.append(tag_dependencies_config)
    
    config_dict = {}
    for tag_config in tag_configs:
        input_rs = Input.start_input_tips(tag_config)
        print(tag_config.tag_tip_name)
        if tag_config.tag_duplicate_check == True:
            check_rs = tag_flag_duplicate_check(input_rs)
            if check_rs == True:
                raise RuntimeError('录入 %s 重复，请检查后重新录入'%(tag_config.tag_tip_name))
        config_dict[tag_config.tag_tip_name] = input_rs

    if config_dict['tag_staticize']==True or config_dict['tag_staticize']=='true':

        batch_config = TagConstantsTips(
            tag_tip='是否批量录入静态变量(Y/N):',
            tag_tip_name='batch_input_static_vars',
            tag_nullable=True,
            tag_defalut_rs='N'
        )

        batch_input_rs = Input.start_input_tips(batch_config)

        if batch_input_rs == 'Y':
            tag_config = TagMultipleConstantsTips(
                tag_tip_name='tag_staticize_codes',
                tag_constants=[],
                tag_complete = TagConstantsTips(
                    tag_tip='是否已完成静态变量录入(Y/N):',
                    tag_options=['Y', 'N'],
                    tag_tip_name='tag_staticize_codes_complete',
                    tag_multilpeable = True,
                    tag_complete_flag='Y'
                )
            )
            tag_staticize_code_config = TagConstantsTips(
                tag_tip='请输入静态变量code:',
                tag_tip_name='tag_staticize_code',
                tag_nullable=False,
            )
            tag_staticize_code_name_config = TagConstantsTips(
                tag_tip='请输入静态变量name:',
                tag_tip_name='tag_staticize_code_name',
                tag_nullable=False,
            )
            tag_config.tag_constants.append(tag_staticize_code_config)
            tag_config.tag_constants.append(tag_staticize_code_name_config)
            input_rs = Input.start_input_tips(tag_config)
            config_dict['tag_staticize_codes']=input_rs
    
    return config_dict

def tag_flag_duplicate_check(tag_flag):

    base_path = os.getcwd()

    tmp_base_path = '../../dw/ads/tag'

    # 加上操作系统的判断
    if platform.system() == 'Windows':
        base_path = base_path.replace("\\", "/")    # // ---> /
        output_path = '%s/dw/ads/tag/' % (base_path)
    else:
        base_path = base_path.replace("\\", "/")    # // ---> /
        output_path = '%s/dw/ads/tag/' % (base_path)

    is_duplicate = False

    for dirpath, dirnames, filenames in os.walk(output_path):
        if dirpath == tag_flag:
            is_duplicate = True
            break
        for filename in filenames:
            if filename == tag_flag or filename == '%s.sql'%(tag_flag):
                is_duplicate = True
                break
        if is_duplicate == True:
            break
    return is_duplicate

# 触发template task
def resume_template_task(config_dict):
    # template_type = 1/离线标签  2/准实时标签
    template_type = 1
    tag_belong = config_dict['tag_belong']
    
    if not isinstance(tag_belong, str) or len(tag_belong) == 0 :
        raise RuntimeError('代码逻辑异常，请联系chaiyuan_dxm排查问题')
    
    __int_tag_belong = int(tag_belong)

    append_belong_path = ''
    # 标签的应用场景，0-普通筛客，1-消费宽表，2-人工电召
    # 默认全部为0-普通筛客，当优先级为高优时可用于人工电召，当放到消费目录下则用于消费宽表
    apply_scenario_value = "  - '0'\n"

    if __int_tag_belong == 1:
        template_type = 1
        append_belong_path = 'index_01_consumption'
    elif __int_tag_belong == 2:
        template_type = 1
        append_belong_path = 'index_02_xiaowei'
    elif __int_tag_belong == 3:
        template_type = 1
        append_belong_path = 'index_03_other'
    elif __int_tag_belong == 4:
        template_type = 1
        append_belong_path = 'index_04_bussiness_operation'
    elif __int_tag_belong == 5:
        template_type = 1
        append_belong_path = 'index_05_history'
    elif __int_tag_belong == 6:
        template_type = 2
        append_belong_path = 'index_06_nrt'
    elif __int_tag_belong == 7:
        template_type = 1
        append_belong_path = 'dws_loan_ccl_tag'
        apply_scenario_value = apply_scenario_value + "  - '1'\n"
    elif __int_tag_belong == 8:
        template_type = 1
        append_belong_path = 'index_08_business_self'
    elif __int_tag_belong == 9:
        template_type = 1
        append_belong_path = 'index_09_ris'
    else:
        raise RuntimeError('不支持的业务归属，请联系chaiyuan_dxm修改')

    # 处理高优标签默认可用于电召场景
    tag_priority = config_dict['tag_priority']
    if tag_priority == 'P0':
        apply_scenario_value = apply_scenario_value + "  - '2'\n"

    data_level = 'ads'

    template_config_dict = config_dict
    template_config_dict['tag_data_level'] = data_level
    template_config_dict['template_type'] = template_type
    template_config_dict['append_path'] = append_belong_path
    template_config_dict['base_path'] = '../../dw/%s/tag'%(data_level)

    # processing_owner = git_utils.get_git_user_name()
    processing_owner='xxx_dxm'

    template_config_dict['processing_owner'] = processing_owner
    # template_config_dict['apply_scenario'] = apply_scenario_value

    TemplateManager.start_construct_tag_template(template_config_dict)


def start_constructor_tag_template():
    # template type support offline_tag and nrt_tag
    config_dict = interactive_tag_config()
    resume_template_task(config_dict)
