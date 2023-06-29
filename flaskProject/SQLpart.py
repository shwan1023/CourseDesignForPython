# 万思昊
# 编写时间：2023/6/16 16:58
import pymysql
#SQL部分

#对于各个专业获的奖项数目的搜索；
sql_major_cst = """SELECT t.num FROM
                       (SELECT c.major_name,COUNT(c.major_name) as num
                       FROM competition_data AS c
                       GROUP BY c.major_name
                       ORDER BY COUNT(c.major_name) desc)
                                                   AS t WHERE t.major_name = '计算机科学与技术'"""
sql_major_is = """SELECT t.num FROM 
                                (SELECT c.major_name,COUNT(c.major_name) as num  
                                FROM competition_data AS c 
                                GROUP BY c.major_name 
                                ORDER BY COUNT(c.major_name) desc) 
                                                    AS t WHERE t.major_name = '信息安全'"""
sql_major_si = """SELECT t.num FROM 
                                (SELECT c.major_name,COUNT(c.major_name) as num  
                                FROM competition_data AS c 
                                GROUP BY c.major_name 
                                ORDER BY COUNT(c.major_name) desc) 
                                                    AS t WHERE t.major_name = '软件工程'"""
sql_major_iot = """SELECT t.num FROM 
                                (SELECT c.major_name,COUNT(c.major_name) as num  
                                FROM competition_data AS c 
                                GROUP BY c.major_name 
                                ORDER BY COUNT(c.major_name) desc) 
                                                    AS t WHERE t.major_name = '物联网工程'"""
sql_major_ii = """SELECT t.num FROM 
                                (SELECT c.major_name,COUNT(c.major_name) as num  
                                FROM competition_data AS c 
                                GROUP BY c.major_name 
                                ORDER BY COUNT(c.major_name) desc) 
                                AS t 
                                WHERE t.major_name = '网络工程'"""
sql_major_ist = """SELECT t.num FROM 
                                (SELECT c.major_name,COUNT(c.major_name) as num  
                                FROM competition_data AS c 
                                GROUP BY c.major_name 
                                ORDER BY COUNT(c.major_name) desc) 
                                AS t 
                                WHERE t.major_name = '智能科学与技术'"""
#硕博和图灵班获奖数目的搜索；
sql_major_gs = """SELECT t.num FROM 
                         (SELECT c.major_name,COUNT(c.major_name) as num  
                          FROM competition_data AS c 
                          GROUP BY c.major_name 
                          ORDER BY COUNT(c.major_name) desc) 
                          AS t
                          WHERE t.major_name = '硕士'"""
sql_major_tl = """SELECT t.num FROM 
                         (SELECT c.major_name,COUNT(c.major_name) as num  
                          FROM competition_data AS c 
                          GROUP BY c.major_name 
                          ORDER BY COUNT(c.major_name) desc) 
                          AS t 
                          WHERE t.major_name = '图灵班'"""

#对于国B、国C、A类竞赛获得奖项的搜索；
sql_ct_b_con = """SELECT * FROM competition_data AS c WHERE c.type = 'B类' AND c.class = '国赛'"""
sql_ct_c_con = """SELECT * FROM competition_data AS c WHERE c.type = 'C类' AND c.class = '国赛'"""
sql_ct_a = """SELECT * FROM competition_data AS c WHERE c.type = 'A类'"""
sql_ct_all = """SELECT * FROM competition_data"""

#对获奖学生人数的搜索；
sql_cs_all = """SELECT DISTINCT c.student_name FROM competition_data AS c"""
#搜索热门竞赛前八的竞赛名称和数量；
sql_c_top8 = """SELECT t.competition_name FROM 
                                           (SELECT c.competition_name, COUNT(c.competition_name) 
                                           FROM competition_data AS c 
                                           GROUP BY c.competition_name 
                                           ORDER BY COUNT(c.competition_name) DESC) 
                                           AS t 
                                           WHERE 1=1 LIMIT 8"""
