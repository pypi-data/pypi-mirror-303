# encoding=utf-8

import os, re, platform

# def create_tag

def start_construct_tag_template(config_dict):
    template_type = config_dict['template_type']
    
    code_base_path="/loan-data-warehouse-python"

    tempalte_path = code_base_path+'/hugsqltools/template_engine/tag_templates/offline'
    if template_type == 1:
        tempalte_path = code_base_path+'/hugsqltools/template_engine/tag_templates/offline'
    elif template_type == 2:
        tempalte_path = code_base_path+'/hugsqltools/template_engine/tag_templates/nrt'
    else :
        raise RuntimeError('程序逻辑异常，请联系chaiyuan_dxm排查')
    
    # base_path = os.getcwd()
    base_path=code_base_path

    # 加上操作系统的判断
    if platform.system() == 'Windows':
        # base_path = base_path.replace("\\", "/")    # // ---> /
        final_path = tempalte_path
        output_path = '%s/dw/%s/tag/%s/%s' % (base_path, config_dict['tag_data_level'], config_dict['append_path'],config_dict['tag_code'])
    else:
        final_path = tempalte_path
        output_path = '%s/dw/%s/tag/%s/%s' % (base_path, config_dict['tag_data_level'], config_dict['append_path'],config_dict['tag_code'])
    

############################################################################################################################
    ######################### 调试模块 #########################
    # final_path='/dxm/loan-data/loan-data-warehouse-python/hugsqltools/template_engine/tag_templates/nrt'
    # output_path='/dxm/loan-data/loan-data-warehouse-python/dw/ads/tag/index_06_nrt/%s' %(config_dict['tag_code'])
    
    print('final_path',final_path)
    print('output_path',output_path)
    # index=0
    # for dirpath, dirnames, filenames in os.walk(final_path):
    #     for filename in filenames:
    #         print(index,dirpath,filename)
    #         index+=1
############################################################################################################################
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for dirpath, dirnames, filenames in os.walk(final_path):
        for filename in filenames:

            temp_dependencies = ''
            pre_rules = []
            for dependency in config_dict['tag_dependencies']:
                table = dependency['table']
                partitions=dependency['partitions']
                partitions_name = dependency['partitions_name']
                temp_dependencies += '  - table: %s\n'%(table)
                temp_dependencies += "    partitions: '%s'\n"%(partitions)
                pre_rule = "SELECT if(count(1)>1, 0, 1) AS res \nFROM hivedgs.%s \nWHERE \n%s='%s'"%(table, partitions_name,partitions)
                pre_rules.append(pre_rule)
            
            batch_staticize_codes=[]

            if 'tag_staticize_codes' in config_dict.keys():    
                for code_item in config_dict['tag_staticize_codes']:
                    statistic_code=code_item['tag_staticize_code']
                    batch_staticize_codes.append(statistic_code)

            tag_entity_key = 'did'

            tag_entity_type = config_dict['tag_entity_type'].lower()
            if tag_entity_type == 'did':
                tag_entity_key = 'did'
            elif tag_entity_type == 'cmid':
                tag_entity_key = 'customer_id'

            temp_staticize_codes=''
            if len(batch_staticize_codes)>0:
                temp_staticize_codes = "\
  multiple_column:\n\
    primary_key: %s\n\
    column_names:\n\
    %s"%(tag_entity_key , "  - "+"\n      - ".join(batch_staticize_codes)+"\n")
            fields_name=",\n".join(batch_staticize_codes)

            pre_check_sql = 'WITH '
            rule_index = 1
            rule_length = len(pre_rules)
            poly_rules = ''

            for pre_rule in pre_rules:
                rule_name = 'rule%s'%(str(rule_index))
                rule_item = '%s AS (\n%s\n)'%(rule_name, pre_rule)
                if rule_index < rule_length:
                    rule_item += ','
                    poly_rules += 'SELECT res FROM %s \nUNION ALL \n'%(rule_name)
                else:
                    poly_rules += 'SELECT res FROM %s'%(rule_name)
                pre_check_sql += '%s \n'%(rule_item)
                rule_index += 1
            
            pre_check_sql += "SELECT if(sum(res) = 0 ,'true','false') AS res \nFROM (\n%s\n)"%(poly_rules)

            replace_config_dict = {
                'tag_code': config_dict['tag_code'],
                'tag_name': config_dict['tag_name'],
                'tag_dependencies': temp_dependencies,
                'tag_version': config_dict['tag_version'],
                'tag_entity_type': config_dict['tag_entity_type'],
                'tag_priority': config_dict['tag_priority'],
                'tag_belong_path': config_dict['append_path'],
                'tag_entity_key': tag_entity_key,
                'pre_check_sql': pre_check_sql,
                # 'tag_rccgroup': config_dict['tag_rccgroup'],
                'processing_owner': config_dict['processing_owner'],
                # 'apply_scenario': config_dict['apply_scenario'],
                'tag_staticize': config_dict['tag_staticize'],
                'tag_staticize_codes': temp_staticize_codes,
                'fields_name':fields_name
            }

            if platform.system() == 'Windows':
                temp_filepath = os.path.join(dirpath, filename).replace("\\", "/")
            else:
                temp_filepath = os.path.join(dirpath, filename)
            # print('temp_filepath',temp_filepath)
            # 指定读写文件的编码方式
            with open(temp_filepath, encoding="utf-8") as file_obj:
                file_content = file_obj.read()

                final_rs = file_content
                for key,value in replace_config_dict.items():
                    regex = r'({{[ ]*%s[ ]*}})'%(key)
                    final_rs = re.sub(regex, value, final_rs)

                output_filepath = '%s/%s'%(output_path, filename.replace('tagcode', config_dict['tag_code']))

                with open(output_filepath, 'w', encoding="utf-8") as write_obj:
                    write_obj.write(final_rs)
                    write_obj.close()

