# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-30 12:08:37
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-12 22:11:05

from __future__ import division


def average_score(scores):
    """
    统计平局分。
    """
    score_values = scores.values()  # 每人分数是多少
    sum_scores = sum(score_values)  # 分数综合是多少
    average = sum_scores / len(score_values)  # 平均分是多少
    return average  # 整个def就是让求平均值


def sorted_score(scores):
    """
    对成绩从高到低排队。
    """
    score_lst = [(scores[k], k) for k in scores]  # 根据需要生成元组
    sort_lst = sorted(score_lst, reverse=True)  # 将元组从大到小排列
    return [(i[1], i[0]) for i in sort_lst]  # 返回一个元组


def max_score(scores):
    """
    成绩最高的姓名和分数
    """
    lst = sorted_score(scores)
    max_score = lst[0][1]
    return[(i[0], i[1]) for i in lst if i[1] == max_score]


def min_score(scores):
    """
    成绩最低的姓名和分数
    """
    lst = sorted_score(scores)
    min_score = lst[len(lst) - 1][1]
    return [(i[0], i[1]) for i in lst if i[1] == min_score]

if __name__ == '__main__':
    examine_scores = {"google": 98, "facebook": 99, "baidu": 52, "alibaba": 80,
                      "yahoo": 49, "IBM": 70, "android": 76, "apple": 99, "amazon": 99}

    ave = average_score(examine_scores)
    print "the average score is: ", ave

    sor = sorted_score(examine_scores)
    print "list of the scores: ", sor

    xueba = max_score(examine_scores)
    print "Xueba is: ", xueba

    xuezha = min_score(examine_scores)
    print "Xuezha is: ", xuezha
