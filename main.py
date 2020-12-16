import os, json

def cal_cond_prob(char_a, char_b, counter1_dict, counter2_dict): 
    """use frequency to replace probability, return conditional probability of the charactor"""
    cond_prob = 0
    try:
        prob_ab = counter2_dict[char_a][char_b] / counter_total
    except KeyError:
        prob_ab = 0
    try:
        prob_a = counter1_dict[char_a] / counter_total
    except KeyError:
        prob_a = 0
        cond_prob = 0
    else:
        cond_prob = prob_ab / prob_a
    char_prob = lam * cond_prob + (1 - lam) * prob_a
    return char_prob


def find_ans(graph, counter1_dict, counter2_dict):
    for layer in range(len(graph)):
        if layer == 0:
            for dict in graph[layer]:
                if dict['char'] in counter1_dict:
                    dict['value'] = counter1_dict[dict['char']] / counter_total
        else:
            for dict in graph[layer]:
                max_value = 0
                pre_dict = None
                for dict_pre in graph[layer - 1]:
                    new_value = dict_pre['value'] * cal_cond_prob(dict_pre['char'], dict['char'], counter1_dict, counter2_dict)
                    if new_value > max_value:
                        max_value = new_value
                        pre_dict = dict_pre
                dict['value'] = max_value
                dict['pre_dict'] = pre_dict

    max_dict = None
    max_value = 0
    for i in range(len(graph[len(graph)-1])):
        if graph[len(graph)-1][i]['value'] > max_value:
            max_value = graph[len(graph)-1][i]['value']
            max_dict = graph[len(graph)-1][i]

    ans = ""
    while True:
        ans += max_dict['char']
        if not max_dict['pre_dict']:
            break
        max_dict = max_dict['pre_dict']
    l = list(ans)
    l.reverse()
    ans = "".join(l)
    print(ans)
    #print(graph)


if __name__ == "__main__":
    # Data input:
    file = open("./resource/pinyin_dict/pinyin_dict_utf.txt", encoding="utf-8")

    # Define the variable:
    strs = file.readlines()
    file.close()
    py_dict = {}
    file1 = open("./counter1_dict.txt", encoding="utf-8")
    file2 = open("./counter2_dict.txt", encoding="utf-8")
    counter1_dict = json.loads(file1.readline()) # 1 character freq
    counter2_dict = json.loads(file2.readline()) # 2 character freq
    counter_total = 396639694
    lam = 0.8 # define the lambda for smoothing algorithm


    # Pinyin dict input:
    for i in range(len(strs)):
        key_n_value = strs[i].split(' ', 1)
        py_dict.update({key_n_value[0]: key_n_value[1][:-1]})

    #  --- Input transfer ---
    input = "chen si yuan"
    input_spilt = input.split(" ")
    print(input_spilt)

    graph = []

    # Build the graph:
    for i in range(len(input_spilt)):
        graph_list = []
        for j in range(0, len( py_dict[input_spilt[i]] ), 2):
            graph_list.append( {'char':py_dict[input_spilt[i]][j], 'value': 0, 'pre_dict': None})
        graph.append(graph_list)
        # graph's type: graph[layers][char_num] = {'char': char, 'value': freq, 'pre_dict': dict}

    find_ans(graph, counter1_dict, counter2_dict)





