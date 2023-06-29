# 万思昊
# 编写时间：2023/6/16 20:38
import pymysql
import InquireWay
import SQLpart
import SQLpart_school

#对于各个专业获的奖项数目的搜索；
Cst_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_cst)
Is_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_is)
Si_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_si)
Iot_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_iot)
Ii_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_ii)
Ist_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_ist)

#硕博和图灵班获奖数目的搜索；
Gs_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_gs)
Tl_num_cache = InquireWay.inquire_one_num(SQLpart.sql_major_tl)

#对于国B、国C、A类竞赛获得奖项的搜索；
CB_con_num_cache = InquireWay.inquire_rows_num(SQLpart.sql_ct_b_con)
CC_con_num_cache = InquireWay.inquire_rows_num(SQLpart.sql_ct_c_con)
CA_num_cache = InquireWay.inquire_rows_num(SQLpart.sql_ct_a)
CAll_num_cache = InquireWay.inquire_rows_num(SQLpart.sql_ct_all)
#对所有奖项获奖项数的搜索；
CSTAll_num_cache = InquireWay.inquire_rows_num(SQLpart.sql_cs_all)
#对热门竞赛前八名情况的搜索；
CTop8_name_cache = InquireWay.inquire_type_list_num(SQLpart.sql_c_top8)
CTop8_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_c_top8_num)
#各年级获奖情况的搜索；
All_Grade_winB_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_grade_winB)
All_Grade_winA_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_grade_winA)
All_Grade_winC_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_grade_winC)
All_Grade_winCon_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_grade_winCon)
All_Grade_winPro_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_grade_winPro)
#竞赛标兵相关情况的搜索；
All_pio_name_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_pio_name)
All_pio_winAll_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_pio_winAll_num)
All_pio_winCon_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_pio_winCon_num)
All_pio_winPro_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_pio_winPro_num)
All_pio_winTir_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_eve_pio_winTir_num)
#论文和专利数量的搜搜；
All_pat_par_num_cache = InquireWay.inquire_one_num(SQLpart.sql_paper_num)+ InquireWay.inquire_one_num(SQLpart.sql_patent_num)
#热门竞赛获得一等奖概率的
lq_pro_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart.sql_only_lqb_pro_first)
                            /InquireWay.inquire_one_num(SQLpart.sql_only_lqb_pro_all),1)
lq_con_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart.sql_only_lqb_con_first)
                            /InquireWay.inquire_one_num(SQLpart.sql_only_lqb_pro_first),1)
wl_pro_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart.sql_only_wl_pro_first)
                                /InquireWay.inquire_one_num(SQLpart.sql_only_wl_pro_all),1)
sx_pro_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart.sql_only_sx_pro_first)
                                /InquireWay.inquire_one_num(SQLpart.sql_only_sx_pro_all),1)
sx_con_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart.sql_only_sx_con_first)
                                /InquireWay.inquire_one_num(SQLpart.sql_only_sx_con_all),1)
mc_con_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart.sql_only_mc_con_first)
                                /InquireWay.inquire_one_num(SQLpart.sql_only_mc_con_all),1)


#////school

All_college_name_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_all_college_name)
All_college_num_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_all_college_num)
SCTop8_name_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_c_top8)
SCTop8_num_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_c_top8_num)

Slq_pro_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart_school.sql_only_lqb_pro_first)
                            /InquireWay.inquire_one_num(SQLpart_school.sql_only_lqb_pro_all),1)
Slq_con_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart_school.sql_only_lqb_con_first)
                            /InquireWay.inquire_one_num(SQLpart_school.sql_only_lqb_pro_first),1)
Swl_pro_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart_school.sql_only_wl_pro_first)
                                /InquireWay.inquire_one_num(SQLpart_school.sql_only_wl_pro_all),1)
Ssx_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart_school.sql_only_sx_first)
                                /InquireWay.inquire_one_num(SQLpart_school.sql_only_sx_all),1)
Srz_con_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart_school.sql_only_rz_pro_first)
                                /InquireWay.inquire_one_num(SQLpart_school.sql_only_rz_pro_all),1)
Smc_con_first_rate_cache = round(100*InquireWay.inquire_one_num(SQLpart_school.sql_only_mc_con_first)
                                /InquireWay.inquire_one_num(SQLpart_school.sql_only_mc_con_all),1)

SAll_num_cache = InquireWay.inquire_rows_num(SQLpart_school.sql_ct_all)-12
SCA_num_cache = InquireWay.inquire_rows_num(SQLpart_school.sql_ct_a)-12
SCB_con_num_cache = InquireWay.inquire_rows_num(SQLpart_school.sql_ct_b_con)
SCC_con_num_cache = InquireWay.inquire_rows_num(SQLpart_school.sql_ct_c_con)
SAll_con_num_cache = InquireWay.inquire_rows_num(SQLpart_school.sql_ct_all_con)
SAll_first_num_cache = InquireWay.inquire_rows_num(SQLpart_school.sql_ct_all_first)
SEvery_month_all_num_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_st_everymonth_all_num)
SEvery_month_all_num_first_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_st_everymonth_all_num_first)
SEvery_month_all_num_b_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_st_everymonth_all_num_b)
SEvery_month_all_num_a_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_st_everymonth_all_num_a)
SEvery_month_all_num_con_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_st_everymonth_all_num_con)
All_pio_college_name_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_top12_college_name)
All_pio_college_con_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_top12_college_con)
All_pio_college_first_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_top12_college_first)
All_pio_college_all_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_top12_college_all)
All_pio_college_up_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_top12_college_up)

Show_major_name_cache = InquireWay.inquire_type_list_num(SQLpart.sql_show_major_name)
Show_major_num_cache = InquireWay.inquire_type_list_num(SQLpart.sql_show_major_num)
Show_con_num_cache = InquireWay.inquire_one_num(SQLpart.sql_show_con_num)
Show_most_com_name_cache = InquireWay.inquire_one_num(SQLpart.sql_most_com_name)
Show_most_com_num_cache = InquireWay.inquire_one_num(SQLpart.sql_most_com_num)

Show_college_name_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_show_college_name)
Show_college_num_cache = InquireWay.inquire_type_list_num(SQLpart_school.sql_show_college_num)
Show_school_b_num =  InquireWay.inquire_one_num(SQLpart_school.sql_show_b_num)




#结束后关闭数据库连接
InquireWay.over()
