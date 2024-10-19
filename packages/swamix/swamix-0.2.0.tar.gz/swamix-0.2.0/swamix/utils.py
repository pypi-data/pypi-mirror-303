# V3.0

import json
import os
import random
import sys
import time
import hashlib
import urllib.parse


import colorama
import requests
from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright


# ----- LOGGING
def error(*args, **kwargs):
    print(colorama.Fore.RED, *args, colorama.Style.RESET_ALL, sep="", **kwargs)


def warn(*args, **kwargs):
    print(colorama.Fore.YELLOW, *args, colorama.Style.RESET_ALL, sep="", **kwargs)


def success(*args, **kwargs):
    print(colorama.Fore.GREEN, *args, colorama.Style.RESET_ALL, sep="", **kwargs)


def info(*args, **kwargs):
    print(colorama.Fore.BLUE, *args, colorama.Style.RESET_ALL, sep="", **kwargs)


# SET DATABASE ------------------


def setload(path, seperator="\n"):
    rset = set(fread(path).split(seperator))
    rset.remove("") if "" in rset else ""
    return rset


def setwrite(path, setDataType):
    fwrite(path, "\n".join(setDataType) + "\n")


def setupdate(path, newset):
    diff = newset - setload(path)
    if diff:
        fappend(path, "\n".join(diff))


# SET DATABASE ------------------
def dictdifference(A, B):
    return dict(A.items() - B.items())


# FILES SYSTEM-------------------
def fread(path, encoding="utf-8"):
    f = open(path, "r+", encoding=encoding).read()
    return f


def fwrite(fpath, content):
    f = open(fpath, "w+", encoding="utf-8", errors="ignore")
    f.write(content)


def fappend(fname, content, suffix="\n", encoding="utf-8"):
    f = open(fname, "a", encoding=encoding, errors="ignore")
    f.write(content + suffix)


def touch(fpath, data=""):
    try:
        os.makedirs(os.path.split(fpath)[0], exist_ok=True)
    except:  # noqa: E722
        pass
    if not os.path.exists(fpath):
        fwrite(fpath, data)
        print("Touched", fpath)


def fgetlastmod(path):
    '''
    Get Last modified time of a file
    '''
    return time.time() - os.path.getmtime(path)


def fincrement(cname, lock=None):
    '''
    uses a file as incrementer, slow, use in
    rare cases where you would need persistance storage.
    Uses lock to prevent I/O race condition.
    lock is derived from threading module.
    '''
    if lock:
        with lock.acquire() as l:  # noqa: E741
            c = int(fread(cname))
            c += 1
            fwrite(cname, str(c))
            l.release()
    else:
        print("please use lock")


# JSON----------------------------


def jloads(string):
    return json.loads(string)  # dict


def jload(path):
    return json.load(open(path))  # return dict


def jdumps(dictonary, indent=None):
    return json.dumps(dictonary, indent=indent)  # return string


def jdump(dictonary, path):
    return json.dump(dictonary, open(path, "w+"), indent="\t")  # write to disk


def jdumpline(dictonary, indent=None):
    return json.dumps(dictonary, indent=indent)


def jdumplines(dictionary, path):
    [fappend(path, jdumpline({k: dictionary[k]})) for k in dictionary]


def jloadlines(path):
    jsonlines = open(path, "r").readlines()
    jldict = {}
    for w in jsonlines:
        try:
            jldict.update(jloads(w))
        except Exception:
            pass
    return jldict


def list_files_timesorted(folder):
    return [folder + x for x in os.listdir(folder)].sort(key=os.path.getmtime)


# TIMESTAMPERS---------------------


def datetime(filesafe=1):
    from datetime import datetime

    template = "%Y%m%dT%H%M%S" if filesafe else "%Y-%m-%dT%H:%M:%S"
    return datetime.today().strftime(template)


def date():
    return datetime().split("T")[0]


def now():
    import time

    return int(time.time())


# RANDOMIZERS ---------------------


def shuffle(L):
    return [poprandom(L) for x in range(len(L))]


def randindex(L):
    return random.randrange(len(L))  # get random index


def poprandom(L):
    i = randindex(L)
    L[i], L[-1] = L[-1], L[i]  # swap with the last element
    return L.pop()  # pop last element O(1)


def randstr(l):
    import random

    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(l))


def hash(string):
    return hashlib.md5(string.encode("utf-8")).hexdigest()


# REQUIRE: THE DEPENDENCY MANAGER____________________
def require(modules_list: list[str]):
    if type(modules_list) is list:
        pass
    else:
        modules_list = [modules_list]

    for m in modules_list:
        try:
            exec(f'import {m}')
        except Exception as e:
            print(e)
            os.system(f"pip install {m}")


# SIMPLE-DB_________________________________
def hash_db(hashkey, *hashvalue, dirname="./LOCAL_DATABASE/"):
    """
    DESC:
        creates a folder , and stores individual hashes as files.
        if: an index(hashkey) is given then check is file exists and open and return a dict{}
        else: if second argument (hashvalue[]) is given then create a dict
    """
    itempath = dirname + hashkey
    if hashvalue:  # write inputted value to memory
        fwrite(itempath, jdumps(hashvalue[0]))
    return jload(itempath)


# THREADING__________________________________


import functools


@functools.lru_cache(maxsize=None)
def get_pool(MAX_THREADS=128):
    import concurrent.futures

    return concurrent.futures.ThreadPoolExecutor(MAX_THREADS)


def apply_async(func, *args, **kwargs):
    """
    Apply a function asynchronously using a thread pool.

    Args:
        func: The function to apply.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        A Future representing the result of the function application.
    """
    import concurrent.futures

    pool = get_pool()
    try:
        result = pool.submit(func, *args, **kwargs)
        return result
    except concurrent.futures.ThreadPoolExecutor._WorkQueueFull:
        # If the work queue is full, wait for some tasks to complete before retrying
        concurrent.futures.wait(pool._work_queue, return_when=concurrent.futures.FIRST_COMPLETED)
        result = pool.submit(func, *args, **kwargs)
        return result
    except Exception as e:
        # Log or handle any other exceptions
        print(f"Error applying function asynchronously: {e}")
        raise


def wlan_ip():
    import subprocess

    result = subprocess.run("ipconfig", stdout=subprocess.PIPE, text=True).stdout.lower()
    scan = 0
    for i in result.split("\n"):
        if "wireless" in i:
            scan = 1
        if scan:
            if "ipv4" in i:
                print(i.split(":")[1].strip())


# Benchmarking _________________
def timeit(fn, *args, times=1000, verbose=False):
    ts = time.time()
    print(f"LOG: run {fn.__name__} X {times} Times") if verbose else None
    for x in range(times):
        fnoutput = fn(*args)
    tdelta = time.time() - ts
    print(f"LOG: Ttotal: {(tdelta)*1000}ms | time/call: {(tdelta/times)*1000}ms") if verbose else None
    print(f"LOG: output == ", fnoutput) if verbose else None
    return tdelta


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    success(a)
    info(b)
