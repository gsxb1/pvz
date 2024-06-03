# 数据表文件，定义对象的属性
data = {
    0:{
        "PATH": "../pic/other/peabullet.png",        #路径
        "IMAGE_INDEX_MAX": 0,                        #帧动画图片的张数
        "IMAGE_INDEX_CD": 0,                         #帧动画图片刷新的时间
        "SUMMON_CD": -1,                             #召唤物cd
        "POSITION_CD": 0.008,                        #图片刷新时间
        "SIZE": (40, 40),                            #尺寸
        "SPEED": (4, 0),
    },
    1:{
        "PATH": "../pic/zombie/0/%d.png",
        "IMAGE_INDEX_MAX": 15,
        "IMAGE_INDEX_CD": 0.2,
        "POSITION_CD": 0.3,
        "SUMMON_CD": -1,
        "SIZE": (100, 128),
        "SPEED": (-2.5, 0),
    },
    2:{
        "PATH": "../pic/other/sunlight/%d.png",
        "IMAGE_INDEX_MAX": 30,
        "IMAGE_INDEX_CD": 0.06,
        "POSITION_CD": 0.05,
        "SUMMON_CD": -1,
        "SIZE": (80, 80),
        "SPEED": (0, 2),
    },
    3:{
        "PATH": "../pic/plant/sunflower/%d.png",
        "IMAGE_INDEX_MAX": 19,
        "IMAGE_INDEX_CD": 0,
        "POSITION_CD": 0.07,
        "SUMMON_CD": 8,
        "SIZE": (128, 128),
        "SPEED": (0, 0),
    },
}