sql_c_top8_num = """SELECT t.num FROM 
                                (SELECT c.competition_name, COUNT(c.competition_name) as num											 
                                 FROM competition_data AS c 
                                 GROUP BY c.competition_name 
                                 ORDER BY COUNT(c.competition_name) DESC) 
                                 AS t 
                                 WHERE 1=1 LIMIT 8"""

#每个年级的获奖情况；
sql_eve_grade_winA = """SELECT COUNT(t.student_grade)-1 FROM 
                                                    (SELECT * 
                                                    FROM winning_students AS ws 
                                                    WHERE ws.competition_type = 'A类') 
                                                    AS t 
                                                    GROUP BY t.student_grade 
                                                    ORDER BY t.student_grade"""
sql_eve_grade_winB = """SELECT COUNT(t.student_grade)-1 FROM 
                                                    (SELECT * 
                                                    FROM winning_students AS ws 
                                                    WHERE ws.competition_type = 'B类') 
                                                    AS t 
                                                    GROUP BY t.student_grade 
                                                    ORDER BY t.student_grade"""
sql_eve_grade_winC = """SELECT COUNT(t.student_grade)-1 FROM 
                                                    (SELECT * 
                                                    FROM winning_students AS ws 
                                                    WHERE ws.competition_type = 'C类') 
                                                    AS t 
                                                    GROUP BY t.student_grade 
                                                    ORDER BY t.student_grade"""
sql_eve_grade_winCon = """SELECT COUNT(t.student_grade)-3 FROM 
                                                    (SELECT * 
                                                    FROM winning_students AS ws 
                                                    WHERE ws.competition_class = '国赛') 
                                                    AS t 
                                                    GROUP BY t.student_grade 
                                                    ORDER BY t.student_grade"""
sql_eve_grade_winPro = """SELECT COUNT(t.student_grade) FROM 
                                                    (SELECT * 
                                                    FROM winning_students AS ws 
                                                    WHERE ws.competition_class = '省赛') 
                                                    AS t 
                                                    GROUP BY t.student_grade 
                                                    ORDER BY t.student_grade"""


#竞赛标兵信息的搜索；
sql_eve_pio_name = """SELECT * FROM 
                              (SELECT c.student_name  
                               FROM competition_data AS c 
                               GROUP BY c.student_name 
                               ORDER BY COUNT(c.student_name) DESC 
                               LIMIT 12 )
                               AS a 
                               ORDER BY a.student_name DESC"""
sql_eve_pio_winAll_num = """SELECT t.num FROM 
                                        (SELECT c.student_name,COUNT(c.student_name) as 'num'  
                                         FROM competition_data AS c 
                                         GROUP BY c.student_name 
                                         ORDER BY COUNT(c.student_name) DESC LIMIT 12) 
                                         as t 
                                         ORDER BY t.student_name DESC"""
sql_eve_pio_winCon_num = """SELECT COUNT(competition_data.grade)-1 as '国赛' FROM 
                                                                         (SELECT c.student_name  
                                                                          FROM competition_data AS c 
                                                                          GROUP BY c.student_name 
                                                                          ORDER BY COUNT(c.student_name) DESC 
                                                                          LIMIT 12 )  AS a , 
                                                                          competition_data 
                           WHERE a.student_name = competition_data.student_name AND competition_data.class = '国赛' 
                           OR competition_data.grade = 'cache'  
                           GROUP BY a.student_name 
                           ORDER BY a.student_name DESC"""
sql_eve_pio_winPro_num = """SELECT COUNT(competition_data.grade)-1 as '省赛' FROM 
                                                                          (SELECT c.student_name  
                                                                           FROM competition_data AS c 
                                                                           GROUP BY c.student_name 
                                                                           ORDER BY COUNT(c.student_name) DESC 
                                                                           LIMIT 12 ) AS a , 
                                                                           competition_data 
                            WHERE a.student_name = competition_data.student_name AND competition_data.class = '省赛' 
                            OR competition_data.grade = 'cache'  
                            GROUP BY a.student_name 
                            ORDER BY a.student_name DESC"""
