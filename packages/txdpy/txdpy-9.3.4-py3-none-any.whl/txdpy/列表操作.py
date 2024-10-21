def liduel(li: list,返回所有元素统计结果=False):
    """查找列表重复元素
    :param li: 列表
    :return: 返回重复元素
    """
    tr_c = li
    tr_c = str(tr_c)
    tr_c = eval(tr_c)
    zwzf = '！已提取索引！'
    if zwzf in tr_c:
        zwzf = zwzf[::-1]
    dic = {}
    for td in tr_c:
        idx = tr_c.index(td)
        if td in dic:
            dic[td] = dic[td] + [idx]
        else:
            dic[td] = [idx]
        tr_c[idx] = zwzf
    repeat_es = []
    for key, value in dic.items():
        if 返回所有元素统计结果:
            repeat_es.append({'重复元素': key, '出现次数': len(value), '元素索引': value})
        elif len(value) > 1:
            repeat_es.append({'重复元素': key, '出现次数': len(value), '元素索引': value})
    return repeat_es

def list_dupl(li):
    """列表去重保持，元素顺序
    :param li:列表
    :return: 返回去重后的列表
    """
    new_list=[]
    for l in li:
        if l not in new_list:
            new_list.append(l)
    return new_list