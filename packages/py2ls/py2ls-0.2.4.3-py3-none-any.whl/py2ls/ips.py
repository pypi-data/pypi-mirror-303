import numpy as np
import pandas as pd

import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from cycler import cycler
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

from sklearn.kernel_approximation import KERNEL_PARAMS
from sympy import is_increasing
import sys, os, shutil, re, yaml, json, subprocess
import importlib.util
import time
from dateutil import parser
from datetime import datetime
import schedule

from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from rembg import remove, new_session

import docx
from fpdf import FPDF
from lxml import etree
from docx import Document
from PyPDF2 import PdfReader
from pptx import Presentation
from pptx.util import Inches
from pdf2image import convert_from_path, pdfinfo_from_path
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk  # nltk.download("punkt")
from docx2pdf import convert
import img2pdf as image2pdf
import nbformat
from nbconvert import MarkdownExporter

from itertools import pairwise
from box import Box, BoxList
from numerizer import numerize
from tqdm import tqdm
import mimetypes
from pprint import pp
from collections import Counter
from fuzzywuzzy import fuzz, process
from langdetect import detect
from duckduckgo_search import DDGS
from typing import List, Optional, Union
from bs4 import BeautifulSoup

from . import netfinder

try:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")
except NameError:
    pass

def plt_font(dir_font: str = "/System/Library/Fonts/Hiragino Sans GB.ttc"):
    """
    Add the Chinese (default) font to the font manager
    Args:
        dir_font (str, optional): _description_. Defaults to "/System/Library/Fonts/Hiragino Sans GB.ttc".
    """
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    slashtype = "/" if 'mac' in get_os() else "\\"
    if slashtype in dir_font:
        font_manager.fontManager.addfont(dir_font)
        fontname = os.path.basename(dir_font).split(".")[0]
    else:
        if "cn" in dir_font.lower() or "ch" in dir_font.lower():
            fontname = "Hiragino Sans GB" # default Chinese font
        else:
            fontname = dir_font

    plt.rcParams["font.sans-serif"] = [fontname]
    # plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False
    fonts_in_system = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
    fontname_in_system = [os.path.basename(i).split(".")[0] for i in fonts_in_system]
    if fontname not in fontname_in_system:
        print(f"Font '{fontname}' not found. Falling back to default.")
        plt.rcParams["font.sans-serif"] = ["Arial"]
    return fontname

# set 'dir_save'
if "dar" in sys.platform:
    dir_save = "/Users/macjianfeng/Dropbox/Downloads/"
else:
    if "win" in sys.platform:
        dir_save = "Z:\\Jianfeng\\temp\\"
    elif "lin" in sys.platform:
        dir_data = "/Users/macjianfeng/Dropbox/github/python/py2ls/confidential_data/gmail_login.json"


def unique(lst, ascending=None):
    """
    移除列表中的重复元素，同时可以选择按升序或降序排序。

    参数:
    lst (list): 输入的列表，其中可能包含重复的元素。
    ascending (bool, 可选): 如果为 True，则按升序排序；如果为 False，则按降序排序；如果为 None，则不排序，只移除重复元素。

    返回:
    list: 一个列表，其中的元素是唯一的，顺序根据参数 `ascending` 进行排序。
    """
    if ascending is not None:
        # 移除重复项
        unique_items = list(set(lst))
        # 统一元素类型（例如，转换为字符串）
        try:
            unique_items = sorted(
                unique_items, key=lambda x: str(x), reverse=not ascending
            )
        except TypeError:
            # 如果排序失败（例如，元素类型不一致），返回原始去重列表
            return unique_items
        return unique_items
    else:
        # 移除重复项同时保持原始顺序
        seen = set()  # 用于记录已见的元素
        result = []  # 用于存储结果
        for item in lst:
            if item not in seen:
                seen.add(item)  # 记录该元素
                result.append(item)  # 添加到结果列表中
        return result


# ************* below section: run_when *************
def run_when(when: str = "every 2 min", job=None, wait: int = 60):
    if "every" in when.lower():
        when = when.replace("every", "")
        run_every(when=when, job=job, wait=wait)
    elif any([i in when.lower() for i in ["at", "@", ":", "am", "pm"]]):
        time_words = ["at", "@", ":", "am", "pm"]
        # 判断'时间词'是否存在
        time_words_bool = [i in when.lower() for i in time_words]
        # 找到'时间词'的位置
        true_indices = [index for index, value in enumerate(time_words_bool) if value]
        time_word = time_words[true_indices[0]]  # 找到第一个'时间词'
        when = when.replace(time_word, "")  # 去除 时间词
        run_at(when=when, job=job, wait=wait)


def run_every(when: str = None, job=None, wait: int = 60):
    """
    Schedules a job to run at the given interval.

    :param when: String specifying the interval, e.g. '2 minutes', '4 hours', '1 day'.
    :param job: The function to be scheduled.
    """
    if job is None:
        print("No job provided!")
        return

    interval, unit = (
        str2num(when),
        strcmp(when.replace("every", ""), ["seconds", "minutes", "hours", "days"])[0],
    )
    print(interval, unit)
    # Mapping the scheduling based on the unit1
    if unit == "seconds":
        schedule.every(interval).seconds.do(job)
    elif unit == "minutes":
        schedule.every(interval).minutes.do(job)
    elif unit == "hours":
        schedule.every(interval).hours.do(job)
    elif unit == "days":
        schedule.every(interval).days.do(job)
    else:
        print(f"Invalid time unit: {unit}")
        return

    print(f"Scheduled job when {interval} {unit}.")

    # Keep the script running to execute the schedule
    while True:
        schedule.run_pending()
        time.sleep(wait)  # in seconds
    time.sleep(wait)  # in seconds


# # usage:
# def job():
#     print("1 sec")
# run_every(when="1 sec", job=job)


def run_at(when: str, job=None, wait: int = 60):
    """
    Schedules a job to run at an exact time of the day.

    :param when: String specifying the time, e.g. '1:30 pm','1.30 am','14:30', '1:30 pm', '8:45 am'.
    :param job: The function to be scheduled.
    :param wait: The sleep interval between checks in seconds.
    """
    if job is None:
        print("No job provided!")
        return
    when = when.replace("A.M.", "AM").replace("P.M.", "PM")
    when = when.replace(".", ":")
    when = when.strip()

    try:
        # Attempt to parse the time in both 24-hour and 12-hour format
        if "am" in when.lower() or "pm" in when.lower():
            scheduled_time = datetime.strptime(
                when, "%I:%M %p"
            ).time()  # 12-hour format with AM/PM
        else:
            scheduled_time = datetime.strptime(when, "%H:%M").time()  # 24-hour format
    except ValueError:
        print(
            f"Invalid time format: {when}. Use 'HH:MM' (24-hour) or 'H:MM AM/PM' format."
        )
        return

    print(f"Job scheduled to run at {scheduled_time}.")

    # Keep checking the current time
    while True:
        now = datetime.now()

        # Check if current time matches the scheduled time
        if (
            now.time().hour == scheduled_time.hour
            and now.time().minute == scheduled_time.minute
        ):
            job()  # Run the job
            time.sleep(
                wait
            )  # Sleep for a minute to avoid running the job multiple times in the same minute

        time.sleep(wait)  # wait to avoid excessive CPU usage


# # Example usage:
# def my_job():
#     print("Job executed at the exact time!")
# # Schedule the job at 14:30 when day
# run_at(when="1.30 pm", job=my_job)

# ************* above section: run_when *************


def get_timezone(timezone: str | list = None):
    if timezone is None:
        usage = """
        usage:
        datetime.now().astimezone(get_timezone("shanghai")).strftime("%H:%M")
        """
        print(usage)
        return None
    from pytz import all_timezones
    import pytz

    if isinstance(timezone, str):
        timezone = [timezone]

    # Extract the part after the "/" in time zones (if exists)
    timezones = [ssplit(i, "/")[1] if "/" in i else i for i in all_timezones]

    # Print all available time zones for debugging purposes
    # print(timezones)

    # Find and return matched time zones using strcmp
    matched_timezones = [all_timezones[strcmp(i, timezones)[1]] for i in timezone]
    if len(matched_timezones) == 1:
        return pytz.timezone(matched_timezones[0])
    else:
        return matched_timezones


def is_package_installed(package_name):
    """Check if a package is installed."""
    package_spec = importlib.util.find_spec(package_name)
    return package_spec is not None


def upgrade(module="py2ls",uninstall=False):
    """
    Installs or upgrades a specified Python module.

    Parameters:
    module (str): The name of the module to install/upgrade.
    uninstall (bool): If True, uninstalls the webdriver-manager before upgrading.
    """
    if not is_package_installed(module):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing {module}: {e}")
    if uninstall:
        subprocess.check_call(["pip", "uninstall", "-y", "webdriver-manager"])
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", module]
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while upgrading py2ls: {e}")


