# 万思昊
# 编写时间：2023/6/26 9:55
import pymysql

#对于各个专业获的奖项数目的搜索；
sql_all_college_name = """SELECT DISTINCT sc.college 
                         FROM sdkj_competition AS sc 
                         ORDER BY sc.college DESC"""
sql_all_college_num = """SELECT COUNT(sc.college) 
                         FROM sdkj_competition AS sc 
                         GROUP BY sc.college 
                         ORDER BY sc.college DESC"""
sql_c_top8 = """SELECT t.competition_name FROM 
                                           (SELECT sc.competition_name, COUNT(sc.competition_name) 
                                           FROM sdkj_competition AS sc 
                                           GROUP BY sc.competition_name 
                                           ORDER BY COUNT(sc.competition_name) DESC) 
                                           AS t 
                                           WHERE 1=1 LIMIT 8"""
sql_c_top8_num = """SELECT t.num FROM 
                                (SELECT sc.competition_name, COUNT(sc.competition_name) as num											 
                                 FROM sdkj_competition AS sc
                                 GROUP BY sc.competition_name 
                                 ORDER BY COUNT(sc.competition_name) DESC) 
                                 AS t 
                                 WHERE 1=1 LIMIT 8"""
#热门竞赛获得一等奖情况搜索；
sql_only_lqb_pro_all = """SELECT COUNT(sc.competition_name ) 
                          FROM sdkj_competition AS sc 
                          WHERE sc.competition_name = '蓝桥杯' AND sc.class = '省赛'"""
sql_only_lqb_pro_first = """SELECT COUNT(sc.competition_name ) 
                            FROM sdkj_competition AS sc 
                            WHERE sc.competition_name = '蓝桥杯' AND sc.class = '省赛' AND sc.grade = '一等奖'"""
sql_only_lqb_con_first = """SELECT COUNT(c.competition_name ) 
                            FROM sdkj_competition AS c 
                            WHERE c.competition_name = '蓝桥杯' AND c.class = '国赛' AND c.grade = '一等奖'"""

sql_only_wl_pro_all ="""SELECT COUNT(c.competition_name )
                        FROM sdkj_competition AS c 
                        WHERE c.competition_name = '省物理竞赛' AND c.class = '省赛'"""
sql_only_wl_pro_first = """SELECT COUNT(c.competition_name ) 
                           FROM sdkj_competition AS c 
                           WHERE c.competition_name = '省物理竞赛' AND c.class = '省赛' AND c.grade = '一等奖'"""

sql_only_sx_all = """SELECT COUNT(c.competition_name ) 
                        FROM sdkj_competition AS c 
                        WHERE c.competition_name = '数学竞赛' """
sql_only_sx_first = """SELECT COUNT(c.competition_name ) 
                           FROM sdkj_competition AS c
                           WHERE c.competition_name = '数学竞赛' AND c.grade = '一等奖'"""

sql_only_mc_con_all = """SELECT COUNT(c.competition_name )
                         FROM sdkj_competition AS c 
                         WHERE c.competition_name = 'MathorCup数模' AND c.class = '国赛'"""
sql_only_mc_con_first = """SELECT COUNT(c.competition_name ) 
                           FROM competition_data AS c 
                           WHERE c.competition_name = 'MathorCup数模' AND c.class = '国赛' AND c.grade = '一等奖'"""
sql_only_rz_pro_all = """SELECT COUNT(c.competition_name )
                         FROM sdkj_competition AS c 
                         WHERE c.competition_name = '大英竞赛'"""
sql_only_rz_pro_first = """SELECT COUNT(c.competition_name ) 
                           FROM competition_data AS c 
                           WHERE c.competition_name = '大英竞赛' AND c.grade = '一等奖'"""

sql_ct_all = """SELECT * FROM sdkj_competition"""
sql_ct_a = """SELECT * FROM sdkj_competition AS c WHERE c.type = 'A类'"""
sql_ct_b_con = """SELECT * FROM sdkj_competition AS c WHERE c.type = 'B类' AND c.class = '国赛'"""
sql_ct_c_con = """SELECT * FROM sdkj_competition AS c WHERE c.type = 'C类' AND c.class = '国赛'"""
sql_ct_all_con = """SELECT * FROM sdkj_competition AS c WHERE  c.class = '国赛'"""
sql_ct_all_first = """SELECT * FROM sdkj_competition AS c WHERE  c.grade = '一等奖'"""



