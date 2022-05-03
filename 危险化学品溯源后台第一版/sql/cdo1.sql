/*
 Navicat Premium Data Transfer

 Source Server         : 0.本机mysql3306连接
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : cdo

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 14/02/2022 14:55:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cars
-- ----------------------------
DROP TABLE IF EXISTS `cars`;
CREATE TABLE `cars`  (
  `car_id` varchar(7) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT ' 车牌',
  `peid1` int(11) NOT NULL COMMENT '承运人一的id',
  `peid2` int(11) NULL DEFAULT NULL COMMENT '承运人二的id'
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cars
-- ----------------------------
INSERT INTO `cars` VALUES ('浙N5RSE0', 101, 102);
INSERT INTO `cars` VALUES ('黑U8Y4KE', 103, 104);
INSERT INTO `cars` VALUES ('甘IHA68N', 105, 106);
INSERT INTO `cars` VALUES ('赣T9RG6L', 107, 108);
INSERT INTO `cars` VALUES ('冀BK0IGV', 109, 110);
INSERT INTO `cars` VALUES ('冀MZHS9O', 111, 112);
INSERT INTO `cars` VALUES ('沪MNF3RQ', 113, 114);
INSERT INTO `cars` VALUES ('陕TG7DSU', 115, 116);
INSERT INTO `cars` VALUES ('云Q8MRFI', 117, 118);
INSERT INTO `cars` VALUES ('桂X5O4XI', 119, 120);
INSERT INTO `cars` VALUES ('晋XKXI4V', 121, 122);
INSERT INTO `cars` VALUES ('青JJDO5X', 123, 124);
INSERT INTO `cars` VALUES ('藏UCPULV', 125, 126);
INSERT INTO `cars` VALUES ('晋YQOM37', 127, 128);
INSERT INTO `cars` VALUES ('青OLD0RF', 129, 130);
INSERT INTO `cars` VALUES ('甘RP0IQL', 131, 132);
INSERT INTO `cars` VALUES ('陕ZF571U', 133, 134);
INSERT INTO `cars` VALUES ('赣IQ70I8', 135, 136);
INSERT INTO `cars` VALUES ('粤P5KDIE', 137, 138);
INSERT INTO `cars` VALUES ('吉NWG18L', 139, 140);

-- ----------------------------
-- Table structure for employees
-- ----------------------------
DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees`  (
  `peid` int(15) NOT NULL COMMENT '员工工号',
  `pename` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '员工姓名',
  `sex` tinyint(1) NULL DEFAULT NULL COMMENT 'true为男，false为女',
  `duty` int(11) NOT NULL DEFAULT '****' COMMENT '员工职责\r\n\r\n1.生产负责人\r\n2.仓库管理员\r\n3.运输负责人（货运司机）\r\n4.销售负责人',
  PRIMARY KEY (`peid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of employees
-- ----------------------------
INSERT INTO `employees` VALUES (1, '侯亨', 1, 2);
INSERT INTO `employees` VALUES (2, '任电伟', 1, 1);
INSERT INTO `employees` VALUES (3, '符忠婷', 0, 4);
INSERT INTO `employees` VALUES (4, '陆婉', 0, 4);
INSERT INTO `employees` VALUES (5, '官欧电艳', 0, 1);
INSERT INTO `employees` VALUES (6, '郭中翠', 0, 1);
INSERT INTO `employees` VALUES (7, '黄中琦', 0, 4);
INSERT INTO `employees` VALUES (8, '农中瑾', 0, 4);
INSERT INTO `employees` VALUES (9, '毛竹', 0, 4);
INSERT INTO `employees` VALUES (10, '姜凯轮', 1, 1);
INSERT INTO `employees` VALUES (11, '程珠', 0, 1);
INSERT INTO `employees` VALUES (12, '沈上学', 1, 2);
INSERT INTO `employees` VALUES (13, '侯楠', 1, 1);
INSERT INTO `employees` VALUES (14, '和中馨', 0, 4);
INSERT INTO `employees` VALUES (15, '幸加薇', 0, 1);
INSERT INTO `employees` VALUES (16, '文昌', 1, 1);
INSERT INTO `employees` VALUES (17, '邱礼勇', 1, 1);
INSERT INTO `employees` VALUES (18, '吴涛', 1, 2);
INSERT INTO `employees` VALUES (19, '逄礼行', 1, 1);
INSERT INTO `employees` VALUES (20, '巴欣', 0, 4);
INSERT INTO `employees` VALUES (21, '戴被菁', 0, 4);
INSERT INTO `employees` VALUES (22, '席九功', 1, 1);
INSERT INTO `employees` VALUES (23, '荣鸣', 1, 2);
INSERT INTO `employees` VALUES (24, '羊友固', 1, 2);
INSERT INTO `employees` VALUES (25, '昌友颖', 0, 4);
INSERT INTO `employees` VALUES (26, '左都琳', 0, 1);
INSERT INTO `employees` VALUES (27, '羊澹智生', 1, 1);
INSERT INTO `employees` VALUES (28, '乔姬', 0, 4);
INSERT INTO `employees` VALUES (29, '游中枫', 0, 4);
INSERT INTO `employees` VALUES (30, '柯都心', 1, 1);
INSERT INTO `employees` VALUES (31, '昌无志', 1, 1);
INSERT INTO `employees` VALUES (32, '莫忠昌', 1, 2);
INSERT INTO `employees` VALUES (33, '宗元', 1, 1);
INSERT INTO `employees` VALUES (34, '黎义', 1, 1);
INSERT INTO `employees` VALUES (35, '逄器子', 1, 1);
INSERT INTO `employees` VALUES (36, '山伦', 1, 1);
INSERT INTO `employees` VALUES (37, '居电和', 1, 1);
INSERT INTO `employees` VALUES (38, '习寒', 0, 1);
INSERT INTO `employees` VALUES (39, '明上琰', 0, 2);
INSERT INTO `employees` VALUES (40, '云智珊', 0, 4);
INSERT INTO `employees` VALUES (41, '温思', 0, 2);
INSERT INTO `employees` VALUES (42, '项忠瑞', 0, 1);
INSERT INTO `employees` VALUES (43, '包信河', 1, 2);
INSERT INTO `employees` VALUES (44, '伊上爽', 0, 1);
INSERT INTO `employees` VALUES (45, '上官义永', 1, 1);
INSERT INTO `employees` VALUES (46, '谷梁上琼', 0, 2);
INSERT INTO `employees` VALUES (47, '隗勤', 0, 1);
INSERT INTO `employees` VALUES (48, '裴上柔', 0, 2);
INSERT INTO `employees` VALUES (49, '文慧', 0, 1);
INSERT INTO `employees` VALUES (50, '盛梅', 0, 4);
INSERT INTO `employees` VALUES (51, '屈之', 1, 1);
INSERT INTO `employees` VALUES (52, '何仁强', 1, 1);
INSERT INTO `employees` VALUES (53, '翁金炎', 1, 2);
INSERT INTO `employees` VALUES (54, '孙艳', 0, 1);
INSERT INTO `employees` VALUES (55, '丁歌柔', 0, 2);
INSERT INTO `employees` VALUES (56, '昌泽', 1, 1);
INSERT INTO `employees` VALUES (57, '邬九岩', 1, 4);
INSERT INTO `employees` VALUES (58, '祝娅', 0, 4);
INSERT INTO `employees` VALUES (59, '徐毓', 0, 1);
INSERT INTO `employees` VALUES (60, '卞器淑', 0, 4);
INSERT INTO `employees` VALUES (61, '巫马瑶', 0, 4);
INSERT INTO `employees` VALUES (62, '石被楠', 1, 1);
INSERT INTO `employees` VALUES (63, '单礼蓉', 0, 1);
INSERT INTO `employees` VALUES (64, '贾妹', 0, 4);
INSERT INTO `employees` VALUES (65, '松珍', 0, 2);
INSERT INTO `employees` VALUES (66, '羊会', 1, 1);
INSERT INTO `employees` VALUES (67, '芮哲', 1, 4);
INSERT INTO `employees` VALUES (68, '吴钰有', 1, 2);
INSERT INTO `employees` VALUES (69, '皇甫伦', 1, 1);
INSERT INTO `employees` VALUES (70, '柳笑悦', 0, 1);
INSERT INTO `employees` VALUES (71, '容伯', 1, 4);
INSERT INTO `employees` VALUES (72, '衡天', 1, 1);
INSERT INTO `employees` VALUES (73, '何电纯', 0, 4);
INSERT INTO `employees` VALUES (74, '崔忠伦', 1, 4);
INSERT INTO `employees` VALUES (75, '尹笑武', 1, 1);
INSERT INTO `employees` VALUES (76, '卫育', 0, 4);
INSERT INTO `employees` VALUES (77, '缪贵', 1, 2);
INSERT INTO `employees` VALUES (78, '萧智安', 1, 4);
INSERT INTO `employees` VALUES (79, '宣强', 1, 1);
INSERT INTO `employees` VALUES (80, '吴好和', 1, 4);
INSERT INTO `employees` VALUES (81, '松娅', 0, 1);
INSERT INTO `employees` VALUES (82, '夏钰慧', 0, 1);
INSERT INTO `employees` VALUES (83, '娄莉', 0, 2);
INSERT INTO `employees` VALUES (84, '杨礼欣', 0, 1);
INSERT INTO `employees` VALUES (85, '储凯栋', 1, 2);
INSERT INTO `employees` VALUES (86, '沈易成', 1, 1);
INSERT INTO `employees` VALUES (87, '麻马悦', 0, 4);
INSERT INTO `employees` VALUES (88, '钱易军', 1, 4);
INSERT INTO `employees` VALUES (89, '罗易婕', 0, 1);
INSERT INTO `employees` VALUES (90, '何可', 0, 1);
INSERT INTO `employees` VALUES (91, '山马毓', 0, 1);
INSERT INTO `employees` VALUES (92, '衡义毓', 0, 4);
INSERT INTO `employees` VALUES (93, '宇文群', 1, 4);
INSERT INTO `employees` VALUES (94, '孙都宁', 0, 4);
INSERT INTO `employees` VALUES (95, '南门都良', 1, 1);
INSERT INTO `employees` VALUES (96, '郝仁伦', 1, 1);
INSERT INTO `employees` VALUES (97, '农凯馨', 0, 2);
INSERT INTO `employees` VALUES (98, '胡露', 0, 4);
INSERT INTO `employees` VALUES (99, '缪上伊', 0, 4);
INSERT INTO `employees` VALUES (100, '康凯风', 1, 2);
INSERT INTO `employees` VALUES (101, '寿震', 1, 3);
INSERT INTO `employees` VALUES (102, '文长金君', 0, 3);
INSERT INTO `employees` VALUES (103, '唐加静', 0, 3);
INSERT INTO `employees` VALUES (104, '毕友行', 1, 3);
INSERT INTO `employees` VALUES (105, '秦思', 0, 3);
INSERT INTO `employees` VALUES (106, '沃辰', 1, 3);
INSERT INTO `employees` VALUES (107, '李玉萍', 0, 3);
INSERT INTO `employees` VALUES (108, '刘凯震', 1, 3);
INSERT INTO `employees` VALUES (109, '郎行', 1, 3);
INSERT INTO `employees` VALUES (110, '秦天', 1, 3);
INSERT INTO `employees` VALUES (111, '臧青', 0, 3);
INSERT INTO `employees` VALUES (112, '房玉飘', 0, 3);
INSERT INTO `employees` VALUES (113, '牧茜', 0, 3);
INSERT INTO `employees` VALUES (114, '游毅', 1, 3);
INSERT INTO `employees` VALUES (115, '徐芸', 0, 3);
INSERT INTO `employees` VALUES (116, '纪琴', 0, 3);
INSERT INTO `employees` VALUES (117, '盛金桂', 0, 3);
INSERT INTO `employees` VALUES (118, '幸笑芸', 0, 3);
INSERT INTO `employees` VALUES (119, '汪上中', 1, 3);
INSERT INTO `employees` VALUES (120, '阮上雪', 0, 3);
INSERT INTO `employees` VALUES (121, '乔怡', 0, 3);
INSERT INTO `employees` VALUES (122, '离宇彪', 1, 3);
INSERT INTO `employees` VALUES (123, '巴菲', 0, 3);
INSERT INTO `employees` VALUES (124, '姚启', 1, 3);
INSERT INTO `employees` VALUES (125, '离宇旭', 1, 3);
INSERT INTO `employees` VALUES (126, '翁都凤', 0, 3);
INSERT INTO `employees` VALUES (127, '符发', 1, 3);
INSERT INTO `employees` VALUES (128, '车贝鸣', 1, 3);
INSERT INTO `employees` VALUES (129, '山笑雅', 0, 3);
INSERT INTO `employees` VALUES (130, '韦九嘉', 0, 3);
INSERT INTO `employees` VALUES (131, '沈瑞', 0, 3);
INSERT INTO `employees` VALUES (132, '隗金雪', 0, 3);
INSERT INTO `employees` VALUES (133, '焦瑾', 0, 3);
INSERT INTO `employees` VALUES (134, '苗卡爽', 0, 3);
INSERT INTO `employees` VALUES (135, '应歌榕', 1, 3);
INSERT INTO `employees` VALUES (136, '粱无丹', 0, 3);
INSERT INTO `employees` VALUES (137, '葛仁蓓', 0, 3);
INSERT INTO `employees` VALUES (138, '王国', 1, 3);
INSERT INTO `employees` VALUES (139, '刘贝钧', 1, 3);
INSERT INTO `employees` VALUES (140, '奚菲', 0, 3);

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `goods_id` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '货物批次号',
  `source` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '****' COMMENT '货物来源',
  `destination` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '****' COMMENT '目的地',
  `goods_num` int(11) NOT NULL COMMENT '内含产品数量',
  PRIMARY KEY (`goods_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of goods
-- ----------------------------

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products`  (
  `pmid` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '产品编号',
  `pmname` char(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '产品名',
  `ofrm` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '****' COMMENT '产品来源地（Origin of raw materials）',
  `rmn` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '原料名（Raw material name）',
  `vi` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '原料供应商信息（Vendor Information）',
  `dp` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '危险属性（dangerous place）',
  `pb` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '生产批次编号（Production batch）',
  `intime` timestamp NULL DEFAULT NULL COMMENT '入库时间',
  `outtime` timestamp NULL DEFAULT NULL COMMENT '出库时间',
  `goods_id` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属货物运输批号',
  `vendors_id` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '经手销售商信息',
  `sale_roll_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '流水id',
  `state` int(11) NOT NULL COMMENT '产品当前状态\r\n\r\n1.生产中\r\n2.仓库存储中\r\n3.运输中\r\n4.销售中\r\n5.已售出',
  PRIMARY KEY (`pmid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of products
-- ----------------------------

-- ----------------------------
-- Table structure for sales_rollover
-- ----------------------------
DROP TABLE IF EXISTS `sales_rollover`;
CREATE TABLE `sales_rollover`  (
  `sale_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '流水号',
  `sale_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '销售时间',
  `sale_num` int(11) NOT NULL COMMENT '销售数量',
  `buyer_id` char(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '购买人身份证号',
  `buyer_tel` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '购买人手机号',
  PRIMARY KEY (`sale_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of sales_rollover
-- ----------------------------

-- ----------------------------
-- Table structure for vendors
-- ----------------------------
DROP TABLE IF EXISTS `vendors`;
CREATE TABLE `vendors`  (
  `vendors_id` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '销售商id',
  `sell_place` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '****' COMMENT '销售地点',
  PRIMARY KEY (`vendors_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of vendors
-- ----------------------------

-- ----------------------------
-- Table structure for warehouse
-- ----------------------------
DROP TABLE IF EXISTS `warehouse`;
CREATE TABLE `warehouse`  (
  `wid` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '仓库编号',
  `wposition` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '仓库地址',
  `wname` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '仓库名',
  `peid` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '负责人id',
  PRIMARY KEY (`wid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of warehouse
-- ----------------------------
INSERT INTO `warehouse` VALUES ('1', '山西省蚌埠市五营区板泉路90号和亭佳苑', '坤江', '30');
INSERT INTO `warehouse` VALUES ('10', '台湾省百色市上甘岭区安澜路37号爱里舍花园', '浩宏', '91');
INSERT INTO `warehouse` VALUES ('2', '江苏省百色市上甘岭区白兰路98号阳光翠竹苑', '亚致力', '36');
INSERT INTO `warehouse` VALUES ('3', '贵州省百色市上甘岭区巴林路127号阳光翠竹苑', '瑞鲜', '45');
INSERT INTO `warehouse` VALUES ('4', '湖南省安庆市带岭区安澜路58号菊园五街坊', '朋恒', '27');
INSERT INTO `warehouse` VALUES ('5', '云南省安阳市金山屯区白渡路92号阳光翠竹苑', '荣世', '22');
INSERT INTO `warehouse` VALUES ('6', '贵州省白山市友好区保屯路34号博泰新苑', '京域', '3');
INSERT INTO `warehouse` VALUES ('7', '河北省安庆市带岭区宝通路71号菊园五街坊', '秋道', '9');
INSERT INTO `warehouse` VALUES ('8', '江苏省宝鸡市汤旺河区宝联路119号阳光翠竹苑', '益百', '69');
INSERT INTO `warehouse` VALUES ('9', '安徽省白城市翠峦区白渡路166号和亭佳苑', '品鑫', '81');

-- ----------------------------
-- View structure for 仓库管理员
-- ----------------------------
DROP VIEW IF EXISTS `仓库管理员`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `仓库管理员` AS select `employees`.`peid` AS `工号`,`employees`.`pename` AS `姓名` from `employees` where (`employees`.`duty` = 2);

-- ----------------------------
-- View structure for 生产负责人
-- ----------------------------
DROP VIEW IF EXISTS `生产负责人`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `生产负责人` AS select `employees`.`peid` AS `工号`,`employees`.`pename` AS `姓名` from `employees` where (`employees`.`duty` = 1);

-- ----------------------------
-- View structure for 运输负责人
-- ----------------------------
DROP VIEW IF EXISTS `运输负责人`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `运输负责人` AS select `employees`.`peid` AS `工号`,`employees`.`pename` AS `姓名` from `employees` where (`employees`.`duty` = 3);

-- ----------------------------
-- View structure for 销售负责人
-- ----------------------------
DROP VIEW IF EXISTS `销售负责人`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `销售负责人` AS select `employees`.`peid` AS `工号`,`employees`.`pename` AS `姓名` from `employees` where (`employees`.`duty` = 4);

SET FOREIGN_KEY_CHECKS = 1;
