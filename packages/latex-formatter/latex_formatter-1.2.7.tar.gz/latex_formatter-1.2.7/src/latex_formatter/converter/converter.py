# from latex_formatter.utils.text_to_latex import conversion_functions
# from latex_formatter.utils import transfer_to_dict
import json
from json import JSONDecodeError
from typing import Union
from .web_converter import LatexRender


def transfer_to_dict(data: dict | str):
    if isinstance(data, dict):
        return data
    if isinstance(data, list):
        return data
    if not data:
        return None
    return json.loads(data)


# def converter(data: Union[dict, str]):
#     if isinstance(data, list):
#         res = []
#         for d in data:
#             converter(d)

#     try:
#         content_dict = transfer_to_dict(data)
#     except JSONDecodeError:
#         # print("load err")
#         # print(type(data))
#         return data
#     question = content_dict["caption"] if "caption" in content_dict else content_dict

#     answer = content_dict.get("answer", None)
#     types = question["type"]

#     try:
#         if types == "wave":
#             print(f"wave")
#             print(conversion_functions.get(types))
#         conversion_func = conversion_functions.get(types)

#         if conversion_func:
#             # maybe \\newline
#             # return conversion_func(te).replace("[br]", "<br />")
#             question_part = conversion_func(question)
#         else:
#             raise ValueError(f"No conversion function for type {types} found.")
#     except Exception as e:
#         #  print(f"error for {type(data)}")
#         #  print(e)
#         pass

#     if not answer:
#         # return 'error'
#         try:
#             return question_part
#         except:
#             return "error"
#     else:
#         if answer_converter(answer):
#             return question_part + answer_converter(answer)
#         return question_part


# def answer_converter(answer: dict):
#     try:
#         answer_dict = transfer_to_dict(answer)
#     except JSONDecodeError:
#         # print("load err")
#         # print(type(data))
#         return answer

#     if answer_dict:
#         types = answer.get("type", None)

#         try:
#             conversion_func = conversion_functions.get(types)

#             if conversion_func:
#                 # maybe \\newline
#                 # return conversion_func(te).replace("[br]", "<br />")

#                 answer_part = conversion_func(answer_dict)
#                 return answer_part
#             else:
#                 raise ValueError(f"No conversion function for type {types} found.")
#         except Exception as e:
#             #  print(f"error for {type(data)}")
#             #  print(e)
#             pass
#         return []


def is_final_object(obj):
    if isinstance(obj, dict):
        for key, val in obj.items():
            if isinstance(val, dict):
                if "type" in val:
                    return False
                if not is_final_object(val):
                    return False
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                if "type" in item:
                    return False
                if not is_final_object(item):
                    return False
    return True


def render(obj):
    if isinstance(obj, dict) and "type" in obj and obj["type"]:
        obj_type = obj["type"].lower()
        conversion_func = conversion_functions.get(obj_type)
        if conversion_func:
            # maybe \\newline
            # return conversion_func(te).replace("[br]", "<br />")
            question_part = conversion_func(obj)

            print(question_part)
            return question_part

    elif isinstance(obj, str):
        return obj.replace("[br]", "\n")
    elif isinstance(obj, list):
        return " ".join(obj)
    else:
        return "Invalid object type"


def to_old_version(obj):
    if isinstance(obj, dict):
        if "type" in obj:
            if obj["type"] in ["merge", "equation", "latexarray"]:
                nobjs = [to_old_version(o) for o in obj["value"]]
                obj["value"] = nobjs
                return obj
            elif obj["type"] in ["select", "multiselect"]:
                nobjs = [to_old_version(o) for o in obj["options"]]
                obj["options"] = nobjs
                return obj
            elif obj["type"] in ["table", "matrix", "grid"]:
                for col in obj["value"]:
                    for i, row in enumerate(col):
                        col[i] = to_old_version(row)
                return obj
            else:
                for k, val in obj.items():
                    obj[k] = to_old_version(val)
                return obj
        else:
            nobjs = {}
            is_list = all(isinstance(k, int) for k in obj.keys())
            for k, o in obj.items():
                nobjs[k] = to_old_version(o)
            if is_list:
                return {"type": "merge", "value": list(nobjs.values())}
            else:
                return nobjs
    elif isinstance(obj, list):
        # 对列表中的每个值递归调用
        print([to_old_version(val) for val in obj])

        return [to_old_version(val) for val in obj]
    else:
        return obj


