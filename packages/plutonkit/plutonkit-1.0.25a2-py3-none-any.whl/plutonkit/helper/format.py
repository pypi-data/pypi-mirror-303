import re


def git_name(name):
    rep_name = re.sub(r"^([\///])", "", name).strip()
    rep_name = re.sub(r"([\///])$", "", rep_name)

    return rep_name

def spilt_char(content,enclose_type):
    raw_list =[]
    for val in content:

        bools = False
        for obVal in enclose_type:
            if re.search(obVal["regex"], val):
                if bools is False:
                    name = obVal["name"]
                    raw_list.append(f"[:{name}]")
                bools = True
        if bools is False:
            raw_list.append(val)

    return "".join(raw_list)

def get_enclose_str(content,data,enclose_type):
    look_name = "none"
    for obVal in enclose_type:
        obVal_name= obVal["name"]
        if re.search(re.compile(f"\\[:{obVal_name}\\]"), content):
            look_name = obVal_name

    if look_name != "none":
        match = re.search(re.compile(f"\\[:{look_name}\\](.*?)\\[:{look_name}\\]"), content)
        if match:
            raw_content = content.replace(match.group(0), "$%"+str(len(data))+"%$")
            data.append({"key": look_name,"target":match.group(0)})
            return get_enclose_str(raw_content,data,enclose_type)
    return {
        "replace_ant":data,
        "content":content
    }

def replace_index_to_enclose(values,enclose_type):
    content = values["content"]
    cnt_search = 0
    for key,value in enumerate(values["replace_ant"]):
        if re.search("$%"+str(key)+"%$", content):
            cnt_search +=1
        content = content.replace("$%"+str(key)+"%$",value["target"])

    for obVal in enclose_type:
        content = content.replace("[:"+obVal["name"]+"]",obVal["value"])

    if cnt_search>0:
        values["content"] = content
        return replace_index_to_enclose(values,enclose_type)
    return content

def get_first_line_string_space(value):
    count = 0
    is_str_empty = True
    for val in value:
        if is_str_empty:
            if re.search(r'[\s]', val):
                count +=1
            elif re.search(r'[\t]', val):
                count +=2
            else:
                is_str_empty = False
    return count

def get_str_if_empty(value):
    count = 0
    empty_count = 0
    for val in value:
        count +=1
        if re.search(r'[\s\t]', val):
            empty_count +=1
    return empty_count == count

def get_first_strings(values):
    is_empty_fetch = False
    string = ""
    for value in values:
        if is_empty_fetch is False:
            is_str_empty = get_str_if_empty(value )
            if is_str_empty is False:
                is_empty_fetch = True
                string = value
    return {
        "is_data_fetch": is_empty_fetch,
        "content": string
    }
