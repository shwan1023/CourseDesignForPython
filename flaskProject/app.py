# 万思昊
# 编写时间：2023/6/29 21:05
from flask import Flask, render_template, send_file
import QueryExecute
import requests
import os
from flask_sqlalchemy import sqlalchemy, SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html");
@app.route('/business')
def business():
    return render_template("business/business.html");
@app.route('/city')
def city():
    return render_template("city/city.html");
@app.route('/world')
def world():
    return render_template("world/world.html");
# 首页（主题一）
@app.route('/first')
def come_first():  # put application's code here
    content = {
        # 各专业获奖数量参数导入；
        "cst_num": QueryExecute.Cst_num_cache,
        "is_num": QueryExecute.Is_num_cache,
        "si_num": QueryExecute.Si_num_cache,
        "ii_num": QueryExecute.Ii_num_cache,
        "iot_num": QueryExecute.Iot_num_cache,
        "ist_num": QueryExecute.Ist_num_cache,
        "gs_num": QueryExecute.Gs_num_cache,
        "tl_num": QueryExecute.Tl_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、获奖学生总数、论文和专利总数数据导入；
        "b_con_num": QueryExecute.CB_con_num_cache,
        "c_con_num": QueryExecute.CC_con_num_cache,
        "a_num": QueryExecute.CA_num_cache,
        "all_num": QueryExecute.CAll_num_cache,
        "stall_num": QueryExecute.CSTAll_num_cache,
        "all_pat_par_num": QueryExecute.All_pat_par_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.CTop8_name_cache,
        "ctop8_num": QueryExecute.CTop8_num_cache,
        # 各年级获奖情况数据导入；
        "all_Grade_win_b_num": QueryExecute.All_Grade_winB_num_cache,
        "all_Grade_win_c_num": QueryExecute.All_Grade_winC_num_cache,
        "all_Grade_win_a_num": QueryExecute.All_Grade_winA_num_cache,
        "all_Grade_win_con_num": QueryExecute.All_Grade_winCon_num_cache,
        "all_Grade_win_pro_num": QueryExecute.All_Grade_winPro_num_cache,
        # 竞赛标兵情况数据导入；
        "all_pio_name": QueryExecute.All_pio_name_cache,
        "all_pio_win_all_num": QueryExecute.All_pio_winAll_num_cache,
        "all_pio_win_con_num": QueryExecute.All_pio_winCon_num_cache,
        "all_pio_win_pro_num": QueryExecute.All_pio_winPro_num_cache,
        "all_pio_win_tir_num": QueryExecute.All_pio_winTir_num_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.lq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.lq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.wl_pro_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.sx_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.sx_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.mc_con_first_rate_cache
    }
    return render_template("college/first.html", **content)


@app.route('/first_school')
def come_in_first():  # put application's code here
    content = {
        "all_college_name": QueryExecute.All_college_name_cache,
        "all_college_num": QueryExecute.All_college_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、国赛获奖总数、一等奖获奖总数数据导入；
        "b_con_num": QueryExecute.SCB_con_num_cache,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.SCTop8_name_cache,
        "ctop8_num": QueryExecute.SCTop8_num_cache,
        # 每月份获奖情况数据导入；
        "every_month_all_num": QueryExecute.SEvery_month_all_num_cache,
        "every_month_all_num_first": QueryExecute.SEvery_month_all_num_first_cache,
        "every_month_all_num_b": QueryExecute.SEvery_month_all_num_b_cache,
        "every_month_all_num_a": QueryExecute.SEvery_month_all_num_a_cache,
        "every_month_all_num_con": QueryExecute.SEvery_month_all_num_con_cache,
        # 竞赛先进学院情况数据导入；
        "all_pio_college_name": QueryExecute.All_pio_college_name_cache,
        "all_pio_college_all": QueryExecute.All_pio_college_all_cache,
        "all_pio_college_con": QueryExecute.All_pio_college_con_cache,
        "all_pio_college_first": QueryExecute.All_pio_college_first_cache,
        "all_pio_college_up": QueryExecute.All_pio_college_up_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.Slq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.Slq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.Swl_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.Ssx_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.Srz_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.Smc_con_first_rate_cache
    }
    return render_template("school/first_school.html", **content)