def c2(obj):
    if not obj:
        return ""

    # if not isinstance(obj, dict):
    #     try:
    #         obj = transfer_to_dict(obj)
    #     except (JSONDecodeError):
    #         # print("load err")
    #         # print(type(data))

    obj = to_old_version(obj)

    while True:
        current_obj = obj
        if is_final_object(obj):
            return render(obj)

        found = False
        if isinstance(obj, dict):
            for key, val in current_obj.items():
                if not isinstance(val, dict):
                    continue
                if is_final_object(val):
                    if "type" in val:
                        current_obj[key] = render(val)

            else:
                current_obj = val
                found = True
                break
        elif isinstance(obj, list):
            length = len(obj)

            for i in range(length):
                current_obj[i] = render(current_obj[i])

        if not found:
            break

        if current_obj is obj:
            break

    return render(current_obj)


def c_by_type(data: dict):
    print(f"data is  {data}")

    data_type = data.get("type")
    solution = transfer_to_dict(data.get("solution", ""))

    content = transfer_to_dict(data.get("content"))
    explains = transfer_to_dict(data.get("explains"))
    knowledge_point = data.get("knowledge_point", None)
    answer = content.get("answer", None)
    # Check for empty solutions in certain question types
    if data_type in [1, 2, 3] and not solution:
        errorMsg("填空答案错误")
        return

    # Check for empty content in single and multiple choice questions
    if data_type in [2, 3] and ("answer" not in content or not answer):
        errorMsg("单选题干错误")
        return

    # Initialize the structure to store the processed data
    json_data = {"type": data_type, "solution": None, "caption": None}

    json_data["caption"] = LatexRender.html_render(content["caption"])
    json_data["knowledge_point"] = knowledge_point

    if data_type == 1 or data_type == "填空":
        # Fill-in-the-blank
        answer_index = get_answer_index(content["caption"])
        answer_index_count = len(answer_index)

        json_data["solution"] = []
        for sk, s in enumerate(solution):
            if sk > (answer_index_count - 1):
                continue

            # if not validate_solution(s, qid):
            #     return

            # Process the solution based on its type
            # json_data['solution'].append(render_solution(s))#
            # Todo: add render
            json_data["solution"].append(s)

    elif data_type == 2:
        # Single choice
        print(solution)
        print(type(solution))
        if not solution[0]["value"]:
            errorMsg("单选题答案为空")
            return

        json_data["option"] = LatexRender.html_render(content["answer"])
        json_data["solution"] = solution[0]["value"]

    elif data_type == 3:
        # Multiple choice
        if not solution[0]["value"]:
            errorMsg("多选题答案为空")
            return

        json_data["option"] = LatexRender.html_render(content["answer"])
        json_data["solution"] = solution[0]["value"]

    elif data_type == 4:
        # Custom question type handling
        qq = {
            "type": data_type,
            "content": content,
            "solution": solution,
            "explains": explains,
        }

        splits = ttl_question_show_answer(qq)

        if solution and splits is False:
            print(f"json data is {json_data}")
            errorMsg("答案拆分失败, c_b_type")
            return

        # json_data['solution'] = process_splits_solution(splits)

        # Todo: add render
        json_data["solution"] = splits

    else:
        errorMsg("题目type错误")
        return

    invalid = ["略", "详见答案"]
    try:
        ss = explains.get("解答设置")
    except:
        print("Ex is ", explains)
    if explains.get("解答设置") == "same":
        json_data["explain"] = ""
    else:
        jieda = explains.get("解答")
        if jieda:
            jieda = jieda.strip() if isinstance(jieda, str) else jieda
            if isinstance(jieda, str) and jieda in invalid:
                json_data["explain"] = ""
            else:
                # 假设 LatexRender.to_html 是一个已定义的函数，用来转换 LaTeX 字符串为 HTML
                json_data["explain"] = LatexRender.html_render(jieda)
        else:
            json_data["explain"] = ""

    return json_data


def errorMsg(msg, qid=1):
    print(f"Error in question {qid}: {msg}")