sql_st_everymonth_all_num = """SELECT COUNT(sc.grade)-1
                               FROM sdkj_competition AS sc 
                               GROUP  BY time ORDER BY time """
sql_st_everymonth_all_num_first = """SELECT COUNT(sc.grade) 
                                     FROM sdkj_competition AS sc WHERE sc.grade = '一等奖' 
                                     GROUP  BY time ORDER BY time """
sql_st_everymonth_all_num_b = """SELECT COUNT(sc.type)
                                     FROM sdkj_competition AS sc WHERE sc.type = 'B类' 
                                     GROUP  BY time ORDER BY time """
sql_st_everymonth_all_num_a = """SELECT COUNT(sc.id)
                                     FROM sdkj_competition AS sc WHERE sc.type = 'A类' 
                                     GROUP  BY time ORDER BY time """
sql_st_everymonth_all_num_con = """SELECT COUNT(sc.class)
                                     FROM sdkj_competition AS sc WHERE sc.class = '国赛' 
                                     GROUP  BY time ORDER BY time """


sql_top12_college_name = """SELECT * FROM 
                              (SELECT c.college 
                               FROM sdkj_competition AS c 
                               WHERE c.college != '济南校区' AND c.college != '泰安校区' 
                               GROUP BY c.college 
                               ORDER BY COUNT(c.college) DESC 
                               LIMIT 10 ) 
                               AS a  
                               ORDER BY a.college DESC"""
sql_top12_college_con = """SELECT COUNT(sdkj_competition.class) as '国赛' FROM  
                                  (SELECT c.college 
                                   FROM sdkj_competition AS c 
                                   WHERE c.college != '济南校区' AND c.college != '泰安校区' 
                                   GROUP BY c.college
                                   ORDER BY COUNT(c.college) DESC 
                                   LIMIT 10 ) AS a ,
                                   sdkj_competition 
                           WHERE a.college = sdkj_competition.college AND sdkj_competition.class = '国赛' 
                           GROUP BY a.college 
                           ORDER BY a.college DESC"""
sql_top12_college_all = """SELECT t.num FROM 
                                (SELECT c.college,COUNT(c.college) as 'num' 
                                 FROM sdkj_competition AS c 
                                 WHERE c.college != '济南校区' AND c.college != '泰安校区' 
                                 GROUP BY c.college
                                 ORDER BY COUNT(c.college) DESC 
                                 LIMIT 10) as t 
                                 ORDER BY t.college DESC"""
sql_top12_college_first = """SELECT COUNT(sc.grade) as '一等奖' FROM 
                                                (SELECT c.college 
                                                FROM sdkj_competition AS c 
                                                WHERE c.college != '济南校区' AND c.college != '泰安校区' 
                                                GROUP BY c.college 
                                                ORDER BY COUNT(c.college) DESC 
                                                LIMIT 10 ) AS a , 
                                                sdkj_competition as sc 
                            WHERE a.college = sc.college AND sc.grade = '三等奖' 
                            GROUP BY a.college 
                            ORDER BY a.college DESC"""
sql_top12_college_up = """SELECT COUNT(sc.class) as '国赛' FROM  
                                              (SELECT c.college 
                                               FROM sdkj_competition AS c 
                                               WHERE c.college != '济南校区' AND c.college != '泰安校区' 
                                               GROUP BY c.college 
                                               ORDER BY COUNT(c.college) DESC 
                                               LIMIT 10 )  AS a ,
                                               sdkj_competition as sc 
                        WHERE a.college = sc.college AND ((sc.class = '国赛'  AND sc.type = 'B类') OR sc.type = 'A类' ) 
                        GROUP BY a.college 
                        ORDER BY a.college DESC"""

sql_show_college_name ="""SELECT c.college
                          FROM sdkj_competition AS c
                          WHERE c.college != '泰安校区' AND c.college != '济南校区' 
                          GROUP BY c.college 
                          ORDER BY COUNT(c.college) DESC"""
sql_show_college_num = """SELECT COUNT(c.college) 
                          FROM sdkj_competition AS c 
                          WHERE c.college != '泰安校区' AND c.college != '济南校区' 
                          GROUP BY c.college
                          ORDER BY COUNT(c.college) DESC"""
sql_show_b_num = """SELECT COUNT(*) FROM sdkj_competition AS c 
                    WHERE c.type = 'B类'"""