# 主题二
@app.route('/second')
def come_second():  # put application's code here
    content = {
        # 各专业获奖数量参数导入；
        "cst_num": QueryExecute.Cst_num_cache,
        "is_num": QueryExecute.Is_num_cache,
        "si_num": QueryExecute.Si_num_cache,
        "ii_num": QueryExecute.Ii_num_cache,
        "iot_num": QueryExecute.Iot_num_cache,
        "ist_num": QueryExecute.Ist_num_cache,
        "gs_num": QueryExecute.Gs_num_cache,
        "tl_num": QueryExecute.Tl_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、获奖学生总数、论文和专利总数数据导入；
        "b_con_num": QueryExecute.CB_con_num_cache,
        "c_con_num": QueryExecute.CC_con_num_cache,
        "a_num": QueryExecute.CA_num_cache,
        "all_num": QueryExecute.CAll_num_cache,
        "stall_num": QueryExecute.CSTAll_num_cache,
        "all_pat_par_num": QueryExecute.All_pat_par_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.CTop8_name_cache,
        "ctop8_num": QueryExecute.CTop8_num_cache,
        # 各年级获奖情况数据导入；
        "all_Grade_win_b_num": QueryExecute.All_Grade_winB_num_cache,
        "all_Grade_win_c_num": QueryExecute.All_Grade_winC_num_cache,
        "all_Grade_win_a_num": QueryExecute.All_Grade_winA_num_cache,
        "all_Grade_win_con_num": QueryExecute.All_Grade_winCon_num_cache,
        "all_Grade_win_pro_num": QueryExecute.All_Grade_winPro_num_cache,
        # 竞赛标兵情况数据导入；
        "all_pio_name": QueryExecute.All_pio_name_cache,
        "all_pio_win_all_num": QueryExecute.All_pio_winAll_num_cache,
        "all_pio_win_con_num": QueryExecute.All_pio_winCon_num_cache,
        "all_pio_win_pro_num": QueryExecute.All_pio_winPro_num_cache,
        "all_pio_win_tir_num": QueryExecute.All_pio_winTir_num_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.lq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.lq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.wl_pro_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.sx_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.sx_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.mc_con_first_rate_cache
    }
    return render_template("college/second.html", **content)


@app.route('/second_school')
def come_in_second():  # put application's code here
    content = {
        "all_college_name": QueryExecute.All_college_name_cache,
        "all_college_num": QueryExecute.All_college_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、国赛获奖总数、一等奖获奖总数数据导入；
        "b_con_num": QueryExecute.SCB_con_num_cache,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.SCTop8_name_cache,
        "ctop8_num": QueryExecute.SCTop8_num_cache,
        # 每月份获奖情况数据导入；
        "every_month_all_num": QueryExecute.SEvery_month_all_num_cache,
        "every_month_all_num_first": QueryExecute.SEvery_month_all_num_first_cache,
        "every_month_all_num_b": QueryExecute.SEvery_month_all_num_b_cache,
        "every_month_all_num_a": QueryExecute.SEvery_month_all_num_a_cache,
        "every_month_all_num_con": QueryExecute.SEvery_month_all_num_con_cache,
        # 竞赛先进学院情况数据导入；
        "all_pio_college_name": QueryExecute.All_pio_college_name_cache,
        "all_pio_college_all": QueryExecute.All_pio_college_all_cache,
        "all_pio_college_con": QueryExecute.All_pio_college_con_cache,
        "all_pio_college_first": QueryExecute.All_pio_college_first_cache,
        "all_pio_college_up": QueryExecute.All_pio_college_up_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.Slq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.Slq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.Swl_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.Ssx_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.Srz_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.Smc_con_first_rate_cache
    }
    return render_template("school/second_school.html", **content)


