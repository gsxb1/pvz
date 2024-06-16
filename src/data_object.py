# 数据表文件，定义对象的属性
data = {
    0:{
        # 子弹
        "PATH": "../pic/other/peabullet.png",        # 路径
        "IMAGE_INDEX_MAX": 0,                        # 帧动画图片的张数
        "IMAGE_INDEX_CD": 0,                         # 帧动画图片刷新的时间
        "POSITION_CD": 0.008,                        # 图片刷新时间
        "SUMMON_CD": -1,                             # 召唤物cd
        "SIZE": (40, 40),                            # 尺寸
        "SPEED": (4, 0),                             # 速度，有正负代表在坐标系的移动
        "CAN_LOOT" : False,                          # 是否可以被拾取
        "PRICE" : 0,                                 # 价值
    },
    1:{
        # 僵尸
        "PATH": "../pic/zombie/0/%d.png",
        "IMAGE_INDEX_MAX": 15,
        "IMAGE_INDEX_CD": 0.2,
        "POSITION_CD": 0.3,
        "SUMMON_CD": -1,
        "SIZE": (100, 128),
        "SPEED": (-2.5, 0),
        "CAN_LOOT" : False,
        "PRICE" : 0,
    },
    2:{
        # 太阳花
        "PATH": "../pic/other/sunlight/%d.png",
        "IMAGE_INDEX_MAX": 30,
        "IMAGE_INDEX_CD": 0.06,
        "POSITION_CD": 0.05,
        "SUMMON_CD": -1,
        "SIZE": (80, 80),
        "SPEED": (0, 2),
        "CAN_LOOT": True,
        "PRICE" : 5,
    },
    3:{
        # 向日葵
        "PATH": "../pic/plant/sunflower/%d.png",
        "IMAGE_INDEX_MAX": 19,
        "IMAGE_INDEX_CD": 0.07,
        "POSITION_CD": -1,
        "SUMMON_CD": 8,
        "SIZE": (128, 128),
        "SPEED": (0, 0),
        "CAN_LOOT": False,
        "PRICE": 30,
    },
    4:{
      # 豌豆射手
        "PATH": "../pic/plant/peashooter/%d.png",
        "IMAGE_INDEX_MAX": 15,
        "IMAGE_INDEX_CD": 0.15,
        "POSITION_CD": -1,
        "SUMMON_CD": 6,
        "SIZE": (128, 128),
        "SPEED": (0, 0),
        "CAN_LOOT": False,
        "PRICE": 20,
    },

}