from yplib.index import *


def do_temp(temp=''):
    print(temp)


# country, table_name_list
@DeprecationWarning
def get_country_table(file_path):
    r_list = []
    need_list = to_list_from_txt_with_blank_line(file_path)
    for table_country_list in need_list:
        country = table_country_list[0]
        r_name_list = []
        # 所有的 table_name
        table_name_list = table_country_list[1:]
        # to_log_file(country)
        for table_name in table_name_list:
            table_name = table_name.strip()
            # 脱敏字段
            desense_column_list = []
            is_log = False
            max_id = -1
            is_done = False
            sp_list = [' ', '\t']
            for sp_o in sp_list:
                if sp_o in table_name:
                    b_n_list = table_name.split(sp_o)
                    table_name = b_n_list[0]
                    desense_temp_list = b_n_list[1:]
                    for o_d in desense_temp_list:
                        # 每个 脱敏字段处理一下, 去掉 \t, 等字段
                        for o_r in sp_list:
                            o_d = o_d.replace(o_r, '')
                        if not len(o_d):
                            continue
                        if o_d.startswith('['):
                            o_d = o_d[1:-1]
                        # 是控制字段,
                        if o_d.startswith('--'):
                            o_d = o_d.replace('--', '')
                            # 是否是log,
                            if o_d.lower() == 'log':
                                is_log = True
                            # 是否完成
                            if o_d.lower() == 'done':
                                is_done = True
                            # 是id
                            if o_d.lower().startswith('max_id='):
                                max_id = to_int(o_d.lower()[len('max_id='):])
                        else:
                            desense_column_list = o_d.split(',')
            if not is_done:
                r_name_list.append([table_name, desense_column_list, is_log, max_id])
        r_list.append([country, r_name_list])
    return r_list




# table_name, column_name_list, type_list, comment_list, column_name_type_comment_list, info_list
@DeprecationWarning
def get_table_sql(file_path):
    table_list = []
    r_list = []
    # 普通文件的解析
    d_list = open(file_path, 'r', encoding='utf-8').readlines()
    # 一个 table 的语句
    table_one = []
    is_start = False
    is_end = False
    for i in range(len(d_list)):
        line = d_list[i].strip()
        if line.lower().startswith('CREATE TABLE `'.lower()) and not is_start:
            is_start = True
        if line.lower().endswith(';'.lower()) and not is_end:
            is_end = True
        if is_start:
            table_one.append(line)
        if is_end:
            if len(table_one):
                table_list.append(table_one)
            table_one = []
            is_start = False
            is_end = False
    # 所有的表结构
    for one_table in table_list:
        # table_name, column_name_list, type_list, comment_list, column_name_type_comment_list, info_list
        table_one_list = ['', [], [], [], [], []]
        # 遍历这个表的,解析出这个表结构数据
        for one_sql in one_table:
            # 表名称
            if one_sql.lower().startswith('CREATE TABLE `'.lower()):
                name_match = re.search(r"CREATE TABLE `(\w+)", one_sql)
                if name_match:
                    table_name = name_match.group(1)
                    # 例如 : analyze_report_loan_tmp
                    # 0 : table_name
                    table_one_list[0] = table_name
            else:
                # 列名称
                one_sql = one_sql.strip()
                if one_sql.startswith('`'):
                    column_match = re.search(r"`(\w+)", one_sql)
                    if column_match:
                        column_name = column_match.group(1)
                        # 1 : column_name
                        table_one_list[1].append(column_name)
                        # 例如 : [order_id]
                        c_list = one_sql.split(' ')
                        column_type = c_list[1]
                        # 2 : column_type
                        table_one_list[2].append(column_type)
                        comment = ''
                        comment_index = -1
                        for i in range(len(c_list)):
                            c = c_list[i]
                            if c.lower() == 'COMMENT'.lower():
                                comment_index = i
                        if comment_index != -1:
                            comment = re.findall(r"'(.+?)'", ''.join(c_list[comment_index + 1:]))[0]
                        comment = comment.strip()
                        if not len(comment) and column_name.lower() == 'id':
                            comment = 'id'
                        # 3 : comment
                        table_one_list[3].append(comment)
                        table_one_list[4].append([column_name, column_type, comment])
        table_one_list[5] = one_table
        r_list.append(table_one_list)
    return r_list