# 主题三
@app.route('/third')
def come_third():  # put application's code here
    content = {
        # 各专业获奖数量参数导入；
        "cst_num": QueryExecute.Cst_num_cache,
        "is_num": QueryExecute.Is_num_cache,
        "si_num": QueryExecute.Si_num_cache,
        "ii_num": QueryExecute.Ii_num_cache,
        "iot_num": QueryExecute.Iot_num_cache,
        "ist_num": QueryExecute.Ist_num_cache,
        "gs_num": QueryExecute.Gs_num_cache,
        "tl_num": QueryExecute.Tl_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、获奖学生总数、论文和专利总数数据导入；
        "b_con_num": QueryExecute.CB_con_num_cache,
        "c_con_num": QueryExecute.CC_con_num_cache,
        "a_num": QueryExecute.CA_num_cache,
        "all_num": QueryExecute.CAll_num_cache,
        "stall_num": QueryExecute.CSTAll_num_cache,
        "all_pat_par_num": QueryExecute.All_pat_par_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.CTop8_name_cache,
        "ctop8_num": QueryExecute.CTop8_num_cache,
        # 各年级获奖情况数据导入；
        "all_Grade_win_b_num": QueryExecute.All_Grade_winB_num_cache,
        "all_Grade_win_c_num": QueryExecute.All_Grade_winC_num_cache,
        "all_Grade_win_a_num": QueryExecute.All_Grade_winA_num_cache,
        "all_Grade_win_con_num": QueryExecute.All_Grade_winCon_num_cache,
        "all_Grade_win_pro_num": QueryExecute.All_Grade_winPro_num_cache,
        # 竞赛标兵情况数据导入；
        "all_pio_name": QueryExecute.All_pio_name_cache,
        "all_pio_win_all_num": QueryExecute.All_pio_winAll_num_cache,
        "all_pio_win_con_num": QueryExecute.All_pio_winCon_num_cache,
        "all_pio_win_pro_num": QueryExecute.All_pio_winPro_num_cache,
        "all_pio_win_tir_num": QueryExecute.All_pio_winTir_num_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.lq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.lq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.wl_pro_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.sx_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.sx_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.mc_con_first_rate_cache
    }
    return render_template("college/third.html", **content)


@app.route('/third_school')
def come_in_third():  # put application's code here
    content = {
        "all_college_name": QueryExecute.All_college_name_cache,
        "all_college_num": QueryExecute.All_college_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、国赛获奖总数、一等奖获奖总数数据导入；
        "b_con_num": QueryExecute.SCB_con_num_cache,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.SCTop8_name_cache,
        "ctop8_num": QueryExecute.SCTop8_num_cache,
        # 每月份获奖情况数据导入；
        "every_month_all_num": QueryExecute.SEvery_month_all_num_cache,
        "every_month_all_num_first": QueryExecute.SEvery_month_all_num_first_cache,
        "every_month_all_num_b": QueryExecute.SEvery_month_all_num_b_cache,
        "every_month_all_num_a": QueryExecute.SEvery_month_all_num_a_cache,
        "every_month_all_num_con": QueryExecute.SEvery_month_all_num_con_cache,
        # 竞赛先进学院情况数据导入；
        "all_pio_college_name": QueryExecute.All_pio_college_name_cache,
        "all_pio_college_all": QueryExecute.All_pio_college_all_cache,
        "all_pio_college_con": QueryExecute.All_pio_college_con_cache,
        "all_pio_college_first": QueryExecute.All_pio_college_first_cache,
        "all_pio_college_up": QueryExecute.All_pio_college_up_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.Slq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.Slq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.Swl_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.Ssx_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.Srz_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.Smc_con_first_rate_cache
    }
    return render_template("school/third_school.html", **content)


# 主题四
@app.route('/fourth')
def come_fourth():  # put application's code here
    content = {
        # 各专业获奖数量参数导入；
        "cst_num": QueryExecute.Cst_num_cache,
        "is_num": QueryExecute.Is_num_cache,
        "si_num": QueryExecute.Si_num_cache,
        "ii_num": QueryExecute.Ii_num_cache,
        "iot_num": QueryExecute.Iot_num_cache,
        "ist_num": QueryExecute.Ist_num_cache,
        "gs_num": QueryExecute.Gs_num_cache,
        "tl_num": QueryExecute.Tl_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、获奖学生总数、论文和专利总数数据导入；
        "b_con_num": QueryExecute.CB_con_num_cache,
        "c_con_num": QueryExecute.CC_con_num_cache,
        "a_num": QueryExecute.CA_num_cache,
        "all_num": QueryExecute.CAll_num_cache,
        "stall_num": QueryExecute.CSTAll_num_cache,
        "all_pat_par_num": QueryExecute.All_pat_par_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.CTop8_name_cache,
        "ctop8_num": QueryExecute.CTop8_num_cache,
        # 各年级获奖情况数据导入；
        "all_Grade_win_b_num": QueryExecute.All_Grade_winB_num_cache,
        "all_Grade_win_c_num": QueryExecute.All_Grade_winC_num_cache,
        "all_Grade_win_a_num": QueryExecute.All_Grade_winA_num_cache,
        "all_Grade_win_con_num": QueryExecute.All_Grade_winCon_num_cache,
        "all_Grade_win_pro_num": QueryExecute.All_Grade_winPro_num_cache,
        # 竞赛标兵情况数据导入；
        "all_pio_name": QueryExecute.All_pio_name_cache,
        "all_pio_win_all_num": QueryExecute.All_pio_winAll_num_cache,
        "all_pio_win_con_num": QueryExecute.All_pio_winCon_num_cache,
        "all_pio_win_pro_num": QueryExecute.All_pio_winPro_num_cache,
        "all_pio_win_tir_num": QueryExecute.All_pio_winTir_num_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.lq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.lq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.wl_pro_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.sx_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.sx_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.mc_con_first_rate_cache
    }
    return render_template("college/fourth.html", **content)