sql_eve_pio_winTir_num = """SELECT COUNT(competition_data.grade)-1 as '三等奖' FROM 
                                                                           (SELECT c.student_name  
                                                                            FROM competition_data AS c 
                                                                            GROUP BY c.student_name 
                                                                            ORDER BY COUNT(c.student_name) DESC 
                                                                            LIMIT 12 ) AS a , 
                                                                            competition_data 
                             WHERE a.student_name = competition_data.student_name AND competition_data.grade = '三等奖'
                             OR competition_data.grade = 'cache'  
                             GROUP BY a.student_name 
                             ORDER BY a.student_name DESC"""
#论文和专利的搜素；
sql_paper_num = """SELECT COUNT(paper_data.id) FROM paper_data"""
sql_patent_num = """SELECT COUNT(patent_data.id) FROM patent_data"""

#热门竞赛获得一等奖情况搜索；
sql_only_lqb_pro_all = """SELECT COUNT(c.competition_name ) 
                          FROM competition_data AS c 
                          WHERE c.competition_name = '蓝桥杯' AND c.class = '省赛'"""
sql_only_lqb_pro_first = """SELECT COUNT(c.competition_name ) 
                            FROM competition_data AS c 
                            WHERE c.competition_name = '蓝桥杯' AND c.class = '省赛' AND c.grade = '一等奖'"""
sql_only_lqb_con_first = """SELECT COUNT(c.competition_name ) 
                            FROM competition_data AS c 
                            WHERE c.competition_name = '蓝桥杯' AND c.class = '国赛' AND c.grade = '一等奖'"""

sql_only_wl_pro_all ="""SELECT COUNT(c.competition_name )
                        FROM competition_data AS c 
                        WHERE c.competition_name = '省物理竞赛' AND c.class = '省赛'"""
sql_only_wl_pro_first = """SELECT COUNT(c.competition_name ) 
                           FROM competition_data AS c 
                           WHERE c.competition_name = '省物理竞赛' AND c.class = '省赛' AND c.grade = '一等奖'"""

sql_only_sx_con_all = """SELECT COUNT(c.competition_name ) 
                        FROM competition_data AS c 
                        WHERE c.competition_name = '数学竞赛国赛'"""
sql_only_sx_con_first = """SELECT COUNT(c.competition_name ) 
                           FROM competition_data AS c
                           WHERE c.competition_name = '数学竞赛国赛' AND c.grade = '一等奖'"""

sql_only_mc_con_all = """SELECT COUNT(c.competition_name )
                         FROM competition_data AS c 
                         WHERE c.competition_name = 'MathorCup数模' AND c.class = '国赛'"""
sql_only_mc_con_first = """SELECT COUNT(c.competition_name ) 
                           FROM competition_data AS c 
                           WHERE c.competition_name = 'MathorCup数模' AND c.class = '国赛' AND c.grade = '一等奖'"""

sql_only_sx_pro_all = """SELECT COUNT(c.competition_name ) 
                         FROM competition_data AS c 
                         WHERE c.competition_name = '省数学竞赛' AND c.class = '省赛'"""
sql_only_sx_pro_first = """SELECT COUNT(c.competition_name ) 
                           FROM competition_data AS c 
                           WHERE c.competition_name = '省数学竞赛' AND c.class = '省赛' AND c.grade = '一等奖'"""

sql_show_major_name ="""SELECT c.major_name 
                          FROM competition_data AS c 
                          GROUP BY c.major_name 
                          ORDER BY COUNT(c.major_name) DESC"""
sql_show_major_num = """SELECT COUNT(c.major_name) 
                          FROM competition_data AS c 
                          GROUP BY c.major_name 
                          ORDER BY COUNT(c.major_name) desc"""
sql_show_con_num = """SELECT COUNT(*) 
                          FROM competition_data AS c 
                          WHERE c.class = '国赛'"""
sql_most_com_name = """SELECT c.type
                  FROM competition_data AS c 
                  GROUP BY c.type 
                  ORDER BY COUNT(c.type) DESC  
                  LIMIT 1"""
sql_most_com_num = """SELECT COUNT(c.type)
                  FROM competition_data AS c 
                  GROUP BY c.type 
                  ORDER BY COUNT(c.type) DESC  
                  LIMIT 1"""