import re


class LatexRender:
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
                    if not LatexRender.is_final_object(val):
                        return False
        elif isinstance(obj, list):
            for item in obj:
                print(f"obj is {item}")
                if isinstance(item, dict) or isinstance(item, list):
                    if not LatexRender.is_final_object(item):
                        return False
        print(f"end")
        return True

    @staticmethod
    def to_old_version(obj):
        if isinstance(obj, dict):
            if "type" in obj:
                obj_type = obj["type"]
                if obj_type in ["merge", "equation", "latexarray"]:
                    nobjs = [LatexRender.to_old_version(o) for o in obj["value"]]
                    obj["value"] = nobjs
                elif obj_type in ["select", "multiselect"]:
                    nobjs = [LatexRender.to_old_version(o) for o in obj["options"]]
                    obj["options"] = nobjs
                elif obj_type in ["table", "matrix", "grid"]:
                    for i in range(len(obj["value"])):
                        for j in range(len(obj["value"][i])):
                            obj["value"][i][j] = LatexRender.to_old_version(
                                obj["value"][i][j]
                            )
                else:
                    for k in list(obj.keys()):
                        obj[k] = LatexRender.to_old_version(obj[k])
                        # print(f"no type {obj[k]}")
                return obj
            else:
                # Handling non-type specific dict transformation
                nobjs = {}
                is_array = True
                for k, v in obj.items():
                    if not isinstance(k, int):
                        is_array = False
                    nobjs[k] = LatexRender.to_old_version(v)
                if is_array:
                    return {"type": "merge", "value": list(nobjs.values())}
                return nobjs
        elif isinstance(obj, list):
            return [LatexRender.to_old_version(o) for o in obj]
        else:
            return obj

    @staticmethod
    def html_render(obj):
        # print(f"obj is {obj}")
        obj = LatexRender.to_old_version(
            obj
        )  # Assume this method adjusts the object to a previous format
        # print(f"ddd")
        # print(f"obj is {obj}")
        if not obj:
            return ""

        stack = [obj]
        while stack:
            print(f"start stack is {stack}")
            current_obj = stack.pop()

            if LatexRender.is_final_object(current_obj):
                print(f"is final object")
                return LatexRender.render(current_obj)

            if isinstance(current_obj, dict):
                for key, val in current_obj.items():
                    if isinstance(val, dict) or isinstance(val, list):
                        if LatexRender.is_final_object(val):
                            if "type" in val:
                                current_obj[key] = LatexRender.render(val)
                        else:
                            stack.append(val)
            elif isinstance(current_obj, list):
                print(f"this is list")
                for i, item in enumerate(current_obj):
                    if isinstance(item, dict) or isinstance(item, list):
                        if LatexRender.is_final_object(item):
                            if "type" in item:
                                current_obj[i] = LatexRender.render(item)
                        else:
                            stack.append(item)

        return LatexRender.render(obj)

    @staticmethod
    def latex(str_val):
        if isinstance(str_val, int):
            return str(str_val)

        replacements = {
            "（": "(",
            "）": ")",
            "%": "\\%",
            "^": "\\^",
            "#": "\\#",
            "|": "\\|",
            "[br]": "\\\\",
            "≈": LatexRender._prefix + "\\approx " + LatexRender._suffix,
            "≠": LatexRender._prefix + "\\ne " + LatexRender._suffix,
            "≌": LatexRender._prefix + "\\cong " + LatexRender._suffix,
            "⊕": LatexRender._prefix + "\\oplus " + LatexRender._suffix,
            "⊗": LatexRender._prefix + "\\otimes " + LatexRender._suffix,
            "⇒": LatexRender._prefix + "\\Rightarrow " + LatexRender._suffix,
            "⇔": LatexRender._prefix + "\\Leftrightarrow " + LatexRender._suffix,
            "⊥": LatexRender._prefix + "\\bot " + LatexRender._suffix,
            "∥": LatexRender._prefix + "\\parallel " + LatexRender._suffix,
            "ε": LatexRender._prefix + "\\varepsilon " + LatexRender._suffix,
            "△": LatexRender._prefix + "\\triangle " + LatexRender._suffix,
            "×": LatexRender._prefix + "\\times " + LatexRender._suffix,
            "÷": LatexRender._prefix + "\\div " + LatexRender._suffix,
            "°": LatexRender._prefix + "{\\circ }" + LatexRender._suffix,
            "≤": LatexRender._prefix + "\\le " + LatexRender._suffix,
            "≥": LatexRender._prefix + "\\ge " + LatexRender._suffix,
            "∠": LatexRender._prefix + "\\angle " + LatexRender._suffix,
            "•": LatexRender._prefix + "\\centerdot " + LatexRender._suffix,
            "π": LatexRender._prefix + "\\pi " + LatexRender._suffix,
            "Ω": LatexRender._prefix + "\\Omega " + LatexRender._suffix,
            "ω": LatexRender._prefix + "\\omega " + LatexRender._suffix,
            "ρ": LatexRender._prefix + "\\rho " + LatexRender._suffix,
            "θ": LatexRender._prefix + "\\theta " + LatexRender._suffix,
            "±": LatexRender._prefix + "\\pm " + LatexRender._suffix,
            "…": LatexRender._prefix + "\\cdots " + LatexRender._suffix,
            "α": LatexRender._prefix + "\\alpha " + LatexRender._suffix,
            "β": LatexRender._prefix + "\\beta " + LatexRender._suffix,
            "φ": LatexRender._prefix + "\\phi " + LatexRender._suffix,
            "μ": LatexRender._prefix + "\\mu " + LatexRender._suffix,
            "∈": LatexRender._prefix + "\\in " + LatexRender._suffix,
            "∉": LatexRender._prefix + "\\notin " + LatexRender._suffix,
            "∅": LatexRender._prefix + "\\varnothing " + LatexRender._suffix,
            "&nbsp;": LatexRender._prefix + "\\quad " + LatexRender._suffix,
            "′": LatexRender._prefix + "' " + LatexRender._suffix,
            "→": LatexRender._prefix + "\\to " + LatexRender._suffix,
            "∞": LatexRender._prefix + "\\infty " + LatexRender._suffix,
            "∫": LatexRender._prefix + "\\int\\limits " + LatexRender._suffix,
            "λ": LatexRender._prefix + "\\lambda " + LatexRender._suffix,
            "⫋": LatexRender._prefix + "\\subsetneqq " + LatexRender._suffix,
            "⫌": LatexRender._prefix + "\\supsetneqq " + LatexRender._suffix,
            "⫅": LatexRender._prefix + "\\subseteqq " + LatexRender._suffix,
            "⫆": LatexRender._prefix + "\\supseteqq " + LatexRender._suffix,
            "∁": LatexRender._prefix + "\\complement " + LatexRender._suffix,
            "δ": LatexRender._prefix + "\\delta " + LatexRender._suffix,
            "ξ": LatexRender._prefix + "\\xi " + LatexRender._suffix,
            "σ": LatexRender._prefix + "\\sigma " + LatexRender._suffix,
            "⊃": LatexRender._prefix + "\\supset " + LatexRender._suffix,
            "⊂": LatexRender._prefix + "\\subset " + LatexRender._suffix,
            "∩": LatexRender._prefix + "\\cap " + LatexRender._suffix,
            "∪": LatexRender._prefix + "\\cup " + LatexRender._suffix,
            "丨": "|",
            "．": ".",
            "＝": "=",
        }
        try:
            for key, value in replacements.items():
                str_val = str_val.replace(key, value)
            return str_val
        except Exception as e:
            print(f"error in latex {str_val}")
            return str_val

    @staticmethod
    def latex2(str_val):
        try:
            return str_val.replace("\\(", "").replace("\\)", "")
        except Exception as e:
            print(f"error in latex2 {str_val}")
            return str_val

    @staticmethod
    def render(obj):
        print(f"start render")

        if isinstance(obj, dict) and "type" in obj and obj["type"]:
            html = ""
            obj_type = obj["type"].lower()
            if obj_type == "string" or obj_type == "integer":
                if isinstance(obj["value"], list):
                    if len(obj["value"]) == 3:
                        html = obj["value"][2]
                    numerator = LatexRender.latex2(LatexRender.latex(obj["value"][0]))
                    denominator = LatexRender.latex2(LatexRender.latex(obj["value"][1]))
                    html += (
                        LatexRender._prefix
                        + f"\\frac{{{numerator}}}{{{denominator}}}"
                        + LatexRender._suffix
                    )
                    # print(f"html is {html}")
                else:
                    html = obj["value"]
                html = re.sub(r"\[br\]", "\n", html, flags=re.IGNORECASE)

            elif obj_type == "merge":
                # print(f"obj value is {obj['value']}")
                for item in obj["value"]:
                    html += LatexRender.html_render(item)

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
                    html += LatexRender.latex2(LatexRender.latex(equation)) + " \\\\ "
                html += " \\end{array}"

            elif obj_type == "latexwrap":
                html = LatexRender._prefix
                left_delimiter = obj["left"]
                right_delimiter = obj.get("right", ".")
                value = LatexRender.latex2(LatexRender.latex(obj["value"]))
                html += f"\\left\\{left_delimiter} {value} \\right{right_delimiter}"
                html += LatexRender._suffix

            elif obj_type == "unit":
                html = LatexRender._prefix
                html += (
                    "\\mathrm{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + "}"
                )
                html += LatexRender._suffix

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
                    html = "\\underline{\\hspace{" + "0.8" + "cm}}"

                else:
                    html = "\\underline" + "{4.8cm}"

                html = LatexRender._prefix + html + LatexRender._suffix
                # html = "______"
            elif obj_type == "fraction":
                if "index" in obj:
                    html = "____/____"
                else:
                    value = obj.get("value")
                    if (
                        not value
                        or not value.get("numerator")
                        or not value.get("denominator")
                    ):
                        html = "\\underline{\\hspace{1cm}} \\bigg/ \\underline{\\hspace{1cm}}"

                    numerator = obj.get("value").get("numerator")
                    if not isinstance(numerator, str):
                        numerator = LatexRender.html_render(numerator)
                    denominator = obj.get("value").get("denominator")
                    if not isinstance(denominator, str):
                        denominator = LatexRender.html_render(denominator)

                    if "integer" in obj["value"]:
                        html = obj["value"]["integer"]
                    numerator = LatexRender.latex2(LatexRender.latex(numerator))
                    denominator = LatexRender.latex2(LatexRender.latex(denominator))
                    html += (
                        LatexRender._prefix
                        + f"\\frac{{{numerator}}}{{{denominator}}}"
                        + LatexRender._suffix
                    )
                    # print(f"prefix is {LatexRender._prefix}")
                    # print(f"html is {html}")

            elif obj_type == "arc":
                html = (
                    LatexRender._prefix
                    + f'\\overset\\frown{{{LatexRender.latex2(LatexRender.latex(obj["value"]))}}}'
                    + LatexRender._suffix
                )

            elif obj_type == "underline":
                html = (
                    LatexRender._prefix
                    + f'\\underline{{{LatexRender.latex2(LatexRender.latex(obj["value"]))}}}'
                    + LatexRender._suffix
                )

            elif obj_type in ["equation", "equations"]:
                direction = obj.get("direction", "left")
                html += LatexRender._prefix
                if direction == "left":
                    html += "\\left\\{"
                    html += "\\begin{matrix}"
                    for equation in obj["value"]:
                        html += (
                            LatexRender.latex2(LatexRender.latex(equation)) + " \\\\ "
                        )
                    html += " \\end{matrix}\\right."
                elif direction == "right":
                    html += "\\left."
                    html += "\\begin{matrix}"
                    for equation in obj["value"]:
                        html += (
                            LatexRender.latex2(LatexRender.latex(equation)) + " \\\\ "
                        )
                    html += " \\end{matrix}\\right\\}"
                else:
                    html += "\\begin{Bmatrix}"
                    for equation in obj["value"]:
                        html += (
                            LatexRender.latex2(LatexRender.latex(equation)) + " \\\\ "
                        )
                    html += " \\end{Bmatrix}"
                html += LatexRender._suffix

            elif obj_type in ["script", "pc"]:
                html += LatexRender._prefix
                if "front" in obj["value"] and obj["value"]["front"]:
                    html += LatexRender.latex2(LatexRender.latex(obj["value"]["front"]))
                if "sub" in obj["value"]:
                    str_val = re.sub(r"(&nbsp;|\[br\])", "", obj["value"]["sub"])
                    if str_val:
                        html += (
                            "_{" + LatexRender.latex2(LatexRender.latex(str_val)) + "}"
                        )
                if "sup" in obj["value"]:
                    str_val = re.sub(r"(&nbsp;|\[br\])", "", obj["value"]["sup"])
                    if str_val:
                        html += (
                            "^{" + LatexRender.latex2(LatexRender.latex(str_val)) + "}"
                        )
                html += LatexRender._suffix

            elif obj_type == "root":
                html += LatexRender._prefix + "\\sqrt"
                if "index" in obj["value"] and obj["value"]["index"]:
                    html += "[" + obj["value"]["index"] + "]"
                html += (
                    "{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]["radicand"]))
                    + "}"
                )
                html += LatexRender._suffix
            elif obj_type in ["select", "multiselect"]:
                html = obj["options"]

            elif obj_type == "repeating":
                html += LatexRender._prefix
                html += LatexRender.latex2(LatexRender.latex(obj["value"]["pre"]))
                repeater = obj["value"]["repeater"]
                html += "\\dot{" + repeater[0] + "}"
                if len(repeater) > 1:
                    html += repeater[1:-1]
                    html += "\\dot{" + repeater[-1] + "}"
                html += LatexRender._suffix

            elif obj_type == "table":
                if LatexRender._mode == 1:
                    html = '<table border="1" style="border-collapse:collapse"><tbody>'
                    for row in obj["value"]:
                        html += "<tr>"
                        for cell in row:
                            colspan = cell.get("colspan", 1)
                            rowspan = cell.get("rowspan", 1)
                            cell_value = cell["value"] if "value" in cell else ""
                            if isinstance(cell_value, list):
                                cell_html = LatexRender.html_render(cell_value)
                            else:
                                cell_html = cell_value.replace("[br]", "\\n")
                            html += f'<td colspan="{colspan}" rowspan="{rowspan}">{cell_html}</td>'
                        html += "</tr>"
                    html += "</tbody></table>"
                elif LatexRender._mode == 2:
                    html = LatexRender._prefix + "\\begin{table}[!ht] \\centering"
                    td_len = len(obj["value"][0])
                    td_align_type = "|" + "l|" * td_len
                    html += f"\\begin{{tabular}}{{{td_align_type}}} \\hline"
                    for row in obj["value"]:
                        arr = []
                        for cell in row:
                            colspan = cell.get("colspan", 1)
                            rowspan = cell.get("rowspan", 1)
                            cell_value = (
                                LatexRender.html_render(cell["value"])
                                if isinstance(cell["value"], list)
                                else cell["value"].replace("[br]", " \\\\ ")
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
                    html += "\\end{tabular} \\end{table}" + LatexRender._suffix

            elif obj_type == "vector":
                html = (
                    LatexRender._prefix
                    + "\\vec{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + "}"
                    + LatexRender._suffix
                )

            elif obj_type == "arrow":
                direction = obj["value"].get("direction", "right")
                html = LatexRender._prefix
                if direction == "right":
                    html += "\\xrightarrow"
                else:
                    html += "\\xleftarrow"
                if obj["value"].get("bottom"):
                    html += (
                        "["
                        + LatexRender.latex2(LatexRender.latex(obj["value"]["bottom"]))
                        + "]"
                    )
                if obj["value"].get("top"):
                    html += (
                        "{"
                        + LatexRender.latex2(LatexRender.latex(obj["value"]["top"]))
                        + "}"
                    )
                html += LatexRender._suffix

            elif obj_type == "parallelequal":
                html = (
                    LatexRender._prefix
                    + "\\underline{\\underline{\\parallel}}"
                    + LatexRender._suffix
                )

            elif obj_type == "underbrace":
                html = LatexRender._prefix + "\\underbrace{"
                html += LatexRender.latex2(LatexRender.latex(obj["value"]["top"]))
                html += (
                    "}_{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]["bottom"]))
                    + "}"
                    + LatexRender._suffix
                )

            elif obj_type == "valence":
                html = LatexRender._prefix + "\\overset{"
                top_val = obj["value"]["top"]
                if isinstance(top_val, str) and top_val.startswith("_"):
                    html += "\\_"
                else:
                    html += LatexRender.latex2(LatexRender.latex(top_val))
                html += (
                    "}{\\mathop{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]["bottom"]))
                    + "}}\\,"
                    + LatexRender._suffix
                )

            elif obj_type == "overline":
                html = (
                    LatexRender._prefix
                    + "\\overline{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + "}"
                    + LatexRender._suffix
                )
            elif obj_type == "matrix":
                real = obj.get("real", "")
                if real == 1:
                    html += LatexRender._prefix + "\\left( \\begin{matrix}"
                    for value in obj["value"]:
                        html += (
                            LatexRender.latex2(LatexRender.latex(" & ".join(value)))
                            + " \\\\ "
                        )
                    html += "\\end{matrix} \\right)" + LatexRender._suffix
                else:
                    html += LatexRender._prefix + "\\left| \\begin{matrix}"
                    for value in obj["value"]:
                        html += (
                            LatexRender.latex2(LatexRender.latex(" & ".join(value)))
                            + " \\\\ "
                        )
                    html += "\\end{matrix} \\right|" + LatexRender._suffix

            elif obj_type == "chemequation":
                top = obj["value"].get("top", "")
                bottom = obj["value"].get("bottom", "")
                html += (
                    LatexRender._prefix
                    + "\\underset{"
                    + LatexRender.latex2(LatexRender.latex(bottom))
                    + "}{\\overset{"
                    + LatexRender.latex2(LatexRender.latex(top))
                    + "}{\\rightleftharpoons}}"
                    + LatexRender._suffix
                )

            elif obj_type == "equalmark":
                top = obj["value"].get("top", "")
                bottom = obj["value"].get("bottom", "")
                html += LatexRender._prefix + "\\begin{matrix}"
                html += (
                    "\\underline{\\underline{"
                    + LatexRender.latex2(LatexRender.latex(top))
                    + "}} \\\\"
                )
                html += LatexRender.latex2(LatexRender.latex(bottom)) + " \\\\"
                html += "\\end{matrix}" + LatexRender._suffix

            elif obj_type == "sum":
                html += LatexRender._prefix + "\\sum\\limits_{"
                html += (
                    LatexRender.latex2(LatexRender.latex(obj["value"]["lower"])) + "}^{"
                )
                html += (
                    LatexRender.latex2(LatexRender.latex(obj["value"]["upper"])) + "}{"
                )
                html += (
                    LatexRender.latex2(LatexRender.latex(obj["value"]["variable"]))
                    + "}"
                    + LatexRender._suffix
                )

            elif obj_type == "limit":
                html += LatexRender._prefix + "\\underset{"
                html += (
                    LatexRender.latex2(LatexRender.latex(obj["value"]["lower"]))
                    + "}{\\mathop{\\lim }}\\,"
                )
                html += (
                    LatexRender.latex2(LatexRender.latex(obj["value"]["function"]))
                    + LatexRender._suffix
                )

            elif obj_type == "italic":
                html += (
                    LatexRender._prefix
                    + "\\textit{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + "}"
                    + LatexRender._suffix
                )

            elif obj_type == "bold":
                html += (
                    LatexRender._prefix
                    + "\\textbf{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + "}"
                    + LatexRender._suffix
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
                html += LatexRender._prefix
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
                html += LatexRender._suffix

            elif obj_type == "repeater":
                html += (
                    LatexRender._prefix
                    + "\\dot{"
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + "}"
                    + LatexRender._suffix
                )

            elif obj_type in ["textcenter", "textright", "textindent"]:
                html += (
                    LatexRender._prefix
                    + LatexRender.latex2(LatexRender.latex(obj["value"]))
                    + LatexRender._suffix
                )

            elif obj_type == "emphasis":
                if obj["value"]:
                    html += (
                        LatexRender._prefix
                        + LatexRender.latex2(LatexRender.latex(obj["value"]))
                        + LatexRender._suffix
                    )
                else:
                    html = ""

            else:
                html = '<span style="color:red">格式错误' + obj["type"] + "</span>"

            # Continue handling all cases as structured in your PHP code.
            # More cases should be implemented here following the same pattern.

            return html

        elif isinstance(obj, str):
            return re.sub(r"\[br\]", "\n", obj, flags=re.IGNORECASE)
        elif isinstance(obj, list):
            return "".join([LatexRender.html_render(o) for o in obj])
        else:
            print(f"Invalid input format: {obj}, {type(obj)}")
            return "Invalid input format"