def get_version(pkg):
    import importlib.metadata

    def get_v(pkg_name):
        try:
            version = importlib.metadata.version(pkg_name)
            print(f"version {pkg_name} == {version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"Package '{pkg_name}' not found")

    if isinstance(pkg, str):
        get_v(pkg)
    elif isinstance(pkg, list):
        [get_v(pkg_) for pkg_ in pkg]


# usage:
# get_version(['pandas','numpy','py2ls'])


def rm_folder(folder_path, verbose=True):
    try:
        shutil.rmtree(folder_path)
        if verbose:
            print(f"Successfully deleted {folder_path}")
    except Exception as e:
        if verbose:
            print(f"Failed to delete {folder_path}. Reason: {e}")


def fremove(path, verbose=True):
    """
    Remove a folder and all its contents or a single file.
    Parameters:
    path (str): The path to the folder or file to remove.
    verbose (bool): If True, print success or failure messages. Default is True.
    """
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            if verbose:
                print(f"Successfully deleted folder {path}")
        elif os.path.isfile(path):
            os.remove(path)
            if verbose:
                print(f"Successfully deleted file {path}")
        else:
            if verbose:
                print(f"Path {path} does not exist")
    except Exception as e:
        if verbose:
            print(f"Failed to delete {path}. Reason: {e}")


def get_cwd(verbose: bool = True):
    """
    get_cwd: to get the current working directory
    Args:
        verbose (bool, optional): to show which function is use. Defaults to True.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        if verbose:
            print("os.path.dirname(os.path.abspath(__file__)):", script_dir)
    except NameError:
        # This works in an interactive environment (like a Jupyter notebook)
        script_dir = os.getcwd()
        if verbose:
            print("os.getcwd():", script_dir)
    return script_dir


def search(
    query,
    limit=5,
    kind="text",
    output="df",
    verbose=False,
    download=False,
    dir_save=dir_save,
    **kwargs,
):

    if "te" in kind.lower():
        results = DDGS().text(query, max_results=limit)
        res = pd.DataFrame(results)
        res.rename(columns={"href": "links"}, inplace=True)
    if verbose:
        print(f'searching "{query}": got the results below\n{res}')
    if download:
        try:
            downloader(
                url=res.links.tolist(), dir_save=dir_save, verbose=verbose, **kwargs
            )
        except:
            if verbose:
                print(f"failed link")
    return res


def echo(*args, **kwargs):
    """
    query, model="gpt", verbose=True, log=True, dir_save=dir_save
    a ai chat tool
    Args:
        query (str): _description_
        model (str, optional): _description_. Defaults to "gpt".
        verbose (bool, optional): _description_. Defaults to True.
        log (bool, optional): _description_. Defaults to True.
        dir_save (str, path, optional): _description_. Defaults to dir_save.

    Returns:
        str: the answer from ai
    """
    global dir_save

    query = None
    model = kwargs.get("model", "gpt")
    verbose = kwargs.get("verbose", True)
    log = kwargs.get("log", True)
    dir_save = kwargs.get("dir_save", dir_save)
    for arg in args:
        if isinstance(arg, str):
            if os.path.isdir(arg):
                dir_save = arg
            # elif os.path.isfile(arg):
            #     dir_save = dirname(arg)
            elif len(arg) <= 5:
                model = arg
            else:
                query = arg
        elif isinstance(arg, dict):
            verbose = arg.get("verbose", verbose)
            log = arg.get("log", log)

    def is_in_any(str_candi_short, str_full, ignore_case=True):
        if isinstance(str_candi_short, str):
            str_candi_short = [str_candi_short]
        res_bool = []
        if ignore_case:
            [res_bool.append(i in str_full.lower()) for i in str_candi_short]
        else:
            [res_bool.append(i in str_full) for i in str_candi_short]
        return any(res_bool)

    def valid_mod_name(str_fly):
        if is_in_any(str_fly, "claude-3-haiku"):
            return "claude-3-haiku"
        elif is_in_any(str_fly, "gpt-3.5"):
            return "gpt-3.5"
        elif is_in_any(str_fly, "llama-3-70b"):
            return "llama-3-70b"
        elif is_in_any(str_fly, "mixtral-8x7b"):
            return "mixtral-8x7b"
        else:
            print(
                f"not support your model{model}, supported models: 'claude','gpt(default)', 'llama','mixtral'"
            )
            return "gpt-3.5"  # default model

    model_valid = valid_mod_name(model)
    res = DDGS().chat(query, model=model_valid)
    if verbose:
        pp(res)
    if log:
        dt_str = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d_%H:%M:%S")
        res_ = f"\n\n####Q:{query}\n\n#####Ans:{dt_str}\n\n>{res}\n"
        if bool(os.path.basename(dir_save)):
            fpath = dir_save
        else:
            os.makedirs(dir_save, exist_ok=True)
            fpath = os.path.join(dir_save, f"log_ai.md")
        fupdate(fpath=fpath, content=res_)
        print(f"log file:{fpath}")
    return res


def chat(*args, **kwargs):
    return echo(*args, **kwargs)


def ai(*args, **kwargs):
    return echo(*args, **kwargs)


def detect_lang(text, output="lang", verbose=True):
    dir_curr_script = os.path.dirname(os.path.abspath(__file__))
    dir_lang_code = dir_curr_script + "/data/lang_code_iso639.json"
    print(dir_curr_script, os.getcwd(), dir_lang_code)
    lang_code_iso639 = fload(dir_lang_code)
    l_lang, l_code = [], []
    [[l_lang.append(v), l_code.append(k)] for v, k in lang_code_iso639.items()]
    try:
        if is_text(text):
            code_detect = detect(text)
            if "c" in output.lower():  # return code
                return l_code[strcmp(code_detect, l_code, verbose=verbose)[1]]
            else:
                return l_lang[strcmp(code_detect, l_code, verbose=verbose)[1]]
        else:
            print(f"{text} is not supported")
            return "no"
    except:
        return "no"


def is_text(s):
    has_alpha = any(char.isalpha() for char in s)
    has_non_alpha = any(not char.isalpha() for char in s)
    # no_special = not re.search(r'[^A-Za-z0-9\s]', s)
    return has_alpha and has_non_alpha


from typing import Any, Union

def shared(lst1:Any, lst2:Any,*args, verbose=True):
    """
    check the shared elelements in two list.
    usage:
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        list3 = [5, 6, 9, 10]   
        a = shared(list1, list2,list3)
    """
    if verbose:
        print("\n********* checking shared elements *********")
    if any([not isinstance(lst1,list),not isinstance(lst1,list)]):
        print(f"{' '*2}type(list1):\t{type(lst1)},\n{' '*2}type(list2):\t{type(lst2)}>")
    shared_elements=set(flatten(lst1,verbose=verbose)).intersection(flatten(lst2,verbose=verbose))
    # support more lists
    if args:
        for arg in args:
            shared_elements=shared_elements.intersection(set(flatten(arg,verbose=verbose)))
    shared_elements = list(shared_elements)
    if verbose:
        elements2show = shared_elements if len(shared_elements)<10 else shared_elements[:5]
        print(f"{' '*2}{len(shared_elements)} elements shared: {' '*2}{elements2show}")
        print("********* checking shared elements *********")
    return shared_elements

def flatten(nested: Any, unique_list=True,verbose=True):
    """
    Recursively flattens a nested structure (lists, tuples, dictionaries, sets) into a single list.
    Parameters:
        nested : Any, Can be a list, tuple, dictionary, or set.
    Returns: list, A flattened list.
    """ 
    flattened_list = []
    stack = [nested]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            stack.extend(current.values())
        elif isinstance(current, (list, tuple, set)):
            stack.extend(current)
        elif isinstance(current, pd.Series):
            stack.extend(current)
        else:
            flattened_list.append(current)
    if verbose:
        print(f"{' '*2}<in info: {len(unique(flattened_list))} elements after flattened>")
    if unique_list:
        return unique(flattened_list)
    else:
        return flattened_list
    
def strcmp(search_term, candidates, ignore_case=True, verbose=False, scorer="WR"):
    """
    Compares a search term with a list of candidate strings and finds the best match based on similarity score.

    Parameters:
    search_term (str): The term to be searched for.
    candidates (list of str): A list of candidate strings to compare against the search term.
    ignore_case (bool): If True, the comparison ignores case differences.
    verbose (bool): If True, prints the similarity score and the best match.

    Returns:
    tuple: A tuple containing the best match and its index in the candidates list.
    """

    def to_lower(s, ignore_case=True):
        # Converts a string or list of strings to lowercase if ignore_case is True.
        if ignore_case:
            if isinstance(s, str):
                return s.lower()
            elif isinstance(s, list):
                s=[str(i) for i in s]# convert all to str
                return [elem.lower() for elem in s]
        return s

    str1_, str2_ = to_lower(search_term, ignore_case), to_lower(candidates, ignore_case)
    if isinstance(str2_, list):
        if "part" in scorer.lower():
            similarity_scores = [fuzz.partial_ratio(str1_, word) for word in str2_]
        elif "W" in scorer.lower():
            similarity_scores = [fuzz.WRatio(str1_, word) for word in str2_]
        elif "ratio" in scorer.lower() or "stri" in scorer.lower():#Ratio (Strictest)
            similarity_scores = [fuzz.ratio(str1_, word) for word in str2_]
        else:
            similarity_scores = [fuzz.WRatio(str1_, word) for word in str2_]
        best_match_index = similarity_scores.index(max(similarity_scores))
        best_match_score = similarity_scores[best_match_index]
    else:
        best_match_index = 0
        if "part" in scorer.lower():
            best_match_score = fuzz.partial_ratio(str1_, str2_)
        elif "W" in scorer.lower():
            best_match_score = fuzz.WRatio(str1_, str2_)
        elif "Ratio" in scorer.lower():
            best_match_score = fuzz.ratio(str1_, str2_)
        else:
            best_match_score = fuzz.WRatio(str1_, str2_)
    if verbose:
        print(f"\nbest_match is: {candidates[best_match_index],best_match_score}")
        best_match = process.extract(search_term, candidates)
        print(f"建议: {best_match}")
    return candidates[best_match_index], best_match_index


# Example usaged
# str1 = "plos biology"
# str2 = ['PLoS Computational Biology', 'PLOS BIOLOGY']
# best_match, idx = strcmp(str1, str2, ignore_case=1)

def cn2pinyin(
    cn_str: Union[str, list] = None,
    sep: str = " ",
    fmt: str = "normal",  # which style you want to set
):
    from pypinyin import pinyin, Style

    """
    Converts Chinese characters to Pinyin.
    usage: 
        cn2pinyin(cn_str, sep="_", fmt="tone")
    Args:
        cn_str (str): Chinese string to convert.
        sep (str): Separator for the output Pinyin string.
        style (Style): "normal","tone", "tone2","tone3",
        "finals","finals_tone","finals_tone2","finals_tone3",
        "initials","bopomofo","bopomofo_first","cyrillic","pl",
    Returns:
        cn_str: The Pinyin representation of the Chinese string.
    """
    fmts = [
        "normal",
        "tone",
        "tone2",
        "tone3",
        "finals",
        "finals_tone",
        "finals_tone2",
        "finals_tone3",
        "initials",
        "bopomofo",
        "bopomofo_first",
        "cyrillic",
        "pl",
    ]
    fmt = strcmp(fmt, fmts)[0]
    if fmt == "normal":
        style = Style.NORMAL
    elif fmt == "tone":
        style = Style.TONE
    elif fmt == "tone2":
        style = Style.TONE2
    elif fmt == "tone3":
        style = Style.TONE3
    elif fmt == "finals":
        style = Style.FINALS
    elif fmt == "finals_tone":
        style = Style.FINALS_TONE
    elif fmt == "finals_tone2":
        style = Style.FINALS_TONE2
    elif fmt == "finals_tone3":
        style = Style.FINALS_TONE3
    elif fmt == "initials":
        style = Style.INITIALS
    elif fmt == "bopomofo":
        style = Style.BOPOMOFO
    elif fmt == "bopomofo_first":
        style = Style.BOPOMOFO_FIRST
    elif fmt == "cyrillic":
        style = Style.CYRILLIC
    elif fmt == "pl":
        style = Style.PL
    else:
        style = Style.NORMAL
    if not isinstance(cn_str,list):
        cn_str=[cn_str]
    pinyin_flat=[]
    for cn_str_ in cn_str:
        pinyin_string = pinyin(cn_str_, style=style)
        pinyin_flat.append(sep.join([item[0] for item in pinyin_string]))
    if len(pinyin_flat)==1:
        return pinyin_flat[0]
    else:
        return pinyin_flat

def counter(list_, verbose=True):
    c = Counter(list_)
    # Print the name counts
    for item, count in c.items():
        if verbose:
            print(f"{item}: {count}")
    return c


# usage:
# print(f"Return an iterator over elements repeating each as many times as its count:\n{sorted(c.elements())}")
# print(f"Return a list of the n most common elements:\n{c.most_common()}")
# print(f"Compute the sum of the counts:\n{c.total()}")


def str2time(time_str, fmt="24"):
    """
    Convert a time string into the specified format.
    Parameters:
    - time_str (str): The time string to be converted.
    - fmt (str): The format to convert the time to. Defaults to '%H:%M:%S'.
    Returns:
        %I represents the hour in 12-hour format.
        %H represents the hour in 24-hour format (00 through 23).
        %M represents the minute.
        %S represents the second.
        %p represents AM or PM.
    - str: The converted time string.
    """

    def time_len_corr(time_str):
        time_str_ = (
            ssplit(time_str, by=[":", " ", "digital_num"]) if ":" in time_str else None
        )
        time_str_split = []
        [time_str_split.append(i) for i in time_str_ if is_num(i)]
        if time_str_split:
            if len(time_str_split) == 2:
                H, M = time_str_split
                time_str_full = H + ":" + M + ":00"
            elif len(time_str_split) == 3:
                H, M, S = time_str_split
                time_str_full = H + ":" + M + ":" + S
        else:
            time_str_full = time_str_
        if "am" in time_str.lower():
            time_str_full += " AM"
        elif "pm" in time_str.lower():
            time_str_full += " PM"
        return time_str_full

    if "12" in fmt:
        fmt = "%I:%M:%S %p"
    elif "24" in fmt:
        fmt = "%H:%M:%S"

    try:
        # Try to parse the time string assuming it could be in 24-hour or 12-hour format
        time_obj = datetime.strptime(time_len_corr(time_str), "%H:%M:%S")
    except ValueError:
        try:
            time_obj = datetime.strptime(time_len_corr(time_str), "%I:%M:%S %p")
        except ValueError as e:
            raise ValueError(f"Unable to parse time string: {time_str}. Error: {e}")

    # Format the time object to the desired output format
    formatted_time = time_obj.strftime(fmt)
    return formatted_time


# # Example usage:
# time_str1 = "14:30:45"
# time_str2 = "02:30:45 PM"

# formatted_time1 = str2time(time_str1, fmt='12')  # Convert to 12-hour format
# formatted_time2 = str2time(time_str2, fmt='24')    # Convert to 24-hour format

# print(formatted_time1)  # Output: 02:30:45 PM
# print(formatted_time2)  # Output: 14:30:45


def str2date(date_str, fmt="%Y-%m-%d_%H:%M:%S"):
    """
    Convert a date string into the specified format.
    Parameters:
    - date_str (str): The date string to be converted.
    - fmt (str): The format to convert the date to. Defaults to '%Y%m%d'.
    Returns:
    - str: The converted date string.
    """
    try:
        date_obj = parser.parse(date_str)
    except ValueError as e:
        raise ValueError(f"Unable to parse date string: {date_str}. Error: {e}")
    # Format the date object to the desired output format
    formatted_date = date_obj.strftime(fmt)
    return formatted_date


# str1=str2date(num2str(20240625),fmt="%a %d-%B-%Y")
# print(str1)
# str2=str2num(str2date(str1,fmt='%a %Y%m%d'))
# print(str2)


def str2num(s, *args, **kwargs):
    delimiter = kwargs.get("sep", None)
    round_digits = kwargs.get("round", None)
    if delimiter is not None:
        s = s.replace(delimiter, "")
    for arg in args:
        if isinstance(arg, str) and delimiter is None:
            delimiter = arg
        elif isinstance(arg, int) and round_digits is None:
            round_digits = arg
    try:
        num = int(s)
    except ValueError:
        try:
            num = float(s)
        except ValueError:
            try:
                numerized = numerize(s)
                num = int(numerized) if "." not in numerized else float(numerized)
            except Exception as e:
                # Attempt to handle multiple number segments
                try:
                    number_segments = re.findall(r"[-+]?\d*\.\d+|\d+", s)
                    nums = []
                    for segment in number_segments:
                        nums.append(str2num(segment))
                    if len(nums) == 1:
                        num = nums[0]
                    else:
                        num = nums
                except Exception as e:
                    return None

    # Apply rounding if specified
    if round_digits is not None:
        if isinstance(num, list):
            num = [round(i + 0.00000000001, round_digits) for i in num]
        else:
            num_adj = num + 0.00000000001  # Ensure precise rounding
            num = round(num_adj, round_digits)
    if round_digits == 0:
        if isinstance(num, list):
            num = [int(i) for i in num]
        else:
            num = int(num)
    # if delimiter is not None:
    #     num_str = f"{num:,}".replace(",", delimiter)
    #     return num_str#s.replace(delimiter, "")

    return num


# Examples
# print(str2num("123"))                # Output: 123
# print(str2num("123.456", 2))         # Output: 123.46
# print(str2num("one hundred and twenty three"))  # Output: 123
# print(str2num("seven million"))      # Output: 7000000
# print(str2num('one thousand thirty one',','))  # Output: 1,031
# print(str2num("12345.6789", ","))    # Output: 12,345.6789
# print(str2num("12345.6789", " ", 2)) # Output: 12 345.68
# print(str2num('111113.34555',3,',')) # Output: 111,113.346
# print(str2num("123.55555 sec miniuets",3)) # Output: 1.3
# print(str2num("every 3,300.55 hours and 5.045555 min", sep=",", round=1))
# print(str2num("five hundred fourty one"), str2num(
#     "this is 5.9435 euros for 10.04499 killograme", round=3
# )[0])


def num2str(num, *args, **kwargs):
    delimiter = kwargs.get("sep", None)
    round_digits = kwargs.get("round", None)

    # Parse additional arguments
    for arg in args:
        if isinstance(arg, str):
            delimiter = arg
        elif isinstance(arg, int):
            round_digits = arg

    # Apply rounding if specified
    if round_digits is not None:
        num = round(num, round_digits)

    # Convert number to string
    num_str = f"{num}"

    # Apply delimiter if specified
    if delimiter is not None:
        num_str = num_str.replace(".", ",")  # Replace decimal point with comma
        num_str_parts = num_str.split(",")
        if len(num_str_parts) > 1:
            integer_part = num_str_parts[0]
            decimal_part = num_str_parts[1]
            integer_part = "{:,}".format(int(integer_part))
            num_str = integer_part + "." + decimal_part
        else:
            num_str = "{:,}".format(int(num_str_parts[0]))

    return num_str


# Examples
# print(num2str(123), type(num2str(123)))  # Output: "123"
# print(num2str(123.456, round=2), type(num2str(123.456, 2)))  # Output: "123.46"
# print(num2str(7000.125, round=1), type(num2str(7000.125, 2)))  # Output: "7000.13"
# print(
#     num2str(12345333.6789, sep=","), type(num2str(12345.6789, ","))
# )  # Output: "12,345.6789"
# print(num2str(7000.00, sep=","), type(num2str(7000.00, ",")))  # Output: "7,000.00"


# Helper to convert text or list of text to HTML
def str2html(text_list, strict=False):
    if not isinstance(text_list, list):
        text_list = [text_list]

    # Define a mapping for escape sequences to their HTML representations
    escape_mapping = {
        "\\": "&bsol;",  # Backslash
        "'": "&apos;",  # Single quote
        '"': "&quot;",  # Double quote
        "\n": "<br>",  # Newline
        "\r": "",  # Carriage return (not represented in HTML)
        "\t": "&nbsp;&nbsp;&nbsp;&nbsp;",  # Tab (4 spaces)
        "\b": "",  # Backspace (not typically represented)
        "\f": "",  # Form feed (not typically represented)
        "\v": "",  # Vertical tab (not typically represented)
        "\a": "",  # Bell/alert sound (not typically represented)
        "\0": "",  # Null character (not typically represented)
    }

    # Convert text by replacing escape sequences with their HTML equivalents
    html_content = ""
    for text in text_list:
        for escape_seq, html_rep in escape_mapping.items():
            text = text.replace(escape_seq, html_rep)
        html_content += text.replace("\n", "<br>")  # Add line breaks for newlines

    if strict:
        html_content = "<html><body>\n" + html_content + "\n</body></html>"

    return html_content


def cm2px(*cm, dpi=300) -> list:
    # Case 1: When the user passes a single argument that is a list or tuple, such as cm2px([8, 5]) or inch2cm((8, 5))
    if len(cm) == 1 and isinstance(cm[0], (list, tuple)):
        # If the input is a single list or tuple, we unpack its elements and convert each to cm
        return [i / 2.54 * dpi for i in cm[0]]
    # Case 2: When the user passes multiple arguments directly, such as cm2px(8, 5)
    else:
        return [i / 2.54 * dpi for i in cm]


def px2cm(*px, dpi=300) -> list:
    # Case 1: When the user passes a single argument that is a list or tuple, such as px2cm([8, 5]) or inch2cm((8, 5))
    if len(px) == 1 and isinstance(px[0], (list, tuple)):
        # If the input is a single list or tuple, we unpack its elements and convert each to cm
        return [i * 2.54 / dpi for i in px[0]]
    # Case 2: When the user passes multiple arguments directly, such as px2cm(8, 5)
    else:
        # Here, we convert each individual argument directly to cm
        return [i * 2.54 / dpi for i in px]


def px2inch(*px, dpi=300) -> list:
    """
    px2inch: converts pixel measurements to inches based on the given dpi.
    Usage:
    px2inch(300, 600, dpi=300); px2inch([300, 600], dpi=300)
    Returns:
        list: in inches
    """
    # Case 1: When the user passes a single argument that is a list or tuple, such as px2inch([300, 600]) or px2inch((300, 600))
    if len(px) == 1 and isinstance(px[0], (list, tuple)):
        # If the input is a single list or tuple, we unpack its elements and convert each to inches
        return [i / dpi for i in px[0]]
    # Case 2: When the user passes multiple arguments directly, such as px2inch(300, 600)
    else:
        # Here, we convert each individual argument directly to inches
        return [i / dpi for i in px]


def cm2inch(*cm) -> list:
    """
    cm2inch: converts centimeter measurements to inches.
    Usage:
    cm2inch(10, 12.7); cm2inch((10, 12.7)); cm2inch([10, 12.7])
    Returns:
        list: in inches
    """
    # Case 1: When the user passes a single argument that is a list or tuple, such as cm2inch([10, 12.7]) or cm2inch((10, 12.7))
    if len(cm) == 1 and isinstance(cm[0], (list, tuple)):
        # If the input is a single list or tuple, we unpack its elements and convert each to inches
        return [i * 2.54 for i in cm[0]]
    # Case 2: When the user passes multiple arguments directly, such as cm2inch(10, 12.7)
    else:
        # Here, we convert each individual argument directly to inches
        return [i * 2.54 for i in cm]


def inch2px(*inch, dpi=300) -> list:
    """
    inch2px: converts inch measurements to pixels based on the given dpi.
    Usage:
    inch2px(1, 2, dpi=300); inch2px([1, 2], dpi=300)
    Returns:
        list: in pixels
    """
    # Case 1: When the user passes a single argument that is a list or tuple, such as inch2px([1, 2]) or inch2px((1, 2))
    if len(inch) == 1 and isinstance(inch[0], (list, tuple)):
        # If the input is a single list or tuple, we unpack its elements and convert each to pixels
        return [i * dpi for i in inch[0]]
    # Case 2: When the user passes multiple arguments directly, such as inch2px(1, 2)
    else:
        # Here, we convert each individual argument directly to pixels
        return [i * dpi for i in inch]


def inch2cm(*inch) -> list:
    """
    inch2cm: converts inch measurements to centimeters.
    Usage:
    inch2cm(8,5); inch2cm((8,5)); inch2cm([8,5])
    Returns:
        list: in centimeters
    """
    # Case 1: When the user passes a single argument that is a list or tuple, such as inch2cm([8, 5]) or inch2cm((8, 5))
    if len(inch) == 1 and isinstance(inch[0], (list, tuple)):
        # If the input is a single list or tuple, we unpack its elements and convert each to cm
        return [i / 2.54 for i in inch[0]]
    # Case 2: When the user passes multiple arguments directly, such as inch2cm(8, 5)
    else:
        # Here, we convert each individual argument directly to cm
        return [i / 2.54 for i in inch]


def sreplace(*args, **kwargs):
    """
    sreplace(text, by=None, robust=True)
    Replace specified substrings in the input text with provided replacements.
    Args:
        text (str): The input text where replacements will be made.
        by (dict, optional): A dictionary containing substrings to be replaced as keys
            and their corresponding replacements as values. Defaults to {".com": "..come", "\n": " ", "\t": " ", "  ": " "}.
        robust (bool, optional): If True, additional default replacements for newline and tab characters will be applied.
                                Default is False.
    Returns:
        str: The text after replacements have been made.
    """
    text = None
    by = kwargs.get("by", None)
    robust = kwargs.get("robust", True)

    for arg in args:
        if isinstance(arg, str):
            text = arg
        elif isinstance(arg, dict):
            by = arg
        elif isinstance(arg, bool):
            robust = arg
        else:
            Error(f"{type(arg)} is not supported")

    # Default replacements for newline and tab characters
    default_replacements = {
        "\a": "",
        "\b": "",
        "\f": "",
        "\n": "",
        "\r": "",
        "\t": "",
        "\v": "",
        "\\": "",  # Corrected here
        # "\?": "",
        "�": "",
        "\\x": "",  # Corrected here
        "\\x hhhh": "",
        "\\ ooo": "",  # Corrected here
        "\xa0": "",
        "  ": " ",
    }

    # If dict_replace is None, use the default dictionary
    if by is None:
        by = {}
    # If robust is True, update the dictionary with default replacements
    if robust:
        by.update(default_replacements)

    # Iterate over each key-value pair in the dictionary and replace substrings accordingly
    for k, v in by.items():
        text = text.replace(k, v)
    return text


# usage:
# sreplace(text, by=dict(old_str='new_str'), robust=True)


def paper_size(paper_type_str="a4"):
    df = pd.DataFrame(
        {
            "a0": [841, 1189],
            "a1": [594, 841],
            "a2": [420, 594],
            "a3": [297, 420],
            "a4": [210, 297],
            "a5": [148, 210],
            "a6": [105, 148],
            "a7": [74, 105],
            "b0": [1028, 1456],
            "b1": [707, 1000],
            "b2": [514, 728],
            "b3": [364, 514],
            "b4": [257, 364],
            "b5": [182, 257],
            "b6": [128, 182],
            "letter": [215.9, 279.4],
            "legal": [215.9, 355.6],
            "business card": [85.6, 53.98],
            "photo china passport": [33, 48],
            "passport single": [125, 88],
            "visa": [105, 74],
            "sim": [25, 15],
        }
    )
    for name in df.columns:
        if paper_type_str in name.lower():
            paper_type = name
    if not paper_type:
        paper_type = "a4"  # default
    return df[paper_type].tolist()


def docx2pdf(dir_docx, dir_pdf=None):
    if dir_pdf:
        convert(dir_docx, dir_pdf)
    else:
        convert(dir_docx)


def img2pdf(dir_img, kind="jpeg", page=None, dir_save=None, page_size="a4", dpi=300):
    def mm_to_point(size):
        return (image2pdf.mm_to_pt(size[0]), image2pdf.mm_to_pt(size[1]))

    def set_dpi(x):
        dpix = dpiy = x
        return image2pdf.get_fixed_dpi_layout_fun((dpix, dpiy))

    if not kind.startswith("."):
        kind = "." + kind
    if dir_save is None:
        dir_save = dir_img.replace(kind, ".pdf")
    imgs = []
    if os.path.isdir(dir_img):
        if not dir_save.endswith(".pdf"):
            dir_save += "#merged_img2pdf.pdf"
        if page is None:
            select_range = listdir(dir_img, kind=kind).fpath
        else:
            if not isinstance(page, (np.ndarray, list, range)):
                page = [page]
            select_range = listdir(dir_img, kind=kind)["fpath"][page]
        for fname in select_range:
            if not fname.endswith(kind):
                continue
            path = os.path.join(dir_img, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
    else:
        imgs = [os.path.isdir(dir_img), dir_img]

    if page_size:
        if isinstance(page_size, str):
            pdf_in_mm = mm_to_point(paper_size(page_size))
        else:
            print("default: page_size = (210,297)")
            pdf_in_mm = mm_to_point(page_size)
            print(f"page size was set to {page_size}")
        p_size = image2pdf.get_layout_fun(pdf_in_mm)
    else:
        p_size = set_dpi(dpi)
    with open(dir_save, "wb") as f:
        f.write(image2pdf.convert(imgs, layout_fun=p_size))


# usage:
# dir_img="/Users/macjianfeng/Dropbox/00-Personal/2015-History/2012-2015_兰州大学/120901-大学课件/生物统计学 陆卫/复习题/"
# img2pdf(dir_img,kind='tif', page=range(3,7,2))


def pdf2ppt(dir_pdf, dir_ppt):
    prs = Presentation()

    # Open the PDF file
    with open(dir_pdf, "rb") as f:
        reader = PdfReader(f)
        num_pages = len(reader.pages)

        # Iterate through each page in the PDF
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()

            # Add a slide for each page's content
            slide_layout = prs.slide_layouts[
                5
            ]  # Use slide layout that suits your needs
            slide = prs.slides.add_slide(slide_layout)
            slide.shapes.title.text = f"Page {page_num + 1}"
            slide.shapes.add_textbox(
                Inches(1), Inches(1.5), Inches(8), Inches(5)
            ).text = text

    # Save the PowerPoint presentation
    prs.save(dir_ppt)
    print(f"Conversion from {dir_pdf} to {dir_ppt} complete.")


def ssplit(text, by="space", verbose=False, strict=False, **kws):
    if isinstance(text, list):
        nested_list = [ssplit(i, by=by, verbose=verbose, **kws) for i in text]
        flat_list = [item for sublist in nested_list for item in sublist]
        return flat_list

    def split_by_word_length(text, length):
        return [word for word in text.split() if len(word) == length]

    def split_by_multiple_delimiters(text, delimiters):
        regex_pattern = "|".join(map(re.escape, delimiters))
        return re.split(regex_pattern, text)

    def split_by_camel_case(text):
        return re.findall(r"[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))", text)

    def split_at_upper_fl_lower(text):
        return re.findall(r"[A-Z](?:[a-z]+|[A-Z]+(?=[A-Z]|$))", text)

    def split_at_lower_fl_upper(text):
        split_text = re.split(r"(?<=[a-z])(?=[A-Z])", text)
        return split_text

    def split_at_upper(text):
        split_text = re.split(r"(?=[A-Z])", text)
        split_text = [part for part in split_text if part]
        return split_text

    def split_by_regex_lookahead(text, pattern):
        return re.split(f"(?<={pattern})", text)

    def split_by_regex_end(text, pattern):
        return re.split(f"(?={pattern})", text)

    # def split_by_sentence_endings(text):
    #     return re.split(r"(?<=[.!?])", text)
    def split_non_ascii(text):
        # return re.split(r"([^\x00-\x7F\w\s,.!?:\"'()\-]+)", text)
        # return re.split(r"[^\x00-\x7F]+", text)
        return re.split(r"([^\x00-\x7F]+)", text)

    def split_by_consecutive_non_alphanumeric(text):
        return re.split(r"\W+", text)

    def split_by_fixed_length_chunks(text, length):
        return [text[i : i + length] for i in range(0, len(text), length)]

    def split_by_sent_num(text, n=10):
        # split text into sentences
        text_split_by_sent = sent_tokenize(text)
        cut_loc_array = np.arange(0, len(text_split_by_sent), n)
        if cut_loc_array[-1] != len(text_split_by_sent):
            cut_loc = np.append(cut_loc_array, len(text_split_by_sent))
        else:
            cut_loc = cut_loc_array
        # get text in section (e.g., every 10 sentences)
        text_section = []
        for i, j in pairwise(cut_loc):
            text_section.append(text_split_by_sent[i:j])
        return text_section

    def split_general(text, by, verbose=False, ignore_case=False):
        if ignore_case:
            if verbose:
                print(f"used {by} to split, ignore_case=True")
            pattern = re.compile(re.escape(by), re.IGNORECASE)
            split_text = pattern.split(text)
            return split_text
        else:
            if verbose:
                print(f"used {by} to split, ignore_case=False")
            return text.split(by)

    def reg_split(text, pattern):
        return re.split(pattern, text)

    if ("sp" in by or "white" in by) and not strict:
        if verbose:
            print(f"splited by space")
        return text.split()
    elif ("word" in by and "len" in by) and not strict:
        if verbose:
            print(f"split_by_word_length(text, length)")
        return split_by_word_length(text, **kws)  # split_by_word_length(text, length)
    # elif "," in by:
    #     if verbose:
    #         print(f"splited by ','")
    #     return text.split(",")
    elif isinstance(by, list):
        if verbose:
            print(f"split_by_multiple_delimiters: ['|','&']")
        return split_by_multiple_delimiters(text, by)
    elif (
        all([("digi" in by or "num" in by), not "sent" in by, not "str" in by])
        and not strict
    ):
        if verbose:
            print(f"splited by digital (numbers)")
        return re.split(r"(\d+)", text)
    elif all([("digi" in by or "num" in by), "str" in by]) and not strict:
        if verbose:
            print(f"Splitting by (number strings)")
        pattern = re.compile(
            r"\b((?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion|and|[\d,]+(?:\.\d+)?)(?:[-\s]?(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion|and|[\d,]+(?:\.\d+)?))*)\b",
            re.IGNORECASE,
        )
        return re.split(pattern, text)
    elif ("pun" in by) and not strict:
        if verbose:
            print(f"splited by 标点('.!?;')")
        return re.split(r"[.!?;]", text)
    elif ("\n" in by or "li" in by) and not strict:
        if verbose:
            print(f"splited by lines('\n')")
        return text.splitlines()
    elif ("cam" in by) and not strict:
        if verbose:
            print(f"splited by camel_case")
        return split_by_camel_case(text)
    elif ("word" in by) and not strict:
        if verbose:
            print(f"splited by word")
        return word_tokenize(text)
    elif ("sen" in by and not "num" in by) and not strict:
        if verbose:
            print(f"splited by sentence")
        return sent_tokenize(text)
    elif ("sen" in by and "num" in by) and not strict:
        return split_by_sent_num(text, **kws)
    elif ("cha" in by) and not strict:
        if verbose:
            print(f"splited by chracters")
        return list(text)
    elif ("up" in by or "cap" in by) and ("l" not in by) and not strict:
        if verbose:
            print(f"splited by upper case")
        return split_at_upper(text)
    elif ("u" in by and "l" in by) and not strict:
        if by.find("u") < by.find("l"):
            if verbose:
                print(f"splited by upper followed by lower case")
            return split_at_upper_fl_lower(text)
        else:
            if verbose:
                print(f"splited by lower followed by upper case")
            return split_at_lower_fl_upper(text)
    elif ("start" in by or "head" in by) and not strict:
        if verbose:
            print(f"splited by lookahead")
        return split_by_regex_lookahead(text, **kws)
    elif ("end" in by or "tail" in by) and not strict:
        if verbose:
            print(f"splited by endings")
        return split_by_regex_end(text, **kws)
    elif ("other" in by or "non_alp" in by) and not strict:
        if verbose:
            print(f"splited by non_alphanumeric")
        return split_by_consecutive_non_alphanumeric(text)
    elif ("len" in by) and not strict:
        if verbose:
            print(f"splited by fixed length")
        return split_by_fixed_length_chunks(text, **kws)
    elif ("re" in by or "cus" in by or "cos" in by) and not strict:
        if verbose:
            print(f"splited by customed, re; => {by}")
        return reg_split(text, **kws)
    elif ("lang" in by or "eng" in by) and not strict:
        return split_non_ascii(text)
    else:
        return split_general(text, by, verbose=verbose, **kws)


def pdf2img(dir_pdf, dir_save=None, page=None, kind="png", verbose=True, **kws):
    df_dir_img_single_page = pd.DataFrame()
    dir_single_page = []
    if verbose:
        pp(pdfinfo_from_path(dir_pdf))
    if isinstance(page, tuple) and page:
        page = list(page)
    if isinstance(page, int):
        page = [page]
    if page is None:
        page = [pdfinfo_from_path(dir_pdf)["Pages"]]
    if len(page) == 1 and page != [pdfinfo_from_path(dir_pdf)["Pages"]]:
        page = [page[0], page[0]]
    else:
        page = [1, page[0]]
    print(page)
    pages = convert_from_path(dir_pdf, first_page=page[0], last_page=page[-1], **kws)
    if dir_save is None:
        dir_save = mkdir(dirname(dir_pdf), basename(dir_pdf).split(".")[0] + "_img")
    for i, page in enumerate(pages):
        if verbose:
            print(f"processing page: {i+1}")
        if i < 9:
            dir_img_each_page = dir_save + f"page_0{i+1}.png"
        else:
            dir_img_each_page = dir_save + f"page_{i+1}.png"
        dir_single_page.append(dir_img_each_page)
        page.save(dir_img_each_page, kind.upper())
    df_dir_img_single_page["fpath"] = dir_single_page
    return df_dir_img_single_page


# dir_pdf = "/Users/macjianfeng/Dropbox/github/python/240308_Python Data Science Handbook.pdf"
# df_page = pdf2img(dir_pdf, page=[1, 5],dpi=300)
def get_encoding(fpath, alternative_encodings=None, verbose=False):
    """
    Attempt to determine the encoding of a file by trying multiple encodings.

    Parameters:
    fpath (str): The path to the file.
    alternative_encodings (list): List of encodings to try. If None, uses a default list.
    verbose (bool): If True, print detailed information about each attempted encoding.

    Returns:
    str: The encoding that successfully read the file, or None if no encoding worked.
    """
    if alternative_encodings is None:
        alternative_encodings = [
            "utf-8",
            "latin1",
            "windows-1252",
            "iso-8859-1",
            "iso-8859-2",
            "iso-8859-3",
            "iso-8859-4",
            "iso-8859-5",
            "iso-8859-6",
            "iso-8859-7",
            "iso-8859-8",
            "iso-8859-9",
            "windows-1250",
            "windows-1251",
            "windows-1253",
            "windows-1254",
            "windows-1255",
            "windows-1256",
            "windows-1257",
            "windows-1258",
            "big5",
            "gb18030",
            "shift_jis",
            "euc_jp",
            "koi8_r",
            "mac_roman",
            "mac_central_europe",
            "mac_greek",
            "mac_cyrillic",
            "mac_arabic",
            "mac_hebrew",
        ]

    if not os.path.isfile(fpath):
        raise FileNotFoundError(f"The file {fpath} does not exist.")

    for enc in alternative_encodings:
        try:
            with open(fpath, mode="r", encoding=enc) as file:
                file.read()  # Try to read the file
            if verbose:
                print(f"Successfully detected encoding: {enc}")
            return enc
        except UnicodeDecodeError:
            if verbose:
                print(f"Failed to decode with encoding: {enc}")
            continue

    # If no encoding worked
    print("No suitable encoding found.")
    return None


def unzip(dir_path, output_dir=None):
    """
    Unzips or extracts various compressed file formats (.gz, .zip, .7z, .tar, .bz2, .xz, .rar).
    If the output directory already exists, it will be replaced.

    Parameters:
    dir_path (str): Path to the compressed file.
    output_dir (str): Directory where the extracted files will be saved.
                      If None, it extracts to the same directory as the file, with the same name.

    Returns:
    str: The path to the output directory where files are extracted.
    """

    # Set default output directory to the same as the input file
    if output_dir is None:
        output_dir = os.path.splitext(dir_path)[0]

    # If the output directory already exists, remove it and replace it
    if os.path.exists(output_dir):
        if os.path.isdir(output_dir):  # check if it is a folder
            shutil.rmtree(output_dir)  # remove folder
        else:
            os.remove(output_dir)  # remove file

    # Handle .tar.gz files
    if dir_path.endswith(".tar.gz") or dir_path.endswith(".tgz"):
        import tarfile

        with tarfile.open(dir_path, "r:gz") as tar_ref:
            tar_ref.extractall(output_dir)
        return output_dir
    # Handle .gz files
    if dir_path.endswith(".gz"):
        import gzip

        output_file = os.path.splitext(dir_path)[0]  # remove the .gz extension
        with gzip.open(dir_path, "rb") as gz_file:
            with open(output_file, "wb") as out_file:
                shutil.copyfileobj(gz_file, out_file)
        return output_file

    # Handle .zip files
    elif dir_path.endswith(".zip"):
        import zipfile

        with zipfile.ZipFile(dir_path, "r") as zip_ref:
            zip_ref.extractall(output_dir)
        return output_dir

    # Handle .7z files (requires py7zr)
    elif dir_path.endswith(".7z"):
        import py7zr

        with py7zr.SevenZipFile(dir_path, mode="r") as z:
            z.extractall(path=output_dir)
        return output_dir

    # Handle .tar files
    elif dir_path.endswith(".tar"):
        import tarfile

        with tarfile.open(dir_path, "r") as tar_ref:
            tar_ref.extractall(output_dir)
        return output_dir

    # Handle .tar.bz2 files
    elif dir_path.endswith(".tar.bz2"):
        import tarfile

        with tarfile.open(dir_path, "r:bz2") as tar_ref:
            tar_ref.extractall(output_dir)
        return output_dir

    # Handle .bz2 files
    elif dir_path.endswith(".bz2"):
        import bz2

        output_file = os.path.splitext(dir_path)[0]  # remove the .bz2 extension
        with bz2.open(dir_path, "rb") as bz_file:
            with open(output_file, "wb") as out_file:
                shutil.copyfileobj(bz_file, out_file)
        return output_file

    # Handle .xz files
    elif dir_path.endswith(".xz"):
        import lzma

        output_file = os.path.splitext(dir_path)[0]  # remove the .xz extension
        with lzma.open(dir_path, "rb") as xz_file:
            with open(output_file, "wb") as out_file:
                shutil.copyfileobj(xz_file, out_file)
        return output_file

    # Handle .rar files (requires rarfile)
    elif dir_path.endswith(".rar"):
        import rarfile

        with rarfile.RarFile(dir_path) as rar_ref:
            rar_ref.extractall(output_dir)
        return output_dir

    else:
        raise ValueError(f"Unsupported file format: {os.path.splitext(dir_path)[1]}")


# Example usage:
# output_dir = unzip('data.tar.gz')
# output_file = unzip('file.csv.gz')
# output_dir_zip = unzip('archive.zip')
# output_dir_7z = unzip('archive.7z')


def is_df_abnormal(df: pd.DataFrame, verbose=False) -> bool:
    """
    Usage
    is_abnormal = is_df_abnormal(df, verbose=1)

    """
    # Initialize a list to hold messages about abnormalities
    messages = []
    is_abnormal = False
    # Check the shape of the DataFrame
    actual_shape = df.shape
    messages.append(f"Shape of DataFrame: {actual_shape}")

    # Check column names
    column_names = df.columns.tolist()

    # Count of delimiters and their occurrences
    delimiter_counts = {"\t": 0, ",": 0, "\n": 0, "": 0}  # Count of empty strings

    for name in column_names:
        # Count occurrences of each delimiter
        delimiter_counts["\t"] += name.count("\t")
        delimiter_counts[","] += name.count(",")
        delimiter_counts["\n"] += name.count("\n")
        if name.strip() == "":
            delimiter_counts[""] += 1

    # Check for abnormalities based on delimiter counts
    if len(column_names) == 1 and delimiter_counts["\t"] > 1:
        messages.append("Abnormal: Column names are not split correctly.")
        is_abnormal = True

    if any(delimiter_counts[d] > 3 for d in delimiter_counts if d != ""):
        messages.append("Abnormal: Too many delimiters in column names.")
        is_abnormal = True

    if delimiter_counts[""] > 3:
        messages.append("Abnormal: There are empty column names.")
        is_abnormal = True

    if any(delimiter_counts[d] > 3 for d in ["\t", ",", "\n"]):
        messages.append("Abnormal: Some column names contain unexpected characters.")
        is_abnormal = True

    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        messages.append("Missing values in columns:")
        messages.append(missing_values[missing_values > 0].to_string())
        is_abnormal = True

    # Check data types
    data_types = df.dtypes
    # messages.append(f"Data types of columns:\n{data_types}")

    # Check for constant values across any column
    constant_columns = df.columns[df.nunique() == 1].tolist()
    if constant_columns:
        messages.append(f"Abnormal: Columns with constant values: {constant_columns}")
        is_abnormal = True

    # Check for an unreasonable number of rows or columns
    if actual_shape[0] < 2 or actual_shape[1] < 2:
        messages.append(
            "Abnormal: DataFrame is too small (less than 2 rows or columns)."
        )
        is_abnormal = True

    # Compile results
    if verbose:
        print("\n".join(messages))
    return is_abnormal  # Data is abnormal


def fload(fpath, kind=None, **kwargs):
    """
    Load content from a file with specified file type.
    Parameters:
        fpath (str): The file path from which content will be loaded.
        kind (str): The file type to load. Supported options: 'docx', 'txt', 'md', 'html', 'json', 'yaml', 'xml', 'csv', 'xlsx', 'pdf'.
        **kwargs: Additional parameters for 'csv' and 'xlsx' file types.
    Returns:
        content: The content loaded from the file.
    """

    def load_txt_md(fpath):
        with open(fpath, "r") as file:
            content = file.read()
        return content

    def load_html(fpath):
        with open(fpath, "r") as file:
            content = file.read()
        return content

    def load_json(fpath, **kwargs):
        output=kwargs.pop("output","json")
        if output=='json': 
            with open(fpath, "r") as file:
                content = json.load(file)
            return content
        else:
            return pd.read_json(fpath,**kwargs)

    def load_yaml(fpath):
        with open(fpath, "r") as file:
            content = yaml.safe_load(file)
        return content

    def load_xml(fpath):
        tree = etree.parse(fpath)
        root = tree.getroot()
        return etree.tostring(root, pretty_print=True).decode()

    def get_comment(fpath, comment=None, encoding="utf-8", lines_to_check=5):
        """
        Detect comment characters in a file.

        Parameters:
        - fpath: str, the file path of the CSV file.
        - encoding: str, the encoding of the file (default is 'utf-8').
        - lines_to_check: int, number of lines to check for comment characters (default is 5).

        Returns:
        - str or None: the detected comment character, or None if no comment character is found.
        """
        comment_chars = [
            "#",
            "!",
            "//",
            ";",
        ]  # can use any character or string as a comment
        try:
            with open(fpath, "r", encoding=encoding) as f:
                lines = [next(f) for _ in range(lines_to_check)]
        except (UnicodeDecodeError, ValueError):
            with open(fpath, "r", encoding=get_encoding(fpath)) as f:
                lines = [next(f) for _ in range(lines_to_check)]
        for line in lines:
            for char in comment_chars:
                if line.startswith(char):
                    return char
        return None

    def load_csv(fpath, **kwargs):
        from pandas.errors import EmptyDataError

        engine = kwargs.pop("engine", "pyarrow")
        sep = kwargs.pop("sep", "\t")
        index_col = kwargs.pop("index_col", None)
        memory_map = kwargs.pop("memory_map", False)
        skipinitialspace = kwargs.pop("skipinitialspace", False)
        encoding = kwargs.pop("encoding", "utf-8")
        on_bad_lines = kwargs.pop("on_bad_lines", "skip")
        comment = kwargs.pop("comment", None)
        fmt=kwargs.pop("fmt",False)
        verbose=kwargs.pop("verbose",False)
        if verbose:
            use_pd("read_csv", verbose=verbose)
            return
        
        if comment is None:
            comment = get_comment(
                fpath, comment=None, encoding="utf-8", lines_to_check=5
            )

        try:
            df = pd.read_csv(
                fpath,
                engine=engine,
                index_col=index_col,
                memory_map=memory_map,
                encoding=encoding,
                comment=comment,
                skipinitialspace=skipinitialspace,
                sep=sep,
                on_bad_lines=on_bad_lines,
                **kwargs,
            )
        except:
            try:
                try:
                    if engine == "pyarrow":
                        df = pd.read_csv(
                            fpath,
                            engine=engine,
                            index_col=index_col,
                            encoding=encoding,
                            sep=sep,
                            on_bad_lines=on_bad_lines,
                            comment=comment,
                            **kwargs,
                        )
                    else:
                        df = pd.read_csv(
                            fpath,
                            engine=engine,
                            index_col=index_col,
                            memory_map=memory_map,
                            encoding=encoding,
                            sep=sep,
                            skipinitialspace=skipinitialspace,
                            on_bad_lines=on_bad_lines,
                            comment=comment,
                            **kwargs,
                        )

                    if is_df_abnormal(df, verbose=0):
                        raise ValueError("the df is abnormal")
                except (UnicodeDecodeError, ValueError):
                    encoding = get_encoding(fpath)
                    # print(f"utf-8 failed. Retrying with detected encoding: {encoding}")
                    if engine == "pyarrow":
                        df = pd.read_csv(
                            fpath,
                            engine=engine,
                            index_col=index_col,
                            encoding=encoding,
                            sep=sep,
                            on_bad_lines=on_bad_lines,
                            comment=comment,
                            **kwargs,
                        )
                    else:
                        df = pd.read_csv(
                            fpath,
                            engine=engine,
                            index_col=index_col,
                            memory_map=memory_map,
                            encoding=encoding,
                            sep=sep,
                            skipinitialspace=skipinitialspace,
                            on_bad_lines=on_bad_lines,
                            comment=comment,
                            **kwargs,
                        )
                    if is_df_abnormal(df, verbose=0):
                        raise ValueError("the df is abnormal")
            except Exception as e:
                separators = [",", "\t", ";", "|", " "]
                for sep in separators:
                    sep2show = sep if sep != "\t" else "\\t"
                    print(f'trying with: engine=pyarrow, sep="{sep2show}"')
                    try:
                        df = pd.read_csv(
                            fpath,
                            engine=engine,
                            skipinitialspace=skipinitialspace,
                            sep=sep,
                            on_bad_lines=on_bad_lines,
                            comment=comment,
                            **kwargs,
                        )
                        if not is_df_abnormal(df, verbose=0):  # normal
                            break
                        else:
                            if is_df_abnormal(df, verbose=0):
                                pass
                    except:
                        pass
                else:
                    engines = [None,"c", "python"]
                    for engine in engines:
                        separators = [",", "\t", ";", "|", " "]
                        for sep in separators:
                            try:
                                sep2show = sep if sep != "\t" else "\\t"
                                print(f"trying with: engine={engine}, sep='{sep2show}'")
                                df = pd.read_csv(
                                    fpath,
                                    engine=engine,
                                    sep=sep,
                                    on_bad_lines=on_bad_lines,
                                    comment=comment,
                                    **kwargs,
                                )
                                if not is_df_abnormal(df, verbose=0):
                                    break
                            except EmptyDataError as e:
                                continue
                        else:
                            pass
        display(df.head(2))
        print(f"shape: {df.shape}")
        return df

    def load_excel(fpath, **kwargs):
        engine = kwargs.get("engine", "openpyxl")
        verbose=kwargs.pop("verbose",False)
        if verbose:
            use_pd("read_excel", verbose=verbose)
        df = pd.read_excel(fpath, engine=engine, **kwargs)
        try:
            meata=pd.ExcelFile(fpath)
            print(f"n_sheet={len(meata.sheet_names)},\t'sheetname = 0 (default)':")
            [print(f"{i}:\t{i_}") for i,i_ in enumerate(meata.sheet_names)]
        except:
            pass
        return df

    def load_ipynb(fpath, **kwargs):
        as_version = kwargs.get("as_version", 4)
        with open(fpath, "r") as file:
            nb = nbformat.read(file, as_version=as_version)
            md_exporter = MarkdownExporter()
            md_body, _ = md_exporter.from_notebook_node(nb)
        return md_body

    def load_pdf(fpath, page="all", verbose=False, **kwargs):
        """
        Parameters:
        fpath: The path to the PDF file to be loaded.
        page (optional):
            Specifies which page or pages to extract text from. By default, it's set to "all", which means text from all
            pages will be returned. It can also be an integer to specify a single page number or a list of integers to
            specify multiple pages.
        verbose (optional):
            If True, prints the total number of pages processed.
        Functionality:
        It initializes an empty dictionary text_dict to store page numbers as keys and their corresponding text as values.
        It iterates through each page of the PDF file using a for loop.
        For each page, it extracts the text using PyPDF2's extract_text() method and stores it in text_dict with the page number incremented by 1 as the key.
        If the page parameter is an integer, it converts it into a list containing that single page number to ensure consistency in handling.
        If the page parameter is a NumPy array, it converts it to a list using the tolist() method to ensure compatibility with list operations.
        If verbose is True, it prints the total number of pages processed.
        If page is a list, it combines the text of the specified pages into a single string combined_text and returns it.
        If page is set to "all", it returns the entire text_dict containing text of all pages.
        If page is an integer, it returns the text of the specified page number.
        If the specified page is not found, it returns the string "Page is not found".
        """
        text_dict = {}
        with open(fpath, "rb") as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                if verbose:
                    print(f"processing page {page_num}")
                page_ = pdf_reader.pages[page_num]
                text_dict[page_num + 1] = page_.extract_text()
        if isinstance(page, int):
            page = [page]
        elif isinstance(page, np.ndarray):
            page = page.tolist()
        if verbose:
            print(f"total pages: {page_num}")
        if isinstance(page, list):
            combined_text = ""
            for page_num in page:
                combined_text += text_dict.get(page_num, "")
            return combined_text
        elif "all" in page.lower():
            combined_text = ""
            for i in text_dict.values():
                combined_text += i
            return combined_text
        else:
            return text_dict.get(int(page), "Page is not found")

    def load_docx(fpath):
        doc = Document(fpath)
        content = [para.text for para in doc.paragraphs]
        return content

    if kind is None:
        _, kind = os.path.splitext(fpath)
        kind = kind.lower()
    kind = kind.lstrip(".").lower()
    img_types = [
        "bmp",
        "eps",
        "gif",
        "icns",
        "ico",
        "im",
        "jpg",
        "jpeg",
        "jpeg2000",
        "msp",
        "pcx",
        "png",
        "ppm",
        "sgi",
        "spider",
        "tga",
        "tiff",
        "tif",
        "webp",
        "json",
    ]
    doc_types = [
        "docx",
        "txt",
        "md",
        "html",
        "json",
        "yaml",
        "xml",
        "csv",
        "xlsx",
        "pdf",
        "ipynb",
    ]
    zip_types = [
        "gz",
        "zip",
        "7z",
        "tar",
        "tar.gz",
        "tar.bz2",
        "bz2",
        "xz",
        "rar",
        "tgz",
    ]
    other_types = ["fcs"]
    supported_types = [*doc_types, *img_types, *zip_types, *other_types]
    if kind not in supported_types:
        print(
            f'Warning:\n"{kind}" is not in the supported list '
        )  # {supported_types}')
    # if os.path.splitext(fpath)[1][1:].lower() in zip_types:
    #     keep=kwargs.get("keep", False)
    #     ifile=kwargs.get("ifile",(0,0))
    #     kwargs.pop("keep",None)
    #     kwargs.pop("ifile",None)
    #     fpath_unzip=unzip(fpath)
    #     if isinstance(fpath_unzip,list):
    #         fpath_unzip=fpath_unzip[ifile[0]]
    #     if os.path.isdir(fpath_unzip):
    #         fpath_selected=listdir(fpath_unzip,kind=kind).fpath[ifile[1]]
    #         fpath_unzip=fpath_selected
    #     content_unzip=fload(fpath_unzip, **kwargs)
    #     if not keep:
    #         os.remove(fpath_unzip)
    #     return content_unzip

    if kind == "docx":
        return load_docx(fpath)
    elif kind == "txt" or kind == "md":
        return load_txt_md(fpath)
    elif kind == "html":
        return load_html(fpath)
    elif kind == "json":
        return load_json(fpath)
    elif kind == "yaml":
        return load_yaml(fpath)
    elif kind == "xml":
        return load_xml(fpath)
    elif kind == "csv":
        content = load_csv(fpath, **kwargs)
        return content
    elif kind in ["ods", "ods", "odt"]:
        engine = kwargs.get("engine", "odf")
        kwargs.pop("engine", None)
        return load_excel(fpath, engine=engine, **kwargs)
    elif kind == "xls":
        engine = kwargs.get("engine", "xlrd")
        kwargs.pop("engine", None)
        content = load_excel(fpath, engine=engine, **kwargs)
        display(content.head(3))
        return content
    elif kind == "xlsx":
        content = load_excel(fpath, **kwargs)
        display(content.head(3))
        return content
    elif kind == "ipynb":
        return load_ipynb(fpath, **kwargs)
    elif kind == "pdf":
        # print('usage:load_pdf(fpath, page="all", verbose=False)')
        return load_pdf(fpath, **kwargs)
    elif kind.lower() in img_types:
        print(f'Image ".{kind}" is loaded.')
        return load_img(fpath)
    elif kind=="gz" and fpath.endswith(".soft.gz"):
        import GEOparse
        return GEOparse.get_GEO(filepath=fpath)
    elif kind.lower() in zip_types:
        keep = kwargs.get("keep", False)
        fpath_unzip = unzip(fpath)
        if os.path.isdir(fpath_unzip):
            print(f"{fpath_unzip} is a folder. fload stoped.")
            fpath_list = os.listdir("./datasets/GSE10927_family.xml")
            print(f"{len(fpath_list)} files within the folder")
            if len(fpath_list) > 5:
                pp(fpath_list[:5])
                print("there are more ...")
            else:
                pp(fpath_list)
            return fpath_list
        elif os.path.isfile(fpath_unzip):
            print(f"{fpath_unzip} is a file.")
            content_unzip = fload(fpath_unzip, **kwargs)
            if not keep:
                os.remove(fpath_unzip)
            return content_unzip
        else:
            print(f"{fpath_unzip} does not exist or is a different type.")

    elif kind.lower() == "gmt":
        import gseapy as gp

        gene_sets = gp.read_gmt(fpath)
        return gene_sets

    elif kind.lower() == "fcs":
        import fcsparser

        # https://github.com/eyurtsev/fcsparser
        meta, data = fcsparser.parse(fpath, reformat_meta=True)
        return meta, data

    else:
        # try:
        #     content = load_csv(fpath, **kwargs)
        # except:
        try:
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.readlines()
            except UnicodeDecodeError:
                print("Failed to read as utf-8, trying different encoding...")
                with open(
                    fpath, "r", encoding=get_encoding(fpath)
                ) as f:  # Trying with a different encoding
                    content = f.readlines()
        except:
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                print("Failed to read as utf-8, trying different encoding...")
                with open(
                    fpath, "r", encoding=get_encoding(fpath)
                ) as f:  # Trying with a different encoding
                    content = f.read()
        return content


# Example usage
# txt_content = fload('sample.txt')
# md_content = fload('sample.md')
# html_content = fload('sample.html')
# json_content = fload('sample.json')
# yaml_content = fload('sample.yaml')
# xml_content = fload('sample.xml')
# csv_content = fload('sample.csv')
# xlsx_content = fload('sample.xlsx')
# docx_content = fload('sample.docx')


def fupdate(fpath, content=None, how="head"):
    """
    Update a file by adding new content at the top and moving the old content to the bottom.
    If the file is a JSON file, merge the new content with the old content.
    
    Parameters
    ----------
    fpath : str
        The file path where the content should be updated.
    content : str or dict, optional
        The new content to add at the top of the file (for text) or merge (for JSON).
        If not provided, the function will not add any new content.
    
    Notes
    -----
    - If the file at `fpath` does not exist, it will be created.
    - For text files, the new content will be added at the top, followed by the old content.
    - For JSON files, the new content will be merged with the existing JSON content.
    """
    content = content or ""
    file_ext = os.path.splitext(fpath)[1]
    how_s=["head", "tail","start","end","beginning", "stop",'last',"before"]
    how = strcmp(how, how_s)[0]
    print(how)
    add_where = 'head' if how in ["head", "start","beginning", "before"] else "tail"
    if "json" in file_ext.lower():
        old_content=fload(fpath,kind='json') if os.path.exists(fpath) else {}
        updated_content =  {**content,**old_content} if add_where=="head" else {**old_content, **content} if isinstance(content, dict) else old_content 
        fsave(fpath,updated_content)
    else:
        # Handle text file
        if os.path.exists(fpath):
            with open(fpath, "r") as file:
                old_content = file.read()
        else:
            old_content = ""

        # Write new content at the top followed by old content
        with open(fpath, "w") as file:
            if add_where=="head":
                file.write(content + "\n")
                file.write(old_content)
            else:
                file.write(old_content)
                file.write(content + "\n")


def fappend(fpath, content=None):
    """
    append new content at the end.
    """
    content = content or ""
    if os.path.exists(fpath):
        with open(fpath, "r") as file:
            old_content = file.read()
    else:
        old_content = ""

    with open(fpath, "w") as file:
        file.write(old_content)
        file.write(content)


def filter_kwargs(kws, valid_kwargs):
    if isinstance(valid_kwargs, dict):
        kwargs_filtered = {
            key: value for key, value in kws.items() if key in valid_kwargs.keys()
        }
    elif isinstance(valid_kwargs, list):
        kwargs_filtered = {
            key: value for key, value in kws.items() if key in valid_kwargs
        }
    return kwargs_filtered


def fsave(
    fpath,
    content,
    how="overwrite",
    kind=None,
    font_name="Times",
    font_size=10,
    spacing=6,
    **kwargs,
):
    """
    Save content into a file with specified file type and formatting.
    Parameters:
        fpath (str): The file path where content will be saved.
        content (list of str or dict): The content to be saved, where each string represents a paragraph or a dictionary for tabular data.
        kind (str): The file type to save. Supported options: 'docx', 'txt', 'md', 'html', 'pdf', 'csv', 'xlsx', 'json', 'xml', 'yaml'.
        font_name (str): The font name for text formatting (only applicable for 'docx', 'html', and 'pdf').
        font_size (int): The font size for text formatting (only applicable for 'docx', 'html', and 'pdf').
        spacing (int): The space after each paragraph (only applicable for 'docx').
        **kwargs: Additional parameters for 'csv', 'xlsx', 'json', 'yaml' file types.
    Returns:
        None
    """

    def save_content(fpath, content, mode="w", how="overwrite"):
        if "wri" in how.lower():
            with open(fpath, mode, encoding="utf-8") as file:
                file.write(content)
        elif "upd" in how.lower():
            fupdate(fpath, content=content)
        elif "app" in how.lower():
            fappend(fpath, content=content)

    def save_docx(fpath, content, font_name, font_size, spacing):
        if isinstance(content, str):
            content = content.split(". ")
        doc = docx.Document()
        for i, paragraph_text in enumerate(content):
            paragraph = doc.add_paragraph()
            run = paragraph.add_run(paragraph_text)
            font = run.font
            font.name = font_name
            font.size = docx.shared.Pt(font_size)
            if i != len(content) - 1:  # Add spacing for all but the last paragraph
                paragraph.space_after = docx.shared.Pt(spacing)
        doc.save(fpath)

    def save_txt_md(fpath, content, sep="\n", mode="w"):
        # Ensure content is a single string
        if isinstance(content, list):
            content = sep.join(content)
        save_content(fpath, sep.join(content), mode)

    def save_html(fpath, content, font_name, font_size, mode="w"):
        html_content = "<html><body>"
        for paragraph_text in content:
            html_content += f'<p style="font-family:{font_name}; font-size:{font_size}px;">{paragraph_text}</p>'
        html_content += "</body></html>"
        save_content(fpath, html_content, mode)

    def save_pdf(fpath, content, font_name, font_size):
        pdf = FPDF()
        pdf.add_page()
        # pdf.add_font('Arial','',r'/System/Library/Fonts/Supplemental/Arial.ttf',uni=True)
        pdf.set_font(font_name, "", font_size)
        for paragraph_text in content:
            pdf.multi_cell(0, 10, paragraph_text)
            pdf.ln(h="")
        pdf.output(fpath, "F")

    def save_csv(fpath, data, **kwargs):
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

        verbose=kwargs.pop("verbose",False)
        if verbose:
            use_pd("to_csv", verbose=verbose)
        kwargs_csv = dict(
            path_or_buf=None,
            sep=",",
            na_rep="",
            float_format=None,
            columns=None,
            header=True,
            index=True,
            index_label=None,
            mode="w",
            encoding="UTF-8",
            compression="infer",
            quoting=None,
            quotechar='"',
            lineterminator=None,
            chunksize=None,
            date_format=None,
            doublequote=True,
            escapechar=None,
            decimal=".",
            errors="strict",
            storage_options=None,
        )
        kwargs_valid = filter_kwargs(kwargs, kwargs_csv)
        df = pd.DataFrame(data)
        df.to_csv(fpath, **kwargs_valid)

    def save_xlsx(fpath, data, **kwargs):
        verbose=kwargs.pop("verbose",False)
        sheet_name = kwargs.pop("sheet_name", "Sheet1")
        if verbose:
            use_pd("to_excel", verbose=verbose)
        if any(kwargs):
            format_excel(df=data, filename=fpath, **kwargs)
        else:
            # Remove non-relevant kwargs
            irrelevant_keys = [
            "format", "usage", "cell", "width", "height", "height_max", "merge",
            "shade", "comment", "link", "protect", "number_format", "conditional_format", 
            "index_default"]
            for key in irrelevant_keys:
                kwargs.pop(key, None)

            df = pd.DataFrame(data)
            # Check if the file exists, then append the sheet, otherwise create a new file
            try:
                # Use ExcelWriter with append mode if the file exists
                with pd.ExcelWriter(fpath, engine='openpyxl', mode='a', if_sheet_exists='new') as writer:
                    df.to_excel(writer, sheet_name=sheet_name, index=False, **kwargs)
            except FileNotFoundError:
                # If file doesn't exist, create a new one
                df.to_excel(fpath, sheet_name=sheet_name, index=False, **kwargs)


    def save_ipynb(fpath, data, **kwargs):
        # Split the content by code fences to distinguish between code and markdown
        parts = data.split("```")
        cells = []

        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Even index: markdown content
                cells.append(nbformat.v4.new_markdown_cell(part.strip()))
            else:
                # Odd index: code content
                cells.append(nbformat.v4.new_code_cell(part.strip()))
        # Create a new notebook
        nb = nbformat.v4.new_notebook()
        nb["cells"] = cells
        # Write the notebook to a file
        with open(fpath, "w", encoding="utf-8") as ipynb_file:
            nbformat.write(nb, ipynb_file)

    # def save_json(fpath, data, **kwargs):
    #     with open(fpath, "w") as file:
    #         json.dump(data, file, **kwargs)

    def save_json(fpath_fname, var_dict_or_df):
        with open(fpath_fname, "w") as f_json:
            if isinstance(var_dict_or_df, pd.DataFrame):
                var_dict_or_df = var_dict_or_df.to_dict(orient="dict")
            if isinstance(var_dict_or_df, dict):
                for key, value in var_dict_or_df.items():
                    if isinstance(value, np.ndarray):
                        var_dict_or_df[key] = value.tolist()
            # Save the dictionary or list of dictionaries to a JSON file
            json.dump(var_dict_or_df, f_json, indent=4)

    # # Example usage:
    # sets = {"title": "mse_path_ MSE"}
    # jsonsave("/.json", sets)
    # # setss = jsonload("/.json")

    def save_yaml(fpath, data, **kwargs):
        with open(fpath, "w") as file:
            yaml.dump(data, file, **kwargs)

    def save_xml(fpath, data):
        root = etree.Element("root")
        if isinstance(data, dict):
            for key, val in data.items():
                child = etree.SubElement(root, key)
                child.text = str(val)
        else:
            raise ValueError("XML saving only supports dictionary data")
        tree = etree.ElementTree(root)
        tree.write(fpath, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    if kind is None:
        _, kind = os.path.splitext(fpath)
        kind = kind.lower()

    kind = kind.lstrip(".").lower()

    if kind not in [
        "docx",
        "txt",
        "md",
        "html",
        "pdf",
        "csv",
        "xlsx",
        "json",
        "xml",
        "yaml",
        "ipynb",
    ]:
        print(
            f"Warning:\n{kind} is not in the supported list ['docx', 'txt', 'md', 'html', 'pdf', 'csv', 'xlsx', 'json', 'xml', 'yaml']"
        )
    mode = kwargs.get("mode", "w")
    if kind == "docx" or kind == "doc":
        save_docx(fpath, content, font_name, font_size, spacing)
    elif kind == "txt":
        save_txt_md(fpath, content, sep="", mode=mode)
    elif kind == "md":
        save_txt_md(fpath, content, sep="", mode=mode)
    elif kind == "html":
        save_html(fpath, content, font_name, font_size)
    elif kind == "pdf":
        save_pdf(fpath, content, font_name, font_size)
    elif kind == "csv":
        save_csv(fpath, content, **kwargs)
    elif kind == "xlsx":
        save_xlsx(fpath, content, **kwargs)
    elif kind == "json":
        save_json(fpath, content)
    elif kind == "xml":
        save_xml(fpath, content)
    elif kind == "yaml":
        save_yaml(fpath, content, **kwargs)
    elif kind == "ipynb":
        save_ipynb(fpath, content, **kwargs)
    else:
        try:
            netfinder.downloader(url=content, dir_save=dirname(fpath), kind=kind)
        except:
            print(
                f"Error:\n{kind} is not in the supported list ['docx', 'txt', 'md', 'html', 'pdf', 'csv', 'xlsx', 'json', 'xml', 'yaml']"
            )


# # Example usage
# text_content = ["Hello, this is a sample text file.", "This is the second paragraph."]
# tabular_content = {"Name": ["Alice", "Bob"], "Age": [24, 30]}
# json_content = {"name": "Alice", "age": 24}
# yaml_content = {"Name": "Alice", "Age": 24}
# xml_content = {"Name": "Alice", "Age": 24}
# dir_save = "/Users/macjianfeng/Dropbox/Downloads/"
# fsave(dir_save + "sample.txt", text_content)
# fsave(dir_save + "sample.md", text_content)
# fsave(dir_save + "sample.html", text_content)
# fsave(dir_save + "sample.pdf", text_content)
# fsave(dir_save + "sample.docx", text_content)
# fsave(dir_save + "sample.csv", tabular_content, index=False)
# fsave(dir_save + "sample.xlsx", tabular_content, sheet_name="Sheet1", index=False)
# fsave(dir_save + "sample.json", json_content, indent=4)
# fsave(dir_save + "sample.yaml", yaml_content)
# fsave(dir_save + "sample.xml", xml_content)


def addpath(fpath):
    sys.path.insert(0, dir)


def dirname(fpath):
    """
    dirname: Extracting Directory Name from a File Path
    Args:
        fpath (str): the file or directory path
    Returns:
        str: directory, without filename
    """
    dirname_ = os.path.dirname(fpath)
    if not dirname_.endswith("/"):
        dirname_ = dirname_ + "/"
    return dirname_


def dir_name(fpath):  # same as "dirname"
    return dirname(fpath)


def basename(fpath):
    """
    basename: # Output: file.txt
    Args:
        fpath (str): the file or directory path
    Returns:
        str: # Output: file.txt
    """
    return os.path.basename(fpath)


def flist(fpath, contains="all"):
    all_files = [
        os.path.join(fpath, f)
        for f in os.listdir(fpath)
        if os.path.isfile(os.path.join(fpath, f))
    ]
    if isinstance(contains, list):
        filt_files = []
        for filter_ in contains:
            filt_files.extend(flist(fpath, filter_))
        return filt_files
    else:
        if "all" in contains.lower():
            return all_files
        else:
            filt_files = [f for f in all_files if isa(f, contains)]
            return filt_files


def sort_kind(df, by="name", ascending=True):
    if df[by].dtype == "object":  # Check if the column contains string values
        if ascending:
            sorted_index = df[by].str.lower().argsort()
        else:
            sorted_index = df[by].str.lower().argsort()[::-1]
    else:
        if ascending:
            sorted_index = df[by].argsort()
        else:
            sorted_index = df[by].argsort()[::-1]
    sorted_df = df.iloc[sorted_index].reset_index(drop=True)
    return sorted_df


def isa(content, kind):
    """
    content, kind='img'
    kinds file paths based on the specified kind.
    Args:
        content (str): Path to the file.
        kind (str): kind of file to kind. Default is 'img' for images. Other options include 'doc' for documents,
                    'zip' for ZIP archives, and 'other' for other types of files.
    Returns:
        bool: True if the file matches the kind, False otherwise.
    """
    if "img" in kind.lower() or "image" in kind.lower():
        return is_image(content)
    elif "doc" in kind.lower():
        return is_document(content)
    elif "zip" in kind.lower():
        return is_zip(content)
    elif "dir" in kind.lower() or ("f" in kind.lower() and "d" in kind.lower()):
        return os.path.isdir(content)
    elif "fi" in kind.lower():  # file
        return os.path.isfile(content)
    elif "num" in kind.lower():  # file
        return os.path.isfile(content)
    elif "text" in kind.lower() or "txt" in kind.lower():  # file
        return is_text(content)
    elif "color" in kind.lower():  # file
        return is_str_color(content)
    elif "html" in kind.lower():
        if content is None or not isinstance(content, str):
            return False
        # Remove leading and trailing whitespace
        content = content.strip()
        # Check for common HTML tags using regex
        # This pattern matches anything that looks like an HTML tag
        tag_pattern = r"<[a-zA-Z][^>]*>(.*?)</[a-zA-Z][^>]*>"
        # Check for any opening and closing tags
        if re.search(tag_pattern, content):
            return True
        # Additional checks for self-closing tags
        self_closing_tags = ["img", "br", "hr", "input", "meta", "link"]
        for tag in self_closing_tags:
            if f"<{tag}" in content:
                return True
        return False
    else:
        print(f"{kind} was not set up correctly")
        return False


import sys


def get_os():
    os_name = sys.platform
    if "dar" in os_name:
        return "macOS"
    else:
        if "win" in os_name:
            return "Windows"
        elif "linux" in os_name:
            return "Linux"
        else:
            print(f"{os_name}, returned 'None'")
            return None


def listdir(
    rootdir,
    kind=None,
    sort_by="name",
    ascending=True,
    contains=None,
    orient="list",
    output="df",  # 'list','dict','records','index','series'
    verbose=True,
):
    if kind is None:
        ls=os.listdir(rootdir)
        ls = [f for f in ls if not f.startswith('.') and not f.startswith('~')]
        print(ls)
        df_all = pd.DataFrame(
            {
                "fname": all_files,
                "fpath": [os.path.join(rootdir, i) for i in ls],
            }
        )
        display(df_all)
        return df_all
    if isinstance(kind, list):
        f_ = []
        for kind_ in kind:
            f_tmp = listdir(
                rootdir=rootdir,
                kind=kind_,
                sort_by=sort_by,
                ascending=ascending,
                contains=contains,
                orient=orient,
                output=output,
            )
            f_.append(f_tmp)
        if f_:
            return pd.concat(f_, ignore_index=True)

    if not kind.startswith("."):
        kind = "." + kind

    if os.path.isdir(rootdir):
        ls = os.listdir(rootdir)
        ls = [f for f in ls if not f.startswith('.') and not f.startswith('~')]
        fd = [".fd", ".fld", ".fol", ".fd", ".folder"]
        i = 0
        f = {
            "name": [],
            "length": [],
            "path": [],
            "created_time": [],
            "modified_time": [],
            "last_open_time": [],
            "size": [],
            "fname": [],
            "fpath": [],
        }
        for item in ls:
            item_path = os.path.join(rootdir, item)
            if item.startswith("."):
                continue
            filename, file_extension = os.path.splitext(item)
            is_folder = kind.lower() in fd and os.path.isdir(item_path)
            is_file = kind.lower() in file_extension.lower() and (
                os.path.isfile(item_path)
            )
            if kind in [".doc", ".img", ".zip"]:  # 选择大的类别
                if kind != ".folder" and not isa(item_path, kind):
                    continue
            elif kind in [".all"]:
                return flist(fpath, contains=contains)
            else:  # 精确到文件的后缀
                if not is_folder and not is_file:
                    continue
            f["name"].append(filename)
            f["length"].append(len(filename))
            f["path"].append(os.path.join(os.path.dirname(item_path), item))
            fpath = os.path.join(os.path.dirname(item_path), item)
            f["size"].append(round(os.path.getsize(fpath) / 1024 / 1024, 3))
            f["created_time"].append(
                pd.to_datetime(os.path.getctime(item_path), unit="s")
            )
            f["modified_time"].append(
                pd.to_datetime(os.path.getmtime(item_path), unit="s")
            )
            f["last_open_time"].append(
                pd.to_datetime(os.path.getatime(item_path), unit="s")
            )
            f["fname"].append(filename)  # will be removed
            f["fpath"].append(fpath)  # will be removed
            i += 1

        f["num"] = i
        f["rootdir"] = rootdir
        f["os"] = get_os()  # os.uname().machine
    else:
        raise FileNotFoundError(
            'The directory "{}" does NOT exist. Please check the directory "rootdir".'.format(
                rootdir
            )
        )

    f = pd.DataFrame(f)

    if contains is not None:
        f = f[f["name"].str.contains(contains, case=False)]

    if "nam" in sort_by.lower():
        f = sort_kind(f, by="name", ascending=ascending)
    elif "crea" in sort_by.lower():
        f = sort_kind(f, by="created_time", ascending=ascending)
    elif "modi" in sort_by.lower():
        f = sort_kind(f, by="modified_time", ascending=ascending)
    elif "s" in sort_by.lower() and "z" in sort_by.lower():
        f = sort_kind(f, by="size", ascending=ascending)

    if "df" in output:
        if verbose:
            display(f.head())
        return f
    else:
        if "l" in orient.lower():  # list # default
            res_output = Box(f.to_dict(orient="list"))
            return res_output
        if "d" in orient.lower():  # dict
            return Box(f.to_dict(orient="dict"))
        if "r" in orient.lower():  # records
            return Box(f.to_dict(orient="records"))
        if "in" in orient.lower():  # records
            return Box(f.to_dict(orient="index"))
        if "se" in orient.lower():  # records
            return Box(f.to_dict(orient="series"))


# Example usage:
# result = listdir('your_root_directory')
# print(result)
# df=listdir("/", contains='sss',sort_by='name',ascending=False)
# print(df.fname.to_list(),"\n",df.fpath.to_list())
def list_func(lib_name, opt="call"):
    if opt == "call":
        funcs = [func for func in dir(lib_name) if callable(getattr(lib_name, func))]
    else:
        funcs = dir(lib_name)
    return funcs


def func_list(lib_name, opt="call"):
    return list_func(lib_name, opt=opt)


def mkdir_nest(fpath: str) -> str:
    """
    Create nested directories based on the provided file path.

    Parameters:
    - fpath (str): The full file path for which the directories should be created.

    Returns:
    - str: The path of the created directory.
    """


    # Split the full path into directories
    f_slash = "/" if "mac" in get_os().lower() else "\\"
    if os.path.isdir(fpath):
        fpath =fpath+f_slash if not fpath.endswith(f_slash) else fpath
        print(fpath)
        return fpath
    dir_parts = fpath.split(f_slash)  # Split the path by the OS-specific separator

    # Start creating directories from the root to the desired path
    current_path = ""
    for part in dir_parts:
        if part:
            current_path = os.path.join(current_path, part)
            if not os.path.isdir(current_path):
                os.makedirs(current_path)
    if not current_path.endswith(f_slash):
        current_path += f_slash
    return current_path


def mkdir(pardir: str = None, chdir: str | list = None, overwrite=False):
    """
    Create a directory.

    Parameters:
    - pardir (str): Parent directory where the new directory will be created. If None, uses the current working directory.
    - chdir (str | list): Name of the new directory or a list of directories to create.
                          If None, a default name 'new_directory' will be used.
    - overwrite (bool): If True, overwrite the directory if it already exists. Defaults to False.

    Returns:
    - str: The path of the created directory or an error message.
    """

    rootdir = [] 
    if chdir is None:
        return mkdir_nest(pardir)
    if isinstance(chdir, str):
        chdir = [chdir] 
    chdir = list(set(chdir))
    if isinstance(pardir, str):  # Dir_parents should be 'str' type
        pardir = os.path.normpath(pardir) 
    if "mac" in get_os().lower() or "lin" in get_os().lower():
        stype = "/"
    elif "win" in get_os().lower():
        stype = "\\"
    else:
        stype = "/"
 
    if os.path.isdir(pardir):
        os.chdir(pardir)  # Set current path
        # Check if subdirectories are not empty
        if chdir:
            chdir.sort() 
            for folder in chdir: 
                child_tmp = os.path.join(pardir, folder)
                if not os.path.isdir(child_tmp):
                    os.mkdir("./" + folder)
                    print(f"\n {folder} was created successfully!\n")
                else:
                    if overwrite:
                        shutil.rmtree(child_tmp)
                        os.mkdir("./" + folder)
                        print(f"\n {folder} overwrite! \n")
                    else:
                        print(f"\n {folder} already exists! \n")
                rootdir.append(child_tmp + stype)  # Note down
        else:
            print("\nWarning: Dir_child doesn't exist\n")
    else:
        print("\nWarning: Dir_parent is not a directory path\n")
    # Dir is the main output, if only one dir, then str type is inconvenient
    if len(rootdir) == 1:
        rootdir = rootdir[0]
    rootdir=rootdir+stype if not rootdir.endswith(stype) else rootdir
    print(rootdir)
    return rootdir


def split_path(fpath):
    f_slash = "/" if "mac" in get_os().lower() else "\\"
    dir_par = f_slash.join(fpath.split(f_slash)[:-1])
    dir_ch = "".join(fpath.split(f_slash)[-1:])
    return dir_par, dir_ch


def figsave(*args, dpi=300):
    dir_save = None
    fname = None
    img = None
    f_slash = "/" if "mac" in get_os().lower() else "\\"
    for arg in args:
        if isinstance(arg, str):
            if f_slash in arg:
                dir_save = arg
            else:
                fname = arg
        elif isinstance(arg, (Image.Image, np.ndarray)):
            img = arg  # Store the PIL image if provided

    if dir_save is None:
        dir_save="./"
    print(dir_save)
    # dir_save=dir_save+f_slash if not dir_save.endswith(f_slash) else dir_save
    dir_par = f_slash.join(dir_save.split(f_slash)[:-1])
    dir_ch = "".join(dir_save.split(f_slash)[-1:])
    if not dir_par.endswith(f_slash):
        dir_par += f_slash
    print(dir_par)
    if fname is None:
        fname = dir_ch
    mkdir(dir_par)
    ftype = fname.split(".")[-1]
    if len(fname.split(".")) == 1:
        ftype = "nofmt"
        fname = dir_par + fname + "." + ftype
    else:
        fname = dir_par + fname

    # Save figure based on file type
    if ftype.lower() == "eps":
        plt.savefig(fname, format="eps", bbox_inches="tight")
        plt.savefig(
            fname.replace(".eps", ".pdf"),
            format="pdf",
            bbox_inches="tight",
            dpi=dpi,
            pad_inches=0,
        )
    elif ftype.lower() == "nofmt":  # default: both "tif" and "pdf"
        fname_corr = fname.replace("nofmt", "pdf")
        plt.savefig(
            fname_corr, format="pdf", bbox_inches="tight", dpi=dpi, pad_inches=0
        )
        fname = fname.replace("nofmt", "tif")
        plt.savefig(fname, format="tiff", dpi=dpi, bbox_inches="tight", pad_inches=0)
        print(f"default saving filetype: both 'tif' and 'pdf")
    elif ftype.lower() == "pdf":
        plt.savefig(fname, format="pdf", bbox_inches="tight", dpi=dpi, pad_inches=0)
    elif ftype.lower() in ["jpg", "jpeg", "png", "tiff", "tif"]:
        if img is not None:  # If a PIL image is provided
            if isinstance(img, Image.Image):
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                img.save(fname, format=ftype.upper(), dpi=(dpi, dpi))
            elif isinstance(img, np.ndarray):
                import cv2

                # Check the shape of the image to determine color mode
                if img.ndim == 2:
                    # Grayscale image
                    Image.fromarray(img).save(
                        fname, format=ftype.upper(), dpi=(dpi, dpi)
                    )
                elif img.ndim == 3:
                    if img.shape[2] == 3:
                        # RGB image
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        Image.fromarray(img).save(
                            fname, format=ftype.upper(), dpi=(dpi, dpi)
                        )
                    elif img.shape[2] == 4:
                        # RGBA image
                        img = cv2.cvtColor(
                            img, cv2.COLOR_BGRA2RGBA
                        )  # Convert BGRA to RGBA
                        Image.fromarray(img).save(
                            fname, format=ftype.upper(), dpi=(dpi, dpi)
                        )
                    else:
                        raise ValueError(
                            "Unexpected number of channels in the image array."
                        )
                else:
                    raise ValueError(
                        "Image array has an unexpected number of dimensions."
                    )
        else:
            plt.savefig(
                fname, format=ftype.lower(), dpi=dpi, bbox_inches="tight", pad_inches=0
            )
    # elif ftype.lower() == "png":
    #     plt.savefig(fname, format="png", dpi=dpi, bbox_inches="tight", transparent=True,pad_inches=0)
    # elif ftype.lower() in ["tiff", "tif"]:
    #     plt.savefig(fname, format="tiff", dpi=dpi, bbox_inches="tight",pad_inches=0)
    elif ftype.lower() == "emf":
        plt.savefig(fname, format="emf", dpi=dpi, bbox_inches="tight", pad_inches=0)
    elif ftype.lower() == "fig":
        plt.savefig(fname, format="pdf", bbox_inches="tight", dpi=dpi, pad_inches=0)
    print(f"\nSaved @: dpi={dpi}\n{fname}")


def is_str_color(s):
    # Regular expression pattern for hexadecimal color codes
    color_code_pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$"
    return re.match(color_code_pattern, s) is not None


def is_num(s):
    """
    Check if a string can be converted to a number (int or float).
    Parameters:
    - s (str): The string to check.
    Returns:
    - bool: True if the string can be converted to a number, False otherwise.
    """
    try:
        float(s)  # Try converting the string to a float
        return True
    except ValueError:
        return False


def isnum(s):
    return is_num(s)


def is_image(fpath):
    mime_type, _ = mimetypes.guess_type(fpath)
    if mime_type and mime_type.startswith("image"):
        return True
    else:
        return False


def is_document(fpath):
    mime_type, _ = mimetypes.guess_type(fpath)
    if mime_type and (
        mime_type.startswith("text/")
        or mime_type == "application/pdf"
        or mime_type == "application/msword"
        or mime_type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        or mime_type == "application/vnd.ms-excel"
        or mime_type
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        or mime_type == "application/vnd.ms-powerpoint"
        or mime_type
        == "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    ):
        return True
    else:
        return False


def is_zip(fpath):
    mime_type, _ = mimetypes.guess_type(fpath)
    if mime_type == "application/zip":
        return True
    else:
        return False


def adjust_spines(ax=None, spines=["left", "bottom"], distance=2):
    if ax is None:
        ax = plt.gca()
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(("outward", distance))  # outward by 2 points
            # spine.set_smart_bounds(True)
        else:
            spine.set_color("none")  # don't draw spine
    # turn off ticks where there is no spine
    if "left" in spines:
        ax.yaxis.set_ticks_position("left")
    else:
        ax.yaxis.set_ticks([])
    if "bottom" in spines:
        ax.xaxis.set_ticks_position("bottom")
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])


# And then plot the data:


def add_colorbar(im, width=None, pad=None, **kwargs):
    # usage: add_colorbar(im, width=0.01, pad=0.005, label="PSD (dB)", shrink=0.8)
    l, b, w, h = im.axes.get_position().bounds  # get boundaries
    width = width or 0.1 * w  # get width of the colorbar
    pad = pad or width  # get pad between im and cbar
    fig = im.axes.figure  # get figure of image
    cax = fig.add_axes([l + w + pad, b, width, h])  # define cbar Axes
    return fig.colorbar(im, cax=cax, **kwargs)  # draw cbar


# =============================================================================
# # for plot figures: setting rcParams
# usage: set_pub()
# or by setting sns.set_theme...see below:
# sns.set_theme(style="ticks", rc=params)      # 白色无刻度线，有坐标轴标度
# # sns.set_theme(style="whitegrid", rc=params)# 白色＋刻度线，无坐标轴标度
# # sns.set_theme(style="white", rc=params)    # 白色无刻度线，无坐标轴标度
# # sns.set_theme(style="dark", rc=params)     # 深色无刻度线，无坐标轴标度
# =============================================================================


def list2str(x_str):
    s = "".join(str(x) for x in x_str)
    return s


def str2list(str_):
    l = []
    [l.append(x) for x in str_]
    return l


def load_img(fpath):
    """
    Load an image from the specified file path.
    Args:
        fpath (str): The file path to the image.
    Returns:
        PIL.Image: The loaded image.
    Raises:
        FileNotFoundError: If the specified file is not found.
        OSError: If the specified file cannot be opened or is not a valid image file.
    """
    from PIL import Image

    try:
        img = Image.open(fpath)
        return img
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{fpath}' was not found.")
    except OSError:
        raise OSError(f"Unable to open file '{fpath}' or it is not a valid image file.")


def apply_filter(img, *args):
    # def apply_filter(img, filter_name, filter_value=None):
    """
    Apply the specified filter to the image.
    Args:
        img (PIL.Image): The input image.
        filter_name (str): The name of the filter to apply.
        **kwargs: Additional parameters specific to the filter.
    Returns:
        PIL.Image: The filtered image.
    """

    def correct_filter_name(filter_name):
        if "bl" in filter_name.lower() and "box" not in filter_name.lower():
            return "BLUR"
        elif "cont" in filter_name.lower():
            return "Contour"
        elif "det" in filter_name.lower():
            return "Detail"
        elif (
            "edg" in filter_name.lower()
            and "mo" not in filter_name.lower()
            and "f" not in filter_name.lower()
        ):
            return "EDGE_ENHANCE"
        elif "edg" in filter_name.lower() and "mo" in filter_name.lower():
            return "EDGE_ENHANCE_MORE"
        elif "emb" in filter_name.lower():
            return "EMBOSS"
        elif "edg" in filter_name.lower() and "f" in filter_name.lower():
            return "FIND_EDGES"
        elif "sh" in filter_name.lower() and "mo" not in filter_name.lower():
            return "SHARPEN"
        elif "sm" in filter_name.lower() and "mo" not in filter_name.lower():
            return "SMOOTH"
        elif "sm" in filter_name.lower() and "mo" in filter_name.lower():
            return "SMOOTH_MORE"
        elif "min" in filter_name.lower():
            return "MIN_FILTER"
        elif "max" in filter_name.lower():
            return "MAX_FILTER"
        elif "mod" in filter_name.lower():
            return "MODE_FILTER"
        elif "mul" in filter_name.lower():
            return "MULTIBAND_FILTER"
        elif "gau" in filter_name.lower():
            return "GAUSSIAN_BLUR"
        elif "box" in filter_name.lower():
            return "BOX_BLUR"
        elif "med" in filter_name.lower():
            return "MEDIAN_FILTER"
        else:
            supported_filters = [
                "BLUR",
                "CONTOUR",
                "DETAIL",
                "EDGE_ENHANCE",
                "EDGE_ENHANCE_MORE",
                "EMBOSS",
                "FIND_EDGES",
                "SHARPEN",
                "SMOOTH",
                "SMOOTH_MORE",
                "MIN_FILTER",
                "MAX_FILTER",
                "MODE_FILTER",
                "MULTIBAND_FILTER",
                "GAUSSIAN_BLUR",
                "BOX_BLUR",
                "MEDIAN_FILTER",
            ]
            raise ValueError(
                f"Unsupported filter: {filter_name}, should be one of: {supported_filters}"
            )

    for arg in args:
        if isinstance(arg, str):
            filter_name = arg
            filter_name = correct_filter_name(filter_name)
        else:
            filter_value = arg
    filter_name = filter_name.upper()  # Ensure filter name is uppercase

    # Supported filters
    supported_filters = {
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
        "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
        "EMBOSS": ImageFilter.EMBOSS,
        "FIND_EDGES": ImageFilter.FIND_EDGES,
        "SHARPEN": ImageFilter.SHARPEN,
        "SMOOTH": ImageFilter.SMOOTH,
        "SMOOTH_MORE": ImageFilter.SMOOTH_MORE,
        "MIN_FILTER": ImageFilter.MinFilter,
        "MAX_FILTER": ImageFilter.MaxFilter,
        "MODE_FILTER": ImageFilter.ModeFilter,
        "MULTIBAND_FILTER": ImageFilter.MultibandFilter,
        "GAUSSIAN_BLUR": ImageFilter.GaussianBlur,
        "BOX_BLUR": ImageFilter.BoxBlur,
        "MEDIAN_FILTER": ImageFilter.MedianFilter,
    }
    # Check if the filter name is supported
    if filter_name not in supported_filters:
        raise ValueError(
            f"Unsupported filter: {filter_name}, should be one of: {[i.lower() for i in supported_filters.keys()]}"
        )

    # Apply the filter
    if filter_name.upper() in [
        "BOX_BLUR",
        "GAUSSIAN_BLUR",
        "MEDIAN_FILTER",
        "MIN_FILTER",
        "MAX_FILTER",
        "MODE_FILTER",
    ]:
        radius = filter_value if filter_value is not None else 2
        return img.filter(supported_filters[filter_name](radius))
    elif filter_name in ["MULTIBAND_FILTER"]:
        bands = filter_value if filter_value is not None else None
        return img.filter(supported_filters[filter_name](bands))
    else:
        if filter_value is not None:
            print(
                f"{filter_name} doesn't require a value for {filter_value}, but it remains unaffected"
            )
        return img.filter(supported_filters[filter_name])


def imgsets(img, **kwargs):
    """
    Apply various enhancements and filters to an image using PIL's ImageEnhance and ImageFilter modules.

    Args:
        img (PIL.Image): The input image.
        sets (dict): A dictionary specifying the enhancements, filters, and their parameters.
        show (bool): Whether to display the enhanced image.
        show_axis (bool): Whether to display axes on the image plot.
        size (tuple): The size of the thumbnail, cover, contain, or fit operation.
        dpi (int): Dots per inch for the displayed image.
        figsize (tuple): The size of the figure for displaying the image.
        auto (bool): Whether to automatically enhance the image based on its characteristics.

    Returns:
        PIL.Image: The enhanced image.

    Supported enhancements and filters:
        - "sharpness": Adjusts the sharpness of the image. Values > 1 increase sharpness, while values < 1 decrease sharpness.
        - "contrast": Adjusts the contrast of the image. Values > 1 increase contrast, while values < 1 decrease contrast.
        - "brightness": Adjusts the brightness of the image. Values > 1 increase brightness, while values < 1 decrease brightness.
        - "color": Adjusts the color saturation of the image. Values > 1 increase saturation, while values < 1 decrease saturation.
        - "rotate": Rotates the image by the specified angle.
        - "crop" or "cut": Crops the image. The value should be a tuple specifying the crop box as (left, upper, right, lower).
        - "size": Resizes the image to the specified dimensions.
        - "thumbnail": Resizes the image to fit within the given size while preserving aspect ratio.
        - "cover": Resizes and crops the image to fill the specified size.
        - "contain": Resizes the image to fit within the specified size, adding borders if necessary.
        - "fit": Resizes and pads the image to fit within the specified size.
        - "filter": Applies various filters to the image (e.g., BLUR, CONTOUR, EDGE_ENHANCE).

    Note:
        The "color" and "enhance" enhancements are not implemented in this function.
    """
    supported_filters = [
        "BLUR",
        "CONTOUR",
        "DETAIL",
        "EDGE_ENHANCE",
        "EDGE_ENHANCE_MORE",
        "EMBOSS",
        "FIND_EDGES",
        "SHARPEN",
        "SMOOTH",
        "SMOOTH_MORE",
        "MIN_FILTER",
        "MAX_FILTER",
        "MODE_FILTER",
        "MULTIBAND_FILTER",
        "GAUSSIAN_BLUR",
        "BOX_BLUR",
        "MEDIAN_FILTER",
    ]
    print('usage: imgsets(dir_img, contrast="auto", rm=True, color=2.2)')
    print("\nlog:\n")

    def confirm_rembg_models(model_name):
        models_support = [
            "u2net",
            "u2netp",
            "u2net_human_seg",
            "u2net_cloth_seg",
            "silueta",
            "isnet-general-use",
            "isnet-anime",
            "sam",
        ]
        if model_name in models_support:
            print(f"model_name: {model_name}")
            return model_name
        else:
            print(
                f"{model_name} cannot be found, check the name:{models_support}, default('isnet-general-use') has been used"
            )
            return "isnet-general-use"

    def auto_enhance(img):
        """
        Automatically enhances the image based on its characteristics.
        Args:
            img (PIL.Image): The input image.
        Returns:
            dict: A dictionary containing the optimal enhancement values.
        """
        # Determine the bit depth based on the image mode
        if img.mode in ["1", "L", "P", "RGB", "YCbCr", "LAB", "HSV"]:
            # 8-bit depth per channel
            bit_depth = 8
        elif img.mode in ["RGBA", "CMYK"]:
            # 8-bit depth per channel + alpha (RGBA) or additional channels (CMYK)
            bit_depth = 8
        elif img.mode in ["I", "F"]:
            # 16-bit depth per channel (integer or floating-point)
            bit_depth = 16
        else:
            raise ValueError("Unsupported image mode")
        # Calculate the brightness and contrast for each channel
        num_channels = len(img.getbands())
        brightness_factors = []
        contrast_factors = []
        for channel in range(num_channels):
            channel_histogram = img.split()[channel].histogram()
            brightness = sum(i * w for i, w in enumerate(channel_histogram)) / sum(
                channel_histogram
            )
            channel_min, channel_max = img.split()[channel].getextrema()
            contrast = channel_max - channel_min
            # Adjust calculations based on bit depth
            normalization_factor = 2**bit_depth - 1  # Max value for the given bit depth
            brightness_factor = (
                1.0 + (brightness - normalization_factor / 2) / normalization_factor
            )
            contrast_factor = (
                1.0 + (contrast - normalization_factor / 2) / normalization_factor
            )
            brightness_factors.append(brightness_factor)
            contrast_factors.append(contrast_factor)
        # Calculate the average brightness and contrast factors across channels
        avg_brightness_factor = sum(brightness_factors) / num_channels
        avg_contrast_factor = sum(contrast_factors) / num_channels
        return {"brightness": avg_brightness_factor, "contrast": avg_contrast_factor}

    # Load image if input is a file path
    if isinstance(img, str):
        img = load_img(img)
    img_update = img.copy()
    # Auto-enhance image if requested

    auto = kwargs.get("auto", False)
    show = kwargs.get("show", True)
    show_axis = kwargs.get("show_axis", False)
    size = kwargs.get("size", None)
    figsize = kwargs.get("figsize", None)
    dpi = kwargs.get("dpi", 100)

    if auto:
        kwargs = {**auto_enhance(img_update), **kwargs}

    for k, value in kwargs.items():
        if "shar" in k.lower():
            enhancer = ImageEnhance.Sharpness(img_update)
            img_update = enhancer.enhance(value)
        elif all(
            ["col" in k.lower(), "bg" not in k.lower(), "background" not in k.lower()]
        ):
            enhancer = ImageEnhance.Color(img_update)
            img_update = enhancer.enhance(value)
        elif "contr" in k.lower():
            if value and isinstance(value, (float, int)):
                enhancer = ImageEnhance.Contrast(img_update)
                img_update = enhancer.enhance(value)
            else:
                print("autocontrasted")
                img_update = ImageOps.autocontrast(img_update)
        elif "bri" in k.lower():
            enhancer = ImageEnhance.Brightness(img_update)
            img_update = enhancer.enhance(value)
        elif "cro" in k.lower() or "cut" in k.lower():
            img_update = img_update.crop(value)
        elif "rota" in k.lower():
            if isinstance(value, str):
                value = detect_angle(img_update, by=value)
                print(f"rotated by {value}°")
            img_update = img_update.rotate(value)

        elif "si" in k.lower():
            if isinstance(value, tuple):
                value = list(value)
            value = [int(i) for i in value]
            img_update = img_update.resize(value)
        elif "thum" in k.lower():
            img_update.thumbnail(value)
        elif "cover" in k.lower():
            img_update = ImageOps.cover(img_update, size=value)
        elif "contain" in k.lower():
            img_update = ImageOps.contain(img_update, size=value)
        elif "fit" in k.lower():
            if isinstance(value, dict):
                for filter_name, filter_value in value.items():
                    img_update = apply_filter(img_update, filter_name, filter_value)
            else:
                img_update = ImageOps.fit(img_update, size=value)
        elif "pad" in k.lower():
            img_update = ImageOps.pad(img_update, size=value)
        elif "rem" in k.lower() or "rm" in k.lower() or "back" in k.lower():
            if isinstance(value, bool):
                session = new_session("isnet-general-use")
                img_update = remove(img_update, session=session)
            elif value and isinstance(value, (int, float, list)):
                print("https://github.com/danielgatis/rembg/blob/main/USAGE.md")
                if isinstance(value, int):
                    value = [value]
                if len(value) < 2:
                    img_update = remove(
                        img_update,
                        alpha_matting=True,
                        alpha_matting_background_threshold=value,
                    )
                elif 2 <= len(value) < 3:
                    img_update = remove(
                        img_update,
                        alpha_matting=True,
                        alpha_matting_background_threshold=value[0],
                        alpha_matting_foreground_threshold=value[1],
                    )
                elif 3 <= len(value) < 4:
                    img_update = remove(
                        img_update,
                        alpha_matting=True,
                        alpha_matting_background_threshold=value[0],
                        alpha_matting_foreground_threshold=value[1],
                        alpha_matting_erode_size=value[2],
                    )
            elif isinstance(value, tuple):  # replace the background color
                if len(value) == 3:
                    value += (255,)
                img_update = remove(img_update, bgcolor=value)
            elif isinstance(value, str):
                if confirm_rembg_models(value):
                    img_update = remove(img_update, session=new_session(value))
                else:
                    img_update = remove(img_update)
        elif "bg" in k.lower() and "color" in k.lower():
            if isinstance(value, list):
                value = tuple(value)
            if isinstance(value, tuple):  # replace the background color
                if len(value) == 3:
                    value += (255,)
                img_update = remove(img_update, bgcolor=value)
    # Display the image if requested
    if show:
        if figsize is None:
            plt.figure(dpi=dpi)
        else:
            plt.figure(figsize=figsize, dpi=dpi)
        plt.imshow(img_update)
        if show_axis:
            plt.axis("on")  # Turn on axis
            plt.minorticks_on()
            plt.grid(
                which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.7
            )

        else:
            plt.axis("off")  # Turn off axis
    return img_update


def thumbnail(dir_img_list, figsize=(10, 10), dpi=100, dir_save=None, kind=".png"):
    """
    Display a thumbnail figure of all images in the specified directory.
    Args:
        dir_img_list (list): List of the Directory containing the images.
    """
    num_images = len(dir_img_list)
    if not kind.startswith("."):
        kind = "." + kind

    if num_images == 0:
        print("No images found to display.")
        return
    grid_size = int(num_images**0.5) + 1  # Determine grid size
    fig, axs = plt.subplots(grid_size, grid_size, figsize=figsize, dpi=dpi)
    for ax, image_file in zip(axs.flatten(), dir_img_list):
        try:
            img = Image.open(image_file)
            ax.imshow(img)
            ax.axis("off")
        except:
            continue
    # for ax in axs.flatten():
    #     ax.axis('off')
    [ax.axis("off") for ax in axs.flatten()]
    plt.tight_layout()
    if dir_save is None:
        plt.show()
    else:
        if basename(dir_save):
            fname = basename(dir_save) + kind
        else:
            fname = "_thumbnail_" + basename(dirname(dir_save)[:-1]) + ".png"
        if dirname(dir_img_list[0]) == dirname(dir_save):
            figsave(dirname(dir_save[:-1]), fname)
        else:
            figsave(dirname(dir_save), fname)


# usage:
# fpath = "/Users/macjianfeng/Dropbox/github/python/py2ls/tests/xample_netfinder/images/"
# thumbnail(listdir(fpath,'png').fpath.to_list(),dir_save=dirname(fpath))
def read_mplstyle(style_file):
    # Load the style file
    plt.style.use(style_file)

    # Get the current style properties
    style_dict = plt.rcParams

    # Convert to dictionary
    style_dict = dict(style_dict)
    # Print the style dictionary
    for i, j in style_dict.items():
        print(f"\n{i}::::{j}")
    return style_dict


# #example usage:
# style_file = "/ std-colors.mplstyle"
# style_dict = read_mplstyle(style_file)


# search and fine the director of the libary, which installed at local
def dir_lib(lib_oi):
    import site

    # Get the site-packages directory
    f = listdir(site.getsitepackages()[0], "folder")

    # Find Seaborn directory within site-packages
    dir_list = []
    for directory in f.fpath:
        if lib_oi in directory.lower():
            dir_list.append(directory)

    if dir_list != []:
        print(f"{lib_oi} directory:", dir_list)
    else:
        print(f"Cannot find the {lib_oi} in site-packages directory.")
    return dir_list


# example usage:
# dir_lib("seaborn")

""" 
    # n = 7
    # clist = get_color(n, cmap="auto", how="linspace")  # get_color(100)
    # plt.figure(figsize=[8, 5], dpi=100)
    # x = np.linspace(0, 2 * np.pi, 50) * 100
    # y = np.sin(x)
    # for i in range(1, n + 1):
    #     plt.plot(x, y + i, c=clist[i - 1], lw=5, label=str(i))
    # plt.legend()
    # plt.ylim(-2, 20)
    # figsets(plt.gca(), {"style": "whitegrid"}) """


class FileInfo:
    def __init__(
        self,
        size,
        creation_time,
        ctime,
        mod_time,
        mtime,
        parent_dir,
        fname,
        kind,
        extra_info=None,
    ):
        self.size = size
        self.creation_time = creation_time
        self.ctime = ctime
        self.mod_time = mod_time
        self.mtime = mtime
        self.parent_dir = parent_dir
        self.fname = fname
        self.kind = kind
        if extra_info:
            for key, value in extra_info.items():
                setattr(self, key, value)
        print("to show the res: 'finfo(fpath).show()'")

    def __repr__(self):
        return (
            f"FileInfo(size={self.size} MB, creation_time='{self.creation_time}', "
            f"ctime='{self.ctime}', mod_time='{self.mod_time}', mtime='{self.mtime}', "
            f"parent_dir='{self.parent_dir}', fname='{self.fname}', kind='{self.kind}')"
        )

    def __str__(self):
        return (
            f"FileInfo:\n"
            f"  Size: {self.size} MB\n"
            f"  Creation Time: {self.creation_time}\n"
            f"  CTime: {self.ctime}\n"
            f"  Modification Time: {self.mod_time}\n"
            f"  MTime: {self.mtime}\n"
            f"  Parent Directory: {self.parent_dir}\n"
            f"  File Name: {self.fname}\n"
            f"  Kind: {self.kind}"
        )

    def show(self):
        # Convert the object to a dictionary
        return {
            "size": self.size,
            "creation_time": self.creation_time,
            "ctime": self.ctime,
            "mod_time": self.mod_time,
            "mtime": self.mtime,
            "parent_dir": self.parent_dir,
            "fname": self.fname,
            "kind": self.kind,
            **{
                key: getattr(self, key)
                for key in vars(self)
                if key
                not in [
                    "size",
                    "creation_time",
                    "ctime",
                    "mod_time",
                    "mtime",
                    "parent_dir",
                    "fname",
                    "kind",
                ]
            },
        }


def finfo(fpath):
    fname, fmt = os.path.splitext(fpath)
    dir_par = os.path.dirname(fpath) + "/"
    data = {
        "size": round(os.path.getsize(fpath) / 1024 / 1024, 3),
        "creation_time": time.ctime(os.path.getctime(fpath)),
        "ctime": time.ctime(os.path.getctime(fpath)),
        "mod_time": time.ctime(os.path.getmtime(fpath)),
        "mtime": time.ctime(os.path.getmtime(fpath)),
        "parent_dir": dir_par,
        "fname": fname.replace(dir_par, ""),
        "kind": fmt,
    }
    extra_info = {}
    if data["kind"] == ".pdf":
        extra_info = pdfinfo_from_path(fpath)

    return FileInfo(
        size=data["size"],
        creation_time=data["creation_time"],
        ctime=data["ctime"],
        mod_time=data["mod_time"],
        mtime=data["mtime"],
        parent_dir=data["parent_dir"],
        fname=data["fname"],
        kind=data["kind"],
        extra_info=extra_info,
    )


# ! format excel file
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment
from openpyxl.formatting.rule import ColorScaleRule


def hex2argb(hex_color):
    """
        Convert a hex color code to aARGB format required by openpyxl.

        :param hex_color: A hex color code in the format #RRGGBB, RRGGBB, or aARRGGBB.
        :return: A hex color code in the format aARRGGBB.

    # Example usage
    print(hex_to_argb("FFFF00"))  # Outputs: FFFFFF00
    print(hex_to_argb("#DF4245"))  # Outputs: FFFFFF00
    print(hex_to_argb("FF00FF00"))  # Outputs: FF00FF00 (already in aARGB format)
    """
    # Remove the hash if present
    if hex_color.startswith("#"):
        hex_color = hex_color[1:]

    # Check if it's already in aARGB format (8 characters)
    if len(hex_color) == 8:
        return hex_color

    # Otherwise, assume it's in RRGGBB format and prepend FF for opaque
    if len(hex_color) == 6:
        return f"FF{hex_color}"
    if len(hex_color) == 7:
        return f"F{hex_color}"
    else:
        if len(hex_color) > 8:
            return hex_color[-9:]
        else:
            return "F" * (9 - len(hex_color)) + hex_color
    raise ValueError(
        "Invalid hex color format. Use RRGGBB, #RRGGBB, or aARRGGBB format."
    )


def convert_indices_to_range(row_slice, col_slice):
    """Convert numerical row and column slices to Excel-style range strings."""
    start_row = row_slice.start + 1
    end_row = row_slice.stop if row_slice.stop is not None else None
    start_col = col_slice.start + 1
    end_col = col_slice.stop if col_slice.stop is not None else None

    start_col_letter = get_column_letter(start_col)
    end_col_letter = get_column_letter(end_col) if end_col else None
    return (
        f"{start_col_letter}{start_row}:{end_col_letter}{end_row}"
        if end_col_letter
        else f"{start_col_letter}{start_row}"
    )


def apply_format(ws, cell, cell_range):
    """Apply cell formatting to a specified range."""
    cell_font, cell_fill, cell_alignment, border = None, None, None, None
    kws_cell = ["font", "fill", "alignment", "border"]
    for K, _ in cell.items():
        if strcmp(K, kws_cell)[0] == "font":
            #! font
            font_color = "000000"
            font_name = "Arial"
            font_underline = "none"
            font_size = 14
            font_bold = False
            font_strike = False
            font_italic = False
            kws_font = [
                "name",
                "size",
                "bold",
                "underline",
                "color",
                "strike",
                "italic",
            ]
            for k_, v_ in cell.get(K, {}).items():
                if strcmp(k_, kws_font)[0] == "name":
                    font_name = v_
                elif strcmp(k_, kws_font)[0] == "size":
                    font_size = v_
                elif strcmp(k_, kws_font)[0] == "bold":
                    font_bold = v_
                elif strcmp(k_, kws_font)[0] == "underline":
                    font_underline = strcmp(v_, ["none", "single", "double"])[0]
                elif strcmp(k_, kws_font)[0] == "color":
                    font_color = hex2argb(v_)
                elif strcmp(k_, kws_font)[0] == "strike":
                    font_strike = v_
                elif strcmp(k_, kws_font)[0] == "italic":
                    font_italic = v_

            cell_font = Font(
                name=font_name,
                size=font_size,
                bold=font_bold,
                italic=font_italic,
                underline=font_underline,
                strike=font_strike,
                color=font_color,
            )

        if strcmp(K, kws_cell)[0] == "fill":
            #! fill
            kws_fill = ["start_color", "end_color", "fill_type", "color"]
            kws_fill_type = [
                "darkVertical",
                "lightDown",
                "lightGrid",
                "solid",
                "darkDown",
                "lightGray",
                "lightUp",
                "gray0625",
                "lightVertical",
                "lightHorizontal",
                "darkHorizontal",
                "gray125",
                "darkUp",
                "mediumGray",
                "darkTrellis",
                "darkGray",
                "lightTrellis",
                "darkGrid",
            ]
            start_color, end_color, fill_type = "FFFFFF", "FFFFFF", "solid"  # default
            for k, v in cell.get(K, {}).items():
                if strcmp(k, kws_fill)[0] == "color":
                    start_color, end_color = hex2argb(v), hex2argb(v)
                    break
            for k, v in cell.get(K, {}).items():
                if strcmp(k, kws_fill)[0] == "start_color":
                    start_color = hex2argb(v)
                elif strcmp(k, kws_fill)[0] == "end_color":
                    end_color = hex2argb(v)
                elif strcmp(k, kws_fill)[0] == "fill_type":
                    fill_type = strcmp(v, kws_fill_type)[0]
            cell_fill = PatternFill(
                start_color=start_color,
                end_color=end_color,
                fill_type=fill_type,
            )

        if strcmp(K, kws_cell)[0] == "alignment":
            #! alignment
            # default
            align_horizontal = "general"
            align_vertical = "center"
            align_rot = 0
            align_wrap = False
            align_shrink = False
            align_indent = 0
            kws_align = [
                "horizontal",
                "ha",
                "vertical",
                "va",
                "text_rotation",
                "rotat",
                "rot",
                "wrap_text",
                "wrap",
                "shrink_to_fit",
                "shrink",
                "indent",
            ]
            for k, v in cell.get(K, {}).items():
                if strcmp(k, kws_align)[0] in ["horizontal", "ha"]:
                    align_horizontal = strcmp(
                        v, ["general", "left", "right", "center"]
                    )[0]
                elif strcmp(k, kws_align)[0] in ["vertical", "va"]:
                    align_vertical = strcmp(v, ["top", "center", "bottom"])[0]
                elif strcmp(k, kws_align)[0] in ["text_rotation", "rotat", "rot"]:
                    align_rot = v
                elif strcmp(k, kws_align)[0] in ["wrap_text", "wrap"]:
                    align_wrap = v
                elif strcmp(k, kws_align)[0] in [
                    "shrink_to_fit",
                    "shrink",
                    "wrap_text",
                    "wrap",
                ]:
                    align_shrink = v
                elif strcmp(k, kws_align)[0] in ["indent"]:
                    align_indent = v
            cell_alignment = Alignment(
                horizontal=align_horizontal,
                vertical=align_vertical,
                text_rotation=align_rot,
                wrap_text=align_wrap,
                shrink_to_fit=align_shrink,
                indent=align_indent,
            )

        if strcmp(K, kws_cell)[0] == "border":
            #! border
            kws_border = [
                "color_left",
                "color_l",
                "color_right",
                "color_r",
                "color_top",
                "color_t",
                "color_bottom",
                "color_b",
                "color_diagonal",
                "color_d",
                "color_outline",
                "color_o",
                "color_vertical",
                "color_v",
                "color_horizontal",
                "color_h",
                "color",
                "style_left",
                "style_l",
                "style_right",
                "style_r",
                "style_top",
                "style_t",
                "style_bottom",
                "style_b",
                "style_diagonal",
                "style_d",
                "style_outline",
                "style_o",
                "style_vertical",
                "style_v",
                "style_horizontal",
                "style_h",
                "style",
            ]
            # * border color
            border_color_l, border_color_r, border_color_t, border_color_b = (
                "FF000000",
                "FF000000",
                "FF000000",
                "FF000000",
            )
            border_color_d, border_color_o, border_color_v, border_color_h = (
                "FF000000",
                "FF000000",
                "FF000000",
                "FF000000",
            )
            # get colors config
            for k, v in cell.get(K, {}).items():
                if strcmp(k, kws_border)[0] in ["color"]:
                    border_color_all = hex2argb(v)
                    # 如果设置了color,表示其它的所有的都设置成为一样的
                    # 然后再才开始自己定义其它的color
                    border_color_l, border_color_r, border_color_t, border_color_b = (
                        border_color_all,
                        border_color_all,
                        border_color_all,
                        border_color_all,
                    )
                    border_color_d, border_color_o, border_color_v, border_color_h = (
                        border_color_all,
                        border_color_all,
                        border_color_all,
                        border_color_all,
                    )
                elif strcmp(k, kws_border)[0] in ["color_left", "color_l"]:
                    border_color_l = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_right", "color_r"]:
                    border_color_r = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_top", "color_t"]:
                    border_color_t = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_bottom", "color_b"]:
                    border_color_b = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_diagonal", "color_d"]:
                    border_color_d = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_outline", "color_o"]:
                    border_color_o = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_vertical", "color_v"]:
                    border_color_v = hex2argb(v)
                elif strcmp(k, kws_border)[0] in ["color_horizontal", "color_h"]:
                    border_color_h = hex2argb(v)
            # *border style
            border_styles = [
                "thin",
                "medium",
                "thick",
                "dotted",
                "dashed",
                "hair",
                "mediumDashed",
                "dashDot",
                "dashDotDot",
                "slantDashDot",
                "none",
            ]
            border_style_l, border_style_r, border_style_t, border_style_b = (
                None,
                None,
                None,
                None,
            )
            border_style_d, border_style_o, border_style_v, border_style_h = (
                None,
                None,
                None,
                None,
            )
            # get styles config
            for k, v in cell.get(K, {}).items():
                # if not "style" in k:
                #     break
                if strcmp(k, kws_border)[0] in ["style"]:
                    border_style_all = strcmp(v, border_styles)[0]
                    # 如果设置了style,表示其它的所有的都设置成为一样的
                    # 然后再才开始自己定义其它的style
                    border_style_l, border_style_r, border_style_t, border_style_b = (
                        border_style_all,
                        border_style_all,
                        border_style_all,
                        border_style_all,
                    )
                    border_style_d, border_style_o, border_style_v, border_style_h = (
                        border_style_all,
                        border_style_all,
                        border_style_all,
                        border_style_all,
                    )
                elif strcmp(k, kws_border)[0] in ["style_left", "style_l"]:
                    border_style_l = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_right", "style_r"]:
                    border_style_r = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_top", "style_t"]:
                    border_style_t = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_bottom", "style_b"]:
                    border_style_b = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_diagonal", "style_d"]:
                    border_style_d = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_outline", "style_o"]:
                    border_style_o = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_vertical", "style_v"]:
                    border_style_v = strcmp(v, border_styles)[0]
                elif strcmp(k, kws_border)[0] in ["style_horizontal", "style_h"]:
                    border_style_h = strcmp(v, border_styles)[0]
            # * apply border config
            border = Border(
                left=Side(border_style=border_style_l, color=border_color_l),
                right=Side(border_style=border_style_r, color=border_color_r),
                top=Side(border_style=border_style_t, color=border_color_t),
                bottom=Side(border_style=border_style_b, color=border_color_b),
                diagonal=Side(border_style=border_style_d, color=border_color_d),
                diagonal_direction=0,
                outline=Side(border_style=border_style_o, color=border_color_o),
                vertical=Side(border_style=border_style_v, color=border_color_v),
                horizontal=Side(border_style=border_style_h, color=border_color_h),
            )

    #! final apply configs
    for row in ws[cell_range]:
        for cell_ in row:
            if cell_font:
                cell_.font = cell_font
            if cell_fill:
                cell_.fill = cell_fill
            if cell_alignment:
                cell_.alignment = cell_alignment
            if border:
                cell_.border = border


def format_excel(
    df=None,
    filename=None,
    sheet_name=0,
    usage=False,
    cell=None,  # dict: or list for multiple locs setting:
    width=None,  # dict
    height=None,  # dict e.g., {2: 50, 3: 25},  keys are columns
    height_max=25,
    merge=None,  # tuple e.g.,  (slice(0, 1), slice(1, 3)),
    shade=None,  # dict
    comment=None,  # dict e.g., {(2, 4): "This is a comment"},
    link=None,  # dict e.g., {(2, 2): "https://example.com"},
    protect=None,  # dict
    number_format=None,  # dict: e.g., {1:"0.00", 2:"#,##0",3:"0%",4:"$#,##0.00"}
    data_validation=None,  # dict
    conditional_format=None,  # dict
    **kwargs,
):
    if not isinstance(df, pd.DataFrame):
        try:
            print(f"is loading file {os.path.basename(df)}")
            df = fload(df)
        except:
            print(f"check the fpath:{df}")
    if filename is None:
        filename = str(datetime.now().strftime("%y%m%d_%H.xlsx"))
    # !show usage:
    func_xample = """
# Example usage
data = {
    "Header 1": [10, 2000000, 30],
    "Header 2": [
        40000,
        '"start_color": "4F81BD", "end_color","start_color": "a1cd1e","start_color": "4F81BD", "end_color","start_color": "a1cd1e"',
        60,
    ],
    "Header 3": [70, 80, 90],
}
df = pd.DataFrame(data)


format_excel(
    df,
    filename="example.xlsx",
    sheet_name="Sheet1",
    cell=[
        {
            (slice(0, 1), slice(0, len(df.columns))): {
                "font": {
                    "name": "Calibri",  # Font name
                    "size": 14,  # Font size
                    "bold": True,  # Bold text
                    "italic": False,  # Italic text
                    "underline": "single",  # Underline (single, double)
                    "color": "#FFFFFF",  # Font color
                },
                "fill": {
                    "start_color": "a1cd1e",  # Starting color
                    "end_color": "4F81BD",  # Ending color (useful for gradients)
                    "fill_type": "solid",  # Fill type (solid, gradient, etc.)
                },
                "alignment": {
                    "horizontal": "center",  # Horizontal alignment (left, center, right)
                    "vertical": "center",  # Vertical alignment (top, center, bottom)
                    "wrap_text": True,  # Wrap text in the cell
                    "shrink_to_fit": True,  # Shrink text to fit within cell
                    "text_rotation": 0,  # Text rotation angle
                },
                "border": {
                    "left": "thin",
                    "right": "thin",
                    "top": "thin",
                    "bottom": "thin",
                    "color": "000000",  # Border color
                },
            }
        },
        {
            (slice(0, 3), slice(1, 3)): {
                "font": {
                    "name": "Arial",  # Font name
                    "size": 12,  # Font size
                    "bold": False,  # Bold text
                    "italic": True,  # Italic text
                    "underline": None,  # No underline
                    "color": "#000000",  # Font color
                },
                "fill": {
                    "start_color": "#c61313",  # Background color
                    "end_color": "#490606",  # End color
                    "fill_type": "solid",  # Fill type
                },
                "alignment": {
                    "horizontal": "left",  # Horizontal alignment
                    "vertical": "top",  # Vertical alignment
                    "wrap_text": True,  # Enable text wrapping
                    "shrink_to_fit": False,  # Disable shrink to fit
                    "indent": 1,  # Indentation level
                    "text_rotation": 0,  # Text rotation angle
                },
                "border": {
                    "left": "thin",  # Left border style
                    "right": "thin",  # Right border style
                    "top": "thin",  # Top border style
                    "bottom": "thin",  # Bottom border style
                    "color": "000000",  # Border color
                },
            }
            # * border settings
            # "thin": Thin border line
            # "medium": Medium border line
            # "thick": Thick border line
            # "dotted": Dotted border line
            # "dashed": Dashed border line
            # "hair": Hairline border (very thin)
            # "mediumDashed": Medium dashed border line
            # "dashDot": Dash-dot border line
            # "dashDotDot": Dash-dot-dot border line
            # "slantDashDot": Slant dash-dot border line
        },
    ],
    width={2: 30},  # when it is None, it will automatic adjust width
    height={2: 50, 3: 25},  # keys are columns
    merge=(slice(0, 1), slice(1, 3)),
    shade={
        (slice(1, 4), slice(1, 3)): {
            "bg_color": "FFFF00",  # Background color
            "pattern_type": "solid",  # Fill pattern (e.g., solid, darkGrid, lightGrid)
            "fg_color": "#0000FF",  # Foreground color, used in patterns
            "end_color": "0000FF",  # End color, useful for gradients
            "fill_type": "solid",  # Type of fill (solid, gradient, etc.)
        }
    },
    comment={(2, 4): "This is a comment"},
    link={(2, 2): "https://example.com"},
    protect={
        "password": "123",  # Password for sheet protection
        "sheet": False,  # True,  # Protect the sheet
        "objects": False,  # True,  # Protect objects
        "scenarios": False,  # True,  # Protect scenarios
        "formatCells": False,  # Disable formatting cells
        "formatColumns": False,  # Disable formatting columns
        "formatRows": False,  # Disable formatting rows
        "insertColumns": False,  # Disable inserting columns
        "insertRows": False,  # Disable inserting rows
        "deleteColumns": False,  # Disable deleting columns
        "deleteRows": False,  # Disable deleting rows
    },
    number_format={
        1: "0.00",  # Two decimal places for column index 1
        2: "#,##0",  # Thousands separator
        3: "0%",  # Percentage format
        4: "$#,##0.00",  # Currency format
    },
    data_validation={
        (slice(1, 2), slice(2, 10)): {
            "type": "list",
            "formula1": '"Option1,Option2,Option3"',  # List of options
            "allow_blank": True,
            "showDropDown": True,
            "showErrorMessage": True,
            "errorTitle": "Invalid input",
            "error": "Please select a valid option.",
        }
    },
    conditional_format={
        (slice(1, 2), slice(2, 10)): [
            {
                "color_scale": {
                    "start_type": "min",  # Type of start point (min, max, percent)
                    "start_color": "#FF0000",  # Starting color
                    "end_type": "max",  # End type (min, max, percent)
                    "end_color": "00FF00",  # Ending color
                    "mid_type": "percentile",  # Midpoint type (optional)
                    "mid_value": 50,  # Midpoint value (optional)
                    "mid_color": "FFFF00",  # Midpoint color (optional)
                }
            }
        ]
    },
)
            """
    if usage:
        print(func_xample)
        return None
    kwargs.pop("format", None)  # 更好地跟fsave结合使用
    kwargs.pop("sheet_name", None)  # 更好地跟df.to_excel结合使用
    sheet_name_corr = (
        sheet_name if isinstance(sheet_name, str) else f"Sheet_{sheet_name}"
    )

    # 只有openpyxl才支持 append
    mode = strcmp(kwargs.get("mode", "w"), ["a", "w"])[0]
    kwargs.pop("mode", None)
    engine = strcmp(kwargs.get("engine", "openpyxl"), ["xlsxwriter", "openpyxl"])[0]
    # 通常是不需要保存index的
    index = kwargs.get("index", False)
    kwargs.pop("index", None)
    # save file
    with pd.ExcelWriter(filename, mode=mode, engine=engine) as writer:
        df.to_excel(writer, sheet_name=sheet_name_corr, index=index, **kwargs)

    wb = load_workbook(filename)
    if isinstance(sheet_name, str):
        ws = wb[sheet_name]
    elif isinstance(sheet_name, int):
        ws = wb.worksheets[sheet_name]
    else:
        ws = wb.worksheets[sheet_name]  # the index of worksheets

    # !Apply cell formatting
    if cell:
        if not isinstance(cell, list):
            cell = [cell]
        for cell_ in cell:
            for indices, format_options in cell_.items():
                cell_range = convert_indices_to_range(*indices)
                apply_format(ws, format_options, cell_range)

    # !Apply cell shading
    if shade:
        for indices, shading in shade.items():
            cell_range = convert_indices_to_range(*indices)
            fill = PatternFill(
                start_color=hex2argb(shading.get("bg_color", "FFFFFF")),
                end_color=hex2argb(shading.get("end_color", "FFFFFF")),
                fill_type=shading.get("fill_type", "solid"),
                patternType=shading.get("pattern_type", "solid"),
                fgColor=hex2argb(shading.get("fg_color", "0000FF")),
            )
            for row in ws[cell_range]:
                for cell in row:
                    cell.fill = fill

    # !number formatting
    if number_format:
        for col_idx, fmt in number_format.items():
            col_letter = get_column_letter(col_idx)
            for cell in ws[col_letter][1:]:  # Skip the header
                cell.number_format = fmt

    # !widths
    if width is None:  # automatic adust width
        for col in ws.columns:
            len_ = [len(str(cell.value)) for cell in col if cell.value]
            if len_:
                # scaling_factor = 1.2
                max_length = max(len_)  # * scaling_factor
                ws.column_dimensions[get_column_letter(col[0].column)].width = (
                    max_length
                )
    else:
        for col_idx, width_ in width.items():
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = width_

    # !heights
    if height is None:  # automatic adust height
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
            max_height = height_max
            for cell in row:
                if cell.value:
                    lines = str(cell.value).split("\n")
                    max_line_length = max(len(line) for line in lines)
                    estimated_height = 15 * len(lines)
                    if max_line_length > 20:
                        estimated_height += 5 * (max_line_length // 20)
                    max_height = max(max_height, estimated_height)
            ws.row_dimensions[row[0].row].height = max_height
    else:
        for row, height_ in height.items():
            ws.row_dimensions[row].height = height_

    # !Merge cells using slice indices
    if merge:
        if isinstance(merge, tuple):
            merge = [merge]
        for indices in merge:
            # Ensure indices are slice objects
            if len(indices) == 2:
                row_slice, col_slice = indices
                merge_range = convert_indices_to_range(row_slice, col_slice)
                ws.merge_cells(merge_range)
            elif len(indices) == 4:
                start_row, start_col, end_row, end_col = indices
                # Convert column numbers to letters (e.g., 1 -> 'A')
                start_cell = f"{get_column_letter(start_col)}{start_row}"
                end_cell = f"{get_column_letter(end_col)}{end_row}"
                merge_range = f"{start_cell}:{end_cell}"
                ws.merge_cells(merge_range)
            else:
                raise ValueError(
                    f"两种方式: 1. format: (start_row, start_col, end_row, end_col), 2. format: (slice(0, 3), slice(1, 2))"
                )

    # !Add comment
    if comment:
        if not isinstance(comment, list):
            comment = [comment]
        for comment_ in comment:
            for (row, col), comment_str in comment_.items():
                ws.cell(row=row + 1, column=col + 1).comment = Comment(
                    comment_str, "Author"
                )

    # !Add link
    if link:
        if not isinstance(link, list):
            link = [link]
        for link_ in link:
            for (row, col), link_str in link_.items():
                ws.cell(row=row + 1, column=col + 1).hyperlink = link_str

    # !Apply data validation
    if data_validation:
        for indices, validation in data_validation.items():
            cell_range = convert_indices_to_range(*indices)
            dv = DataValidation(**validation)
            ws.add_data_validation(dv)
            dv.add(cell_range)

    # !Protect sheet with a password
    if protect:
        ws.protection.password = protect.get("password", False)
        ws.protection.objects = protect.get("objects", True)
        ws.protection.sheet = protect.get("sheet", True)
        ws.protection.scenarios = protect.get("scenarios", True)
        ws.protection.formatCells = protect.get("formatCells", False)
        ws.protection.formatColumns = protect.get("formatColumns", False)
        ws.protection.formatRows = protect.get("formatRows", False)
        ws.protection.insertColumns = protect.get("insertColumns", True)
        ws.protection.insertRows = protect.get("insertRows", True)
        ws.protection.deleteColumns = protect.get("deleteColumns", True)
        ws.protection.deleteRows = protect.get("deleteRows", True)

    # !conditional formatting
    if conditional_format:
        for indices, rules in conditional_format.items():
            cell_range = convert_indices_to_range(*indices)
            for rule in rules:
                if "color_scale" in rule:
                    color_scale = rule["color_scale"]
                    start_color = hex2argb(color_scale.get("start_color", "FFFFFF"))
                    mid_color = hex2argb(color_scale.get("mid_color", "FFFFFF"))
                    end_color = hex2argb(color_scale.get("end_color", "FFFFFF"))

                    color_scale_rule = ColorScaleRule(
                        start_type=color_scale.get("start_type", "min"),
                        start_value=color_scale.get("start_value"),
                        start_color=start_color,
                        mid_type=color_scale.get("mid_type"),
                        mid_value=color_scale.get("mid_value"),
                        mid_color=mid_color,
                        end_type=color_scale.get("end_type", "max"),
                        end_value=color_scale.get("end_value"),
                        end_color=end_color,
                    )
                    ws.conditional_formatting.add(cell_range, color_scale_rule)
    # Save the workbook
    wb.save(filename)
    print(f"Formatted Excel file saved as:\n{filename}")


from IPython.display import display, HTML, Markdown


def preview(var):
    """Master function to preview formatted variables in Jupyter."""

    if isinstance(var, str):
        if isa(var, "html"):
            display(HTML(var))  # Render as HTML
        # Check if it's a valid markdown
        elif var.startswith("#"):
            display(Markdown(var))
        else:
            # Otherwise, display as plain text
            print(var)
    elif isinstance(var, BeautifulSoup):
        preview(str(var))
    elif isinstance(var, pd.DataFrame):
        # Display pandas DataFrame
        display(var)

    elif isinstance(var, list) or isinstance(var, dict):
        # Display JSON
        json_str = json.dumps(var, indent=4)
        display(Markdown(f"```json\n{json_str}\n```"))

    elif isinstance(var, bytes):
        # Display image if it's in bytes format
        display(Image(data=var))

    elif isinstance(var, str) and (var.endswith(".png") or var.endswith(".jpg")):
        # Display image from file path
        display(Image(filename=var))

    elif isinstance(var, dict):
        # Handle dictionary formatting
        json_str = json.dumps(var, indent=4)
        display(Markdown(f"```json\n{json_str}\n```"))

    else:
        # If the format is not recognized, print a message
        print("Format not recognized or unsupported.")


# # Example usages:
# preview("This is a plain text message.")
# preview("# This is a Markdown header")
# preview(pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]}))
# preview({"key": "value", "numbers": [1, 2, 3]})
def df_extend(data: pd.DataFrame, column, axis=0, sep=None, prefix="col"):
    """
    Extend a DataFrame by the list elecments in the column.
    
    Parameters:
    ----------
    data : pd.DataFrame
        The input DataFrame to be extended.
    
    column : str
        The name of the column to be split.
    
    axis : int, optional
        The axis along which to expand the DataFrame. 
        - 0 (default): Expand the specified column into multiple rows.
        - 1: Expand the specified column into multiple columns.
    
    sep : str, optional
        The separator used to split the values in the specified column.
        Must be provided for the function to work correctly.
    """
    
    data = data.copy() 
    mask = data[column].str.contains(sep, na=False)
    data = data.copy()
    if mask.any():
        data[column] = (
            data[column]
            .apply(lambda x: x.split(sep) if isinstance(x, str) else x)  # Only split if x is a string
        )
        
        # Strip spaces from each item in the lists
        data[column] = data[column].apply(lambda x: [item.strip() for item in x] if isinstance(x, list) else x)
        
    data = data.explode(column, ignore_index=True)
    return data
# ! DataFrame
def df_astype(
    data: pd.DataFrame,
    columns: Optional[Union[str, List[str]]] = None,
    astype: str = "datetime",
    skip_row:Union[str,list]=None,
    fmt: Optional[str] = None,
    inplace: bool = True,
    errors: str = "coerce",  # Can be "ignore", "raise", or "coerce"
    **kwargs,
) -> Optional[pd.DataFrame]:
    """
    Convert specified columns of a DataFrame to a specified type (e.g., datetime, float, int, numeric, timedelta).
    If columns is None, all columns in the DataFrame will be converted.

    Parameters:
    - df: DataFrame containing the columns to convert.
    - columns: Either a single column name, a list of column names, or None to convert all columns.
    - astype: The target type to convert the columns to ('datetime', 'float', 'int', 'numeric', 'timedelta', etc.).
    - fmt: Optional; format to specify the datetime format (only relevant for 'datetime' conversion).
    - inplace: Whether to modify the DataFrame in place or return a new one. Defaults to False.
    - errors: Can be "ignore", "raise", or "coerce"
    - **kwargs: Additional keyword arguments to pass to the conversion function (e.g., errors='ignore' for pd.to_datetime or pd.to_numeric).

    Returns:
    - If inplace=False: DataFrame with the specified columns (or all columns if columns=None) converted to the specified type.
    - If inplace=True: The original DataFrame is modified in place, and nothing is returned.
    """
    astypes = [
        "datetime",
        "timedelta",
        "numeric",
        "int",
        "int8",
        "int16",
        "int32",
        "int64",
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "float",
        "float16",
        "float32",
        "float64",
        "complex",
        "complex64",
        "complex128",
        "str",
        "string",
        "bool",
        "datetime64",
        "datetime64[ns]",
        "timedelta64",
        "timedelta64[ns]",
        "category",
        "object",
        "Sparse",
        "hour",
        "minute",
        "second",
        "time",
        "week",
        "date","day",
        "month",
        "year",
    ]
    # If inplace is False, make a copy of the DataFrame
    if not inplace:
        data = data.copy()
    if skip_row is not None:
        data = data.drop(index=skip_row, errors='ignore')
    # If columns is None, apply to all columns
    if columns is None:
        columns = data.columns.tolist()
    # correct the astype input
    if isinstance(astype,str):
        astype = strcmp(astype, astypes)[0]
        print(f"converting as type: {astype}")
    elif isinstance(astype,dict):
        for col, dtype in astype.items():
            dtype='date' if dtype=="day" else dtype
            data["col"]=data["col"].adtype(strcmp(dtype, astypes)[0])
        return data if not inplace else None

    # Ensure columns is a list
    if isinstance(columns, str):
        columns = [columns]

    # Convert specified columns
    for column in columns:
        try:
            if astype in [
                "datetime",
                "hour",
                "minute",
                "second",
                "time",
                "week",
                "date",
                "month",
                "year",
            ]:
                kwargs.pop("errors", None)
                # convert it as type: datetime
                if isinstance(column, int):
                    data.iloc[:, column] = pd.to_datetime(
                        data.iloc[:, column], format=fmt, errors=errors, **kwargs
                    )
                    # further convert:
                    if astype == "time":
                        data.iloc[:, column] = data.iloc[:, column].dt.time
                    elif astype == "month":
                        data.iloc[:, column] = data.iloc[:, column].dt.month
                    elif astype == "year":
                        data.iloc[:, column] = data.iloc[:, column].dt.year
                    elif astype == "date" or astype == "day":
                        data.iloc[:, column] = data.iloc[:, column].dt.date
                    elif astype == "hour":
                        data.iloc[:, column] = data.iloc[:, column].dt.hour
                    elif astype == "minute":
                        data.iloc[:, column] = data.iloc[:, column].dt.minute
                    elif astype == "second":
                        data.iloc[:, column] = data.iloc[:, column].dt.second
                    elif astype == "week":
                        data.iloc[:, column] = data.iloc[:, column].dt.day_name()
                else:
                    data[column] = (
                        pd.to_datetime(
                            data[column], format=fmt, errors=errors, **kwargs
                        )
                        if fmt
                        else pd.to_datetime(data[column], errors=errors, **kwargs)
                    )
                    # further convert:
                    if astype == "time":
                        data[column] = data[column].dt.time
                    elif astype == "month":
                        data[column] = data[column].dt.month
                    elif astype == "year":
                        data[column] = data[column].dt.year
                    elif astype == "date":
                        data[column] = data[column].dt.date
                    elif astype == "hour":
                        data[column] = data[column].dt.hour
                    elif astype == "minute":
                        data[column] = data[column].dt.minute
                    elif astype == "second":
                        data[column] = data[column].dt.second
                    elif astype == "week":
                        data[column] = data[column].dt.day_name()

            elif astype == "numeric":
                kwargs.pop("errors", None)
                data[column] = pd.to_numeric(data[column], errors=errors, **kwargs)
                # print(f"Successfully converted '{column}' to numeric.")
            elif astype == "timedelta":
                kwargs.pop("errors", None)
                data[column] = pd.to_timedelta(data[column], errors=errors, **kwargs)
                # print(f"Successfully converted '{column}' to timedelta.")
            else:
                # Convert to other types (e.g., float, int)
                data[column] = data[column].astype(astype)
                # print(f"Successfully converted '{column}' to {astype}.")
        except Exception as e:
            print(f"Error converting '{column}' to {astype}: {e}")
    try:
        display(data.info()[:10])
    except:
        pass
    return data


# ! DataFrame
def df_sort_values(df, column, by=None, ascending=True, inplace=True, **kwargs):
    """
    Sort a DataFrame by a specified column based on a custom order or by count.

    Parameters:
    - df: DataFrame to be sorted.
    - column: The name of the column to sort by.
    - by: List specifying the custom order for sorting or 'count' to sort by frequency.
    - ascending: Boolean or list of booleans, default True.
                 Sort ascending vs. descending.
    - inplace: If True, perform operation in place and return None.
    - **kwargs: Additional arguments to pass to sort_values.

    Returns:
    - Sorted DataFrame if inplace is False, otherwise None.
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

    if isinstance(by, str) and 'count' in by.lower():
        # Count occurrences of each value in the specified column
        value_counts = df[column].value_counts()

        # Determine the order based on counts
        count_ascending = kwargs.pop("count_ascending", ascending)
        sorted_counts = value_counts.sort_values(ascending=count_ascending).index.tolist()

        # Convert to a categorical type with the new order
        df[column] = pd.Categorical(df[column], categories=sorted_counts, ordered=True)
        # Set ascending to count_ascending for sorting
        ascending = count_ascending  # Adjust ascending for the final sort
    elif isinstance(by, list):
        # Convert the specified column to a categorical type with the custom order
        df[column] = pd.Categorical(df[column], categories=by, ordered=True)
    else:
        raise ValueError("Custom order must be a list or 'count'.")

    try:
        if inplace:  # replace the original
            data.sort_values(column, ascending=ascending, inplace=True, **kwargs)
            print(f"Successfully sorted DataFrame by '{column}'")
            return None
        else:
            sorted_df = data.sort_values(column, ascending=ascending, **kwargs)
            print(f"Successfully sorted DataFrame by '{column}' using custom order.")
            return sorted_df
    except Exception as e:
        print(f"Error sorting DataFrame by '{column}': {e}")
        return df


# # Example usage:
# # Sample DataFrame
# data = {
#     "month": ["March", "January", "February", "April", "December"],
#     "Amount": [200, 100, 150, 300, 250],
# }
# df_month = pd.DataFrame(data)

# # Define the month order
# month_order = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December",
# ]
# display(df_month)
# sorted_df_month = df_sort_values(df_month, "month", month_order, ascending=True)
# display(sorted_df_month)
# df_sort_values(df_month, "month", month_order, ascending=True, inplace=True)
# display(df_month)


def df_merge(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    use_index: bool = True,
    columns: list = ["col_left", "col_right"],
    how: str = "left",
) -> pd.DataFrame:
    """
    Merges two DataFrames based on either the index or shared columns with matching data types.
    usage:
        #(1) if the index are the same
            df_merged = df_merge(df1, df2, use_index=True(defalut), how='outer')
        #(2) if there are shaed columns, then based on shared columns
            df_merged = df_merge(df1, df2, how='outer')
        #(3) if columns: then based on the specific columns
            df_merged = df_merge(df1, df2, columns=["col_left", "col_right"],how='outer')
    Parameters:
    - df1 (pd.DataFrame): The first DataFrame.
    - df2 (pd.DataFrame): The second DataFrame.
    - use_index (bool): If True, first try to merge by index if they are comparable; otherwise, fall back to column-based merge.
    - how (str): Type of merge to perform: 'inner', 'outer', 'left', or 'right'. Default is 'inner'.
    'inner': only the rows that have matching values in both DataFrames (intersection)
    'outer': keeps all rows from both DataFrames and fills in missing values with NaN
    'left': keeps all rows from the left DataFrame and matches rows from the right DataFrame
    'right': keeps all rows from the right DataFrame and matches rows from the left DataFrame, filling with NaN if there is no match.

    Returns:
    - pd.DataFrame: The merged DataFrame.
    """

    # 1. Check if indices are comparable (same length and types)
    if use_index:
        print(f"Merging based on index using '{how}' join...")
        df_merged = pd.merge(df1, df2, left_index=True, right_index=True, how=how)
        return df_merged

    # 2. Find common columns with the same dtype
    common_columns = df1.columns.intersection(df2.columns)
    shared_columns = []
    for col in common_columns:
        if df1[col].dtype == df2[col].dtype:
            shared_columns.append(col)
    if not isinstance(columns, list):
        columns = [columns]
    if len(columns) != 2:
        raise ValueError(
            "'columns':list shoule be a list: columns=['col_left','col_right']"
        )
    if all(columns):
        print(f"Merging based on columns: {columns} using '{how}' join...")
        df_merged = pd.merge(df1, df2, left_on=columns[0], right_on=columns[1], how=how)
    elif shared_columns:
        print(
            f"Merging based on shared columns: {shared_columns} using '{how}' join..."
        )
        df_merged = pd.merge(df1, df2, on=shared_columns, how=how)
    else:
        raise ValueError(
            "No common columns with matching data types to merge on, and indices are not comparable."
        )
    return df_merged

def df_fillna(
    data: pd.DataFrame,
    method: str = "mean",
    axis: int = 0,# column-wise
    constant: float = None,
    inplace: bool = True,
) -> pd.DataFrame:
    """
    Fill missing values in a DataFrame using specified imputation method.

    Parameters:
    data (pd.DataFrame): The DataFrame to fill missing values.
    method (str): The imputation method to use. Options are:
        - 'mean': Replace missing values with the mean of the column.
        - 'median': Replace missing values with the median of the column.
        - 'most_frequent': Replace missing values with the most frequent value in the column.
        - 'constant': Replace missing values with a constant value provided by the `constant` parameter.
        - 'knn': Use K-Nearest Neighbors imputation.
        - 'iterative': Use Iterative imputation.
    axis (int): The axis along which to impute:
        - 0: Impute column-wise (default).
        - 1: Impute row-wise.
    constant (float, optional): Constant value to use for filling NaNs if method is 'constant'.
    inplace (bool): If True, modify the original DataFrame. If False, return a new DataFrame.

    """

    if data.empty:
        raise ValueError("Input DataFrame is empty.")

    # Validate method
    methods = ["mean", "median", "most_frequent", "constant", "knn", "iterative"]
    method = strcmp(method, methods)[0]

    # If using constant method, ask for a constant value
    if constant is not None:
        method = "constant"
        try:
            constant = float(constant)
        except ValueError:
            raise ValueError("Constant value must be a number.")

    # Initialize SimpleImputer with the chosen method
    if method == "constant":
        imputer = SimpleImputer(strategy=method, fill_value=constant)
    elif method == "knn":
        from sklearn.impute import KNNImputer

        imputer = KNNImputer(n_neighbors=n_neighbors)
    elif method == "iterative":
        from sklearn.impute import IterativeImputer

        imputer = IterativeImputer(max_iter=max_iter)
    else:
        from sklearn.impute import SimpleImputer

        imputer = SimpleImputer(strategy=method)

    # Fit and transform the data
    if axis == 0:
        # Impute column-wise
        imputed_data = imputer.fit_transform(data)
        imputed_data.shape
    elif axis == 1:
        # Impute row-wise
        imputed_data = imputer.fit_transform(data.T)
        imputed_data.shape
    else:
        raise ValueError("Invalid axis. Use 0 for columns or 1 for rows.")

    df_filled = pd.DataFrame(
        imputed_data if axis == 0 else imputed_data.T,
        index=data.index,# if axis == 0 else data.columns,
        columns=data.columns,# if axis == 0 else data.index,
    )

    if inplace:
        data.update(df_filled)
        return None  # replace original
    else:
        return df_filled
def df_scaler(
    data: pd.DataFrame,
    method="standard",
    columns=None,  # default, select all numeric col/row
    inplace=False,
    verbose=False,  # show usage
    axis=0,  # defalut column-wise
    **kwargs,
):
    """
    df_scaler(data, scaler="standard", inplace=False, axis=0, verbose=True)

    Parameters:
    - data: pandas DataFrame to be scaled.
    - method: Scaler type ('standard', 'minmax', 'robust'). Default is 'standard'.
    - columns: List of columns (for axis=0) or rows (for axis=1) to scale.
               If None, all numeric columns/rows will be scaled.
    - inplace: If True, modify the DataFrame in place. Otherwise, return a new DataFrame.
    - axis: Axis along which to scale. 0 for column-wise, 1 for row-wise. Default is 0.
    - verbose: If True, prints logs of the process.
    - kwargs: Additional arguments to be passed to the scaler.
    """
    if verbose:
        print('df_scaler(data, scaler="standard", inplace=False, axis=0, verbose=True)')

    methods = ["standard", "minmax", "robust"]
    method = strcmp(method, methods)[0]
    if method == "standard":
        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler(**kwargs)
    elif method == "minmax":
        from sklearn.preprocessing import MinMaxScaler

        scaler = MinMaxScaler(**kwargs)
    elif method == "robust":
        from sklearn.preprocessing import RobustScaler

        scaler = RobustScaler(**kwargs)
    if axis not in [0, 1]:
        raise ValueError("Axis must be 0 (column-wise) or 1 (row-wise).")

    if axis == 0:
        # Column-wise scaling (default)
        if columns is None:
            columns = data.select_dtypes(include=["float64", "int64"]).columns.tolist()
        non_numeric_columns = data.columns.difference(columns)
        print(f"Scaling columns")

        scaled_data = scaler.fit_transform(data[columns])

        if inplace:
            data[columns] = scaled_data
            print("Original DataFrame modified in place (column-wise).")
        else:
            scaled_df = pd.concat(
                [
                    pd.DataFrame(scaled_data, columns=columns, index=data.index),
                    data[non_numeric_columns],
                ],
                axis=1,
            )
            scaled_df = scaled_df[data.columns]  # Maintain column order
            return scaled_df

    elif axis == 1:
        # Row-wise scaling
        if columns is None:
            columns = data.index.tolist()
        numeric_rows = data.loc[columns].select_dtypes(include=["float64", "int64"])
        if numeric_rows.empty:
            raise ValueError("No numeric rows to scale.")

        print(f"Scaling rows")

        scaled_data = scaler.fit_transform(
            numeric_rows.T
        ).T  # Transpose for scaling and then back

        if inplace:
            data.loc[numeric_rows.index] = scaled_data
            print("Original DataFrame modified in place (row-wise).")
        else:
            scaled_df = data.copy()
            scaled_df.loc[numeric_rows.index] = scaled_data
            return scaled_df

def df_cluster(
    data: pd.DataFrame,
    columns: Optional[list] = None,
    n_clusters: Optional[int] = None,
    range_n_clusters: Union[range, np.ndarray] = range(2, 11),
    scale: bool = True,
    plot: Union[str, list] = "all",
    inplace: bool = True,
    ax: Optional[plt.Axes] = None,
) -> tuple[pd.DataFrame, int, Optional[plt.Axes]]:
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score, silhouette_samples
    import seaborn as sns
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    """
    Performs clustering analysis on the provided feature matrix using K-Means.

    Parameters:
        X (np.ndarray):
            A 2D numpy array or DataFrame containing numerical feature data,
            where each row corresponds to an observation and each column to a feature.

        range_n_clusters (range):
            A range object specifying the number of clusters to evaluate for K-Means clustering.
            Default is range(2, 11), meaning it will evaluate from 2 to 10 clusters.

        scale (bool):
            A flag indicating whether to standardize the features before clustering.
            Default is True, which scales the data to have a mean of 0 and variance of 1.

        plot (bool):
            A flag indicating whether to generate visualizations of the clustering analysis.
            Default is True, which will plot silhouette scores, inertia, and other relevant plots.
    Returns:
        tuple: 
            A tuple containing the modified DataFrame with cluster labels, 
            the optimal number of clusters, and the Axes object (if any).
    """
    X = data[columns].values if columns is not None else data.values

    silhouette_avg_scores = []
    inertia_scores = []

    # Standardize the features
    if scale:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

    for n_cluster in range_n_clusters:
        kmeans = KMeans(n_clusters=n_cluster, random_state=1)
        cluster_labels = kmeans.fit_predict(X)

        silhouette_avg = silhouette_score(X, cluster_labels)
        silhouette_avg_scores.append(silhouette_avg)
        inertia_scores.append(kmeans.inertia_)
        print(
            f"For n_clusters = {n_cluster}, the average silhouette_score is : {silhouette_avg:.4f}"
        )

    # Determine the optimal number of clusters based on the maximum silhouette score
    if n_clusters is None:
        n_clusters = range_n_clusters[np.argmax(silhouette_avg_scores)]
    print(f"n_clusters = {n_clusters}")

    # Apply K-Means Clustering with Optimal Number of Clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=1)
    cluster_labels = kmeans.fit_predict(X)

    if plot:
        # ! Interpreting the plots from your K-Means clustering analysis
        # ! 1. Silhouette Score and Inertia vs Number of Clusters
        # Description:
        # This plot has two y-axes: the left y-axis represents the Silhouette Score, and the right y-axis
        # represents Inertia.
        # The x-axis represents the number of clusters (k).

        # Interpretation:

        # Silhouette Score:
        # Ranges from -1 to 1, where a score close to 1 indicates that points are well-clustered, while a
        # score close to -1 indicates that points might be incorrectly clustered.
        # A higher silhouette score generally suggests that the data points are appropriately clustered.
        # Look for the highest value to determine the optimal number of clusters.

        # Inertia:
        # Represents the sum of squared distances from each point to its assigned cluster center.
        # Lower inertia values indicate tighter clusters.
        # As the number of clusters increases, inertia typically decreases, but the rate of decrease
        # may slow down, indicating diminishing returns for additional clusters.

        # Optimal Number of Clusters:
        # You can identify an optimal number of clusters where the silhouette score is maximized and
        # inertia starts to plateau (the "elbow" point).
        # This typically suggests that increasing the number of clusters further yields less meaningful
        # separations.
        if ax is None:
            _, ax = plt.subplots(figsize=inch2cm(10, 6))
        color = "tab:blue"
        ax.plot(
            range_n_clusters,
            silhouette_avg_scores,
            marker="o",
            color=color,
            label="Silhouette Score",
        )
        ax.set_xlabel("Number of Clusters")
        ax.set_ylabel("Silhouette Score", color=color)
        ax.tick_params(axis="y", labelcolor=color)
        # add right axis: inertia
        ax2 = ax.twinx()
        color = "tab:red"
        ax2.set_ylabel("Inertia", color=color)
        ax2.plot(
            range_n_clusters,
            inertia_scores,
            marker="x",
            color=color,
            label="Inertia",
        )
        ax2.tick_params(axis="y", labelcolor=color)

        plt.title("Silhouette Score and Inertia vs Number of Clusters")
        plt.xticks(range_n_clusters)
        plt.grid()
        plt.axvline(x=n_clusters, linestyle="--", color="r", label="Optimal n_clusters")
        # ! 2. Elbow Method Plot
        # Description:
        # This plot shows the Inertia against the number of clusters.

        # Interpretation:
        # The elbow point is where the inertia begins to decrease at a slower rate. This point suggests that
        # adding more clusters beyond this point does not significantly improve the clustering performance.
        # Look for a noticeable bend in the curve to identify the optimal number of clusters, indicated by the
        # vertical dashed line.
        # Inertia plot
        plt.figure(figsize=inch2cm(10, 6))
        plt.plot(range_n_clusters, inertia_scores, marker="o")
        plt.title("Elbow Method for Optimal k")
        plt.xlabel("Number of clusters")
        plt.ylabel("Inertia")
        plt.grid()
        plt.axvline(
            x=np.argmax(silhouette_avg_scores) + 2,
            linestyle="--",
            color="r",
            label="Optimal n_clusters",
        )
        plt.legend()
        # ! Silhouette Plots
        # 3. Silhouette Plot for Various Clusters
        # Description:
        # This horizontal bar plot shows the silhouette coefficient values for each sample, organized by cluster.

        # Interpretation:
        # Each bar represents the silhouette score of a sample within a specific cluster. Longer bars indicate
        # that the samples are well-clustered.
        # The height of the bars shows how similar points within the same cluster are to one another compared to
        # points in other clusters.
        # The vertical red dashed line indicates the average silhouette score for all samples.
        # You want the majority of silhouette values to be above the average line, indicating that most points
        # are well-clustered.

        # 以下代码不用再跑一次了
        # n_clusters = (
        #     np.argmax(silhouette_avg_scores) + 2
        # )  # Optimal clusters based on max silhouette score
        # kmeans = KMeans(n_clusters=n_clusters, random_state=1)
        # cluster_labels = kmeans.fit_predict(X)
        silhouette_vals = silhouette_samples(X, cluster_labels)

        plt.figure(figsize=inch2cm(10, 6))
        y_lower = 10
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to cluster i
            ith_cluster_silhouette_values = silhouette_vals[cluster_labels == i]

            # Sort the values
            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            # Create a horizontal bar plot for the silhouette scores
            plt.barh(range(y_lower, y_upper), ith_cluster_silhouette_values, height=0.5)

            # Label the silhouette scores
            plt.text(-0.05, (y_lower + y_upper) / 2, str(i + 2))
            y_lower = y_upper + 10  # 10 for the 0 samples

        plt.title("Silhouette Plot for the Various Clusters")
        plt.xlabel("Silhouette Coefficient Values")
        plt.ylabel("Cluster Label")
        plt.axvline(x=np.mean(silhouette_vals), color="red", linestyle="--")

        df_clusters = pd.DataFrame(
            X, columns=[f"Feature {i+1}" for i in range(X.shape[1])]
        )
        df_clusters["Cluster"] = cluster_labels
        # ! pairplot of the clusters
        # Overview of the Pairplot
        # Axes and Grid:
        # The pairplot creates a grid of scatter plots for each pair of features in your dataset.
        # Each point in the scatter plots represents a sample from your dataset, colored according to its cluster assignment.

        # Diagonal Elements:
        # The diagonal plots usually show the distribution of each feature. In this case, since X.shape[1] <= 4,
        # there will be a maximum of four features plotted against each other. The diagonal could display histograms or
        # kernel density estimates (KDE) for each feature.

        # Interpretation of the Pairplot

        # Feature Relationships:
        # Look at each scatter plot in the off-diagonal plots. Each plot shows the relationship between two features. Points that
        # are close together in the scatter plot suggest similar values for those features.
        # Cluster Separation: You want to see clusters of different colors (representing different clusters) that are visually distinct.
        # Good separation indicates that the clustering algorithm effectively identified different groups within your data.
        # Overlapping Points: If points from different clusters overlap significantly in any scatter plot, it indicates that those clusters
        # might not be distinct in terms of the two features being compared.
        # Cluster Characteristics:
        # Shape and Distribution: Observe the shape of the clusters. Are they spherical, elongated, or irregular? This can give insights
        # into how well the K-Means (or other clustering methods) has performed:
        # Spherical Clusters: Indicates that clusters are well defined and separated.
        # Elongated Clusters: May suggest that the algorithm is capturing variations along specific axes but could benefit from adjustments
        # in clustering parameters or methods.
        # Feature Influence: Identify which features contribute most to cluster separation. For instance, if you see that one feature
        # consistently separates two clusters, it may be a key factor for clustering.
        # Diagonal Histograms/KDE:
        # The diagonal plots show the distribution of individual features across all samples. Look for:
        # Distribution Shape: Is the distribution unimodal, bimodal, skewed, or uniform?
        # Concentration: Areas with a high density of points may indicate that certain values are more common among samples.
        # Differences Among Clusters: If you see distinct peaks in the histograms for different clusters, it suggests that those clusters are
        # characterized by specific ranges of feature values.
        # Example Observations
        # Feature 1 vs. Feature 2: If there are clear, well-separated clusters in this scatter plot, it suggests that these two features
        # effectively distinguish between the clusters.
        # Feature 3 vs. Feature 4: If you observe significant overlap between clusters in this plot, it may indicate that these features do not
        # provide a strong basis for clustering.
        # Diagonal Plots: If you notice that one cluster has a higher density of points at lower values for a specific feature, while another
        # cluster is concentrated at higher values, this suggests that this feature is critical for differentiating those clusters.

        # Pairplot of the clusters
        # * 为什么要限制到4个features?
        # 2 features=1 scatter plot            # 3 features=3 scatter plots
        # 4 features=6 scatter plots           # 5 features=10 scatter plots
        # 6 features=15 scatter plots          # 10 features=45 scatter plots
        # Pairplot works well with low-dimensional data, 如果维度比较高的话, 子图也很多,失去了它的意义
        if X.shape[1] <= 6:
            plt.figure(figsize=(8, 4))
            sns.pairplot(df_clusters, hue="Cluster", palette="tab10")
            plt.suptitle("Pairplot of Clusters", y=1.02)

    # Add cluster labels to the DataFrame or modify in-place
    if inplace:  # replace the oringinal data
        data["Cluster"] = cluster_labels
        return None, n_clusters, kmeans, ax  # Return None when inplace is True
    else:
        data_copy = data.copy()
        data_copy["Cluster"] = cluster_labels
        return data_copy, n_clusters, kmeans, ax


# example:
# clustering_features = [marker + "_log" for marker in markers]
# df_cluster(data, columns=clustering_features, n_clusters=3,range_n_clusters=np.arange(3, 7))

"""
# You're on the right track, but let's clarify how PCA and clustering (like KMeans) work, especially 
# in the context of your dataset with 7 columns and 23,121 rows.

# Principal Component Analysis (PCA)
# Purpose of PCA:
# PCA is a dimensionality reduction technique. It transforms your dataset from a high-dimensional space 
# (in your case, 7 dimensions corresponding to your 7 columns) to a lower-dimensional space while 
# retaining as much variance (information) as possible.
# How PCA Works:
# PCA computes new features called "principal components" that are linear combinations of the original 
# features.
# The first principal component captures the most variance, the second captures the next most variance 
# (orthogonal to the first), and so on.
# If you set n_components=2, for example, PCA will reduce your dataset from 7 columns to 2 columns. 
# This helps in visualizing and analyzing the data with fewer dimensions.
# Result of PCA:
# After applying PCA, your original dataset with 7 columns will be transformed into a new dataset with 
# the specified number of components (e.g., 2 or 3).
# The transformed dataset will have fewer columns but should capture most of the important information 
# from the original dataset.

# Clustering (KMeans)
# Purpose of Clustering:
# Clustering is used to group data points based on their similarities. KMeans, specifically, partitions 
# your data into a specified number of clusters (groups).
# How KMeans Works:
# KMeans assigns each data point to one of the k clusters based on the feature space (original or 
# PCA-transformed).
# It aims to minimize the variance within each cluster while maximizing the variance between clusters.
# It does not classify the data in each column independently; instead, it considers the overall similarity 
# between data points based on their features.
# Result of KMeans:
# The output will be cluster labels for each data point (e.g., which cluster a particular observation 
# belongs to).
# You can visualize how many groups were formed and analyze the characteristics of each cluster.

# Summary
# PCA reduces the number of features (columns) in your dataset, transforming it into a lower-dimensional
# space.
# KMeans then classifies data points based on the features of the transformed dataset (or the original 
# if you choose) into different subgroups (clusters).
# By combining these techniques, you can simplify the complexity of your data and uncover patterns that 
# might not be visible in the original high-dimensional space. Let me know if you have further questions!
"""


def df_reducer(
    data: pd.DataFrame,
    columns: Optional[List[str]] = None,
    method: str = "umap",  # 'pca', 'umap'
    n_components: int = 2,  # Default for umap, but 50 for PCA
    umap_neighbors: int = 15,  # UMAP-specific
    umap_min_dist: float = 0.1,  # UMAP-specific
    tsne_perplexity: int = 30,  # t-SNE-specific
    scale: bool = True,
    fill_missing: bool = True,
    debug: bool = False,
    inplace: bool = True,  # replace the oringinal data
    plot_:bool = False,# plot scatterplot, but no 'hue',so it is meaningless
) -> pd.DataFrame:
    """
    Reduces the dimensionality of the selected DataFrame using PCA or UMAP.

    Parameters:
    -----------
    data : pd.DataFrame
        The input DataFrame (samples x features).

    columns : List[str], optional
        List of column names to reduce. If None, all columns are used.

    method : str, optional, default="umap"
        Dimensionality reduction method, either "pca" or "umap".

    n_components : int, optional, default=50
        Number of components for PCA or UMAP.

    umap_neighbors : int, optional, default=15
        Number of neighbors considered for UMAP embedding.

    umap_min_dist : float, optional, default=0.1
        Minimum distance between points in UMAP embedding.

    scale : bool, optional, default=True
        Whether to scale the data using StandardScaler.

    fill_missing : bool, optional, default=True
        Whether to fill missing values using the mean before applying PCA/UMAP.

    Returns:
    --------
    reduced_df : pd.DataFrame
        DataFrame with the reduced dimensions.
    """
    
    """
       PCA: explained_variance: 
            indicates the proportion of the dataset's total variance that each principal 
            component (PC) explains. It gives you a sense of how much information
            (or variance) is captured by each PC
        Interpretation:
            - Higher values indicate that the corresponding PC captures more variance.
            - The sum of the explained variances for all PCs equals 1 (or 100%).
            - If the first few components explain a high percentage (e.g., 90%), 
            it means you can reduce the dimensionality of the data significantly without losing much information.
        Use case: 
            You may plot a scree plot, which shows the explained variance for each PC, to help decide 
            how many components to keep for analysis.

        PCA: Singular values:
            represent the magnitude of variance along each principal component. Mathematically, 
            they are the square roots of the eigenvalues of the covariance matrix.
        Interpretation:
            Larger singular values indicate that the associated PC captures more variance.
            Singular values are related to the scale of the data. If the data are scaled
            before PCA (e.g., standardized), then the singular values will provide a measure
            of the spread of data along each PC.
        Use case: 
            Singular values help quantify the contribution of each principal component in a
            similar way to the explained variance. They are useful in understanding the overall 
            structure of the data.
    """
    from sklearn.preprocessing import StandardScaler
    from sklearn.impute import SimpleImputer

    # Select columns if specified, else use all columns
    X = data[columns].values if columns else data.values

    # Handle missing values
    if fill_missing:
        imputer = SimpleImputer(strategy="mean")
        X = imputer.fit_transform(X)

    # Optionally scale the data
    if scale:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

    # Check valid method input
    methods=["pca", "umap","tsne","factor","isolation_forest"]
    method=strcmp(method, methods)[0]
    # Apply PCA if selected
    if method == "pca": 
        from sklearn.decomposition import PCA
        pca = PCA(n_components=n_components)
        X_reduced = pca.fit_transform(X)
        
        # Additional PCA information
        explained_variance = pca.explained_variance_ratio_
        singular_values = pca.singular_values_
        loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

        if debug:
            print(f"PCA completed: Reduced to {n_components} components.")
            print(f"Explained Variance: {explained_variance}")
            print(f"Singular Values: {singular_values}")

        # Plot explained variance if debug=True
        if debug:
            # Plot explained variance
            cumulative_variance = np.cumsum(explained_variance)
            plt.figure(figsize=(8, 5))
            plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker="o")
            plt.title("Cumulative Explained Variance by Principal Components")
            plt.xlabel("Number of Principal Components")
            plt.ylabel("Cumulative Explained Variance")
            plt.axhline(y=0.95, color="r", linestyle="--", label="Threshold (95%)")
            plt.axvline(x=n_components, color="g", linestyle="--", label=f"n_components = {n_components}")
            plt.legend()
            plt.grid()
            plt.show()

        # Prepare reduced DataFrame with additional PCA info
        pca_df = pd.DataFrame(
            X_reduced, index=data.index,
            columns=[f"PC_{i+1}" for i in range(n_components)]
        ) 
        # pca_df["Explained Variance"] = np.tile(explained_variance[:n_components], (pca_df.shape[0], 1))
        # pca_df["Singular Values"] = np.tile(singular_values[:n_components], (pca_df.shape[0], 1))
        # Expand explained variance to multiple columns if needed
        for i in range(n_components):
            pca_df[f"Explained Variance PC_{i+1}"] = np.tile(format(explained_variance[i]*100,".3f")+"%", (pca_df.shape[0], 1))
        for i in range(n_components):
            pca_df[f"Singular Values PC_{i+1}"] = np.tile(singular_values[i], (pca_df.shape[0], 1))

    # Apply UMAP if selected
    elif method == "umap":
        import umap
        umap_reducer = umap.UMAP(
            n_neighbors=umap_neighbors,
            min_dist=umap_min_dist,
            n_components=n_components
        )
        X_reduced = umap_reducer.fit_transform(X)

        # Additional UMAP information
        embedding = umap_reducer.embedding_
        trustworthiness = umap_reducer._raw_data[:, :n_components]

        if debug:
            print(f"UMAP completed: Reduced to {n_components} components.")
            print(f"Embedding Shape: {embedding.shape}")
            print(f"Trustworthiness: {trustworthiness}")

        # Prepare reduced DataFrame with additional UMAP info
        umap_df = pd.DataFrame(
            X_reduced, index=data.index,
            columns=[f"UMAP_{i+1}" for i in range(n_components)]
        )
        umap_df["Embedding"] = embedding[:, 0]  # Example of embedding data
        umap_df["Trustworthiness"] = trustworthiness[:, 0]  # Trustworthiness metric
    elif method == "tsne":
        from sklearn.manifold import TSNE
        tsne = TSNE(n_components=n_components, perplexity=tsne_perplexity, random_state=1)
        X_reduced = tsne.fit_transform(X)

        # Prepare reduced DataFrame with additional t-SNE info
        tsne_df = pd.DataFrame(
            X_reduced, index=data.index,
            columns=[f"tSNE_{i+1}" for i in range(n_components)]
        )
        tsne_df["Perplexity"] = np.tile(f"Perplexity: {tsne_perplexity}", (tsne_df.shape[0], 1))

    # Apply Factor Analysis if selected
    elif method == "factor":
        from sklearn.decomposition import FactorAnalysis
        factor = FactorAnalysis(n_components=n_components, random_state=1)
        X_reduced = factor.fit_transform(X)
        # Factor Analysis does not directly provide explained variance, but we can approximate it
        fa_variance = factor.noise_variance_
        # Prepare reduced DataFrame with additional Factor Analysis info
        factor_df = pd.DataFrame(
            X_reduced, index=data.index,
            columns=[f"Factor_{i+1}" for i in range(n_components)]
        )
        factor_df["Noise Variance"] = np.tile(format(np.mean(fa_variance) * 100, ".3f") + "%", (factor_df.shape[0], 1))

    # Apply Isolation Forest for outlier detection if selected
    elif method == "isolation_forest":
        from sklearn.decomposition import PCA
        from sklearn.ensemble import IsolationForest
        # Step 1: Apply PCA for dimensionality reduction to 2 components
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(X)

        explained_variance = pca.explained_variance_ratio_
        singular_values = pca.singular_values_

        # Prepare reduced DataFrame with additional PCA info
        iso_forest_df = pd.DataFrame(
            X_pca, index=data.index,
            columns=[f"PC_{i+1}" for i in range(n_components)]
        )

        isolation_forest = IsolationForest(n_estimators=100, contamination='auto',random_state=1)
        isolation_forest.fit(X)
        anomaly_scores = isolation_forest.decision_function(X)  # Anomaly score: larger is less anomalous
        # Predict labels: 1 (normal), -1 (anomaly)
        anomaly_labels = isolation_forest.fit_predict(X) 
        # Add anomaly scores and labels to the DataFrame
        iso_forest_df["Anomaly Score"] = anomaly_scores
        iso_forest_df["Anomaly Label"] = anomaly_labels
        # add info from pca
        for i in range(n_components):
            iso_forest_df[f"Explained Variance PC_{i+1}"] = np.tile(format(explained_variance[i]*100,".3f")+"%", (iso_forest_df.shape[0], 1))
        for i in range(n_components):
            iso_forest_df[f"Singular Values PC_{i+1}"] = np.tile(singular_values[i], (iso_forest_df.shape[0], 1))

    # Return reduced data and info as a new DataFrame with the same index
    if method == "pca":
        reduced_df = pca_df
        colname_met = "PC_"
        if plot_:
            sns.scatterplot(
                data=pca_df,
                x="PC_1",
                y="PC_2",
                # hue="condition",
            )
    elif method == "umap":
        reduced_df = umap_df
        colname_met = "UMAP_"
        if plot_:
            sns.scatterplot(
                data=umap_df,
                x="UMAP_1",
                y="UMAP_2",
                # hue="condition",
            )
    elif method == "tsne":
        reduced_df = tsne_df
        colname_met = "t-SNE_"
        if plot_:
            sns.scatterplot(
                data=tsne_df,
                x="tSNE_1",
                y="tSNE_2",
                # hue="batch",
            )
    elif method == "factor":
        reduced_df = factor_df
        colname_met = "Factor_"
        if plot_:
            sns.scatterplot(
                data=factor_df,
                x="Factor_1",
                y="Factor_2",
                # hue="batch",
            )
    elif method == "isolation_forest":
        reduced_df = iso_forest_df  # Already a DataFrame for outliers
        colname_met = "PC_"
        if plot_:
            ax = sns.scatterplot(
                data=iso_forest_df[iso_forest_df["Anomaly Label"] == 1],
                x="PC_1",
                y="PC_2",
                label="normal", c="b",
            )
            ax = sns.scatterplot(
                ax=ax,
                data=iso_forest_df[iso_forest_df["Anomaly Label"] == -1],
                x="PC_1",
                y="PC_2",
                c="r",
                label="outlier", marker="+", s=30,
            )


    if inplace:
        # If inplace=True, add components back into the original data
        for col_idx in range(n_components):
            data[f"{colname_met}{col_idx+1}"] = reduced_df.iloc[:, col_idx]
        
        # Add extra info for PCA/UMAP
        if method == "pca":
            data["Explained Variance"] = reduced_df["Explained Variance"]
            data["Singular Values"] = reduced_df["Singular Values"]
        elif method == "umap":
            data["Embedding"] = reduced_df["Embedding"]
            data["Trustworthiness"] = reduced_df["Trustworthiness"]
        return None  # No return when inplace=True

    return reduced_df 


# example:
# df_reducer(data=data_log, columns=markers, n_components=2)


def plot_cluster(
    data: pd.DataFrame,
    labels: np.ndarray,
    metrics: dict = None,
    cmap="tab20",
    true_labels: Optional[np.ndarray] = None,
) -> None:
    """
    Visualize clustering results with various plots.

    Parameters:
    -----------
    data : pd.DataFrame
        The input data used for clustering.
    labels : np.ndarray
        Cluster labels assigned to each point.
    metrics : dict
        Dictionary containing evaluation metrics from evaluate_cluster function.
    true_labels : Optional[np.ndarray], default=None
        Ground truth labels, if available.
    """
    import seaborn as sns
    from sklearn.metrics import silhouette_samples

    if metrics is None:
        metrics = evaluate_cluster(data=data, labels=labels, true_labels=true_labels)

    # 1. Scatter Plot of Clusters
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 3, 1)
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=labels, cmap=cmap, s=20)
    plt.title("Cluster Scatter Plot")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.colorbar(label="Cluster Label")
    plt.grid()

    # 2. Silhouette Plot
    if "Silhouette Score" in metrics:
        silhouette_vals = silhouette_samples(data, labels)
        plt.subplot(1, 3, 2)
        y_lower = 10
        for i in range(len(set(labels))):
            # Aggregate the silhouette scores for samples belonging to the current cluster
            cluster_silhouette_vals = silhouette_vals[labels == i]
            cluster_silhouette_vals.sort()
            size_cluster_i = cluster_silhouette_vals.shape[0]
            y_upper = y_lower + size_cluster_i

            plt.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_vals)
            plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            y_lower = y_upper + 10  # 10 for the 0 samples

        plt.title("Silhouette Plot")
        plt.xlabel("Silhouette Coefficient Values")
        plt.ylabel("Cluster Label")
        plt.axvline(x=metrics["Silhouette Score"], color="red", linestyle="--")
        plt.grid()

    # 3. Metrics Plot
    plt.subplot(1, 3, 3)
    metric_names = ["Davies-Bouldin Index", "Calinski-Harabasz Index"]
    metric_values = [
        metrics["Davies-Bouldin Index"],
        metrics["Calinski-Harabasz Index"],
    ]

    if true_labels is not None:
        metric_names += ["Homogeneity Score", "Completeness Score", "V-Measure"]
        metric_values += [
            metrics["Homogeneity Score"],
            metrics["Completeness Score"],
            metrics["V-Measure"],
        ]

    plt.barh(metric_names, metric_values, color="lightblue")
    plt.title("Clustering Metrics")
    plt.xlabel("Score")
    plt.axvline(x=0, color="gray", linestyle="--")
    plt.grid()
    plt.tight_layout()


def evaluate_cluster(
    data: pd.DataFrame, labels: np.ndarray, true_labels: Optional[np.ndarray] = None
) -> dict:
    """
    Evaluate clustering performance using various metrics.

    Parameters:
    -----------
    data : pd.DataFrame
        The input data used for clustering.
    labels : np.ndarray
        Cluster labels assigned to each point.
    true_labels : Optional[np.ndarray], default=None
        Ground truth labels, if available.

    Returns:
    --------
    metrics : dict
        Dictionary containing evaluation metrics.

    1. Silhouette Score:
    The silhouette score measures how similar an object is to its own cluster (cohesion) compared to
    how similar it is to other clusters (separation). The score ranges from -1 to +1:
    +1: Indicates that the data point is very far from the neighboring clusters and well clustered.
    0: Indicates that the data point is on or very close to the decision boundary between two neighboring
    clusters.
    -1: Indicates that the data point might have been assigned to the wrong cluster.

    Interpretation:
    A higher average silhouette score indicates better-defined clusters.
    If the score is consistently high (above 0.5), it suggests that the clusters are well separated.
    A score near 0 may indicate overlapping clusters, while negative scores suggest points may have
    been misclassified.

    2. Davies-Bouldin Index:
    The Davies-Bouldin Index (DBI) measures the average similarity ratio of each cluster with its
    most similar cluster. The index values range from 0 to ∞, with lower values indicating better clustering.
    It is defined as the ratio of within-cluster distances to between-cluster distances.

    Interpretation:
    A lower DBI value indicates that the clusters are compact and well-separated.
    Ideally, you want to minimize the Davies-Bouldin Index. If your DBI value is above 1, this indicates
    that your clusters might not be well-separated.

    3. Adjusted Rand Index (ARI):
    The Adjusted Rand Index (ARI) is a measure of the similarity between two data clusterings. The ARI
    score ranges from -1 to +1:
    1: Indicates perfect agreement between the two clusterings.
    0: Indicates that the clusterings are no better than random.
    Negative values: Indicate less agreement than expected by chance.

    Interpretation:
    A higher ARI score indicates better clustering, particularly if it's close to 1.
    An ARI score of 0 or lower suggests that the clustering results do not represent the true labels
    well, indicating a poor clustering performance.

    4. Calinski-Harabasz Index:
    The Calinski-Harabasz Index (also known as the Variance Ratio Criterion) evaluates the ratio of
    the sum of between-cluster dispersion to within-cluster dispersion. Higher values indicate better clustering.

    Interpretation:
    A higher Calinski-Harabasz Index suggests that clusters are dense and well-separated. It is typically
    used to validate the number of clusters, with higher values favoring more distinct clusters.

    5. Homogeneity Score:
    The homogeneity score measures how much a cluster contains only members of a single class (if true labels are provided).
    A score of 1 indicates perfect homogeneity, where all points in a cluster belong to the same class.

    Interpretation:
    A higher homogeneity score indicates that the clustering result is pure, meaning the clusters are composed
    of similar members. Lower values indicate mixed clusters, suggesting poor clustering performance.

    6. Completeness Score:
    The completeness score evaluates how well all members of a given class are assigned to the same cluster.
    A score of 1 indicates perfect completeness, meaning all points in a true class are assigned to a single cluster.

    Interpretation:
    A higher completeness score indicates that the clustering effectively groups all instances of a class together.
    Lower values suggest that some instances of a class are dispersed among multiple clusters.

    7. V-Measure:
    The V-measure is the harmonic mean of homogeneity and completeness, giving a balanced measure of clustering performance.

    Interpretation:
    A higher V-measure score indicates that the clusters are both homogenous (pure) and complete (cover all members of a class).
    Scores closer to 1 indicate better clustering quality.
    """
    from sklearn.metrics import (
        silhouette_score,
        davies_bouldin_score,
        adjusted_rand_score,
        calinski_harabasz_score,
        homogeneity_score,
        completeness_score,
        v_measure_score,
    )

    metrics = {}
    unique_labels = set(labels)
    if len(unique_labels) > 1 and len(unique_labels) < len(data):
        # Calculate Silhouette Score
        try:
            metrics["Silhouette Score"] = silhouette_score(data, labels)
        except Exception as e:
            metrics["Silhouette Score"] = np.nan
            print(f"Silhouette Score calculation failed: {e}")

        # Calculate Davies-Bouldin Index
        try:
            metrics["Davies-Bouldin Index"] = davies_bouldin_score(data, labels)
        except Exception as e:
            metrics["Davies-Bouldin Index"] = np.nan
            print(f"Davies-Bouldin Index calculation failed: {e}")

        # Calculate Calinski-Harabasz Index
        try:
            metrics["Calinski-Harabasz Index"] = calinski_harabasz_score(data, labels)
        except Exception as e:
            metrics["Calinski-Harabasz Index"] = np.nan
            print(f"Calinski-Harabasz Index calculation failed: {e}")

        # Calculate Adjusted Rand Index if true labels are provided
        if true_labels is not None:
            try:
                metrics["Adjusted Rand Index"] = adjusted_rand_score(
                    true_labels, labels
                )
            except Exception as e:
                metrics["Adjusted Rand Index"] = np.nan
                print(f"Adjusted Rand Index calculation failed: {e}")

            # Calculate Homogeneity Score
            try:
                metrics["Homogeneity Score"] = homogeneity_score(true_labels, labels)
            except Exception as e:
                metrics["Homogeneity Score"] = np.nan
                print(f"Homogeneity Score calculation failed: {e}")

            # Calculate Completeness Score
            try:
                metrics["Completeness Score"] = completeness_score(true_labels, labels)
            except Exception as e:
                metrics["Completeness Score"] = np.nan
                print(f"Completeness Score calculation failed: {e}")

            # Calculate V-Measure
            try:
                metrics["V-Measure"] = v_measure_score(true_labels, labels)
            except Exception as e:
                metrics["V-Measure"] = np.nan
                print(f"V-Measure calculation failed: {e}")
    else:
        # Metrics cannot be computed with 1 cluster or all points as noise
        metrics["Silhouette Score"] = np.nan
        metrics["Davies-Bouldin Index"] = np.nan
        metrics["Calinski-Harabasz Index"] = np.nan
        if true_labels is not None:
            metrics["Adjusted Rand Index"] = np.nan
            metrics["Homogeneity Score"] = np.nan
            metrics["Completeness Score"] = np.nan
            metrics["V-Measure"] = np.nan

    return metrics


def use_pd(
    func_name="excel",
    verbose=True,
    dir_json="/Users/macjianfeng/Dropbox/github/python/py2ls/py2ls/data/usages_pd.json",
):
    default_settings = fload(dir_json, output='json')
    valid_kinds = list(default_settings.keys())
    kind = strcmp(func_name, valid_kinds)[0]
    usage=default_settings[kind]
    if verbose:
        for i, i_ in enumerate(ssplit(usage, by=",")):
            i_ = i_.replace("=", "\t= ") + ","
            print(i_) if i == 0 else print("\t", i_)
    else:
        print(usage)