def get_answer_index(caption):
    if isinstance(caption, dict):
        index = []
        if "index" in caption and "type" in caption:
            index.append(caption)
        else:
            for key, value in caption.items():
                if isinstance(value, dict) and "index" in value and "type" in value:
                    index.append(value)
                elif isinstance(value, (dict, list)):
                    temp = get_answer_index(value)
                    if temp:
                        index.extend(temp)
        return index

    elif isinstance(caption, list):
        index = []
        for item in caption:
            if isinstance(item, dict) and "index" in item and "type" in item:
                index.append(item)
            elif isinstance(item, (dict, list)):
                temp = get_answer_index(item)
                if temp:
                    index.extend(temp)
        return index


def ttl_question_show_answer(question, q_type=1, mode=0):
    if question["type"] != 4:
        return False

    splits = split_question(
        question["type"],
        question["content"],
        question["solution"],
        question["explains"],
        True,
        mode,
    )
    if splits is False:
        return False

    return splits


def split_question(q_type, content, solution, explains, flag, mode):
    # Implementation of split_question method
    pass


def c_by_type_new(data: dict):
    data_id = data.get("id")
    data_type = data.get("type")
    solution = transfer_to_dict(data.get("solution", ""))
    print(f"solution is {solution}")
    if solution is None:
        print(data_id)
    content = transfer_to_dict(data.get("content"))
    explains = transfer_to_dict(data.get("explain"))

    knowledge_point = data.get("knowledge_point", None)
    difficulty = data.get("difficulty", None)
    answer = content.get("answer", None)
    # Check for empty solutions in certain question types
    if data_type in [1, 2, 3] and not solution:
        errorMsg("填空答案错误", data_id)
        return

    # Check for empty content in single and multiple choice questions
    if data_type in [2, 3] and ("answer" not in content or not answer):
        errorMsg("单选题干错误", data_id)
        return

    # Initialize the structure to store the processed data
    json_data = {"type": data_type, "solution": None, "caption": None, "id": data_id}

    json_data["caption"] = LatexRender.html_render(content["caption"])
    json_data["knowledge_point"] = knowledge_point
    json_data["difficulty"] = difficulty

    if data_type == 1:
        # Fill-in-the-blank
        answer_index = get_answer_index(content["caption"])
        answer_index_count = len(answer_index)

        json_data["solution"] = []
        for sk, s in enumerate(solution):
            if sk > (answer_index_count - 1):
                continue

            # if not validate_solution(s, qid):
            #     return

            # Process the solution based on its type
            # json_data['solution'].append(render_solution(s))#
            # Todo: add render
            json_data["solution"].append(s)

    elif data_type == 2:
        # Single choice
        if not solution[0]["value"]:
            errorMsg("单选题答案为空", data_id)
            return

        json_data["option"] = LatexRender.html_render(content["answer"])
        json_data["solution"] = solution[0]["value"]

    elif data_type == 3:
        # Multiple choice
        if not solution[0]["value"]:
            errorMsg("多选题答案为空", data_id)
            return

        json_data["option"] = LatexRender.html_render(content["answer"])
        json_data["solution"] = solution[0]["value"]

    elif data_type == 4:
        # Custom question type handling
        qq = {
            "type": data_type,
            "content": content,
            "solution": solution,
            "explains": explains,
        }

        splits = ttl_question_show_answer(qq)

        if solution and splits is False:
            errorMsg("答案拆分失败", data_id)
            return

        # json_data['solution'] = process_splits_solution(splits)

        # Todo: add render
        json_data["solution"] = splits

    else:
        errorMsg("题目type错误", data_id)
        return

    invalid = ["略", "详见答案"]

    if explains.get("解答设置") == "same":
        json_data["explain"] = ""
    else:
        jieda = explains.get("解答")
        if jieda:
            jieda = jieda.strip() if isinstance(jieda, str) else jieda
            if isinstance(jieda, str) and jieda in invalid:
                json_data["explain"] = ""
            else:
                # 假设 LatexRender.to_html 是一个已定义的函数，用来转换 LaTeX 字符串为 HTML
                json_data["explain"] = LatexRender.html_render(jieda)
        else:
            json_data["explain"] = ""

    return json_data
