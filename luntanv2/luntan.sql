/*
 Navicat Premium Data Transfer

 Source Server         : 8
 Source Server Type    : MySQL
 Source Server Version : 50739
 Source Host           : 8.210.92.129:3306
 Source Schema         : luntan

 Target Server Type    : MySQL
 Target Server Version : 50739
 File Encoding         : 65001

 Date: 17/03/2024 22:21:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for api_banner
-- ----------------------------
DROP TABLE IF EXISTS `api_banner`;
CREATE TABLE `api_banner`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `banner` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for api_comment
-- ----------------------------
DROP TABLE IF EXISTS `api_comment`;
CREATE TABLE `api_comment`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `post_id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `api_comment_post_id_251fc0c3_fk_api_posts_postId`(`post_id`) USING BTREE,
  INDEX `api_comment_user_id_14315666_fk_api_userinfo_id`(`user_id`) USING BTREE,
  CONSTRAINT `api_comment_post_id_251fc0c3_fk_api_posts_postId` FOREIGN KEY (`post_id`) REFERENCES `api_posts` (`postId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `api_comment_user_id_14315666_fk_api_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `api_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_comment
-- ----------------------------
INSERT INTO `api_comment` VALUES (1, '123321', '2024-03-17 16:33:17.464471', 1, 10);
INSERT INTO `api_comment` VALUES (2, '123321', '2024-03-17 16:33:22.052207', 1, 10);
INSERT INTO `api_comment` VALUES (3, '123321', '2024-03-17 16:46:17.592134', 1, 10);
INSERT INTO `api_comment` VALUES (7, '测试', '2024-03-17 17:09:55.732073', 1, 10);

-- ----------------------------
-- Table structure for api_continent
-- ----------------------------
DROP TABLE IF EXISTS `api_continent`;
CREATE TABLE `api_continent`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_continent
-- ----------------------------
INSERT INTO `api_continent` VALUES (1, '大洋洲');
INSERT INTO `api_continent` VALUES (2, '北美洲');
INSERT INTO `api_continent` VALUES (3, '南美洲');
INSERT INTO `api_continent` VALUES (4, '非洲');
INSERT INTO `api_continent` VALUES (5, '亚洲');
INSERT INTO `api_continent` VALUES (6, '欧洲');

-- ----------------------------
-- Table structure for api_country
-- ----------------------------
DROP TABLE IF EXISTS `api_country`;
CREATE TABLE `api_country`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `continent_id` bigint(20) NOT NULL,
  `info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `pic` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `api_country_continent_id_9123d683_fk_api_continent_id`(`continent_id`) USING BTREE,
  CONSTRAINT `api_country_continent_id_9123d683_fk_api_continent_id` FOREIGN KEY (`continent_id`) REFERENCES `api_continent` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_country
-- ----------------------------
INSERT INTO `api_country` VALUES (1, '中国', 5, '中华人民共和国', 'country_pic/微信截图_20231118170228.png');
INSERT INTO `api_country` VALUES (2, '越南', 5, '特价越南', 'country_pic/40.png');
INSERT INTO `api_country` VALUES (3, '印度', 5, '有难度来印度', 'country_pic/微信截图_20240310082040.png');

-- ----------------------------
-- Table structure for api_feedback
-- ----------------------------
DROP TABLE IF EXISTS `api_feedback`;
CREATE TABLE `api_feedback`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for api_likenum
-- ----------------------------
DROP TABLE IF EXISTS `api_likenum`;
CREATE TABLE `api_likenum`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `discussion_id` int(11) NULL DEFAULT NULL,
  `user_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `api_likenum_discussion_id_9a98adb8_fk_api_posts_postId`(`discussion_id`) USING BTREE,
  INDEX `api_likenum_user_id_3d98089f_fk_api_userinfo_id`(`user_id`) USING BTREE,
  CONSTRAINT `api_likenum_discussion_id_9a98adb8_fk_api_posts_postId` FOREIGN KEY (`discussion_id`) REFERENCES `api_posts` (`postId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `api_likenum_user_id_3d98089f_fk_api_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `api_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for api_location
-- ----------------------------
DROP TABLE IF EXISTS `api_location`;
CREATE TABLE `api_location`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `country_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `api_location_country_id_b01153c7_fk_api_country_id`(`country_id`) USING BTREE,
  CONSTRAINT `api_location_country_id_b01153c7_fk_api_country_id` FOREIGN KEY (`country_id`) REFERENCES `api_country` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_location
-- ----------------------------
INSERT INTO `api_location` VALUES (1, '天安门', 1);
INSERT INTO `api_location` VALUES (2, '中央大街', 1);
INSERT INTO `api_location` VALUES (3, '莫高窟', 1);
INSERT INTO `api_location` VALUES (4, '丽江', 1);
INSERT INTO `api_location` VALUES (5, '大理', 1);
INSERT INTO `api_location` VALUES (6, '北京', 1);
INSERT INTO `api_location` VALUES (7, '6', 1);

-- ----------------------------
-- Table structure for api_posts
-- ----------------------------
DROP TABLE IF EXISTS `api_posts`;
CREATE TABLE `api_posts`  (
  `postId` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `publish_date` datetime(6) NOT NULL,
  `types` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `post_title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `shared` tinyint(1) NOT NULL,
  `top` tinyint(1) NOT NULL,
  `view` int(11) NOT NULL,
  `newer_post` int(11) NULL DEFAULT NULL,
  `jinghua` int(11) NULL DEFAULT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `likes` int(10) UNSIGNED NOT NULL,
  `zhiding` tinyint(1) NOT NULL,
  `continent_id` bigint(20) NOT NULL,
  `country_id` bigint(20) NOT NULL,
  `location_id` bigint(20) NOT NULL,
  `user_id_id` bigint(20) NULL DEFAULT NULL,
  `is_publish` int(11) NOT NULL,
  `pic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`postId`) USING BTREE,
  INDEX `api_posts_user_id_id_788d42ac_fk_api_userinfo_id`(`user_id_id`) USING BTREE,
  INDEX `api_posts_continent_id_bd635806_fk_api_continent_id`(`continent_id`) USING BTREE,
  INDEX `api_posts_country_id_66e5b91a_fk_api_country_id`(`country_id`) USING BTREE,
  INDEX `api_posts_location_id_155ddb75_fk_api_location_id`(`location_id`) USING BTREE,
  CONSTRAINT `api_posts_continent_id_bd635806_fk_api_continent_id` FOREIGN KEY (`continent_id`) REFERENCES `api_continent` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `api_posts_country_id_66e5b91a_fk_api_country_id` FOREIGN KEY (`country_id`) REFERENCES `api_country` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `api_posts_location_id_155ddb75_fk_api_location_id` FOREIGN KEY (`location_id`) REFERENCES `api_location` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `api_posts_user_id_id_788d42ac_fk_api_userinfo_id` FOREIGN KEY (`user_id_id`) REFERENCES `api_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_posts
-- ----------------------------
INSERT INTO `api_posts` VALUES (1, '123', '2024-03-16 15:43:00.000000', '随笔', '天安门随笔1', 1, 1, 215, 1, 1, '我爱i北京天安门', 0, 0, 5, 1, 1, 1, 1, NULL);
INSERT INTO `api_posts` VALUES (2, '123', '2024-03-16 15:44:00.000000', '随笔', '随笔大理', 1, 1, 180, 1, 1, '大理真的很美', 0, 0, 5, 1, 5, 1, 1, NULL);
INSERT INTO `api_posts` VALUES (3, '123', '2024-03-16 15:45:00.000000', '随笔', '随笔丽江', 1, 1, 18, 1, 1, '1', 0, 0, 5, 1, 5, 1, 1, NULL);
INSERT INTO `api_posts` VALUES (7, NULL, '2024-03-17 19:37:09.836957', NULL, '4444保存草稿', 0, 0, 10, NULL, NULL, '<p>123123</p>', 0, 0, 5, 1, 6, 10, 0, '');
INSERT INTO `api_posts` VALUES (8, NULL, '2024-03-17 19:46:31.809250', NULL, '保存草稿', 0, 0, 2, NULL, NULL, '<p><img src=\"http://testks.natapp1.cc/static/media/pic/2a1a787443cb44dfa62953c0b1743851.jpg\" alt=\"alt\" data-href=\"http://testks.natapp1.cc/static/media/pic/2a1a787443cb44dfa62953c0b1743851.jpg\" style=\"\"/></p>', 0, 0, 5, 1, 6, 10, 1, 'null');
INSERT INTO `api_posts` VALUES (9, NULL, '2024-03-17 19:47:11.894463', NULL, '保存草稿反反复复', 0, 0, 34, NULL, NULL, '<p>fffff2222</p>', 0, 0, 5, 1, 7, 10, 1, 'static/media/pic/00b2f4d34b754f6e8a4df90885c9fa15.png');

-- ----------------------------
-- Table structure for api_posts_kind
-- ----------------------------
DROP TABLE IF EXISTS `api_posts_kind`;
CREATE TABLE `api_posts_kind`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `types` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_posts_kind
-- ----------------------------
INSERT INTO `api_posts_kind` VALUES (1, '随笔');

-- ----------------------------
-- Table structure for api_reply
-- ----------------------------
DROP TABLE IF EXISTS `api_reply`;
CREATE TABLE `api_reply`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `comment_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `api_reply_comment_id_7ec276ba_fk_api_comment_id`(`comment_id`) USING BTREE,
  INDEX `api_reply_user_id_a6c5c70f_fk_api_userinfo_id`(`user_id`) USING BTREE,
  CONSTRAINT `api_reply_comment_id_7ec276ba_fk_api_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `api_comment` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `api_reply_user_id_a6c5c70f_fk_api_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `api_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_reply
-- ----------------------------
INSERT INTO `api_reply` VALUES (1, '123321', '2024-03-17 16:48:49.548677', 1, 10);

-- ----------------------------
-- Table structure for api_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `api_userinfo`;
CREATE TABLE `api_userinfo`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `headurl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `level` int(11) NOT NULL,
  `is_vip` int(11) NOT NULL,
  `author` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sign` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `is_talk` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of api_userinfo
-- ----------------------------
INSERT INTO `api_userinfo` VALUES (1, '/static/media/app/1/2a1a787443cb44dfa62953c0b1743851.jpg', 0, 0, NULL, 'sss123444', NULL, NULL, '123', 'QWe123456', NULL, 1);
INSERT INTO `api_userinfo` VALUES (2, NULL, 0, 0, NULL, NULL, NULL, NULL, '123456', '123456', NULL, 1);
INSERT INTO `api_userinfo` VALUES (3, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `api_userinfo` VALUES (4, NULL, 0, 0, NULL, NULL, NULL, NULL, '444', '444', NULL, 1);
INSERT INTO `api_userinfo` VALUES (5, NULL, 0, 0, NULL, NULL, NULL, NULL, '4444', '4444', NULL, 1);
INSERT INTO `api_userinfo` VALUES (6, NULL, 0, 0, NULL, NULL, NULL, NULL, '44441', '3333', NULL, 1);
INSERT INTO `api_userinfo` VALUES (7, NULL, 0, 0, NULL, NULL, NULL, NULL, '111', '111', NULL, 1);
INSERT INTO `api_userinfo` VALUES (8, NULL, 0, 0, NULL, NULL, NULL, NULL, '1312', '3123', NULL, 1);
INSERT INTO `api_userinfo` VALUES (9, '/static/media/app/9/2a1a787443cb44dfa62953c0b1743851.jpg', 0, 0, NULL, '请重置名称444', NULL, NULL, '1111', '1111', NULL, 1);
INSERT INTO `api_userinfo` VALUES (10, '/static/media/app/10/00b2f4d34b754f6e8a4df90885c9fa15.png', 0, 0, NULL, '我叫张三12344', NULL, NULL, '123123', '123123', NULL, 1);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 69 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add banner', 7, 'add_banner');
INSERT INTO `auth_permission` VALUES (26, 'Can change banner', 7, 'change_banner');
INSERT INTO `auth_permission` VALUES (27, 'Can delete banner', 7, 'delete_banner');
INSERT INTO `auth_permission` VALUES (28, 'Can view banner', 7, 'view_banner');
INSERT INTO `auth_permission` VALUES (29, 'Can add comment', 8, 'add_comment');
INSERT INTO `auth_permission` VALUES (30, 'Can change comment', 8, 'change_comment');
INSERT INTO `auth_permission` VALUES (31, 'Can delete comment', 8, 'delete_comment');
INSERT INTO `auth_permission` VALUES (32, 'Can view comment', 8, 'view_comment');
INSERT INTO `auth_permission` VALUES (33, 'Can add continent', 9, 'add_continent');
INSERT INTO `auth_permission` VALUES (34, 'Can change continent', 9, 'change_continent');
INSERT INTO `auth_permission` VALUES (35, 'Can delete continent', 9, 'delete_continent');
INSERT INTO `auth_permission` VALUES (36, 'Can view continent', 9, 'view_continent');
INSERT INTO `auth_permission` VALUES (37, 'Can add country', 10, 'add_country');
INSERT INTO `auth_permission` VALUES (38, 'Can change country', 10, 'change_country');
INSERT INTO `auth_permission` VALUES (39, 'Can delete country', 10, 'delete_country');
INSERT INTO `auth_permission` VALUES (40, 'Can view country', 10, 'view_country');
INSERT INTO `auth_permission` VALUES (41, 'Can add feedback', 11, 'add_feedback');
INSERT INTO `auth_permission` VALUES (42, 'Can change feedback', 11, 'change_feedback');
INSERT INTO `auth_permission` VALUES (43, 'Can delete feedback', 11, 'delete_feedback');
INSERT INTO `auth_permission` VALUES (44, 'Can view feedback', 11, 'view_feedback');
INSERT INTO `auth_permission` VALUES (45, 'Can add location', 12, 'add_location');
INSERT INTO `auth_permission` VALUES (46, 'Can change location', 12, 'change_location');
INSERT INTO `auth_permission` VALUES (47, 'Can delete location', 12, 'delete_location');
INSERT INTO `auth_permission` VALUES (48, 'Can view location', 12, 'view_location');
INSERT INTO `auth_permission` VALUES (49, 'Can add posts_kind', 13, 'add_posts_kind');
INSERT INTO `auth_permission` VALUES (50, 'Can change posts_kind', 13, 'change_posts_kind');
INSERT INTO `auth_permission` VALUES (51, 'Can delete posts_kind', 13, 'delete_posts_kind');
INSERT INTO `auth_permission` VALUES (52, 'Can view posts_kind', 13, 'view_posts_kind');
INSERT INTO `auth_permission` VALUES (53, 'Can add user info', 14, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (54, 'Can change user info', 14, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (55, 'Can delete user info', 14, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (56, 'Can view user info', 14, 'view_userinfo');
INSERT INTO `auth_permission` VALUES (57, 'Can add reply', 15, 'add_reply');
INSERT INTO `auth_permission` VALUES (58, 'Can change reply', 15, 'change_reply');
INSERT INTO `auth_permission` VALUES (59, 'Can delete reply', 15, 'delete_reply');
INSERT INTO `auth_permission` VALUES (60, 'Can view reply', 15, 'view_reply');
INSERT INTO `auth_permission` VALUES (61, 'Can add posts', 16, 'add_posts');
INSERT INTO `auth_permission` VALUES (62, 'Can change posts', 16, 'change_posts');
INSERT INTO `auth_permission` VALUES (63, 'Can delete posts', 16, 'delete_posts');
INSERT INTO `auth_permission` VALUES (64, 'Can view posts', 16, 'view_posts');
INSERT INTO `auth_permission` VALUES (65, 'Can add like num', 17, 'add_likenum');
INSERT INTO `auth_permission` VALUES (66, 'Can change like num', 17, 'change_likenum');
INSERT INTO `auth_permission` VALUES (67, 'Can delete like num', 17, 'delete_likenum');
INSERT INTO `auth_permission` VALUES (68, 'Can view like num', 17, 'view_likenum');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$260000$WKkkt2FOaRs3pLuWbuunsD$hQL1PkhxhP5biPuh1K7GVM1tN17xILDHEgF7fEzvunc=', '2024-03-17 15:32:54.251225', 1, 'admin', '', '', 'admin@qq.com', 1, 1, '2024-03-16 10:03:27.001264');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (7, 'api', 'banner');
INSERT INTO `django_content_type` VALUES (8, 'api', 'comment');
INSERT INTO `django_content_type` VALUES (9, 'api', 'continent');
INSERT INTO `django_content_type` VALUES (10, 'api', 'country');
INSERT INTO `django_content_type` VALUES (11, 'api', 'feedback');
INSERT INTO `django_content_type` VALUES (17, 'api', 'likenum');
INSERT INTO `django_content_type` VALUES (12, 'api', 'location');
INSERT INTO `django_content_type` VALUES (16, 'api', 'posts');
INSERT INTO `django_content_type` VALUES (13, 'api', 'posts_kind');
INSERT INTO `django_content_type` VALUES (15, 'api', 'reply');
INSERT INTO `django_content_type` VALUES (14, 'api', 'userinfo');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2024-03-17 11:45:58.244360');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2024-03-17 11:46:01.975480');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2024-03-17 11:46:02.996771');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2024-03-17 11:46:03.140904');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-17 11:46:03.282808');
INSERT INTO `django_migrations` VALUES (6, 'api', '0001_initial', '2024-03-17 11:46:09.980641');
INSERT INTO `django_migrations` VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2024-03-17 11:46:10.659353');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2024-03-17 11:46:10.941369');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0003_alter_user_email_max_length', '2024-03-17 11:46:11.150386');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0004_alter_user_username_opts', '2024-03-17 11:46:11.287278');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0005_alter_user_last_login_null', '2024-03-17 11:46:11.546763');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0006_require_contenttypes_0002', '2024-03-17 11:46:11.674359');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2024-03-17 11:46:11.822821');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0008_alter_user_username_max_length', '2024-03-17 11:46:12.108465');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2024-03-17 11:46:12.396580');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0010_alter_group_name_max_length', '2024-03-17 11:46:12.619591');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0011_update_proxy_permissions', '2024-03-17 11:46:12.948694');
INSERT INTO `django_migrations` VALUES (18, 'auth', '0012_alter_user_first_name_max_length', '2024-03-17 11:46:13.231565');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2024-03-17 11:46:13.759882');
INSERT INTO `django_migrations` VALUES (20, 'api', '0002_posts_pic', '2024-03-17 19:32:33.535116');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('o7mbyx0xju5rrz1c1pe23uxnfymjptp9', '.eJxVjE0OwiAYBe_C2hAoYMGle89Avh-QqoGktCvj3W2TLnT7Zua9RYR1KXHtaY4Ti4vQ4vS7IdAz1R3wA-q9SWp1mSeUuyIP2uWtcXpdD_fvoEAvW-2sd9ZlZJXIZfasFRplTRoHQhrQO9DnEBQYDlmj0gmQxs3SgTIFJz5f7D84Tw:1rll0o:JrLTwIrCrWk2Cd59qQRWyxS1mYLxnn_GmN27Nj_NZN4', '2024-03-31 15:32:54.318932');

SET FOREIGN_KEY_CHECKS = 1;