@app.route('/fourth_school')
def come_in_fourth():  # put application's code here
    content = {
        "all_college_name": QueryExecute.All_college_name_cache,
        "all_college_num": QueryExecute.All_college_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、国赛获奖总数、一等奖获奖总数数据导入；
        "b_con_num": QueryExecute.SCB_con_num_cache,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.SCTop8_name_cache,
        "ctop8_num": QueryExecute.SCTop8_num_cache,
        # 每月份获奖情况数据导入；
        "every_month_all_num": QueryExecute.SEvery_month_all_num_cache,
        "every_month_all_num_first": QueryExecute.SEvery_month_all_num_first_cache,
        "every_month_all_num_b": QueryExecute.SEvery_month_all_num_b_cache,
        "every_month_all_num_a": QueryExecute.SEvery_month_all_num_a_cache,
        "every_month_all_num_con": QueryExecute.SEvery_month_all_num_con_cache,
        # 竞赛先进学院情况数据导入；
        "all_pio_college_name": QueryExecute.All_pio_college_name_cache,
        "all_pio_college_all": QueryExecute.All_pio_college_all_cache,
        "all_pio_college_con": QueryExecute.All_pio_college_con_cache,
        "all_pio_college_first": QueryExecute.All_pio_college_first_cache,
        "all_pio_college_up": QueryExecute.All_pio_college_up_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.Slq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.Slq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.Swl_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.Ssx_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.Srz_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.Smc_con_first_rate_cache
    }
    return render_template("school/fourth_school.html", **content)


# 主题五
@app.route('/fifth')
def come_fifth():  # put application's code here
    content = {
        # 各专业获奖数量参数导入；
        "cst_num": QueryExecute.Cst_num_cache,
        "is_num": QueryExecute.Is_num_cache,
        "si_num": QueryExecute.Si_num_cache,
        "ii_num": QueryExecute.Ii_num_cache,
        "iot_num": QueryExecute.Iot_num_cache,
        "ist_num": QueryExecute.Ist_num_cache,
        "gs_num": QueryExecute.Gs_num_cache,
        "tl_num": QueryExecute.Tl_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、获奖学生总数、论文和专利总数数据导入；
        "b_con_num": QueryExecute.CB_con_num_cache,
        "c_con_num": QueryExecute.CC_con_num_cache,
        "a_num": QueryExecute.CA_num_cache,
        "all_num": QueryExecute.CAll_num_cache,
        "stall_num": QueryExecute.CSTAll_num_cache,
        "all_pat_par_num": QueryExecute.All_pat_par_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.CTop8_name_cache,
        "ctop8_num": QueryExecute.CTop8_num_cache,
        # 各年级获奖情况数据导入；
        "all_Grade_win_b_num": QueryExecute.All_Grade_winB_num_cache,
        "all_Grade_win_c_num": QueryExecute.All_Grade_winC_num_cache,
        "all_Grade_win_a_num": QueryExecute.All_Grade_winA_num_cache,
        "all_Grade_win_con_num": QueryExecute.All_Grade_winCon_num_cache,
        "all_Grade_win_pro_num": QueryExecute.All_Grade_winPro_num_cache,
        # 竞赛标兵情况数据导入；
        "all_pio_name": QueryExecute.All_pio_name_cache,
        "all_pio_win_all_num": QueryExecute.All_pio_winAll_num_cache,
        "all_pio_win_con_num": QueryExecute.All_pio_winCon_num_cache,
        "all_pio_win_pro_num": QueryExecute.All_pio_winPro_num_cache,
        "all_pio_win_tir_num": QueryExecute.All_pio_winTir_num_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.lq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.lq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.wl_pro_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.sx_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.sx_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.mc_con_first_rate_cache
    }
    return render_template("college/fifth.html", **content)


