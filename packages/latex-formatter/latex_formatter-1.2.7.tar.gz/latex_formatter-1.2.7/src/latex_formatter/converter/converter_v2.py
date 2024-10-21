import re


class LatexRenderV2:
    mode = 1
    _mode = 1
    _prefix = "\\("
    _suffix = "\\)"

    # _prefix = ""
    # _suffix = ""

    @staticmethod
    def is_final_object(obj):
        if isinstance(obj, dict):
            for key, val in obj.items():
                if isinstance(val, dict) or isinstance(val, list):
                    if "type" in val:
                        return False
                    if not LatexRenderV2.is_final_object(val):
                        return False
        elif isinstance(obj, list):
            print(f"obj is {obj}")
            for item in obj:
                print(f"item is {item}")
                if isinstance(item, dict) or isinstance(item, list):
                    print(f"is final function {item}")
                    if "type" in item:
                        return False
                    if not LatexRenderV2.is_final_object(item):
                        return False
        return True

    @staticmethod
    def to_old_version(obj):
        if isinstance(obj, dict):
            if "type" in obj:
                obj_type = obj["type"]
                if obj_type in ["merge", "equation", "latexarray"]:
                    nobjs = [LatexRenderV2.to_old_version(o) for o in obj["value"]]
                    obj["value"] = nobjs
                elif obj_type in ["select", "multiselect"]:
                    print(f"SELECT is {obj}")
                    nobjs = [LatexRenderV2.to_old_version(o) for o in obj["options"]]
                    obj["options"] = nobjs
                elif obj_type in ["table", "matrix", "grid"]:
                    for i in range(len(obj["value"])):
                        for j in range(len(obj["value"][i])):
                            obj["value"][i][j] = LatexRenderV2.to_old_version(
                                obj["value"][i][j]
                            )
                else:
                    for k in list(obj.keys()):
                        obj[k] = LatexRenderV2.to_old_version(obj[k])
                        # print(f"no type {obj[k]}")
                return obj
            else:
                # Handling non-type specific dict transformation
                nobjs = {}
                is_array = True
                for k, v in obj.items():
                    if not isinstance(k, int):
                        is_array = False
                    nobjs[k] = LatexRenderV2.to_old_version(v)
                if is_array:
                    return {"type": "merge", "value": list(nobjs.values())}
                return nobjs
        elif isinstance(obj, list):
            return [LatexRenderV2.to_old_version(o) for o in obj]
        else:
            return obj

    @staticmethod
    def html_render(obj):
        dict_type = "string"
        index = -1
        input_type = ""
        # print(f"obj is {obj}")
        obj = LatexRenderV2.to_old_version(
            obj
        )  # Assume this method adjusts the object to a previous format
        # print(f"ddd")
        # print(f"obj is {obj}")
        if not obj:
            return ""

        stack = [obj]
        while stack:
            print(f"stack is {stack}")
            current_obj = stack.pop()

            if LatexRenderV2.is_final_object(current_obj):
                print(f"final obj is {current_obj}")

                if isinstance(current_obj, list):
                    current_obj = "".join(str(item) for item in current_obj)

                # try:
                #     index = current_obj.get("index", -1)
                #     print(f"index is {index}")
                # except Exception as e:
                #     print(f"error in index {e}")

                # try:
                #     dict_type = current_obj.get("type", "string")
                # except Exception as e:
                #     print(f"error in dict type {e}, The final obj is {current_obj}")

                if isinstance(current_obj, dict):
                    dict_type = current_obj.get("type", "string")
                    if "index" in current_obj:
                        index = current_obj["index"]
                    if "input_type" in current_obj:
                        input_type = current_obj["input_type"]
                    if current_obj.get("type", "") == "fraction" and index != -1:
                        input_type = "fraction"
                        dict_type = "text"
                    if index == -1:
                        dict_type = "string"
                print(f"obj type is {current_obj.get('type')}")
                print(f"berore return")
                print(f"current_obj is {current_obj}")
                print(f"Input type is {input_type}")
                # current_obj = LatexRenderV2.render(current_obj)
                return (
                    LatexRenderV2.render(current_obj),
                    dict_type,
                    index,
                    input_type,
                )

            if isinstance(current_obj, dict):
                for key, val in current_obj.items():
                    if isinstance(val, dict) or isinstance(val, list):
                        if LatexRenderV2.is_final_object(val):
                            if "type" in val:
                                print(f"type is {val}")
                                print(f"list current_obj is {current_obj}")
                                dict_type = val["type"]
                                current_obj[key] = LatexRenderV2.render(val)
                                if "index" in val:
                                    index = val["index"]

                                    # current_obj["index"] = index
                        else:
                            print(f"val is {val}")
                            stack.append(val)
            elif isinstance(current_obj, list):
                for i, item in enumerate(current_obj):
                    if isinstance(item, dict) or isinstance(item, list):
                        if LatexRenderV2.is_final_object(item):
                            if "type" in item:
                                print(f"current_obj is {current_obj}")
                                print(f"type2 is {item}")
                                current_obj[i] = LatexRenderV2.render(item)
                                dict_type = item["type"]
                            if "index" in item:
                                index = item["index"]
                        else:
                            print(f"item is {item}")
                            stack.append(item)

        print(f"re obj is {obj}")
        # print(f"re cucurrent_obj is {current_obj}")
        print(f"dict type is {dict_type}")
        if obj.get("type", "") == "fraction" and dict_type == "text":
            input_type = "fraction"
        try:
            dict_type = obj.get("type", "")
        except Exception as e:
            print(f"error in input type {e}")
        st1 = LatexRenderV2.html_render(obj), dict_type, index, input_type
        print(f"st1 is {st1}")
        return st1

    @staticmethod
    def star_render(items):
        result = []
        print(f"items is {items}")
        for item in items:
            if isinstance(item, dict):
                print(f" star item is {item}")
                rendered_values = LatexRenderV2.html_render(item)
                print(f"rendered_values is {rendered_values}")
                if len(rendered_values) == 4:
                    value, value_type, index, input_type = rendered_values
                    updated_item = {
                        **item,  # Copy existing item properties
                        "value": value,
                        "type": value_type,
                        "index": index,
                        "input_type": input_type,
                    }
                    print(f"updat is {updated_item}")
                    result.append(updated_item)
                else:
                    raise ValueError(
                        "LatexRenderV2.html_render did not return 4 elements."
                    )
            else:
                print(f"in item is {item}")
                item_dict = {"type": "string", "value": item}
                rendered_values = LatexRenderV2.html_render(item_dict)
                if len(rendered_values) == 4:
                    value, value_type, index, input_type = rendered_values
                    updated_item = {
                        **item_dict,  # Copy existing item properties
                        "value": value,
                        "type": value_type,
                        "index": index,
                        "input_type": input_type,
                    }
                    result.append(updated_item)
                # raise TypeError("Each item must be a dictionary.")

        for item in result:
            if type(item["value"]) == tuple:
                item["value"] = item["value"][0]

        return result

    @staticmethod
    def latex(str_val):
        print(f"str val is {str_val}")
        if str_val is None:
            return ""
        if isinstance(str_val, int):
            return str(str_val)
        if isinstance(str_val, list):
            str_val = " ".join(str(item) for item in str_val)

        print(f"start replace")

        replacements = {
            "（": "(",
            "）": ")",
            "√": "✓",
            "u3000": " ",
            # "%": "\\%",
            # "^": "\\^",
            # "#": "\\#",
            # "|": "\\|",
            "[br]": "",
            "[BR]": "",
            "≈": LatexRenderV2._prefix + "\\approx " + LatexRenderV2._suffix,
            "≠": LatexRenderV2._prefix + "\\ne " + LatexRenderV2._suffix,
            "≌": LatexRenderV2._prefix + "\\cong " + LatexRenderV2._suffix,
            "⊕": LatexRenderV2._prefix + "\\oplus " + LatexRenderV2._suffix,
            "⊗": LatexRenderV2._prefix + "\\otimes " + LatexRenderV2._suffix,
            "⇒": LatexRenderV2._prefix + "\\Rightarrow " + LatexRenderV2._suffix,
            "⇔": LatexRenderV2._prefix + "\\Leftrightarrow " + LatexRenderV2._suffix,
            "⊥": LatexRenderV2._prefix + "\\bot " + LatexRenderV2._suffix,
            "∥": LatexRenderV2._prefix + "\\parallel " + LatexRenderV2._suffix,
            "ε": LatexRenderV2._prefix + "\\varepsilon " + LatexRenderV2._suffix,
            "△": LatexRenderV2._prefix + "\\triangle " + LatexRenderV2._suffix,
            # "×": LatexRenderV2._prefix + "\\times " + LatexRenderV2._suffix,
            # "÷": LatexRenderV2._prefix + "\\div " + LatexRenderV2._suffix,
            "°": LatexRenderV2._prefix + "{\\circ }" + LatexRenderV2._suffix,
            "≤": LatexRenderV2._prefix + "\\le " + LatexRenderV2._suffix,
            "≥": LatexRenderV2._prefix + "\\ge " + LatexRenderV2._suffix,
            "∠": LatexRenderV2._prefix + "\\angle " + LatexRenderV2._suffix,
            "•": LatexRenderV2._prefix + "\\centerdot " + LatexRenderV2._suffix,
            "π": LatexRenderV2._prefix + "\\pi " + LatexRenderV2._suffix,
            "Ω": LatexRenderV2._prefix + "\\Omega " + LatexRenderV2._suffix,
            "ω": LatexRenderV2._prefix + "\\omega " + LatexRenderV2._suffix,
            "ρ": LatexRenderV2._prefix + "\\rho " + LatexRenderV2._suffix,
            "θ": LatexRenderV2._prefix + "\\theta " + LatexRenderV2._suffix,
            "±": LatexRenderV2._prefix + "\\pm " + LatexRenderV2._suffix,
            "…": LatexRenderV2._prefix + "\\cdots " + LatexRenderV2._suffix,
            "α": LatexRenderV2._prefix + "\\alpha " + LatexRenderV2._suffix,
            "β": LatexRenderV2._prefix + "\\beta " + LatexRenderV2._suffix,
            "φ": LatexRenderV2._prefix + "\\phi " + LatexRenderV2._suffix,
            "μ": LatexRenderV2._prefix + "\\mu " + LatexRenderV2._suffix,
            "∈": LatexRenderV2._prefix + "\\in " + LatexRenderV2._suffix,
            "∉": LatexRenderV2._prefix + "\\notin " + LatexRenderV2._suffix,
            "∅": LatexRenderV2._prefix + "\\varnothing " + LatexRenderV2._suffix,
            "&nbsp;": LatexRenderV2._prefix + "\\quad " + LatexRenderV2._suffix,
            "′": LatexRenderV2._prefix + "' " + LatexRenderV2._suffix,
            "→": LatexRenderV2._prefix + "\\to " + LatexRenderV2._suffix,
            "∞": LatexRenderV2._prefix + "\\infty " + LatexRenderV2._suffix,
            "∫": LatexRenderV2._prefix + "\\int\\limits " + LatexRenderV2._suffix,
            "λ": LatexRenderV2._prefix + "\\lambda " + LatexRenderV2._suffix,
            "⫋": LatexRenderV2._prefix + "\\subsetneqq " + LatexRenderV2._suffix,
            "⫌": LatexRenderV2._prefix + "\\supsetneqq " + LatexRenderV2._suffix,
            "⫅": LatexRenderV2._prefix + "\\subseteqq " + LatexRenderV2._suffix,
            "⫆": LatexRenderV2._prefix + "\\supseteqq " + LatexRenderV2._suffix,
            "∁": LatexRenderV2._prefix + "\\complement " + LatexRenderV2._suffix,
            "δ": LatexRenderV2._prefix + "\\delta " + LatexRenderV2._suffix,
            "ξ": LatexRenderV2._prefix + "\\xi " + LatexRenderV2._suffix,
            "σ": LatexRenderV2._prefix + "\\sigma " + LatexRenderV2._suffix,
            "⊃": LatexRenderV2._prefix + "\\supset " + LatexRenderV2._suffix,
            "⊂": LatexRenderV2._prefix + "\\subset " + LatexRenderV2._suffix,
            "∩": LatexRenderV2._prefix + "\\cap " + LatexRenderV2._suffix,
            "∪": LatexRenderV2._prefix + "\\cup " + LatexRenderV2._suffix,
            "丨": "|",
            "．": ".",
            "＝": "=",
        }
        try:
            for key, value in replacements.items():
                if "（" in str_val:
                    print("key is ", key)
                str_val = str_val.replace(key, value)
            print(f"str is {str_val}")
            return str_val
        except Exception as e:
            print(f"error in latex {str_val}")
            return str_val

    @staticmethod
    def latex2(str_val):
        try:
            return str_val
            # return str_val.replace("\\(", "").replace("\\)", "")
        except Exception as e:
            print(f"error in latex2 {str_val}")
            return str_val

    @staticmethod
    def render(obj):
        # print(f"start render")

        if isinstance(obj, dict) and "type" in obj and obj["type"]:
            html = ""
            obj_type = obj["type"].lower()
            if obj_type == "string" or obj_type == "integer":
                print(f"objj is {obj}")
                if isinstance(obj.get("value", None), list):
                    print(f"get list ")
                    print(f"str obj is {obj}")
                    # if len(obj.get("value", 0)) == 3:
                    #     html = obj["value"][2]
                    # numerator = LatexRenderV2.latex2(
                    #     LatexRenderV2.latex(obj["value"][0])
                    # )
                    # print(f"ffffffffffffffffffffffffffffffffffffffffff")
                    # denominator = LatexRenderV2.latex2(
                    #     LatexRenderV2.latex(obj["value"][1])
                    # )
                    # html += (
                    #     LatexRenderV2._prefix
                    #     + f"\\frac{{{numerator}}}{{{denominator}}}"
                    #     + LatexRenderV2._suffix
                    # )
                    # print(f"html is {html}")

                    html = LatexRenderV2.latex2(
                        LatexRenderV2.latex(obj.get("value", ""))
                    )
                else:
                    print(f"html is {html}")
                    print(f"sssssssssssssssssssss")
                    html = LatexRenderV2.latex2(
                        LatexRenderV2.latex(obj.get("value", ""))
                    )
                    print(f"html4 is {html}")
                print(f"html5 is {html}")
                html = re.sub(r"\[br\]", "\n", html, flags=re.IGNORECASE)
                # 看起来丢了很多
                print(f"html 2 is {html}")

            elif obj_type == "merge":
                # print(f"obj value is {obj['value']}")
                for item in obj["value"]:
                    print(f"merge item is {item}")
                    print(f"type is {type(item)}")
                    if isinstance(item, str):
                        html += item
                    else:
                        ht = LatexRenderV2.html_render(item)
                        print(f"ht is {ht}")
                        print(f"html is {html}")
                        html += LatexRenderV2.html_render(item)
                    print(f"merge html is {html}")

            elif obj_type in ["richtext"]:
                if isinstance(obj["value"], list):
                    # print(f"obj value is {obj['value']}")
                    html = "".join(obj["value"])
                else:
                    html = obj["value"]
                html = re.sub(r"\[br\]", "\n", html, flags=re.IGNORECASE)

            elif obj_type == "latexarray":
                align = "l" * len(obj["value"])
                html = "\\begin{array}{" + align + "} "
                for equation in obj["value"]:
                    print(f"before equ is {equation}")
                    print(f"equa type is {type(equation)}")
                    if isinstance(equation, list):
                        equation = " ".join(str(item) for item in equation[0])
                    print(f"EQUation is {equation}")
                    html += (
                        LatexRenderV2.latex2(LatexRenderV2.latex(equation)) + " \\\\ "
                    )
                print(f"html is {html}")
                html += " \\end{array}"

            elif obj_type == "latexwrap":
                html = LatexRenderV2._prefix
                left_delimiter = obj["left"]
                right_delimiter = obj.get("right", "}")
                if right_delimiter == "":
                    right_delimiter = "}"
                print(f"latex value is {obj['value']}")
                value = LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                html += f"\\left\\{left_delimiter} {value} \\right\\{right_delimiter}"
                html += LatexRenderV2._suffix

            elif obj_type == "unit":
                html = LatexRenderV2._prefix
                html += (
                    # "\\mathrm{"
                    +LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    # + "}"
                )
                html += LatexRenderV2._suffix

            elif obj_type == "img":
                object_img = (
                    obj["value"]["src"]
                    if obj["value"]["src"].startswith("http")
                    else "http://www.leleketang.com" + obj["value"]["src"]
                )
                html = f'<img src="{object_img}" '
                if "style" in obj["value"]:
                    html += f' style="{obj["value"]["style"]}" '
                if "width" in obj["value"]:
                    html += f' width="{obj["value"]["width"]}" '
                if "height" in obj["value"]:
                    html += f' height="{obj["value"]["height"]}" '
                html += "/>"

            elif obj_type == "text":
                value = "______"
                new_line_flg = obj.get("wordwrap")
                if new_line_flg:
                    html = "\\newline ".join(value.split("\n"))
                if not obj.get("noautowidth"):
                    html = "\\Box"

                else:
                    html = "\\Box"

                html = LatexRenderV2._prefix + html + LatexRenderV2._suffix
                # html = "______"
            elif obj_type == "fraction":
                print(f"frace obj is {obj}")
                if "index" in obj:
                    print(f"obj is {obj}")
                    html = "\\Box"
                else:
                    value = obj.get("value")
                    if isinstance(value, list):
                        numerator = value[0]
                        denominator = value[1]
                        if len(value) == 2:
                            html = (
                                LatexRenderV2._prefix
                                + f"\\frac{{{numerator}}}{{{denominator}}}"
                                + LatexRenderV2._suffix
                            )
                        else:
                            number = value[2]
                            html = (
                                LatexRenderV2._prefix
                                + f"{number}\\frac{{{numerator}}}{{{denominator}}}"
                                + LatexRenderV2._suffix
                            )
                    else:
                        if (
                            not value
                            or not value.get("numerator")
                            or not value.get("denominator")
                        ):
                            html = "\\Box"

                        numerator = obj.get("value").get("numerator")
                        print(f"this ss")
                        if not isinstance(numerator, str):
                            print(f"numerator is {numerator}")
                            numerator = LatexRenderV2.render(numerator)
                        denominator = obj.get("value").get("denominator")
                        if not isinstance(denominator, str):
                            print(f"denominator is {denominator}")
                            denominator = LatexRenderV2.render(denominator)

                        if "integer" in obj["value"]:
                            html = obj["value"]["integer"]
                        print(f"numerator is {numerator}")
                        numerator = LatexRenderV2.latex2(LatexRenderV2.latex(numerator))
                        denominator = LatexRenderV2.latex2(
                            LatexRenderV2.latex(denominator)
                        )
                        html += (
                            LatexRenderV2._prefix
                            + f"\\frac{{{numerator}}}{{{denominator}}}"
                            + LatexRenderV2._suffix
                        )
                    # print(f"prefix is {LatexRenderV2._prefix}")
                    # print(f"html is {html}")

            elif obj_type == "arc":
                html = (
                    LatexRenderV2._prefix
                    + f'\\overset\\frown{{{LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))}}}'
                    + LatexRenderV2._suffix
                )

            elif obj_type == "underline":
                html = (
                    LatexRenderV2._prefix
                    + f'\\underline{{{LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))}}}'
                    + LatexRenderV2._suffix
                )

            elif obj_type in ["equation", "equations"]:
                print(f"que", obj)
                direction = obj.get("direction", "left")
                html += LatexRenderV2._prefix
                if direction == "left":
                    html += "\\left\\{"
                    html += "\\begin{matrix}"
                    for equation in obj["value"]:
                        print(f"equation is {equation}")
                        if isinstance(equation, list):
                            equation = " ".join(str(item) for item in equation)
                        html += (
                            LatexRenderV2.latex2(LatexRenderV2.latex(equation))
                            + " \\\\ "
                        )
                    html += " \\end{matrix}\\right."
                elif direction == "right":
                    html += "\\left."
                    html += "\\begin{matrix}"
                    for equation in obj["value"]:
                        html += (
                            LatexRenderV2.latex2(LatexRenderV2.latex(equation))
                            + " \\\\ "
                        )
                    html += " \\end{matrix}\\right\\}"
                else:
                    print(f"eeee")
                    html += "\\begin{Bmatrix}"
                    for equation in obj["value"]:
                        print(f"equation is {equation}")
                        html += (
                            LatexRenderV2.latex2(LatexRenderV2.latex(equation))
                            + " \\\\ "
                        )
                    html += " \\end{Bmatrix}"
                html += LatexRenderV2._suffix

            elif obj_type in ["script", "pc"]:
                html += LatexRenderV2._prefix
                if "front" in obj["value"] and obj["value"]["front"]:
                    html += LatexRenderV2.latex2(
                        LatexRenderV2.latex(obj["value"]["front"])
                    )
                if "sub" in obj["value"]:
                    str_val = re.sub(r"(&nbsp;|\[br\])", "", obj["value"]["sub"])
                    if str_val:
                        html += (
                            "_{"
                            + LatexRenderV2.latex2(LatexRenderV2.latex(str_val))
                            + "}"
                        )
                if "sup" in obj["value"]:
                    if isinstance(obj["value"]["sup"], list):
                        value = "".join(str(item) for item in obj["value"]["sup"])
                        str_val = re.sub(r"(&nbsp;|\[br\])", "", value)
                    else:
                        str_val = re.sub(r"(&nbsp;|\[br\])", "", obj["value"]["sup"])
                    if str_val:
                        html += (
                            "^{"
                            + LatexRenderV2.latex2(LatexRenderV2.latex(str_val))
                            + "}"
                        )
                html += LatexRenderV2._suffix

            elif obj_type == "root":
                html += LatexRenderV2._prefix + "\\sqrt"
                print(f"ROOT is {obj}")
                if "index" in obj["value"] and obj["value"]["index"]:
                    html += "[" + obj["value"]["index"] + "]"

                html += (
                    "{"
                    + LatexRenderV2.latex2(
                        LatexRenderV2.latex(obj["value"]["radicand"])
                    )
                    + "}"
                )
                html += LatexRenderV2._suffix
            elif obj_type in ["select", "multiselect"]:
                print("select")
                options = obj["options"]
                print(f"options is {options}")
                # if isinstance(options, list):
                #     options = "".join(str(item) for item in options)
                html = options

            elif obj_type == "repeating":
                html += LatexRenderV2._prefix
                html += LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["pre"]))
                repeater = obj["value"]["repeater"]
                html += "\\dot{" + repeater[0] + "}"
                if len(repeater) > 1:
                    html += repeater[1:-1]
                    html += "\\dot{" + repeater[-1] + "}"
                html += LatexRenderV2._suffix

            elif obj_type == "table":
                if LatexRenderV2._mode == 1:
                    html = '<table border="1" style="border-collapse:collapse"><tbody>'
                    for row in obj["value"]:
                        html += "<tr>"
                        for cell in row:
                            colspan = cell.get("colspan", 1)
                            rowspan = cell.get("rowspan", 1)
                            cell_value = cell["value"] if "value" in cell else ""
                            if isinstance(cell_value, list):
                                cell_html = LatexRenderV2.html_render(cell_value)
                            elif isinstance(cell_value, dict):
                                print(f"before render is{cell_value}")
                                cell_html = LatexRenderV2.render(cell_value)
                                print(f"Dict Cell is {cell_html}")
                            else:
                                print(f"Cell is {cell_value}")
                                cell_html = cell_value.replace("", "\\n")
                            html += f'<td colspan="{colspan}" rowspan="{rowspan}">{cell_html}</td>'
                        html += "</tr>"
                    html += "</tbody></table>"
                elif LatexRenderV2._mode == 2:
                    html = LatexRenderV2._prefix + "\\begin{table}[!ht] \\centering"
                    td_len = len(obj["value"][0])
                    td_align_type = "|" + "l|" * td_len
                    html += f"\\begin{{tabular}}{{{td_align_type}}} \\hline"
                    for row in obj["value"]:
                        arr = []
                        for cell in row:
                            colspan = cell.get("colspan", 1)
                            rowspan = cell.get("rowspan", 1)
                            cell_value = (
                                LatexRenderV2.html_render(cell["value"])
                                if isinstance(cell["value"], list)
                                else cell["value"].replace("[br]", "")
                            )
                            if colspan > 1:
                                arr.append(
                                    f"\\multicolumn{{{colspan}}}{{l}}{{{cell_value}}}"
                                )
                            elif rowspan > 1:
                                arr.append(
                                    f"\\multirow{{{rowspan}}}{{*}}{{{cell_value}}}"
                                )
                            else:
                                arr.append(cell_value)
                        html += " & ".join(arr) + " \\\\ \\hline"
                    html += "\\end{tabular} \\end{table}" + LatexRenderV2._suffix

            elif obj_type == "vector":
                html = (
                    LatexRenderV2._prefix
                    + "\\vec{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    + "}"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "arrow":
                direction = obj["value"].get("direction", "right")
                html = LatexRenderV2._prefix
                if direction == "right":
                    html += "\\xrightarrow"
                else:
                    html += "\\xleftarrow"
                if obj["value"].get("bottom"):
                    html += (
                        "["
                        + LatexRenderV2.latex2(
                            LatexRenderV2.latex(obj["value"]["bottom"])
                        )
                        + "]"
                    )
                if obj["value"].get("top"):
                    html += (
                        "{"
                        + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["top"]))
                        + "}"
                    )
                html += LatexRenderV2._suffix

            elif obj_type == "parallelequal":
                html = (
                    LatexRenderV2._prefix
                    + "\\underline{\\underline{\\parallel}}"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "underbrace":
                html = LatexRenderV2._prefix + "\\underbrace{"
                html += LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["top"]))
                html += (
                    "}_{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["bottom"]))
                    + "}"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "valence":
                # html = LatexRenderV2._prefix + "\\overset{"
                html = LatexRenderV2._prefix
                top_val = obj["value"]["top"]
                if isinstance(top_val, str) and top_val.startswith("_"):
                    html += "\\_"
                else:
                    html += LatexRenderV2.latex2(LatexRenderV2.latex(top_val))
                html += (
                    # "}{\\mathop{"
                    +LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["bottom"]))
                    # + "}}\\,"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "overline":
                html = (
                    LatexRenderV2._prefix
                    + "\\overline{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    + "}"
                    + LatexRenderV2._suffix
                )
            elif obj_type == "matrix":
                real = obj.get("real", "")
                if real == 1:
                    html += LatexRenderV2._prefix + "\\left( \\begin{matrix}"
                    for value in obj["value"]:
                        html += (
                            LatexRenderV2.latex2(LatexRenderV2.latex(" & ".join(value)))
                            + " \\\\ "
                        )
                    html += "\\end{matrix} \\right)" + LatexRenderV2._suffix
                else:
                    html += LatexRenderV2._prefix + "\\left| \\begin{matrix}"
                    for value in obj["value"]:
                        html += (
                            LatexRenderV2.latex2(LatexRenderV2.latex(" & ".join(value)))
                            + " \\\\ "
                        )
                    html += "\\end{matrix} \\right|" + LatexRenderV2._suffix

            elif obj_type == "chemequation":
                top = obj["value"].get("top", "")
                bottom = obj["value"].get("bottom", "")
                html += (
                    LatexRenderV2._prefix
                    + "\\underset{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(bottom))
                    + "}{\\overset{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(top))
                    + "}{\\rightleftharpoons}}"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "equalmark":
                top = obj["value"].get("top", "")
                bottom = obj["value"].get("bottom", "")
                html += LatexRenderV2._prefix + "\\begin{matrix}"
                html += (
                    "\\underline{\\underline{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(top))
                    + "}} \\\\"
                )
                html += LatexRenderV2.latex2(LatexRenderV2.latex(bottom)) + " \\\\"
                html += "\\end{matrix}" + LatexRenderV2._suffix

            elif obj_type == "sum":
                html += LatexRenderV2._prefix + "\\sum\\limits_{"
                html += (
                    LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["lower"]))
                    + "}^{"
                )
                html += (
                    LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["upper"]))
                    + "}{"
                )
                html += (
                    LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["variable"]))
                    + "}"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "limit":
                # html += LatexRenderV2._prefix + "\\underset{"
                html += LatexRenderV2._prefix
                html += (
                    LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["lower"]))
                    # + "}{\\mathop{\\lim }}\\,"
                    + "{\\lim }\\,"
                )
                html += (
                    LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]["function"]))
                    + LatexRenderV2._suffix
                )

            elif obj_type == "italic":
                html += (
                    LatexRenderV2._prefix
                    # + "\\textit{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    # + "}"
                    + LatexRenderV2._suffix
                )

            elif obj_type == "bold":
                html += (
                    LatexRenderV2._prefix
                    + "\\textbf{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    + "}"
                    + LatexRenderV2._suffix
                )

            elif obj_type in ["wave", "font"]:
                html = obj["value"]

            elif obj_type in [
                "colorred",
                "colorpeach",
                "colorblue",
                "colorskyblue",
                "colorwhite",
                "coloryellow",
                "coloryellow2",
                "colororange",
                "colorgreen",
                "colorgreen2",
                "colorpurple",
                "colorpurple2",
                "colorcyan",
                "colorjujubered",
                "colorochre",
                "colorblack",
                "fontsize40",
                "fontsize32",
                "fontsize30",
                "fontsize24",
                "fontsize16",
                "fontsize18",
                "fontsize54",
                "fontsize12",
                "fyouyuan",
                "fwryh",
                "fabc",
                "farial",
                "ffzzy",
                "ffzcy",
                "fshsregular",
                "fshsmedium",
                "fshsbold",
                "flelehand",
                "fhtsc",
                "formula",
                "bookname",
                "strike",
            ]:
                html = obj["value"]

            elif obj_type == "repeating":
                repeater = obj["value"]["repeater"]
                len_repeater = len(repeater)
                html += LatexRenderV2._prefix
                if len_repeater > 1:
                    html += (
                        "\\dot{"
                        + repeater[0]
                        + "}"
                        + repeater[1 : len_repeater - 1]
                        + "\\dot{"
                        + repeater[-1]
                        + "}"
                    )
                elif len_repeater == 1:
                    html += "\\dot{" + repeater + "}"
                html += LatexRenderV2._suffix

            elif obj_type == "repeater":
                html += (
                    LatexRenderV2._prefix
                    + "\\dot{"
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    + "}"
                    + LatexRenderV2._suffix
                )

            elif obj_type in ["textcenter", "textright", "textindent"]:
                html += (
                    LatexRenderV2._prefix
                    + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                    + LatexRenderV2._suffix
                )

            elif obj_type == "emphasis":
                if obj["value"]:
                    html += (
                        LatexRenderV2._prefix
                        + LatexRenderV2.latex2(LatexRenderV2.latex(obj["value"]))
                        + LatexRenderV2._suffix
                    )
                else:
                    html = ""
            elif obj_type == "numeric":
                html = obj["value"]

            elif obj_type == "integer":
                html = obj["value"]
            else:
                html = '<span style="color:red">格式错误' + obj["type"] + "</span>"

            # Continue handling all cases as structured in your PHP code.
            # More cases should be implemented here following the same pattern.

            return html

        elif isinstance(obj, str):
            return re.sub(r"", "\n", obj, flags=re.IGNORECASE)
            # return re.sub(r"\[br\]", "\n", obj, flags=re.IGNORECASE)
        elif isinstance(obj, int):
            return str(obj)
        elif isinstance(obj, list):
            return "".join(str(item) for item in obj)
        else:
            # print(f"Invalid input format: {obj}, {type(obj)}")
            return "Invalid input format"
