import os, json


if __name__ == "__main__":
    # Data input:
    file = open("./resource/pinyin_dict/pinyin_dict_utf.txt", encoding="utf-8")

    # Define the variable:
    strs = file.readlines()
    file.close()
    py_dict = {}
    data_dict_list = []
    counter1_dict = {} # 1 character freq
    counter2_dict = {} # 2 character freq
    counter_total = 0 # total freq
    not_count_char = "!@#$%^&*()！……「」【】{}|\:：;\"“”（）。，；,.1234567890《》<>?？/、~` qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


    # News data input:
    data_path = "./resource/sina_news_utf8/"
    data_path_list = os.listdir(data_path)
    for i in range(len(data_path_list)):
        file = open(data_path + data_path_list[i], encoding="utf-8")
        #file = open(data_path+"test.txt", encoding="utf-8")
        while True:
            line = file.readline()
            if not line:
                break
            data_dict_list.append(json.loads(line))

    # --- Counting ---
    for i in range(len(data_dict_list)):
        string = data_dict_list[i]['html']
        for j in range(len(string) - 1):
            # Ignore the character not Chinese
            # Counting 1-gram
            if string[j] in not_count_char:
                continue
            if string[j] not in not_count_char:
                if string[j] not in counter1_dict:
                    counter1_dict.update({string[j]: 1})
                    counter_total += 1
                else:
                    counter1_dict[string[j]] += 1
                    counter_total += 1
            # counter1_dict's type: { char1 : value , char2 : value}

            # Counting 2-gram
            if string[j+1] in not_count_char:
                j += 1
                continue
            if string[j] not in counter2_dict:
                counter2_dict.update({string[j]: {string[j+1]: 1}})
            elif string[j+1] not in counter2_dict[string[j]]:
                counter2_dict[string[j]].update({string[j+1]: 1})
            else:
                counter2_dict[string[j]][string[j+1]] += 1
            # counter2_dict's type: { char_a1: { char_b1: value, char_b2: value }, char_a2: ... }

    file1 = open("./counter1_dict.txt", "w", encoding="utf-8")
    file2 = open("./counter2_dict.txt", "w", encoding="utf-8")
    file1.write(json.dumps(counter1_dict, ensure_ascii=False))
    file2.write(json.dumps(counter2_dict, ensure_ascii=False))


    print(counter_total)