@app.route('/fifth_school')
def come_in_fifth():  # put application's code here
    content = {
        "all_college_name": QueryExecute.All_college_name_cache,
        "all_college_num": QueryExecute.All_college_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、国赛获奖总数、一等奖获奖总数数据导入；
        "b_con_num": QueryExecute.SCB_con_num_cache,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.SCTop8_name_cache,
        "ctop8_num": QueryExecute.SCTop8_num_cache,
        # 每月份获奖情况数据导入；
        "every_month_all_num": QueryExecute.SEvery_month_all_num_cache,
        "every_month_all_num_first": QueryExecute.SEvery_month_all_num_first_cache,
        "every_month_all_num_b": QueryExecute.SEvery_month_all_num_b_cache,
        "every_month_all_num_a": QueryExecute.SEvery_month_all_num_a_cache,
        "every_month_all_num_con": QueryExecute.SEvery_month_all_num_con_cache,
        # 竞赛先进学院情况数据导入；
        "all_pio_college_name": QueryExecute.All_pio_college_name_cache,
        "all_pio_college_all": QueryExecute.All_pio_college_all_cache,
        "all_pio_college_con": QueryExecute.All_pio_college_con_cache,
        "all_pio_college_first": QueryExecute.All_pio_college_first_cache,
        "all_pio_college_up": QueryExecute.All_pio_college_up_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.Slq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.Slq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.Swl_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.Ssx_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.Srz_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.Smc_con_first_rate_cache
    }
    return render_template("school/fifth_school.html", **content)


# 主题六
@app.route('/sixth')
def come_sixth():  # put application's code here
    content = {
        # 各专业获奖数量参数导入；
        "cst_num": QueryExecute.Cst_num_cache,
        "is_num": QueryExecute.Is_num_cache,
        "si_num": QueryExecute.Si_num_cache,
        "ii_num": QueryExecute.Ii_num_cache,
        "iot_num": QueryExecute.Iot_num_cache,
        "ist_num": QueryExecute.Ist_num_cache,
        "gs_num": QueryExecute.Gs_num_cache,
        "tl_num": QueryExecute.Tl_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、获奖学生总数、论文和专利总数数据导入；
        "b_con_num": QueryExecute.CB_con_num_cache,
        "c_con_num": QueryExecute.CC_con_num_cache,
        "a_num": QueryExecute.CA_num_cache,
        "all_num": QueryExecute.CAll_num_cache,
        "stall_num": QueryExecute.CSTAll_num_cache,
        "all_pat_par_num": QueryExecute.All_pat_par_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.CTop8_name_cache,
        "ctop8_num": QueryExecute.CTop8_num_cache,
        # 各年级获奖情况数据导入；
        "all_Grade_win_b_num": QueryExecute.All_Grade_winB_num_cache,
        "all_Grade_win_c_num": QueryExecute.All_Grade_winC_num_cache,
        "all_Grade_win_a_num": QueryExecute.All_Grade_winA_num_cache,
        "all_Grade_win_con_num": QueryExecute.All_Grade_winCon_num_cache,
        "all_Grade_win_pro_num": QueryExecute.All_Grade_winPro_num_cache,
        # 竞赛标兵情况数据导入；
        "all_pio_name": QueryExecute.All_pio_name_cache,
        "all_pio_win_all_num": QueryExecute.All_pio_winAll_num_cache,
        "all_pio_win_con_num": QueryExecute.All_pio_winCon_num_cache,
        "all_pio_win_pro_num": QueryExecute.All_pio_winPro_num_cache,
        "all_pio_win_tir_num": QueryExecute.All_pio_winTir_num_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.lq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.lq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.wl_pro_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.sx_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.sx_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.mc_con_first_rate_cache
    }
    return render_template("college/sixth.html", **content)


