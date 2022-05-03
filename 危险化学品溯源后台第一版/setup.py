# -*- coding: UTF-8 -*-

import pymysql

if __name__ == '__main__':
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "cdo"
    }
    conn = pymysql.connect(**config)
    car_num = ['浙N5RSE0', '黑U8Y4KE', '甘IHA68N', '赣T9RG6L', '冀BK0IGV', '冀MZHS9O',
               '沪MNF3RQ', '陕TG7DSU', '云Q8MRFI', '桂X5O4XI', '晋XKXI4V', '青JJDO5X',
               '藏UCPULV', '晋YQOM37', '青OLD0RF', '甘RP0IQL', '陕ZF571U', '赣IQ70I8',
               '粤P5KDIE', '吉NWG18L'
               ]
    # driver = {'寿震': [True, 3], '文长金君': [False, 3], '唐加静': [False, 3], '毕友行': [True, 3], '秦思': [False, 3], '沃辰': [True, 3], '李玉萍': [False, 3], '刘凯震': [True, 3], '郎行': [True, 3], '秦天': [True, 3], '臧青': [False, 3], '房玉飘': [False, 3], '牧茜': [False, 3], '游毅': [True, 3], '徐芸': [False, 3], '纪琴': [False, 3], '盛金桂': [False, 3], '幸笑芸': [False, 3], '汪上中': [True, 3], '阮上雪': [False, 3], '乔怡': [False, 3], '离宇彪': [True, 3], '巴菲': [False, 3], '姚启': [True, 3], '离宇旭': [True, 3], '翁都凤': [False, 3], '符发': [True, 3], '车贝鸣': [True, 3], '山笑雅': [False, 3], '韦九嘉': [False, 3], '沈瑞': [False, 3], '隗金雪': [False, 3], '焦瑾': [False, 3], '苗卡爽': [False, 3], '应歌榕': [True, 3], '粱无丹': [False, 3], '葛仁蓓': [False, 3], '王国': [True, 3], '刘贝钧': [True, 3], '奚菲': [False, 3]}
    # employees = {'侯亨': [True, 2], '任电伟': [True, 1], '符忠婷': [False, 4], '陆婉': [False, 4], '官欧电艳': [False, 1], '郭中翠': [False, 1], '黄中琦': [False, 4], '农中瑾': [False, 4], '毛竹': [False, 4], '姜凯轮': [True, 1], '程珠': [False, 1], '沈上学': [True, 2], '侯楠': [True, 1], '和中馨': [False, 4], '幸加薇': [False, 1], '文昌': [True, 1], '邱礼勇': [True, 1], '吴涛': [True, 2], '逄礼行': [True, 1], '巴欣': [False, 4], '戴被菁': [False, 4], '席九功': [True, 1], '荣鸣': [True, 2], '羊友固': [True, 2], '昌友颖': [False, 4], '左都琳': [False, 1], '羊澹智生': [True, 1], '乔姬': [False, 4], '游中枫': [False, 4], '柯都心': [True, 1], '昌无志': [True, 1], '莫忠昌': [True, 2], '宗元': [True, 1], '黎义': [True, 1], '逄器子': [True, 1], '山伦': [True, 1], '居电和': [True, 1], '习寒': [False, 1], '明上琰': [False, 2], '云智珊': [False, 4], '温思': [False, 2], '项忠瑞': [False, 1], '包信河': [True, 2], '伊上爽': [False, 1], '上官义永': [True, 1], '谷梁上琼': [False, 2], '隗勤': [False, 1], '裴上柔': [False, 2], '文慧': [False, 1], '盛梅': [False, 4], '屈之': [True, 1], '何仁强': [True, 1], '翁金炎': [True, 2], '孙艳': [False, 1], '丁歌柔': [False, 2], '昌泽': [True, 1], '邬九岩': [True, 4], '祝娅': [False, 4], '徐毓': [False, 1], '卞器淑': [False, 4], '巫马瑶': [False, 4], '石被楠': [True, 1], '单礼蓉': [False, 1], '贾妹': [False, 4], '松珍': [False, 2], '羊会': [True, 1], '芮哲': [True, 4], '吴钰有': [True, 2], '皇甫伦': [True, 1], '柳笑悦': [False, 1], '容伯': [True, 4], '衡天': [True, 1], '何电纯': [False, 4], '崔忠伦': [True, 4], '尹笑武': [True, 1], '卫育': [False, 4], '缪贵': [True, 2], '萧智安': [True, 4], '宣强': [True, 1], '吴好和': [True, 4], '松娅': [False, 1], '夏钰慧': [False, 1], '娄莉': [False, 2], '杨礼欣': [False, 1], '储凯栋': [True, 2], '沈易成': [True, 1], '麻马悦': [False, 4], '钱易军': [True, 4], '罗易婕': [False, 1], '何可': [False, 1], '山马毓': [False, 1], '衡义毓': [False, 4], '宇文群': [True, 4], '孙都宁': [False, 4], '南门都良': [True, 1], '郝仁伦': [True, 1], '农凯馨': [False, 2], '胡露': [False, 4], '缪上伊': [False, 4], '康凯风': [True, 2]}
    employees = {'钱民': [True, 3], '赵忠祥': [True, 3], '柳义家': [True, 3], '粱都维': [True, 3], '于闾超': [True, 3], '米歌振': [True, 3], '游无士': [True, 3], '殴中斌': [True, 3], '傅成': [True, 3], '滑礼厚': [True, 3]}

    sql_employees = "INSERT INTO employees (`peid`, `pename`, `sex`, `duty`) VALUES "
    name = []
    for i in employees:
        name.append(i)
    num = 141
    for name_ in name:
        sql_employees += \
            f"('{num}','{name_}',{employees[name_][0]},'5')"
        num += 1
        sql_employees += ","
    sql_employees = sql_employees[0:-1] + ";"
    print(sql_employees)



    # sql_car = "INSERT INTO cars (`car_id`,`peid1`,`peid2`) values"
    #
    # num = 101
    # for i in range(1, 21):
    #     sql_car += f"('{car_num[i-1]}','{num}','{num+1}'),"
    #     num += 2
    # sql_car = sql_car[0:-1]+";"
    # print(sql_car)
