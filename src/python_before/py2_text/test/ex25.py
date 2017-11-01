# -*- coding:utf-8 -*-


# 复杂的定义乱七八糟 相当于这是一个模块 用import调用
def break_words(stuff):
    """This funtion with break up words for us."""
    words = stuff.split(' ')  # 定义stuff 分离（‘ ’）
    return words


def sort_words(words):
    """sorts the words."""
    return sorted(words)  # 定义了种类


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)  # pop(0) 第0个是啥
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sord_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sord_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
