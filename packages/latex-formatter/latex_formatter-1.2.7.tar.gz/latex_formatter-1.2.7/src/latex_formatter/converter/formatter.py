import json
from latex_formatter.converter.converter_v2 import LatexRenderV2
from typing import Union, List, Dict, Any
import pandas as pd


def question_formatter(content: str) -> Union[List[Dict[str, Any]], str]:
    """
    result_df["question_formatter"] = result_df["content"].apply(question_formatter)
    """
    try:
        json_content = json.loads(content)
        if (
            "caption" in json_content
            and "type" in json_content["caption"]
            and "value" in json_content["caption"]
        ):
            question_caption_type = json_content["caption"]["type"]
            if question_caption_type == "merge":
                question = json_content["caption"]["value"]
                return LatexRenderV2.star_render(question)
            else:
                return [json_content["caption"]]
    except:
        pass
    return content  # Fallback if JSON is not in expected format or exception occurs


def get_option_formatter(answer_formatter: Any) -> Any:
    while isinstance(answer_formatter, tuple):
        answer_formatter = answer_formatter[0]
    return answer_formatter


def option_formatter(content: str) -> Union[List[Dict[str, Any]], None]:
    """
    result_df["option"] = result_df["content"].apply(option_formatter)
    """
    try:
        json_content = json.loads(content)
        if "answer" in json_content:
            if not json_content["answer"] or json_content["answer"]["type"] == "text":
                return None
            answer_formatter = LatexRenderV2.html_render(json_content["answer"])
            answer_formatter = get_option_formatter(answer_formatter)

            for option in answer_formatter:
                if isinstance(option["option"], list):
                    option["option"] = "".join(str(i) for i in option["option"])
            return answer_formatter
    except Exception as e:
        print(f"Error: {e}, Content: {content}")
    return None


def explain_formatter(content: str) -> Union[List[str], None]:
    """
    result_df["explain_formatter"] = result_df["explains"].apply(explain_formatter)
    """
    try:
        content = json.loads(content)
        if "解答" in content:
            explains = content["解答"]
            if explains is None:
                return None
            return LatexRenderV2.star_render([explains])
    except Exception as e:
        print(f"Error: {e}, Content: {content}")
    return None


def answer_formatter(
    question: List[Dict[str, Any]], content: str
) -> Union[Dict[str, Any], List[Dict[str, Any]], str, None]:
    """
    result_df["answer_formatter"] = result_df.apply(lambda row: answer_formatter(row["question_formatter"], row["solution"], row["type"]), axis=1)
    """
    try:
        if not content or content in ["[]", ""]:
            return None
        content = json.loads(content)
        if not content:
            return None
        if isinstance(content, str):
            return {"type": "string", "value": content}
        for item in question:
            if "index" in item and item["index"] != -1:
                input_type = item["input_type"]
                index = int(item["index"])
                if isinstance(content[index], list):
                    content[index]["type"] = input_type
        return LatexRenderV2.star_render(content) if content else None
    except Exception as e:
        print(f"Error: {e}, Content: {content}, Question: {question}")
        return content


def difficulty_changer(difficulty: int) -> int:
    """
    result_df["difficulty_new"] = result_df.apply(lambda row: difficulty_changer(row["difficulty"]), axis=1)
    """
    return difficulty * 1000 if difficulty != 0 else 2000


def content_packager(question: str | dict) -> str:
    """
    result_df["question_model"] = result_df["question_formatter"].apply(content_packager)
    """
    if question is None:
        return None

    if isinstance(question, str):
        try:
            question = json.loads(question)
        except ValueError:
            return question

    def process_value(value):
        if isinstance(value, (list, tuple)):
            return "".join(process_value(v) for v in value)
        elif isinstance(value, dict):
            if "value" in value:
                return process_value(value["value"])
            else:
                return "".join(process_value(v) for v in value.values())
        return str(value)

    if isinstance(question, dict):
        if "caption" in question:
            return process_value(question["caption"])
        else:
            return process_value(question)
    else:
        return "".join(process_value(e.get("value", "")) for e in question)


def explain_packager(explain: str | List) -> str:
    """
    Usage: result_df["explain_model"] = result_df["explain_formatter"].apply(explain_packager)
    """
    if explain is None:
        return None

    def process_value(value):
        if isinstance(value, (list, tuple)):
            return "".join(process_value(v) for v in value)
        elif isinstance(value, dict):
            return process_value(value.get("value", ""))
        return str(value)

    if isinstance(explain, str):
        try:
            explain = json.loads(explain)
        except ValueError:
            return explain

    if isinstance(explain, list):
        return "".join(process_value(item) for item in explain)
    elif isinstance(explain, dict):
        return process_value(explain)
    else:
        return str(explain)


def process_dataframe(result_df: pd.DataFrame) -> pd.DataFrame:
    try:
        # 添加错误检查的函数
        def safe_apply(func):
            def wrapper(x):
                try:
                    return func(x)
                except Exception as e:
                    print(f"Error in {func.__name__} for input: {x}")
                    print(f"Error message: {str(e)}")
                    return None

            return wrapper

        result_df["question_formatter"] = result_df["content"].apply(
            safe_apply(question_formatter)
        )
        result_df["option"] = result_df["content"].apply(safe_apply(option_formatter))
        result_df["explain_formatter"] = result_df["explains"].apply(
            safe_apply(explain_formatter)
        )
        result_df["answer_formatter"] = result_df.apply(
            safe_apply(
                lambda row: answer_formatter(row["question_formatter"], row["solution"])
            ),
            axis=1,
        )
        result_df["difficulty_new"] = result_df.apply(
            safe_apply(lambda row: difficulty_changer(row["difficulty"])), axis=1
        )
        result_df["question_model"] = result_df["question_formatter"].apply(
            safe_apply(content_packager)
        )
        result_df["explain_model"] = result_df["explain_formatter"].apply(
            safe_apply(explain_packager)
        )

        # 添加去除[br]的功能，应用于所有列
        columns_to_process = [
            "question_formatter",
            "option",
            "explain_formatter",
            "answer_formatter",
            "question_model",
            "explain_model",
        ]
        for column in columns_to_process:
            if result_df[column].dtype == "object":
                result_df[column] = (
                    result_df[column].astype(str).str.replace(r"\[br\]", "", regex=True)
                )
    except Exception as e:
        print("error", e)

    return result_df