@app.route('/sixth_school')
def come_in_sixth():  # put application's code here
    content = {
        "all_college_name": QueryExecute.All_college_name_cache,
        "all_college_num": QueryExecute.All_college_num_cache,
        # B类国家级、C类国家级、A类竞赛、获奖总数、国赛获奖总数、一等奖获奖总数数据导入；
        "b_con_num": QueryExecute.SCB_con_num_cache,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
        # 获奖数最多的前八项比赛的名称和数量导入；
        "ctop8_name": QueryExecute.SCTop8_name_cache,
        "ctop8_num": QueryExecute.SCTop8_num_cache,
        # 每月份获奖情况数据导入；
        "every_month_all_num": QueryExecute.SEvery_month_all_num_cache,
        "every_month_all_num_first": QueryExecute.SEvery_month_all_num_first_cache,
        "every_month_all_num_b": QueryExecute.SEvery_month_all_num_b_cache,
        "every_month_all_num_a": QueryExecute.SEvery_month_all_num_a_cache,
        "every_month_all_num_con": QueryExecute.SEvery_month_all_num_con_cache,
        # 竞赛先进学院情况数据导入；
        "all_pio_college_name": QueryExecute.All_pio_college_name_cache,
        "all_pio_college_all": QueryExecute.All_pio_college_all_cache,
        "all_pio_college_con": QueryExecute.All_pio_college_con_cache,
        "all_pio_college_first": QueryExecute.All_pio_college_first_cache,
        "all_pio_college_up": QueryExecute.All_pio_college_up_cache,
        # 热门竞赛获得一等奖数据导入；
        "lq_pro_first_rate": QueryExecute.Slq_pro_first_rate_cache,
        "lq_con_first_rate": QueryExecute.Slq_con_first_rate_cache,
        "wl_pro_first_rate": QueryExecute.Swl_pro_first_rate_cache,
        "sx_con_first_rate": QueryExecute.Ssx_first_rate_cache,
        "sx_pro_first_rate": QueryExecute.Srz_con_first_rate_cache,
        "mc_con_first_rate": QueryExecute.Smc_con_first_rate_cache
    }
    return render_template("school/sixth_school.html", **content)


@app.route('/show_college')
def show_college():
    content = {
        "major_name": QueryExecute.Show_major_name_cache,
        "major_num": QueryExecute.Show_major_num_cache,
        "college_com_num": QueryExecute.CAll_num_cache,
        "college_com_st_num": QueryExecute.CSTAll_num_cache,
        "college_pp_num": QueryExecute.All_pat_par_num_cache,
        "college_con_num": QueryExecute.Show_con_num_cache,
        "college_most_com_name": QueryExecute.Show_most_com_name_cache,
        "college_most_com_num": QueryExecute.Show_most_com_num_cache,
        "show_ctop8_name": QueryExecute.CTop8_name_cache,
        "show_ctop8_num": QueryExecute.CTop8_num_cache,
    }
    return render_template("analyse/show_college.html", **content)


@app.route('/show_school')
def show_school():
    content = {
        "college_name": QueryExecute.Show_college_name_cache,
        "college_num": QueryExecute.Show_college_num_cache,
        "show_ctop8_name": QueryExecute.SCTop8_name_cache,
        "show_ctop8_num": QueryExecute.SCTop8_num_cache,
        "b_num": QueryExecute.Show_school_b_num,
        "c_con_num": QueryExecute.SCC_con_num_cache,
        "a_num": QueryExecute.SCA_num_cache,
        "all_num": QueryExecute.SAll_num_cache,
        "all_con_num": QueryExecute.SAll_con_num_cache,
        "all_first_num": QueryExecute.SAll_first_num_cache,
    }
    return render_template("analyse/show_school.html", **content)


@app.route('/get_sql')
def scrape_github_sql():
    sql_file_path = './computer_college.sql'

    # 检查文件是否存在
    if os.path.exists(sql_file_path):
        return render_template("analyse/sql_status.html", flag='1')

    sql_url = 'https://raw.githubusercontent.com/{username}/{repository}/{branch}/{path_to_sql_file}'
    username = 'WorkflowWan'
    repository = 'CourseDesignForPython'
    branch = 'main'
    path_to_sql_file = 'computer college.sql'

    sql_file_url = sql_url.format(username=username, repository=repository, branch=branch,
                                  path_to_sql_file=path_to_sql_file)

    response = requests.get(sql_file_url)

    # 检查响应状态码，确保请求成功
    if response.status_code == 200:
        sql_content = response.text

        with open(sql_file_path, 'w') as file:
            file.write(sql_content)

        return render_template("analyse/sql_status.html", flag='1')

    return render_template("analyse/sql_status.html", flag='0')



if __name__ == '__main__':
    app.run()
