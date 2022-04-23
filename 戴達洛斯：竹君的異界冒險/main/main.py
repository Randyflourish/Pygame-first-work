# 就是import
import copy  # 複製出新物件（因為python的物件會有位置重複的問題)
import numpy as np    # 位置陣列並列運算
import pygame  # 遊戲函式庫
import random  # 隨機亂數
import os  # 從電腦抓圖片的方法
import gc  # 優化暫存變數區域


# 遊戲基礎設定（螢幕、最高執行速度）

FPS = 45
WIDTH = 1500
HIGHTH = 800


# 顏色變數

WHITE = (255, 255, 255)
RED = (255, 0, 0)
STRONG_RED = (230, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
HP_GREEN = (14, 209, 69)
BLACK = (0, 0, 0)
GRAY = (105, 105, 105)
BLUE_VIOLET = (138, 43, 226)
NAVAJO_WHITE = (255, 222, 173)
MIMOSA = (230, 217, 51)
GOLDEN = (255, 210, 0)
SUN_ORANGE = (255, 115, 0)
DODGER_BLUE = (30, 144, 255)
SADDLE_BROWN = (139, 69, 19)
DARK_RED = (139, 0, 0)
AZURU = (0, 127, 255)
SAND_BROWN = (244, 164, 96)
AMBER = (255, 191, 0)
GRAYISH_PURPLE = (134, 116, 161)
LIGHT_KHAKI = (240, 230, 140)
POWDER_BLUE = (176, 224, 230)
MAUVE = (102, 64, 255)
MIDIUM_PURPLE = (147, 112, 219)


pygame.init()  # 初始化
screen = pygame.display.set_mode((WIDTH, HIGHTH))  # 螢幕輸出
pygame.display.set_caption("戴達洛斯——竹君的異界冒險  made by 羅鵬博、江柏廷、王藝翔")  # 程式名稱
clock = pygame.time.Clock()  # 時間控制


# 變數存放區

# 所有的flag
class flags(object):
    def __init__(self):
        self.in_welcome = True
        self.in_fn_list = False
        self.running = True
        self.in_bag = False
        self.in_cha = False
        self.in_weapon = False
        self.in_partner = False
        self.in_tower = False
        self.in_shop = False
        self.in_key_in = False
        self.in_bag_intro = False
        self.in_chest_gain = False
        self.in_pray = False
        self.in_battle = False
        self.in_dmg_phrase = False
        self.battle_initial = False
        self.new_round = False
        self.attack_choose = False
        self.heal_cha = False
        self.room_change = False
        self.sprite_need_change = True
        self.enter_tower = False
        self.out_tower = False
        self.lose_game = False
        self.roomgone = []
        self.win_battle = False
        self.in_nobgift = False
        self.in_gacha = False
        self.in_gotcha = False
        self.in_wp_intro = False
        self.partner_font = False
        self.partner_up = False


flag = flags()

# 所有的variable


# 商店商品
class shopitem:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def buy(self, amount):
        totcost = (self.cost*amount)
        if variable.coin >= totcost:
            return [True, variable.coin-totcost]
        else:
            return [False, variable.coin]


# 商品以陣列排序
il = []
il.append(shopitem("招募用紙", 100))
il.append(shopitem("回復藥水", 50))
il.append(shopitem("經驗值藥水", 120))
il.append(shopitem("潛能輝星", 500))

# 武器


class weapon(object):
    def __init__(self, code, ATKtype, ATK, DEFtype, DEF, Str, type):
        self.code = code
        self.type = type
        self.ATKtype = ATKtype  # 0：數值、1：％
        self.ATK = ATK
        self.DEFtype = DEFtype
        self.DEF = DEF
        self.has = False
        self.str = Str
        self.ATKstr = 'ATK'
        self.DEFstr = 'DEF'
        if self.ATKtype == 0:
            self.ATKstr += (' + ' + str(self.ATK))
        else:
            self.ATKstr += (' * '+str(self.ATK)+' %')
        if self.DEFtype == 0:
            self.DEFstr += (' + '+str(self.DEF))
        else:
            self.DEFstr += (' * '+str(self.DEF)+' %')


weaponname = [['操場上的樹枝'], ['裝滿課本的書包', '清潔用乳膠手套', '鄉民專用尺'],
              ['沾滿髒水的拖把', '泡成湯麵的維X炸醬麵', '髒掉的粉筆'], ['講桌上的籤筒', '兩根水管', '實驗室的燒杯'], ['不等臂天秤', '大辣乾鍋', '偷渡進來的澀澀書刊']]
weapontype = ['', '物理傷害', '魔法傷害', '真實傷害', '治療（對隊友使用）']
w_r0_1 = weapon((0, 0), 0, 0, 0, 0, '其實是乾掉的草', 1)
w_r1_1 = weapon((1, 0), 1, 125, 0, 0, '承載著手機、鑰匙、錢包......沒了', 1)
w_r1_2 = weapon((1, 1), 1, 85, 0, 0, '普通攻擊是巴掌二連擊', 1)
w_r1_3 = weapon((1, 2), 1, 110, 1, 110, '人人都是15公分', 1)
w_r2_1 = weapon((2, 0), 1, 140, 0, 0, '最終兵器......對有潔癖的人來說', 1)
w_r2_2 = weapon((2, 1), 1, 200, 0, 8, '如果世上有100人，就有100種吃法', 1)
w_r2_3 = weapon((2, 2), 1, 130, 0, 0, '多功能型：丟人、刮黑板都可以造成殺傷', 1)
w_r3_1 = weapon((3, 0), 1, 300, 0, 0, '掌握了它，就是掌握了命運', 1)
w_r3_2 = weapon((3, 1), 1, 150, 1, 120, '善有善報，星有星爆，不是不爆，十秒未到', 1)
w_r3_3 = weapon((3, 2), 0, 10, 1, 150, '怎麼有咖啡渣......', 1)
w_r4_1 = weapon((4, 0), 1, 175, 1, 120, '先天劣勢並不會影響後天結果', 1)
w_r4_2 = weapon((4, 1), 1, 500, 0, 0, '洗腎，GO！！！', 2)
w_r4_3 = weapon((4, 2), 1, 125, 1, 110, '有人說像綠豆糕，有人說像棋盤，但我很肯定，那是馬賽克', 4)


class variables(object):
    def __init__(self):
        self.floor = 1  # 樓層
        self.fr = 3  # 樓層+2
        self.nowroom = []  # 現在位置
        self.direction = 0  # 角色前進方向
        self.usecha = [0]  # 使用中角色代碼，最多3位
        self.dmg_phrase_index = 0  # 戰階時，當前行動的角色代碼
        self.room = []  # 地圖房間
        self.coin = 0  # 持有金錢
        self.haveitem = {"gi": 0, "lp": 0, "exp": 0, "us": 0, "mgs": 0}  # 持有道具
        self.character_list = []  # 角色總表
        self.buff = []   # 角色的buff
        self.enemy = []  # 敵人
        self.act_order = []  # 行動順序：通常：0,1,2,3,4,5
        self.work = 0  # 時間變數（控制螢幕是否更新）
        # 攻擊種類 0：普 1：技 2：奧
        self.myATKtype = [0, 0, 0]
        # 攻擊目標（0～5）
        self.myATKobject = [[], [], []]
        self.eneATKobject = []
        # 武器
        self.weapon_list = [[], [], [], [], []]
        self.weapon_list[0].append(copy.copy(w_r0_1))
        self.weapon_list[0][0].has = True
        self.weapon_list[1].append(copy.copy(w_r1_1))
        self.weapon_list[1].append(copy.copy(w_r1_2))
        self.weapon_list[1].append(copy.copy(w_r1_3))
        self.weapon_list[2].append(copy.copy(w_r2_1))
        self.weapon_list[2].append(copy.copy(w_r2_2))
        self.weapon_list[2].append(copy.copy(w_r2_3))
        self.weapon_list[3].append(copy.copy(w_r3_1))
        self.weapon_list[3].append(copy.copy(w_r3_2))
        self.weapon_list[3].append(copy.copy(w_r3_3))
        self.weapon_list[4].append(copy.copy(w_r4_1))
        self.weapon_list[4].append(copy.copy(w_r4_2))
        self.weapon_list[4].append(copy.copy(w_r4_3))
        self.equip_wp = [0, 0]

    def character_init(self):
        self.character_list.append(Mainc)
        self.character_list.append(classleader)
        self.character_list.append(secclassleader)
        self.character_list.append(studentMP)
        self.character_list.append(moneymanager)
        for i in self.character_list:
            i.LV0()
        Mainc.LVup()
        Mainc.SKCD = Mainc.oriSKCD


variable = variables()


# 鍵盤滑鼠讀入
mouse_press = pygame.mouse.get_pressed()
mouse_location = pygame.mouse.get_pos()
keyboard_press = pygame.key.get_pressed()
events = pygame.event.get()

# 鍵盤單次點擊判定("any":任意鍵)


def keyboard_one_press(n):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if n == 'any':
                return True
            elif event.key == n:
                return True
    return False

# 滑鼠單次點擊判定


def mouse_one_press(n):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_press[n]:
                return True


# 內部地圖處理區

# 地圖房間種類代碼
roomtypeq = ['S', 'M', 'M', 'M', 'M', 'B', 'B', 'B', 'G', 'M',
             'M', 'M', 'M', 'B', 'B', 'E', 'M', 'M', 'M', 'M',
             'M', 'B', 'B', 'E', 'D', 'M', 'M', 'M', 'M', 'M',
             'M', 'M', 'M', 'B', 'B', 'G', 'M', 'M', 'M', 'M',
             'M', 'M', 'M', 'M', 'B', 'B', 'B', 'D', 'P', 'M',
             'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'B', 'B',
             'B', 'G', 'E', 'D', 'M', 'M', 'M', 'M', 'M', 'M',
             'M', 'M', 'M', 'M', 'B', 'B', 'B', 'B', 'G', 'E',
             'P', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M',
             'M', 'M', 'B', 'B', 'B', 'B', 'G', 'E', 'D', 'P']
# 全房間個數，S:樓梯、M:怪、B:箱子、G:神像、D:遺骸、P:守衛、E:其他事件
"""
第一層: 1S  4M   3B   1G
第二層: 1S  8M   5B   1G   1E
第三層: 1S  13M  7B   1G   2E   1D
第四層: 1S  21M  9B   2G   2E   1D
第五層: 1S  29M  12B  2G   2E   2D   1P
第六層: 1S  38M  15B  3G   3E   3D   1P
第七層: 1S  48M  19B  4G   4E   3D   2P
第八層: 1S  59M  23B  5G   5E   4D   3P
第九層: 王
"""


# 房間隨機排序


def shuffle_room():
    tmp = []
    roo = []
    for i in range(variable.fr**2):
        tmp.append(i)
    random.shuffle(tmp)
    for y in range(variable.fr):
        roox = []
        for x in range(variable.fr):
            roox.append(roomtypeq[tmp[y*(variable.fr)+x]])
        roo.append(roox)
        del roox
    return roo


# 角色數據表


class character(object):
    def __init__(self, name, ATK, DEF, HP, SKCD, UPSKCD, ULTCD,  ATKtype, workstr):
        self.level = 0  # 獲得角色時，LV提升至1
        self.name = name
        self.ATK = ATK
        self.nATK = self.ATK[self.level]
        # 1：物理 2：法術 3：真實 4：補血 5:隨機目標 乘-1：全部敵方 乘-10：自身以外我方 乘-100：（含對方）全場 乘-1000：自身以外全場 乘-10000：全部我方
        self.ATKtype = ATKtype
        self.DEF = DEF
        self.nDEF = self.DEF[self.level]
        self.HP = HP
        self.nHP = self.HP[self.level]
        self.oriSKCD = SKCD
        self.oriUPSKCD = UPSKCD
        self.oriULTCD = ULTCD
        self.SKCD = SKCD
        self.UPSKCD = UPSKCD
        self.ULTCD = ULTCD
        self.CR = 5
        self.nCR = self.CR
        self.exp = 0  # 升級所需：此等級*2的經驗藥
        self.dizz = 0
        self.burn = 0
        self.poison = 0
        self.mock = 0
        self.recover = 0
        self.skilling = 0
        self.ultskilling = 0
        self.skillup = False
        self.norfont = ''
        self.skfont = []
        self.uskfont = []
        self.ultfont = []
        self.DEFlimit = 0
        self.ATKlimit = 0
        self.workstr = workstr

    def HPpercentage(self, len):
        if self.nHP <= 0:
            return 0
        return (self.nHP*len)//self.HP[self.level]

    def LVup(self):
        self.level += 1
        self.nATK = self.ATK[self.level]
        self.nDEF = self.DEF[self.level]
        self.nHP = self.HP[self.level]
        self.nCR = self.CR
        if not self.skillup:
            self.SKCD = 0
        else:
            self.UPSKCD = 0
        self.exp = 0
        if self.name == '竹君':
            self.equip()

    def LV0(self):
        self.level = 0
        self.nATK = self.ATK[self.level]
        self.nDEF = self.DEF[self.level]
        self.nHP = self.HP[self.level]
        self.nCR = self.CR
        self.SKCD = self.oriSKCD
        self.UPSKCD = self.oriUPSKCD
        self.ULTCD = self.oriULTCD
        self.exp = 0

    def equip(self):
        r, c = variable.equip_wp
        ewp = variable.weapon_list[r][c]
        self.ATKtype = ewp.type
        try:
            sprite.act_information.wpSK = 0
        except:
            pass
        if ewp.ATKtype == 0:
            self.nATK = self.ATK[self.level]+ewp.ATK
        else:
            self.nATK = int(self.ATK[self.level]*(ewp.ATK/100))
        if ewp.DEFtype == 0:
            self.nDEF = self.DEF[self.level]+ewp.DEF
        else:
            self.nDEF = int(self.DEF[self.level]*(ewp.DEF/100))

# 角色、武器創作


# 0
Mainc = character("竹君", ATK=[0, 5, 9, 16, 26, 40], DEF=[0, 1, 3, 7, 11, 17], HP=[
    0, 30, 45, 70, 100, 140], SKCD=5, UPSKCD=4, ULTCD=20,  ATKtype=1, workstr='多功能')
variable.character_list.append(Mainc)
Mainc.LVup()
Mainc.SKCD = Mainc.oriSKCD

# 1
classleader = character("班長", ATK=[0, 7, 15, 25, 45, 65], DEF=[0, 2, 4, 8, 12, 20], HP=[
    0, 30, 45, 65, 90, 135], SKCD=2, UPSKCD=2, ULTCD=7,  ATKtype=1, workstr='物理、輸出')
variable.character_list.append(classleader)

# 2
secclassleader = character("副班長", ATK=[0, 3, 7, 10, 15, 20], DEF=[0, 3, 8, 12, 19, 26], HP=[
    0, 50, 75, 110, 150, 195], SKCD=4, UPSKCD=4, ULTCD=8,  ATKtype=1, workstr='物理、坦克')
variable.character_list.append(secclassleader)

# 3
studentMP = character("學生議員", ATK=[0, 10, 23, 40, 60, 85], DEF=[0, 1, 2, 4, 7, 10], HP=[
    0, 20, 35, 50, 75, 100], SKCD=4, UPSKCD=3, ULTCD=10,  ATKtype=2, workstr='法術、輸出')
variable.character_list.append(studentMP)

# 4
moneymanager = character("總務股長", ATK=[0, 3, 7, 11, 18, 27], DEF=[0, 1, 3, 6, 10, 15], HP=[
    0, 25, 45, 70, 95, 125], SKCD=4, UPSKCD=4, ULTCD=9,  ATKtype=4, workstr='回復、支援')
variable.character_list.append(moneymanager)


# 5 未實裝
'''cornerperson = character("邊緣人", ATK=[0, 10, 23, 40, 60, 85], DEF=[0, 0, 0, 0, 0, 0], HP=[
    0, 25, 38, 55, 75, 100], SKCD=4, UPSKCD=3, ULTCD=9,  ATKtype=1)
variable.character_list.append(cornerperson)'''

# 角色技能與文字

ATKtype_font = ['因武器而異', '物理傷害', '魔法傷害', '真實傷害', '回復血量']


def attack_str_set():
    Mainc.norfont = '竹君 使出 普通攻擊'
    Mainc.skfont = [['竹君 使出 戰技：異於常人'], ['提升自身攻擊、防禦']]
    Mainc.uskfont = [['竹君 使出 戰技：異於常人‧改'], ['大幅提升自身攻擊、防禦']]
    Mainc.ultfont = [['竹君 使出 奧義：力逐上游'], ['永久提升自身攻擊、防禦']]
    classleader.norfont = '班長 使出 普通攻擊'
    classleader.skfont = [['班長 使出 戰技：班級統帥'], ['下次攻擊轉變為群體']]
    classleader.uskfont = [['班長 使出 戰技：班級統帥‧改'], ['提升攻擊，且下次普通攻擊轉變為群體']]
    classleader.ultfont = [['班長 使出 奧義：領導者風範'], ['削弱 ', '，並造成 ', ' 點真實傷害']]
    secclassleader.norfont = '副班長 使出 普通攻擊'
    secclassleader.skfont = [['副班長 使出 戰技：班級後盾'], ['獲得【守護】效果']]
    secclassleader.uskfont = [['副班長 使出 戰技：班級後盾‧改'], ['提升防禦，獲得【守護】效果']]
    secclassleader.ultfont = [['副班長 使出 奧義：缺曠無效'], ['抵銷並反擊下三次敵方傷害']]
    studentMP.norfont = '學生議員 使出 普通攻擊'
    studentMP.skfont = [['學生議員 使出 戰技：質詢'], ['提高所有敵人所受傷害']]
    studentMP.uskfont = [['學生議員 使出 戰技：質詢‧改'], ['提高所有敵人所受傷害']]
    studentMP.ultfont = [['學生議員 使出 奧義：言語攻擊'],
                         ['對 ', '造成 ', ' 點魔法傷害，並給予【燃燒】效果']]
    moneymanager.norfont = '總務股長 使出 普通攻擊'
    moneymanager.skfont = [['總務股長 使出 戰技：班費資助'], ['防禦力增加']]
    moneymanager.uskfont = [
        ['總務股長 使出 戰技：班費資助‧改'], ['隨機使一名DEF<=15的隊友，防禦力大幅增加']]
    moneymanager.ultfont = [
        ['總務股長 使出 奧義：冷氣！！！'], ['回復全隊 ', ' 點血量，並給予【恢復】效果']]


class monster(object):
    def __init__(self, type, ATK, DEF, HP, ATKtype, cost):
        self.level = variable.floor
        self.cost = cost
        self.type = type
        self.ATK = ATK
        self.nATK = self.ATK[self.level]
        self.ATKtype = ATKtype  # 物理、魔法、真實、補血、隨機
        self.DEF = DEF
        self.nDEF = self.DEF[self.level]
        self.HP = HP
        self.nHP = self.HP[self.level]
        self.nCR = 5
        self.DEFlimit = 0
        self.ATKlimit = 0
        self.dizz = 0
        self.burn = 0
        self.poison = 0
        self.recover = 0
        self.mock = 0

    def HPpercentage(self, len):
        if self.nHP <= 0:
            return 0
        return (self.nHP*len)//self.HP[self.level]

    def update(self):
        self.level = variable.floor
        self.nATK = self.ATK[self.level]
        self.nDEF = self.DEF[self.level]
        self.nHP = self.HP[self.level]


Slime = monster("史萊姆", ATK=[0, 5, 6, 7, 8, 9, 10, 11, 12], DEF=[0, 0, 1, 2, 3, 4, 5, 6, 7], HP=[
                0, 15, 17, 19, 21, 23, 25, 27, 29], ATKtype=1, cost=1)

Goblin = monster("哥布林", ATK=[0, 6, 8, 10, 12, 14, 16, 18, 20], DEF=[
    0, 1, 3, 5, 7, 9, 11, 13, 15], HP=[0, 32, 35, 38, 41, 44, 47, 51, 54],  ATKtype=1, cost=2)

CultPriest = monster("邪教祭司", ATK=[0,  11, 14, 17, 20, 23, 26, 29, 32], DEF=[
    0, 4, 6, 8, 10, 12, 14, 16, 18], HP=[0,  47, 51, 55, 59, 63, 67, 71, 75],  ATKtype=2, cost=3)

Orcs = monster("半獸人", ATK=[0,  15, 20, 25, 30, 35, 40, 45, 50], DEF=[
               0,  7, 9, 11, 13, 15, 17, 19, 21], HP=[0,  78, 96, 114, 132, 150, 168, 186, 204],  ATKtype=1, cost=7)

OrichalcumGolem = monster("奧利哈鋼魔像", ATK=[0, 7, 11, 15, 19, 23, 27, 31, 35], DEF=[
    0,  6, 10, 14, 18, 22, 26, 30, 34], HP=[0,  200, 300, 400, 500, 600, 700, 800, 900],  ATKtype=1, cost=12)
OrichalcumGolem.mock = 1


# 戰鬥流程與變數


enemy_cost = [0, 2, 3, 4, 6, 8, 10, 13, 16]


def enter_battle():
    variable.act_order = []
    cost = enemy_cost[variable.floor]
    sprite.battle_font.h_update()
    set_enemt_type(cost)
    for n in range(0, 3):
        if sprite_group.battle_sprite.has(sprite.battle_enemy_list[n]):
            sprite_group.battle_sprite.remove(sprite.battle_enemy_list[n])
            sprite_group.battle_sprite.remove(sprite.eneHP_list[n])
    for n in range(len(variable.usecha)):
        variable.act_order.append(n)
        if not sprite_group.battle_sprite.has(sprite.chaHP_list[n]):
            sprite_group.battle_sprite.add(sprite.chaHP_list[n])
        if not sprite_group.battle_sprite.has(sprite.battle_character_list[n]):
            sprite_group.battle_sprite.add(sprite.battle_character_list[n])
    for n in range(len(variable.enemy)):
        sprite_group.battle_sprite.add(sprite.battle_enemy_list[n])
        sprite_group.battle_sprite.add(sprite.eneHP_list[n])
        variable.act_order.append(n+3)
    sprite_group.battle_sprite.remove(sprite.act_information)
    sprite_group.battle_sprite.add(sprite.act_information)
    sprite_group.battle_sprite.remove(sprite.battle_large_image)
    sprite_group.battle_sprite.add(sprite.battle_large_image)
    for i in variable.usecha:
        c = variable.character_list[i]
        c.dizz = 0
        c.poison = 0
        c.burn = 0
        c.recover = 0
        c.mock = 0
        c.ATKlimit = 0
        c.DEFlimit = 0
        c.skilling = 0
        if c != variable.character_list[0]:
            c.ultskilling = 0
        if i == 0:
            c.ATKlimit += c.ultskilling*5
            c.DEFlimit += c.ultskilling*3


# S1：建置怪物

def set_enemt_type(n):
    variable.enemy = []
    tmp = 0
    times = 0
    while (tmp < n and times < 3):
        tmptype = random.randint(1, 100)
        if n-tmp >= 12 and variable.floor >= 7:
            if tmptype <= 60:
                variable.enemy.append(copy.copy(OrichalcumGolem))
                tmp += OrichalcumGolem.cost
                sprite.battle_enemy_list[times].type_img = Golem_img
            else:
                variable.enemy.append(copy.copy(Orcs))
                tmp += Orcs.cost
                sprite.battle_enemy_list[times].type_img = Orcs_img
        elif n-tmp >= 7 and variable.floor >= 5:
            if tmptype <= 60:
                variable.enemy.append(copy.copy(Orcs))
                tmp += Orcs.cost
                sprite.battle_enemy_list[times].type_img = Orcs_img
            else:
                variable.enemy.append(copy.copy(CultPriest))
                tmp += CultPriest.cost
                sprite.battle_enemy_list[times].type_img = CultPriest_img
        elif n-tmp >= 3 and variable.floor >= 3:
            if tmptype <= 60:
                variable.enemy.append(copy.copy(CultPriest))
                tmp += CultPriest.cost
                sprite.battle_enemy_list[times].type_img = CultPriest_img
            else:
                variable.enemy.append(copy.copy(Goblin))
                tmp += Goblin.cost
                sprite.battle_enemy_list[times].type_img = Goblin_img
        elif n-tmp >= 2 and variable.floor >= 2:
            if tmptype <= 60:
                variable.enemy.append(copy.copy(Goblin))
                tmp += Goblin.cost
                sprite.battle_enemy_list[times].type_img = Goblin_img
            else:
                variable.enemy.append(copy.copy(Slime))
                tmp += Slime.cost
                sprite.battle_enemy_list[times].type_img = Slime_img
        else:
            variable.enemy.append(copy.copy(Slime))
            tmp += Slime.cost
            sprite.battle_enemy_list[times].type_img = Slime_img
        variable.enemy[times].update()
        times += 1

# S2：回合開始


def round_start():
    sprite.act_information.act = 0
    sprite.act_information.ringrect.top = 205
    sprite.act_information.havecalculate = False
    variable.myATKtype = [-1, -1, -1]
    variable.myATKobject = [[], [], []]
    variable.act_order = []
    variable.dmg_phrase_index = 0
    flag.in_dmg_phrase = False
    # 過場 0.2 sec（？）
    for i in range(len(variable.usecha)):
        cha = variable.usecha[i]
        perform = variable.character_list[cha]
        if perform.nHP <= 0:
            perform.nHP = 0
            perform.dizz = 0
            perform.burn = 0
            perform.mock = 0
            perform.poison = 0
            perform.recover = 0
        if perform.nHP > 0:
            if perform.dizz > 0:
                perform.dizz -= 1
            if perform.burn > 0:
                perform.burn -= 1
                perform.nHP -= max(int(perform.HP[perform.level]
                                       * 0.08)-perform.nDEF, 1)
                perform.nHP = max(0, perform.nHP)
            if perform.mock > 0:
                perform.mock -= 1
                if perform.mock == 0 and cha == 2:
                    if perform.DEFlimit >= int(perform.nDEF*0.2):
                        perform.DEFlimit -= int(perform.nDEF*0.2)
            if perform.poison > 0:
                perform.poison -= 1
                perform.nHP -= max(int(perform.HP[perform.level]
                                       * 0.03), 1)
                perform.nHP = max(0, perform.nHP)
            if perform.recover > 0:
                perform.recover -= 1
                perform.nHP += max(int((perform.HP[perform.level])
                                       * 0.05), 1)
                perform.nHP = min(
                    perform.nHP, perform.HP[perform.level])
            if perform.skilling > 0:
                if cha == 1:
                    pass
                else:
                    perform.skilling -= 1
                # if ==0 and name==
            if perform.ultskilling > 0:
                if cha == 0 or cha == 2:
                    pass
                else:
                    perform.ultskilling -= 1
                # if ==0 and name==
            if perform.SKCD > 0:
                perform.SKCD -= 1
            if perform.ULTCD > 0:
                perform.ULTCD -= 1
            variable.act_order.append(i)
    for i in range(len(variable.enemy)):
        ene = variable.enemy[i]
        if ene.nHP <= 0:
            ene.nHP = 0
            ene.dizz = 0
            ene.burn = 0
            ene.mock = 0
            ene.poison = 0
            ene.recover = 0
        elif ene.nHP > 0:
            if ene.dizz > 0:
                ene.dizz -= 1
            if ene.burn > 0:
                ene.burn -= 1
                ene.nHP -= max(int(ene.HP[ene.level]
                                   * 0.08)-ene.nDEF, 1)
                ene.nHP = max(0, ene.nHP)
            if ene.mock > 0 and ene.type != "奧利哈鋼魔像":
                ene.mock -= 1
            if ene.poison > 0:
                ene.poison -= 1
                ene.nHP -= max(int(ene.HP[ene.level]
                                   * 0.03), 1)
                ene.nHP = max(0, ene.nHP)
            if ene.recover > 0:
                ene.recover -= 1
                ene.nHP += max(int((ene.HP[ene.level])
                                   * 0.05), 1)
                ene.nHP = min(
                    ene.nHP, ene.HP[ene.level])
            variable.act_order.append(i+3)
            if ene.DEFlimit == -ene.nDEF:
                if variable.character_list[1].ultskilling == 0:
                    ene.DEFlimit = 0
    ene_ATK_choose()

# S3：攻擊選定


# S3-1：敵方（於round_start()執行）
def ene_ATK_choose():
    variable.eneATKobject = []
    # 攻擊對象選取
    for i in range(len(variable.enemy)):
        object = (random.randint(1, 99)) % len(variable.usecha)
        while variable.character_list[variable.usecha[object]].nHP == 0:
            object = (random.randint(1, 99)) % len(variable.usecha)
        variable.eneATKobject.append(object)


# 載入圖片
function_list_img = pygame.image.load(
    os.path.join("main", "image", "list.png")).convert()
function_list_back_img = pygame.image.load(
    os.path.join("main", "image", "list_back.png")).convert()
village_map_img = pygame.image.load(
    os.path.join("main", "image", "village_map.png")).convert()
in_back_img = pygame.image.load(
    os.path.join("main", "image", "Meadow.png")).convert()
tower_outline_img = pygame.image.load(
    os.path.join("main", "image", "tower_outline.png")).convert_alpha()  # 透明背景convert
gachaboard_img = pygame.image.load(
    os.path.join("main", "image", "gachaboard.png")).convert_alpha()
g_gachaitem_img = pygame.image.load(os.path.join(
    "main", "image", "gacha", "g_gachaitem.png")).convert_alpha()
gift_img = pygame.image.load(
    os.path.join("main", "image", "gift.png")).convert_alpha()
shop_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "Shop.png")).convert_alpha()
shopmenu_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "shopmenu.png")).convert()
shop_back_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "shop_background.jpeg")).convert()
cancel_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "cancel.png")).convert_alpha()
gachaitem_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "gachaitem.png")).convert_alpha()
life_potion_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "life_potion.png")).convert_alpha()
exp_potion_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "exp_potion.png")).convert_alpha()
upstar_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "upstar.png")).convert_alpha()
b_gachaitem_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_gachaitem.png")).convert_alpha()
b_life_potion_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_life_potion.png")).convert_alpha()
b_exp_potion_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_exp_potion.png")).convert_alpha()
b_upstar_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_upstar.png")).convert_alpha()
b_magic_stone_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_magic_stone.png")).convert_alpha()
b_coin_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_coin.png")).convert_alpha()
b_introblock_img = pygame.image.load(os.path.join(
    "main", "image", "bag", "b_introduce.png")).convert_alpha()
inpbox_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "inpbox.png")).convert()
no_img = pygame.image.load(os.path.join(
    "main", "image", "no.png")).convert_alpha()
yes_img = pygame.image.load(os.path.join(
    "main", "image", "yes.png")).convert_alpha()
inp_error_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "inp_error.png")).convert()
buy_suc_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "buy_suc.png")).convert_alpha()
buy_fail_img = pygame.image.load(os.path.join(
    "main", "image", "shop", "buy_fail.png")).convert_alpha()
tower_room_img = pygame.image.load(os.path.join(
    "main", "image", "room.png")).convert()
door1_img = pygame.image.load(os.path.join(
    "main", "image", "door1.png")).convert()
door2_img = pygame.image.load(os.path.join(
    "main", "image", "door2.png")).convert()
door3_img = pygame.image.load(os.path.join(
    "main", "image", "door3.png")).convert()
door4_img = pygame.image.load(os.path.join(
    "main", "image", "door4.png")).convert()
portal_img = pygame.image.load(
    os.path.join("main", "image", "portal.png")).convert_alpha()
chest_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "chest.png")).convert_alpha()
openedchest_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "chestopened.png")).convert_alpha()
c_gachaitem_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "c_gachaitem.png")).convert_alpha()
c_upstar_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "c_upstar.png")).convert_alpha()
c_magic_stone_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "c_magic_stone.png")).convert_alpha()
c_coin_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "c_coin.png")).convert_alpha()
c_life_potion_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "c_life_potion.png")).convert_alpha()
c_exp_potion_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "c_exp_potion.png")).convert_alpha()
chestgain_img = pygame.image.load(os.path.join(
    "main", "image", "chest", "gain.png")).convert_alpha()
Slime_l_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Slime_a.png")).convert_alpha()
Slime_s_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Slime_b.png")).convert_alpha()
Slime_img = [Slime_l_img, Slime_s_img]
Goblin_l_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Goblin_a.png")).convert_alpha()
Goblin_s_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Goblin_b.png")).convert_alpha()
Goblin_img = [Goblin_l_img, Goblin_s_img]
CultPriest_l_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "CultPriest_a.png")).convert_alpha()
CultPriest_s_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "CultPriest_b.png")).convert_alpha()
CultPriest_img = [CultPriest_l_img, CultPriest_s_img]
Orcs_l_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Orcs_a.png")).convert_alpha()
Orcs_s_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Orcs_b.png")).convert_alpha()
Orcs_img = [Orcs_l_img, Orcs_s_img]
Golem_l_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Golem_a.png")).convert_alpha()
Golem_s_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Golem_b.png")).convert_alpha()
Golem_img = [Golem_l_img, Golem_s_img]
deadslime_img = pygame.image.load(os.path.join(
    "main", "image", "enemy", "Slimedead.png")).convert_alpha()
statue_img = pygame.image.load(os.path.join(
    "main", "image", "statue.png")).convert_alpha()
bigstatue_img = pygame.image.load(os.path.join(
    "main", "image", "bigstatue.png")).convert_alpha()
statue_2_img = pygame.image.load(os.path.join(
    "main", "image", "statue_bless.png")).convert_alpha()
bigstatue_2_img = pygame.image.load(os.path.join(
    "main", "image", "bigstatue_bless.png")).convert_alpha()
tomb_img = pygame.image.load(os.path.join(
    "main", "image", "tomb.png")).convert_alpha()
knight_img = pygame.image.load(os.path.join(
    "main", "image", "knight.png")).convert_alpha()
NPC_img = pygame.image.load(os.path.join(
    "main", "image", "NPC.png")).convert_alpha()
cha_ba_1_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_ba_1.png")).convert_alpha()
cha_ba_2_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_ba_2.png")).convert_alpha()
cha_ba_3_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_ba_3.png")).convert_alpha()
cha_ba_img = [cha_ba_2_img, cha_ba_1_img, cha_ba_3_img, cha_ba_1_img]
cha_fr_1_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_fr_1.png")).convert_alpha()
cha_fr_2_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_fr_2.png")).convert_alpha()
cha_fr_3_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_fr_3.png")).convert_alpha()
cha_fr_img = [cha_fr_2_img, cha_fr_1_img, cha_fr_3_img, cha_fr_1_img]
cha_le_1_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_le_1.png")).convert_alpha()
cha_le_2_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_le_2.png")).convert_alpha()
cha_le_3_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_le_3.png")).convert_alpha()
cha_le_img = [cha_le_2_img, cha_le_1_img, cha_le_3_img, cha_le_1_img]
cha_ri_1_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_ri_1.png")).convert_alpha()
cha_ri_2_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_ri_2.png")).convert_alpha()
cha_ri_3_img = pygame.image.load(os.path.join(
    "main", "image", "cha", "cha_ri_3.png")).convert_alpha()
cha_ri_img = [cha_ri_2_img, cha_ri_1_img, cha_ri_3_img, cha_ri_1_img]
tow_midblock_img = pygame.image.load(os.path.join(
    "main", "image", "tower_midblock.png")).convert_alpha()
HPbar_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "HPbar.png")).convert()
s_HPbar_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "small_HPbar.png")).convert()
normalATK_botton_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "bot_1.png")).convert_alpha()
skillATK_botton_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "bot_2.png")).convert_alpha()
ultraATK_botton_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "bot_3.png")).convert_alpha()
healATK_botton_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "bot_4.png")).convert_alpha()
execute_botton_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "bot_5.png")).convert_alpha()
detail_botton_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "bot_6.png")).convert_alpha()
botton_ring_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "choose_ring.png")).convert_alpha()
bat_font_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "font.png")).convert_alpha()
recover_font_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "recover_font.png")).convert_alpha()
recover_font2_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "recover_font2.png")).convert_alpha()
victory_gain_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "vic_gain.png")).convert_alpha()
gachaUI_img = pygame.image.load(os.path.join(
    "main", "image", "gacha", "gacha_UI.png")).convert()
w_ring_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "usering.png")).convert_alpha()
w_equip_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "equip_bot.png")).convert()
w_r0_1_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "操場上的樹枝.png")).convert_alpha()
w_r1_1_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "裝滿課本的書包.png")).convert_alpha()
w_r1_2_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "清潔用乳膠手套.png")).convert_alpha()
w_r1_3_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "鄉民專用尺.png")).convert_alpha()
w_r2_1_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "沾滿髒水的拖把.png")).convert_alpha()
w_r2_2_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "泡成湯麵的維X炸醬麵.png")).convert_alpha()
w_r2_3_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "髒掉的粉筆.png")).convert_alpha()
w_r3_1_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "講桌上的籤筒.png")).convert_alpha()
w_r3_2_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "兩根水管.png")).convert_alpha()
w_r3_3_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "實驗室的燒杯.png")).convert_alpha()
w_r4_1_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "不等臂天秤.png")).convert_alpha()
w_r4_2_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "大辣乾鍋.png")).convert_alpha()
w_r4_3_img = pygame.image.load(os.path.join(
    "main", "image", "weapon", "偷渡進來的澀澀書刊.png")).convert_alpha()
weapon_img = [[w_r0_1_img], [w_r1_1_img, w_r1_2_img, w_r1_3_img], [w_r2_1_img, w_r2_2_img,
                                                                   w_r2_3_img], [w_r3_1_img, w_r3_2_img, w_r3_3_img], [w_r4_1_img, w_r4_2_img, w_r4_3_img]]

partner_0_s_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_0_a.png")).convert_alpha()
partner_1_s_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_1_a.png")).convert_alpha()
partner_2_s_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_2_a.png")).convert_alpha()
partner_3_s_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_3_a.png")).convert_alpha()
partner_4_s_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_4_a.png")).convert_alpha()
partner_0_l_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_0_b.png")).convert_alpha()
partner_1_l_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_1_b.png")).convert_alpha()
partner_2_l_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_2_b.png")).convert_alpha()
partner_3_l_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_3_b.png")).convert_alpha()
partner_4_l_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "cha_4_b.png")).convert_alpha()
partner_s_img = [partner_0_s_img, partner_1_s_img,
                 partner_2_s_img, partner_3_s_img, partner_4_s_img]
partner_l_img = [partner_0_l_img, partner_1_l_img,
                 partner_2_l_img, partner_3_l_img, partner_4_l_img]
p_equip_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "equip_bot.png")).convert()
p_goup_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "go_up.png")).convert_alpha()
p_plus_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "up_plus.png")).convert_alpha()
p_HP_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "HP_bot.png")).convert_alpha()
p_recover_font_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "recover_font.png")).convert_alpha()
p_recover_font2_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "recover_font2.png")).convert_alpha()
p_EXP_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "EXP_bot.png")).convert_alpha()
p_EXP_font_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "EXP_font.png")).convert_alpha()
p_EXP_font2_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "EXP_font2.png")).convert_alpha()
p_star_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "star_bot.png")).convert_alpha()
p_star_font_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "star_font.png")).convert_alpha()
p_star_font2_img = pygame.image.load(os.path.join(
    "main", "image", "partner", "star_font2.png")).convert_alpha()
bat_back_img = pygame.image.load(os.path.join(
    "main", "image", "battle", "GrassMaze.png")).convert()

# 字體(font)設定
font_27_18 = pygame.font.SysFont("microsoftjhenghei", 18)
font_27_18_B = pygame.font.SysFont("microsoftjhenghei", 18, bold=True)
font_27_24 = pygame.font.SysFont("microsoftjhenghei", 24)
font_27_24_B = pygame.font.SysFont("microsoftjhenghei", 24, bold=True)
font_27_30 = pygame.font.SysFont("microsoftjhenghei", 30)
font_27_30_B = pygame.font.SysFont("microsoftjhenghei", 30, bold=True)
font_27_40 = pygame.font.SysFont("microsoftjhenghei", 40)
font_27_40_B = pygame.font.SysFont("microsoftjhenghei", 40, bold=True)
font_27_50 = pygame.font.SysFont("microsoftjhenghei", 50)
font_27_50_B = pygame.font.SysFont("microsoftjhenghei", 50, bold=True)
font_27_60 = pygame.font.SysFont("microsoftjhenghei", 60)
font_27_60_B = pygame.font.SysFont("microsoftjhenghei", 60, bold=True)
font_27_80 = pygame.font.SysFont("microsoftjhenghei", 80)
font_27_80_B = pygame.font.SysFont("microsoftjhenghei", 80, bold=True)
font_27_100_B = pygame.font.SysFont("microsoftjhenghei", 100, bold=True)
font_m_55 = pygame.font.Font(None, 55)
font_m_60 = pygame.font.Font(None, 60)
font_m_100 = pygame.font.Font(None, 100)
font_m_200 = pygame.font.Font(None, 200)


# 文字方塊
title_font_1 = font_27_100_B.render("戴達洛斯", False, MAUVE)
title_font_1_h = title_font_1.get_height()
title_font_2 = font_27_80.render("竹君的異界冒險", False, MIDIUM_PURPLE)
enter_tower_font_1 = font_27_40.render("魔塔", False, BLUE_VIOLET)
enter_tower_font_1_h = enter_tower_font_1.get_height()
enter_tower_font_2 = font_27_30.render("點擊 E 以進入魔塔", False, GRAY)
gacha_font_1 = font_27_40.render("招募", False, SUN_ORANGE)
gacha_font_1_h = gacha_font_1.get_height()
gacha_font_2 = font_27_30.render("點擊 E 以進入招募介面", False, GRAY)
gacha_hasno_font = font_27_50_B.render("招募卷不足", False, BLACK)
gacha_go_font = font_27_50_B.render("點擊左鍵並拖曳至招募板上", False, BLACK)
gacha_cancel_font = font_27_50_B.render("點擊右鍵或 C 以取消", False, BLACK)
gift_font_1 = font_27_40.render("新手支援禮包", False, AMBER)
gift_font_1_h = gift_font_1.get_height()
gift_font_2 = font_27_30.render("點擊 E 以開啟禮包", False, GRAY)
village_shop_font_1 = font_27_40.render("商店", False, SUN_ORANGE)
village_shop_font_1_h = village_shop_font_1.get_height()
village_shop_font_2 = font_27_30.render("點擊 E 以進入商店介面", False, GRAY)
bag_font_1 = font_27_50_B.render("背包", False, BLACK)
bag_font_1_h = bag_font_1.get_height()
bag_font_1_w = bag_font_1.get_width()
bag_font_2 = font_27_40_B.render("點擊圖示以查看詳情", False, GRAY)
bag_font_2_w = bag_font_2.get_width()
bag_coin_font_1 = font_27_80_B.render("錢", False, GOLDEN)
bag_coin_font_1_w = bag_coin_font_1.get_width()
bag_coin_font_1_h = bag_coin_font_1.get_height()
bag_coin_font_2 = font_27_50.render("就是錢", False, BLACK)
bag_us_font_1 = font_27_80_B.render("潛能輝星", False, BLUE_VIOLET)
bag_us_font_1_w = bag_us_font_1.get_width()
bag_us_font_1_h = bag_us_font_1.get_height()
bag_us_font_2 = font_27_50.render("擁有不可思議力量的一顆星星", False, BLACK)
bag_us_font_2_h = bag_us_font_2.get_height()
bag_us_font_3 = font_27_50.render("似乎可以讓角色進化", False, BLACK)
bag_us_font_3_h = bag_us_font_3.get_height()
bag_us_font_4 = font_27_40_B.render("可於角色介面使用", False, GRAY)
bag_lp_font_1 = font_27_80_B.render("生命藥水", False, DARK_RED)
bag_lp_font_1_w = bag_lp_font_1.get_width()
bag_lp_font_1_h = bag_lp_font_1.get_height()
bag_lp_font_2 = font_27_50.render("使用後回復全隊生命值", False, BLACK)
bag_lp_font_2_h = bag_lp_font_2.get_height()
bag_lp_font_3 = font_27_40_B.render("可於戰鬥中/角色介面使用", False, GRAY)
bag_exp_font_1 = font_27_80_B.render("經驗藥水", False, AZURU)
bag_exp_font_1_w = bag_exp_font_1.get_width()
bag_exp_font_1_h = bag_exp_font_1.get_height()
bag_exp_font_2 = font_27_50.render("使用後提升全隊經驗值", False, BLACK)
bag_exp_font_2_h = bag_exp_font_2.get_height()
bag_exp_font_3 = font_27_40_B.render("可於角色介面使用", False, GRAY)
bag_gi_font_1 = font_27_80_B.render("招募契約", False, SAND_BROWN)
bag_gi_font_1_w = bag_gi_font_1.get_width()
bag_gi_font_1_h = bag_gi_font_1.get_height()
bag_gi_font_2 = font_27_50.render("招募角色的必要道具", False, BLACK)
bag_gi_font_2_h = bag_gi_font_2.get_height()
bag_gi_font_3 = font_27_40_B.render("可於村落的招募板使用", False, GRAY)
bag_mgs_font_1 = font_27_80_B.render("神秘的石頭", False, STRONG_RED)
bag_mgs_font_1_w = bag_mgs_font_1.get_width()
bag_mgs_font_1_h = bag_mgs_font_1.get_height()
bag_mgs_font_2 = font_27_50.render("？？？", False, BLACK)
bag_mgs_font_2_h = bag_mgs_font_2.get_height()
bag_mgs_font_3 = font_27_40_B.render("自動使用", False, GRAY)
wp_font_1 = font_27_50_B.render("武器列表", False, BLACK)
wp_font_1_h = wp_font_1.get_height()
wp_font_1_w = wp_font_1.get_width()
wp_font_2 = font_27_40_B.render("點擊圖示以查看詳情（主角等級與武器階級相關）", False, GRAY)
wp_font_2_w = wp_font_2.get_width()
pn_font_1 = font_27_50_B.render("角色列表", False, BLACK)
pn_font_1_h = pn_font_1.get_height()
pn_font_1_w = pn_font_1.get_width()
pn_font_2 = font_27_40_B.render("點擊圖示以查看詳情", False, GRAY)
pn_font_2_w = pn_font_2.get_width()
door_direction_font_l_1 = font_27_40.render("前往左方房間", False, BLACK)
door_direction_font_2_1 = font_27_40.render("前往上方房間", False, BLACK)
door_direction_font_3_1 = font_27_40.render("前往右方房間", False, BLACK)
door_direction_font_4_1 = font_27_40.render("前往下方房間", False, BLACK)
door_direction_font_1_h = door_direction_font_l_1.get_height()
door_direction_font_2 = font_27_30.render("點擊 E 以前進", False, GRAY)
portal_font_1 = font_27_40.render("傳送門", False, DODGER_BLUE)
portal_font_1_h = portal_font_1.get_height()
portal_font_2 = font_27_30.render("點擊 E 以傳送回村莊", False, GRAY)
chest_font_1_1 = font_27_40.render("寶箱", False, AMBER)
chest_font_1_2 = font_27_40.render("開過的寶箱", False, AMBER)
chest_font_1_h = chest_font_1_1.get_height()
chest_font_2 = font_27_30.render("點擊 E 開啟寶箱", False, GRAY)
idol_font_1 = font_27_40_B.render("神像", False, GRAYISH_PURPLE)
idol_font_1_h = portal_font_1.get_height()
idol_font_2_1 = font_27_30.render("點擊 E 以獻上祈禱", False, GRAY)
idol_font_2_2 = font_27_30.render("充滿著神聖的氣息", False, GRAY)
idol_font_3 = font_27_40_B.render("請連續點擊滑鼠左鍵以獻上祈禱", False, BLACK)
idol_font_3_w = idol_font_3.get_width()
monster_font_1_1 = font_27_80.render("怪物迅速的朝你撲過來", False, DARK_RED)
monster_font_1_1_h = monster_font_1_1.get_height()
monster_font_1_1_w = monster_font_1_1.get_width()
monster_font_1_2 = font_27_50_B.render("戰鬥開始", False, GRAY)
monster_font_1_2_w = monster_font_1_2.get_width()
monster_font_2 = font_27_40.render("怪物的屍體", False, GRAY)
NPC_font_1 = font_27_40_B.render("奇怪的人", False, GRAY)
NPC_font_1_h = NPC_font_1.get_height()
NPC_font_2 = font_27_30.render("系統尚未開放", False, GRAY)
knight_font_1 = font_27_40_B.render("身穿鎧甲的物體", False, GRAY)
knight_font_1_h = knight_font_1.get_height()
knight_font_2 = font_27_30.render("系統尚未開放", False, GRAY)
tomb_font_1 = font_27_40_B.render("詭異的墓碑", False, GRAY)
tomb_font_1_h = tomb_font_1.get_height()
tomb_font_2 = font_27_30.render("系統尚未開放", False, GRAY)

# userevent，使用者事件自定義
"""
def moving():
    sprite.manipulate_character.walkt += 1
"""
moving = pygame.USEREVENT+0
pygame.time.set_timer(moving, 150)  # 計時器


# sprite 物件設定

# 開圓形表面（Surface）
def circleSurface(color, radius):
    shape_surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    return shape_surf


# 歡迎文字
class wel_font(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((600, 400), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.midtop = (750, 30)
        self.font1rect = title_font_1.get_rect()
        self.font1rect.midtop = (300, 25)
        self.font2rect = title_font_2.get_rect()
        self.font2rect.midtop = (300, 65+title_font_1_h)
        self.image.blit(title_font_1, self.font1rect)
        self.image.blit(title_font_2, self.font2rect)

# 退出


class quit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((400, 150))
        self.image.fill(HP_GREEN)
        self.rect = self.image.get_rect()
        self.rect.midtop = (750, 600)
        self.font = font_27_80_B.render("退出程式", False, BLACK)
        self.fontrect = self.font.get_rect()
        self.fontrect.center = (200, 75)
        self.image.blit(self.font, self.fontrect)

    def update(self):
        if self.rect.collidepoint(mouse_location) and mouse_one_press(0):
            flag.running = False


# 開始


class play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((400, 150), False)
        self.image.fill(HP_GREEN)
        self.rect = self.image.get_rect()
        self.rect.midtop = (750, 400)
        self.font = font_27_80_B.render("開始遊戲", False, BLACK)
        self.fontrect = self.font.get_rect()
        self.fontrect.center = (200, 75)
        self.image.blit(self.font, self.fontrect)

    def update(self):
        if self.rect.collidepoint(mouse_location) and mouse_one_press(0):
            flag.in_welcome = False
            flag.sprite_need_change = True


# 輸入框


class inpbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.inp = inpbox_img
        self.inpRect = self.inp.get_rect()
        self.inpRect.center = (650, 400)
        self.y = yes_img
        self.yRect = self.y.get_rect()
        self.yRect.topleft = (750, 520)
        self.n = no_img
        self.nRect = self.n.get_rect()
        self.nRect.topright = (550, 520)
        self.text = ""
        self.font = font_m_100.render(self.text, True, BLACK)

    def keyin(self):
        if (self.yRect.collidepoint(mouse_location) and mouse_one_press(0)) or keyboard_one_press(pygame.K_RETURN):
            try:
                tmp = self.text
                self.text = ""
                return int(tmp)
            except:
                self.text = ""
                return (-1)
        elif self.nRect.collidepoint(mouse_location) and mouse_one_press(0):
            self.text = ""
            return 0
        elif keyboard_one_press(pygame.K_BACKSPACE):
            self.text = self.text[:-1]
            return -2
        elif len(self.text) <= 1:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    self.text += event.unicode
            return -2

    def update(self):
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.font = font_m_100.render(self.text, True, BLACK)
        self.image.blit(self.inp, self.inpRect)
        self.image.blit(self.font, (self.inpRect.x+50, self.inpRect.y+100))
        self.image.blit(self.y, self.yRect)
        self.image.blit(self.n, self.nRect)


# 背景透明
class Alpha_back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500, 800), pygame.SRCALPHA)
        self.image.fill(WHITE)
        self.image.set_alpha(159)
        self.rect = self.image.get_rect()
        self.rect = (0, 0)

    def h_update(self):
        if flag.in_welcome:
            self.image = pygame.Surface((1500, 800), pygame.SRCALPHA)
            self.image.fill(WHITE)
            self.image.set_alpha(127)
            self.rect = self.image.get_rect()
            self.rect = (0, 0)
        else:
            self.image = pygame.Surface((1500, 800), pygame.SRCALPHA)
            self.image.fill(WHITE)
            self.image.set_alpha(159)
            self.rect = self.image.get_rect()
            self.rect = (0, 0)


# 村莊地圖
class vil_map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = village_map_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = (750, 800)


# 塔內地圖
class tow_map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower_room_img.copy()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = 800


# 操作的角色
class mani_cha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cha_fr_1_img  # 圖片
        self.rect = self.image.get_rect()
        self.rect.center = (650, 600)
        self.circle = circleSurface(RED, 100)
        self.mask = pygame.mask.from_surface(self.circle)
        self.maskRect = self.mask.get_rect()
        self.dir = 2
        self.walkt = 0
        self.walk = False
        self.c1 = []
        self.stepl = 8
        self.walkdown = False
        self.walkup = False
        self.walkright = False

    def update(self):
        self.background = sprite.village_map
        self.maskRect.center = self.rect.center
        self.c1 = [(self.rect.right < sprite.gachaboard.imgRect.left) or (self.rect.left > sprite.gachaboard.imgRect.right),
                   (self.rect.right < sprite.village_shop.imgRect.left) or (
                       self.rect.left > sprite.village_shop.imgRect.right),
                   (self.rect.top > sprite.gachaboard.imgRect.bottom) or (
                       self.rect.bottom < sprite.gachaboard.imgRect.top),
                   (self.rect.top > sprite.village_shop.imgRect.bottom) or (self.rect.bottom < sprite.village_shop.imgRect.top)]
        if flag.in_fn_list == False:
            self.walk = False
            self.walkup = False
            self.walkright = False
            self.walkdown = False
            if flag.in_tower == False:
                if keyboard_press[pygame.K_s] or keyboard_press[pygame.K_DOWN]:
                    if (abs(self.rect.bottom-sprite.gachaboard.imgRect.top) > self.stepl or self.c1[0]) and (abs(self.rect.bottom-sprite.village_shop.imgRect.top) > self.stepl or self.c1[1]):
                        if self.rect.bottom < 700:
                            self.rect.y += self.stepl
                            self.walk = True
                            self.walkdown = True
                        elif self.background.rect.bottom > 800:
                            self.background.rect.y -= self.stepl
                            self.walk = True
                            self.walkdown = True
                        elif self.rect.bottom < 800:
                            self.rect.y += self.stepl
                            self.walk = True
                            self.walkdown = True
                        else:
                            self.walk = False
                            self.walkdown = False
                    else:
                        self.walk = False
                        self.walkdown = False
                    self.dir = 4
                if keyboard_press[pygame.K_w] or keyboard_press[pygame.K_UP]:
                    if (abs(self.rect.top-sprite.gachaboard.imgRect.bottom) > self.stepl or self.c1[0]) and (abs(self.rect.top-sprite.village_shop.imgRect.bottom) > self.stepl or self.c1[1]):
                        if self.rect.top > 200:
                            self.rect.y -= self.stepl
                            if self.walkdown:
                                self.walk = False
                                self.walkup = False
                                self.walkdown = False
                            else:
                                self.walk = True
                                self.walkup = True
                        elif self.background.rect.top < 0:
                            self.background.rect.y += self.stepl
                            if self.walkdown:
                                self.walk = False
                                self.walkup = False
                                self.walkdown = False
                            else:
                                self.walk = True
                                self.walkup = True
                        elif self.background != sprite.village_map and self.rect.top > 0:
                            self.rect.y -= self.stepl
                            if self.walkdown:
                                self.walk = False
                                self.walkup = False
                                self.walkdown = False
                            else:
                                self.walk = True
                                self.walkup = True
                        else:
                            self.walk = False or self.walk
                    else:
                        self.walk = False or self.walk
                    self.dir = 2
                if keyboard_press[pygame.K_d] or keyboard_press[pygame.K_RIGHT]:
                    if (abs(self.rect.right-sprite.gachaboard.imgRect.left) > self.stepl or self.c1[2]) and (abs(self.rect.right-sprite.village_shop.imgRect.left) > self.stepl or self.c1[3]):
                        if self.rect.right < 1100:
                            self.rect.x += self.stepl
                            self.walk = True
                            self.walkright = True
                        elif self.background.rect.right > 1500:
                            self.background.rect.x -= self.stepl
                            self.walk = True
                            self.walkright = True
                        elif self.rect.right < 1300:
                            self.rect.x += self.stepl
                            self.walk = True
                            self.walkright = True
                        else:
                            self.walk = False or self.walk
                            self.walkright = False
                    else:
                        self.walk = False or self.walk
                        self.walkright = False
                    self.dir = 3
                if keyboard_press[pygame.K_a] or keyboard_press[pygame.K_LEFT]:
                    if (abs(self.rect.left-sprite.gachaboard.imgRect.right) > self.stepl or self.c1[2]) and (abs(self.rect.left-sprite.village_shop.imgRect.right) > self.stepl or self.c1[3]):
                        if self.rect.left > 150:
                            self.rect.x -= self.stepl
                            if self.walkright:
                                self.walk = False or self.walkdown or self.walkup
                                if self.walk:
                                    if self.walkup:
                                        self.dir = 2
                                    else:
                                        self.dir = 4
                            else:
                                self.walk = True
                                self.dir = 1
                        elif self.background.rect.left < 0:
                            self.background.rect.x += self.stepl
                            if self.walkright:
                                self.walk = False or self.walkdown or self.walkup
                                if self.walk:
                                    if self.walkup:
                                        self.dir = 2
                                    else:
                                        self.dir = 4
                            else:
                                self.walk = True
                                self.dir = 1
                        elif self.rect.x > 0:
                            self.rect.x -= self.stepl
                            if self.walkright:
                                self.walk = False or self.walkdown or self.walkup
                                if self.walk:
                                    if self.walkup:
                                        self.dir = 2
                                    else:
                                        self.dir = 4
                            else:
                                self.walk = True
                                self.dir = 1
                        else:
                            self.walk = False or self.walk
                    else:
                        self.walk = False or self.walk
            elif flag.in_tower:
                if keyboard_press[pygame.K_s] or keyboard_press[pygame.K_DOWN]:
                    if self.rect.bottom < 700:
                        self.rect.y += self.stepl
                        self.walk = True
                        self.walkdown = True
                    else:
                        self.walk = False
                        self.walkdown = False
                    self.dir = 4
                if keyboard_press[pygame.K_w] or keyboard_press[pygame.K_UP]:
                    if self.rect.top > 100:
                        self.rect.y -= self.stepl
                        if self.walkdown:
                            self.walk = False
                            self.walkup = False
                            self.walkdown = False
                        else:
                            self.walk = True
                            self.walkup = True
                    else:
                        self.walk = False or self.walk
                    self.dir = 2
                if keyboard_press[pygame.K_d] or keyboard_press[pygame.K_RIGHT]:
                    if self.rect.right < 1140:
                        self.rect.x += self.stepl
                        self.walk = True
                        self.walkright = True
                    else:
                        self.walk = False or self.walk
                        self.walkright = False
                    self.dir = 3
                if keyboard_press[pygame.K_a] or keyboard_press[pygame.K_LEFT]:
                    if self.rect.left > 160:
                        self.rect.x -= self.stepl
                        if self.walkright:
                            self.walk = False or self.walkdown or self.walkup
                            if self.walk:
                                if self.walkup:
                                    self.dir = 2
                                else:
                                    self.dir = 4
                        else:
                            self.walk = True
                            self.dir = 1
                    else:
                        self.walk = False or self.walk
        if self.walk:
            if self.walkt >= 4:
                self.walkt = 0
            if self.dir == 2:
                self.image = cha_fr_img[self.walkt]
            elif self.dir == 4:
                self.image = cha_ba_img[self.walkt]
            elif self.dir == 1:
                self.image = cha_le_img[self.walkt]
            else:
                self.image = cha_ri_img[self.walkt]
        else:
            self.walkt = 0
            if self.dir == 4:
                self.image = cha_ba_1_img
            elif self.dir == 2:
                self.image = cha_fr_1_img
            elif self.dir == 1:
                self.image = cha_le_1_img
            else:
                self.image = cha_ri_1_img


# 功能列
class fn_list(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = function_list_img

    def update(self):
        if flag.in_fn_list:
            if mouse_one_press(0):
                if mouse_location[0] >= 1300 and mouse_location[0] <= 1500 and mouse_location[1] >= 600 and mouse_location[1] <= 800:
                    flag.in_fn_list = False
                    if flag.in_bag:
                        flag.in_bag = False
                        flag.sprite_need_change = True
                    elif flag.in_partner:
                        flag.in_partner = False
                        flag.sprite_need_change = True
                    elif flag.in_weapon:
                        flag.in_weapon = False
                        flag.sprite_need_change = True
            self.image = function_list_back_img.copy()
            self.rect = self.image.get_rect()
            self.rect.x = 1300
            self.rect.y = 600
        else:
            if mouse_one_press(0):
                if mouse_location[0] >= 1300 and mouse_location[0] <= 1500:
                    if mouse_location[1] >= 0 and mouse_location[1] <= 200:
                        flag.in_fn_list = True
                        flag.in_bag = True
                        sprite.bag.h_update()
                        flag.sprite_need_change = True
                    elif mouse_location[1] > 200 and mouse_location[1] <= 400:
                        flag.in_fn_list = True
                        flag.in_partner = True
                        flag.sprite_need_change = True
                    elif mouse_location[1] > 400 and mouse_location[1] <= 600:
                        flag.in_fn_list = True
                        flag.in_weapon = True
                        flag.sprite_need_change = True
            self.image = function_list_img.copy()
            self.rect = self.image.get_rect()
            self.rect.x = 1300
            self.rect.y = 0


# 功能列中的背包介面
class fn_bag(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500, 800))
        self.image.fill(SADDLE_BROWN)
        self.itcode = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.font = pygame.Surface((500, 150), pygame.SRCALPHA)
        self.fontrect = self.font.get_rect()
        self.fontrect.midtop = (750, 0)
        self.font.blit(bag_font_1, (250-(bag_font_1_w//2), 0))
        self.font.blit(
            bag_font_2, (250-(bag_font_2_w//2), bag_font_1_h))
        self.image.blit(self.font, self.fontrect)
        self.numsurface = pygame.Surface((400, 150), pygame.SRCALPHA)
        self.coin_img = b_coin_img
        self.coinrect = self.coin_img.get_rect()
        self.coinrect.topleft = (100, 150)
        self.coin_font = font_m_200.render(str(variable.coin), False, BLACK)
        self.coin_numimg = self.numsurface
        self.coin_numimg.blit(self.coin_font, (0, 0))
        self.coin_numrect = self.coin_numimg.get_rect()
        self.coin_numrect.topleft = (270, 160)
        self.image.blit(self.coin_img, self.coinrect)
        self.image.blit(self.coin_numimg, self.coin_numrect)
        self.us_image = b_upstar_img
        self.usrect = self.us_image.get_rect()
        self.usrect.topleft = (100, 550)
        self.us_font = font_m_200.render(
            str(variable.haveitem["us"]), False, BLACK)
        self.us_numimg = self.numsurface
        self.us_numimg.blit(self.us_font, (0, 0))
        self.us_numrect = self.us_numimg.get_rect()
        self.us_numrect.topleft = (270, 560)
        self.image.blit(self.us_image, self.usrect)
        self.image.blit(self.us_numimg, self.us_numrect)
        self.lp_image = b_life_potion_img
        self.lprect = self.lp_image.get_rect()
        self.lprect.topleft = (100, 350)
        self.lp_font = font_m_200.render(
            str(variable.haveitem["lp"]), False, BLACK)
        self.lp_numimg = self.numsurface
        self.lp_numimg.blit(self.lp_font, (0, 0))
        self.lp_numrect = self.lp_numimg.get_rect()
        self.lp_numrect.topleft = (270, 360)
        self.image.blit(self.lp_image, self.lprect)
        self.image.blit(self.lp_numimg, self.lp_numrect)
        self.exp_image = b_exp_potion_img
        self.exprect = self.exp_image.get_rect()
        self.exprect.topleft = (750, 350)
        self.exp_font = font_m_200.render(
            str(variable.haveitem["exp"]), False, BLACK)
        self.exp_numimg = self.numsurface
        self.exp_numimg.blit(self.exp_font, (0, 0))
        self.exp_numrect = self.exp_numimg.get_rect()
        self.exp_numrect.topleft = (920, 360)
        self.image.blit(self.exp_image, self.exprect)
        self.image.blit(self.exp_numimg, self.exp_numrect)
        self.gi_image = b_gachaitem_img
        self.girect = self.gi_image.get_rect()
        self.girect.topleft = (750, 150)
        self.gi_font = font_m_200.render(
            str(variable.haveitem["gi"]), False, BLACK)
        self.gi_numimg = self.numsurface
        self.gi_numimg.blit(self.gi_font, (0, 0))
        self.gi_numrect = self.gi_numimg.get_rect()
        self.gi_numrect.topleft = (920, 160)
        self.image.blit(self.gi_image, self.girect)
        self.image.blit(self.gi_numimg, self.gi_numrect)
        self.mgs_image = b_magic_stone_img
        self.mgsrect = self.mgs_image.get_rect()
        self.mgsrect.topleft = (750, 550)
        self.mgs_font = font_m_200.render(
            str(variable.haveitem["mgs"]), False, BLACK)
        self.mgs_numimg = self.numsurface
        self.mgs_numimg.blit(self.mgs_font, (0, 0))
        self.mgs_numrect = self.mgs_numimg.get_rect()
        self.mgs_numrect.topleft = (920, 560)
        self.image.blit(self.mgs_image, self.mgsrect)
        self.image.blit(self.mgs_numimg, self.mgs_numrect)

    def update(self):
        if mouse_one_press(0):
            if self.coinrect.collidepoint(mouse_location):
                variable.work += 100
                self.itcode = 1
                flag.in_bag_intro = True
                flag.sprite_need_change = True
                sprite.bag_item_intro.change = False
            elif self.usrect.collidepoint(mouse_location):
                variable.work += 100
                self.itcode = 2
                flag.in_bag_intro = True
                flag.sprite_need_change = True
                sprite.bag_item_intro.change = False
            elif self.lprect.collidepoint(mouse_location):
                variable.work += 100
                self.itcode = 3
                flag.in_bag_intro = True
                flag.sprite_need_change = True
                sprite.bag_item_intro.change = False
            elif self.exprect.collidepoint(mouse_location):
                variable.work += 100
                self.itcode = 4
                flag.in_bag_intro = True
                flag.sprite_need_change = True
                sprite.bag_item_intro.change = False
            elif self.girect.collidepoint(mouse_location):
                variable.work += 100
                self.itcode = 5
                flag.in_bag_intro = True
                flag.sprite_need_change = True
                sprite.bag_item_intro.change = False
            elif self.mgsrect.collidepoint(mouse_location):
                variable.work += 100
                self.itcode = 6
                flag.in_bag_intro = True
                flag.sprite_need_change = True
                sprite.bag_item_intro.change = False

    def h_update(self):
        self.image = pygame.Surface((1500, 800))
        self.image.fill(SADDLE_BROWN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.font = pygame.Surface((500, 150), pygame.SRCALPHA)
        self.fontrect = self.font.get_rect()
        self.fontrect.midtop = (750, 0)
        self.font.blit(bag_font_1, (250-(bag_font_1_w//2), 0))
        self.font.blit(
            bag_font_2, (250-(bag_font_2_w//2), bag_font_1_h))
        self.image.blit(self.font, self.fontrect)
        self.numsurface = pygame.Surface((400, 150), pygame.SRCALPHA)
        self.coin_img = b_coin_img.copy()
        self.coinrect = self.coin_img.get_rect()
        self.coinrect.topleft = (100, 150)
        self.coin_font = font_m_200.render(str(variable.coin), False, BLACK)
        self.coin_numimg = self.numsurface.copy()
        self.coin_numimg.blit(self.coin_font, (0, 0))
        self.coin_numrect = self.coin_numimg.get_rect()
        self.coin_numrect.topleft = (270, 160)
        self.image.blit(self.coin_img, self.coinrect)
        self.image.blit(self.coin_numimg, self.coin_numrect)
        self.us_image = b_upstar_img.copy()
        self.usrect = self.us_image.get_rect()
        self.usrect.topleft = (100, 550)
        self.us_font = font_m_200.render(
            str(variable.haveitem["us"]), False, BLACK)
        self.us_numimg = self.numsurface.copy()
        self.us_numimg.blit(self.us_font, (0, 0))
        self.us_numrect = self.us_numimg.get_rect()
        self.us_numrect.topleft = (270, 560)
        self.image.blit(self.us_image, self.usrect)
        self.image.blit(self.us_numimg, self.us_numrect)
        self.lp_image = b_life_potion_img.copy()
        self.lprect = self.lp_image.get_rect()
        self.lprect.topleft = (100, 350)
        self.lp_font = font_m_200.render(
            str(variable.haveitem["lp"]), False, BLACK)
        self.lp_numimg = self.numsurface.copy()
        self.lp_numimg.blit(self.lp_font, (0, 0))
        self.lp_numrect = self.lp_numimg.get_rect()
        self.lp_numrect.topleft = (270, 360)
        self.image.blit(self.lp_image, self.lprect)
        self.image.blit(self.lp_numimg, self.lp_numrect)
        self.exp_image = b_exp_potion_img.copy()
        self.exprect = self.exp_image.get_rect()
        self.exprect.topleft = (750, 350)
        self.exp_font = font_m_200.render(
            str(variable.haveitem["exp"]), False, BLACK)
        self.exp_numimg = self.numsurface.copy()
        self.exp_numimg.blit(self.exp_font, (0, 0))
        self.exp_numrect = self.exp_numimg.get_rect()
        self.exp_numrect.topleft = (920, 360)
        self.image.blit(self.exp_image, self.exprect)
        self.image.blit(self.exp_numimg, self.exp_numrect)
        self.gi_image = b_gachaitem_img.copy()
        self.girect = self.gi_image.get_rect()
        self.girect.topleft = (750, 150)
        self.gi_font = font_m_200.render(
            str(variable.haveitem["gi"]), False, BLACK)
        self.gi_numimg = self.numsurface.copy()
        self.gi_numimg.blit(self.gi_font, (0, 0))
        self.gi_numrect = self.gi_numimg.get_rect()
        self.gi_numrect.topleft = (920, 160)
        self.image.blit(self.gi_image, self.girect)
        self.image.blit(self.gi_numimg, self.gi_numrect)
        self.mgs_image = b_magic_stone_img.copy()
        self.mgsrect = self.mgs_image.get_rect()
        self.mgsrect.topleft = (750, 550)
        self.mgs_font = font_m_200.render(
            str(variable.haveitem["mgs"]), False, BLACK)
        self.mgs_numimg = self.numsurface.copy()
        self.mgs_numimg.blit(self.mgs_font, (0, 0))
        self.mgs_numrect = self.mgs_numimg.get_rect()
        self.mgs_numrect.topleft = (920, 560)
        self.image.blit(self.mgs_image, self.mgsrect)
        self.image.blit(self.mgs_numimg, self.mgs_numrect)


# 功能列：武器
class fn_wp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1500, 800))
        self.image.fill(POWDER_BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.ring = w_ring_img.copy()
        self.font = pygame.Surface((500, 150), pygame.SRCALPHA)
        self.fontrect = self.font.get_rect()
        self.fontrect.midtop = (750, 0)
        self.font.blit(wp_font_1, (250-(wp_font_1_w//2), 0))
        self.font.blit(
            wp_font_2, (250-(wp_font_2_w//2), wp_font_1_h))
        self.image.blit(self.font, self.fontrect)
        self.wpl = pygame.surface.Surface((1300, 1200), pygame.SRCALPHA)
        self.wprect = np.empty(shape=(5, 3, 2))  # 初始位置
        self.alpha = pygame.surface.Surface((180, 180), pygame.SRCALPHA)
        self.alpha.fill(BLACK)
        self.alpha.set_alpha(159)
        self.act = [0, 0]
        time = 0
        t0 = 0
        for i in copy.copy(weapon_img):
            t1 = 0
            for img in i:
                x = 50 + ((time % 5)*220)
                y = 200*(time//5)
                self.wpl.blit(img, (x, y))
                if time != 0:
                    self.wpl.blit(self.alpha, (x, y))
                tmprect = np.array([x, y])
                self.wprect[t0][t1] = tmprect
                time += 1
                t1 += 1
            while(t1 != 3):
                self.wprect[t0][t1] = np.array([-1, -1])
                t1 += 1
            t0 += 1
        self.wploc = self.wprect.copy()  # 移動後位置
        self.wprect = self.wprect.tolist()
        self.image.blit(self.wpl, (0, 180))

    def update(self):
        # 滑鼠滾動時，對wploc[:,:,1]進行統一更改
        if mouse_one_press(0):
            i = 0
            for locs in self.wploc:
                j = 0
                for loc in locs:
                    if self.collide(loc):
                        flag.sprite_need_change = True
                        flag.in_wp_intro = True
                        self.act = [i, j]
                        self.h_update()
                        sprite.bag_weapon_intro.h_update()
                        return
                    j += 1
                i += 1

    def h_update(self):
        self.image = pygame.surface.Surface((1500, 800))
        self.image.fill(POWDER_BLUE)
        self.image.blit(self.font, self.fontrect)
        self.wpl = pygame.surface.Surface((1300, 1200), pygame.SRCALPHA)
        for i in range(len(self.wprect)):
            for j in range(len(self.wprect[i])):
                if self.wprect[i][j] != [-1, -1]:
                    self.wpl.blit(
                        copy.copy(weapon_img[i][j]), self.wprect[i][j])
                    if not variable.weapon_list[i][j].has:
                        self.wpl.blit(self.alpha, self.wprect[i][j])
                    self.wploc = self.wprect
                    if variable.equip_wp[0] == i and variable.equip_wp[1] == j:
                        self.wpl.blit(self.ring, self.wprect[i][j])
        self.image.blit(self.wpl, (0, 180))

    def collide(self, arr):
        ml = mouse_location
        if ml[0] > arr[0] and ml[0] < arr[0]+180 and ml[1] > arr[1]+200 and ml[1] < arr[1]+380:
            return True
        return False

# 功能列：角色一覽


class fn_pn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1500, 800))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.image.fill(POWDER_BLUE)
        self.font = pygame.Surface((500, 150), pygame.SRCALPHA)
        self.fontrect = self.font.get_rect()
        self.fontrect.midtop = (750, 0)
        self.font.blit(pn_font_1, (250-(pn_font_1_w//2), 0))
        self.font.blit(
            pn_font_2, (250-(pn_font_2_w//2), pn_font_1_h))
        self.image.blit(self.font, self.fontrect)
        self.act = 0
        self.perform = variable.character_list[self.act]
        self.pnl = pygame.surface.Surface((400, 1200), pygame.SRCALPHA)
        self.pnrect = np.empty(
            shape=(len(variable.character_list), 2))  # 初始位置
        self.alpha = pygame.surface.Surface((150, 150), pygame.SRCALPHA)
        self.alpha.fill(BLACK)
        self.alpha.set_alpha(159)
        for i in range(len(variable.character_list)):
            tmpimage = partner_s_img[i].copy()
            if variable.character_list[i].level == 0:
                tmpimage.blit(self.alpha, (0, 0))
            x = 50+(i % 2)*200
            y = (i//2)*170
            self.pnl.blit(tmpimage, (x, y))
            self.pnrect[i] = np.array([x, y])
        self.pnloc = self.pnrect.copy()
        self.pnrect = self.pnrect.tolist()
        self.image.blit(self.pnl, (0, 150))
        self.pndetail = pygame.surface.Surface((1100, 650), pygame.SRCALPHA)
        self.pndetailrect = self.pndetail.get_rect()
        self.pndetailrect.topleft = (400, 150)
        self.pnd_name = font_27_50_B.render(self.perform.name, False, BLACK)
        self.pnd_namerect = self.pnd_name.get_rect()
        self.pnd_work = font_27_30_B.render(
            '定位： '+self.perform.workstr, False, GRAY)
        self.pnd_workrect = self.pnd_work.get_rect()
        self.pnd_equipbot = p_equip_img.copy()
        self.pnd_equiprect = self.pnd_equipbot.get_rect()
        self.pnd_img = partner_l_img[self.act].copy()
        self.pnd_rect = self.pnd_img.get_rect()
        self.pnd_detal_LV = font_27_30_B.render(
            'LV：'+str(self.perform.level), False, BLACK)
        self.pnd_detal_LVrect = self.pnd_detal_LV.get_rect()
        self.pnd_detal_EXP = font_27_30_B.render(
            'EXP：'+str(self.perform.exp)+' / '+str(self.perform.level*2), False, BLACK)
        self.pnd_detal_EXPrect = self.pnd_detal_EXP.get_rect()
        self.pnd_detal_HP = font_27_30_B.render(
            'HP：'+str(self.perform.nHP)+' / '+str(self.perform.HP[self.perform.level]), False, BLACK)
        self.pnd_detal_HPrect = self.pnd_detal_HP.get_rect()
        self.pnd_detal_ATK = font_27_30_B.render(
            'ATK：'+str(self.perform.nATK), False, BLACK)
        self.pnd_detal_ATKrect = self.pnd_detal_ATK.get_rect()
        self.pnd_detal_DEF = font_27_30_B.render(
            'DEF：'+str(self.perform.nDEF), False, BLACK)
        self.pnd_detal_DEFrect = self.pnd_detal_DEF.get_rect()
        self.pnd_HPrec = p_HP_img.copy()
        self.pnd_HPrecrect = self.pnd_HPrec.get_rect()
        self.pnd_HPrec_mask = pygame.mask.from_surface(self.pnd_HPrec)
        self.pnd_HPrec_maskrect = self.pnd_HPrec_mask.get_rect()
        self.pnd_HPrec_maskrect.topleft = (1360, 170)
        self.pnd_EXP = p_EXP_img.copy()
        self.pnd_EXPrect = self.pnd_EXP.get_rect()
        self.pnd_EXP_mask = pygame.mask.from_surface(self.pnd_EXP)
        self.pnd_EXP_maskrect = self.pnd_EXP_mask.get_rect()
        self.pnd_EXP_maskrect.topleft = (1360, 270)
        self.pnd_star = p_star_img.copy()
        self.pnd_starrect = self.pnd_star.get_rect()
        self.pnd_star_mask = pygame.mask.from_surface(self.pnd_star)
        self.pnd_star_maskrect = self.pnd_star_mask.get_rect()
        self.pnd_star_maskrect.topleft = (1360, 370)
        self.image.blit(self.pndetail, self.pndetailrect)

    def update(self):
        if mouse_one_press(0):
            for i in range(len(self.pnrect)):
                if self.collide(self.pnrect[i]):
                    self.act = i
                    self.h_update()
                    break
            else:
                if self.perform.level != 0 and not flag.in_battle:
                    if self.pnd_HPrec_maskrect.collidepoint(mouse_location):
                        flag.partner_font = True
                        flag.sprite_need_change = True
                        sprite.partner_font.situation = 0
                    elif self.pnd_EXP_maskrect.collidepoint(mouse_location):
                        flag.partner_font = True
                        flag.sprite_need_change = True
                        sprite.partner_font.situation = 1
                    elif self.pnd_star_maskrect.collidepoint(mouse_location):
                        flag.partner_font = True
                        flag.sprite_need_change = True
                        sprite.partner_font.situation = 2
                if self.pnd_equiprect.collidepoint(mouse_location):
                    flag.partner_up = True
                    flag.sprite_need_change = True
                    sprite.partner_up.h_update()

    def h_update(self):
        self.image = pygame.surface.Surface((1500, 800))
        self.image.fill(POWDER_BLUE)
        self.image.blit(self.font, self.fontrect)
        self.pnl = pygame.surface.Surface((400, 1200), pygame.SRCALPHA)
        for i in range(len(self.pnrect)):
            tmpimage = partner_s_img[i].copy()
            if variable.character_list[i].level == 0:
                tmpimage.blit(self.alpha, (0, 0))
            self.pnl.blit(tmpimage, self.pnrect[i])
        self.image.blit(self.pnl, (0, 150))
        self.perform = variable.character_list[self.act]
        self.pndetail = pygame.surface.Surface((1100, 650), pygame.SRCALPHA)
        self.pndetailrect = self.pndetail.get_rect()
        self.pndetailrect.topleft = (400, 150)
        self.pnd_name = font_27_50_B.render(self.perform.name, False, BLACK)
        self.pnd_namerect = self.pnd_name.get_rect()
        self.pnd_namerect.topleft = (40, 40)
        self.pndetail.blit(self.pnd_name, self.pnd_namerect)
        self.pnd_work = font_27_30_B.render(
            '定位： '+self.perform.workstr, False, GRAY)
        self.pnd_workrect = self.pnd_work.get_rect()
        self.pnd_workrect.topleft = (45, self.pnd_namerect.bottom+5)
        self.pndetail.blit(self.pnd_work, self.pnd_workrect)
        self.pnd_equipbot = p_equip_img.copy()
        self.pnd_equiprect = self.pnd_equipbot.get_rect()
        if self.perform.level != 0 and not flag.in_battle and self.act != 0:
            self.pnd_equiprect.topleft = (45, self.pnd_workrect.bottom+10)
        else:
            self.pnd_equiprect.topleft = (45, 801)
        self.pndetail.blit(self.pnd_equipbot, self.pnd_equiprect)
        self.pnd_equiprect.topleft = (self.pnd_equiprect.x+400,
                                      self.pnd_equiprect.y+150)
        self.pnd_img = partner_l_img[self.act].copy()
        self.pnd_rect = self.pnd_img.get_rect()
        self.pnd_rect.midtop = (450, 100)
        self.pndetail.blit(self.pnd_img, self.pnd_rect)
        self.pnd_detal_LV = font_27_30_B.render(
            'LV：'+str(self.perform.level), False, BLACK)
        self.pnd_detal_LVrect = self.pnd_detal_LV.get_rect()
        self.pnd_detal_LVrect.topleft = (650, 40)
        self.pndetail.blit(self.pnd_detal_LV, self.pnd_detal_LVrect)
        self.pnd_detal_EXP = font_27_30_B.render(
            'EXP：'+str(self.perform.exp)+' / '+str(self.perform.level*2), False, BLACK)
        self.pnd_detal_EXPrect = self.pnd_detal_EXP.get_rect()
        self.pnd_detal_EXPrect.topleft = (650, self.pnd_detal_LVrect.bottom+5)
        self.pndetail.blit(self.pnd_detal_EXP, self.pnd_detal_EXPrect)
        self.pnd_detal_HP = font_27_30_B.render(
            'HP：'+str(self.perform.nHP)+' / '+str(self.perform.HP[self.perform.level]), False, BLACK)
        self.pnd_detal_HPrect = self.pnd_detal_HP.get_rect()
        self.pnd_detal_HPrect.topleft = (650, self.pnd_detal_EXPrect.bottom+5)
        self.pndetail.blit(self.pnd_detal_HP, self.pnd_detal_HPrect)
        self.pnd_detal_ATK = font_27_30_B.render(
            'ATK：'+str(self.perform.nATK), False, BLACK)
        self.pnd_detal_ATKrect = self.pnd_detal_ATK.get_rect()
        self.pnd_detal_ATKrect.topleft = (650, self.pnd_detal_HPrect.bottom+5)
        self.pndetail.blit(self.pnd_detal_ATK, self.pnd_detal_ATKrect)
        self.pnd_detal_DEF = font_27_30_B.render(
            'DEF：'+str(self.perform.nDEF), False, BLACK)
        self.pnd_detal_DEFrect = self.pnd_detal_DEF.get_rect()
        self.pnd_detal_DEFrect.topleft = (650, self.pnd_detal_ATKrect.bottom+5)
        self.pndetail.blit(self.pnd_detal_DEF, self.pnd_detal_DEFrect)
        norATKfont = '普通攻擊：'
        if self.act != 0 and self.perform.ATKtype != 4:
            norATKfont += '造成'
        if self.act != 0:
            norATKfont += ATKtype_font[self.perform.ATKtype]
        elif self.act == 0:
            norATKfont += ATKtype_font[0]
        self.pnd_detal_norATK = font_27_30_B.render(
            norATKfont, False, BLACK)
        self.pnd_detal_norATKrect = self.pnd_detal_norATK.get_rect()
        self.pnd_detal_norATKrect.midtop = (450, 350)
        self.pndetail.blit(self.pnd_detal_norATK, self.pnd_detal_norATKrect)
        if not self.perform.skillup:
            skATKfont = self.skfont()
        else:
            skATKfont = self.uskfont()
        self.pnd_detal_skATK = font_27_30_B.render(
            skATKfont, False, BLACK)
        self.pnd_detal_skATKrect = self.pnd_detal_skATK.get_rect()
        self.pnd_detal_skATKrect.midtop = (
            450, self.pnd_detal_norATKrect.bottom+5)
        self.pndetail.blit(self.pnd_detal_skATK, self.pnd_detal_skATKrect)
        ultATKfont = self.ultfont()
        self.pnd_detal_ultATK = font_27_30_B.render(
            ultATKfont, False, BLACK)
        self.pnd_detal_ultATKrect = self.pnd_detal_ultATK.get_rect()
        self.pnd_detal_ultATKrect.midtop = (
            450, self.pnd_detal_skATKrect.bottom+5)
        self.pndetail.blit(self.pnd_detal_ultATK, self.pnd_detal_ultATKrect)
        self.pnd_HPrec = p_HP_img.copy()
        self.pnd_HPrecrect = self.pnd_HPrec.get_rect()
        self.pnd_HPrecrect.topleft = (960, 20)
        self.pnd_EXP = p_EXP_img.copy()
        self.pnd_EXPrect = self.pnd_EXP.get_rect()
        self.pnd_EXPrect.topleft = (960, 120)
        self.pnd_star = p_star_img.copy()
        self.pnd_starrect = self.pnd_star.get_rect()
        self.pnd_starrect.topleft = (960, 220)
        if self.perform.level != 0 and not flag.in_battle:
            self.pndetail.blit(self.pnd_HPrec, self.pnd_HPrecrect)
            self.pndetail.blit(self.pnd_EXP, self.pnd_EXPrect)
            self.pndetail.blit(self.pnd_star, self.pnd_starrect)
        self.image.blit(self.pndetail, self.pndetailrect)

    def skfont(self):
        if self.act == 0:
            return '戰技：異於常人： 提升攻擊、防禦'
        elif self.act == 1:
            return '戰技：班級統帥： 下次攻擊轉變為群體'
        elif self.act == 2:
            return '戰技：班級後盾： 獲得【守護】效果'
        elif self.act == 3:
            return '戰技：質詢： 提高所有敵人所受傷害'
        elif self.act == 4:
            return '戰技：班費資助： 隨機使一名防禦<=7的隊友，防禦力增加'

    def uskfont(self):
        if self.act == 0:
            return '戰技：異於常人‧改： 大幅提升攻擊、防禦'
        elif self.act == 1:
            return '戰技：班級統帥‧改： 提升自身攻擊，且下次攻擊轉變為群體'
        elif self.act == 2:
            return '戰技：班級後盾‧改： 提升自身防禦，並獲得【守護】效果'
        elif self.act == 3:
            return '戰技：質詢‧改： 大幅提高所有敵人所受傷害'
        elif self.act == 4:
            return '戰技：班費資助‧改： 隨機使一名防禦<=15的隊友，防禦力大幅增加'

    def ultfont(self):
        if self.act == 0:
            return '奧義：力逐上游： 永久提升攻擊、防禦'
        elif self.act == 1:
            return '奧義：領導者風範： 降低目標防禦，並造成真實傷害'
        elif self.act == 2:
            return '奧義：缺曠無效： 抵銷並反擊下三次敵方傷害'
        elif self.act == 3:
            return '奧義：言語攻擊： 對目標造成魔法傷害，並給予【燃燒】效果'
        elif self.act == 4:
            return '奧義：冷氣！！！： 回復全隊血量，並給予【恢復】效果'

    def collide(self, arr):
        ml = mouse_location
        if ml[0] > arr[0] and ml[0] < arr[0]+150 and ml[1] > arr[1]+150 and ml[1] < arr[1]+350:
            return True
        return False

# 夥伴升級


class p_font(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.yrect = yes_img.get_rect()
        self.yrect.topleft = (875, 550)
        self.nrect = no_img.get_rect()
        self.nrect.topleft = (475, 550)
        self.image.blit(yes_img.copy(), self.yrect)
        self.image.blit(no_img.copy(), self.nrect)
        self.situation = 0
        self.font_img = [p_recover_font_img, p_EXP_font_img, p_star_font_img]
        self.font2_img = [p_recover_font2_img,
                          p_EXP_font2_img, p_star_font2_img]
        self.item = ['lp', 'exp', 'us']

    def update(self):
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.image.blit(self.font_img[self.situation].copy(), (450, 150))
        self.image.blit(yes_img.copy(), self.yrect)
        self.image.blit(no_img.copy(), self.nrect)
        if self.yrect.collidepoint(mouse_location) and mouse_one_press(0):
            if variable.haveitem[self.item[self.situation]] > 0:
                variable.haveitem[self.item[self.situation]] -= 1
                if self.situation == 0:
                    sprite.partner_bag.perform.nHP += ((
                        sprite.partner_bag.perform.HP[sprite.partner_bag.perform.level])//5)
                elif self.situation == 1:
                    sprite.partner_bag.perform.exp += 1
                    if sprite.partner_bag.perform.exp == sprite.partner_bag.perform.level*2:
                        sprite.partner_bag.perform.LVup()
                elif self.situation == 2:
                    sprite.partner_bag.perform.skillup = True
                flag.partner_font = False
                flag.sprite_need_change = True
            else:
                self.image = pygame.surface.Surface(
                    (1500, 800), pygame.SRCALPHA)
                self.image.blit(
                    self.font2_img[self.situation].copy(), (450, 150))
                variable.work = 700
        elif self.nrect.collidepoint(mouse_location) and mouse_one_press(0):
            flag.partner_font = False
            flag.sprite_need_change = True

# 夥伴上陣


class p_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = p_goup_img.copy()
        self.imgrect = self.img.get_rect()
        self.imgrect.center = (750, 400)
        self.plus = p_plus_img.copy()
        self.back = cancel_img.copy()
        self.backrect = self.back.get_rect()
        self.backrect.bottomleft = (1150, 210)
        self.img.blit(self.back, self.backrect)
        self.image.blit(self.img, self.imgrect)
        self.loc = [(0, 0), (320, 90), (550, 90)]

    def update(self):
        if mouse_one_press(0):
            if mouse_location[1] <= 540 and mouse_location[1] >= 250:
                if mouse_location[0] >= 650 and mouse_location[0] <= 870:
                    try:
                        if variable.usecha[2] == sprite.partner_bag.act:
                            variable.usecha[1], variable.usecha[2] = variable.usecha[2], variable.usecha[1]
                        else:
                            variable.usecha[1] = sprite.partner_bag.act
                    except:
                        try:
                            variable.usecha[1] = sprite.partner_bag.act
                        except:
                            variable.usecha.append(sprite.partner_bag.act)
                    self.h_update()
                elif mouse_location[0] >= 890 and mouse_location[0] <= 1110:
                    try:
                        if variable.usecha[1] == sprite.partner_bag.act:
                            variable.usecha[1], variable.usecha[2] = variable.usecha[2], variable.usecha[1]
                        else:
                            variable.usecha[2] = sprite.partner_bag.act
                    except:
                        try:
                            if variable.usecha[1] == sprite.partner_bag.act:
                                pass
                            else:
                                variable.usecha.append(sprite.partner_bag.act)
                        except:
                            variable.usecha.append(sprite.partner_bag.act)
                    self.h_update()
            elif self.backrect.collidepoint(mouse_location):
                flag.sprite_need_change = True
                flag.partner_up = False

    def h_update(self):
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.img = p_goup_img.copy()
        self.image.blit(self.back, self.backrect)
        for i in range(1, 3):
            if len(variable.usecha) > i:
                self.img.blit(
                    partner_l_img[variable.usecha[i]],  (self.loc[i][0], self.loc[i][1]))
            else:
                self.img.blit(
                    self.plus, (self.loc[i][0]+40, self.loc[i][1]+50))
        self.image.blit(self.img, self.imgrect)


# 新手禮物箱


class nobgift(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1300, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.gift = gift_img.copy()
        self.giftrect = self.gift.get_rect()
        self.giftrect.center = (1000, 650)
        self.mask = pygame.mask.from_surface(self.gift)
        self.maskRect = self.mask.get_rect()
        self.font = pygame.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        self.font.blit(gift_font_1, (self.fontRect.x, self.fontRect.y))
        self.font.blit(gift_font_2, (self.fontRect.x,
                       self.fontRect.y+gift_font_1_h))

    def update(self):
        self.giftrect.center = (1000, sprite.village_map.rect.bottom-150)
        self.mask = pygame.mask.from_surface(self.gift)
        self.maskRect = self.mask.get_rect()
        self.maskRect.center = self.giftrect.center
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.image.blit(self.gift, self.giftrect)
        if sprite.manipulate_character.mask.overlap(self.mask, ((self.maskRect.x-sprite.manipulate_character.maskRect.x), (self.maskRect.y-sprite.manipulate_character.maskRect.y))):
            self.image.blit(self.font, self.fontRect)
            if keyboard_one_press(pygame.K_e):
                flag.sprite_need_change = True
                flag.in_nobgift = True
                sprite_group.village_sprite.remove(self)
        elif variable.floor == 2 and sprite_group.village_sprite.has(self):
            sprite_group.village_sprite.remove(self)


class gift_gain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = chestgain_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.image.blit(c_gachaitem_img, (250, 150))
        self.image.blit(c_life_potion_img, (550, 150))
        self.lpfont = font_m_60.render('10', False, BLACK)
        self.image.blit(self.lpfont, (730, 310))

    def update(self):
        if mouse_one_press(0) or keyboard_one_press("any"):
            flag.sprite_need_change = True
            flag.in_nobgift = False
            background_sprite.empty()
            variable.haveitem["gi"] += 1
            variable.haveitem["lp"] += 10

# 背包中的道具介紹介面


class b_item_intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = b_introblock_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 400)
        self.change = True

    def update(self):
        if mouse_one_press(0) or keyboard_one_press("any"):
            flag.in_bag_intro = False
            flag.sprite_need_change = True

    def h_update(self):
        self.image = b_introblock_img.copy()
        if sprite.bag.itcode == 1:
            self.image.blit(b_coin_img, (20, 20))
            self.image.blit(bag_coin_font_1,
                            (500-(bag_coin_font_1_w//2), 40))
            self.image.blit(bag_coin_font_2,
                            (20, 200))
        elif sprite.bag.itcode == 2:
            self.image.blit(b_upstar_img, (20, 20))
            self.image.blit(bag_us_font_1,
                            (500-(bag_us_font_1_w//2), 40))
            self.image.blit(bag_us_font_2,
                            (20, 200))
            self.image.blit(bag_us_font_3,
                            (20, 200+bag_us_font_2_h+10))
            self.image.blit(
                bag_us_font_4, (20, 200+bag_us_font_2_h+bag_us_font_3_h+20))
        elif sprite.bag.itcode == 3:
            self.image.blit(b_life_potion_img, (20, 20))
            self.image.blit(bag_lp_font_1,
                            (500-(bag_lp_font_1_w//2), 40))
            self.image.blit(bag_lp_font_2,
                            (20, 200))
            self.image.blit(bag_lp_font_3,
                            (20, 200+bag_lp_font_2_h+10))
        elif sprite.bag.itcode == 4:
            self.image.blit(b_exp_potion_img, (20, 20))
            self.image.blit(bag_exp_font_1,
                            (500-(bag_exp_font_1_w//2), 40))
            self.image.blit(bag_exp_font_2,
                            (20, 200))
            self.image.blit(bag_exp_font_3,
                            (20, 200+bag_exp_font_2_h+10))
        elif sprite.bag.itcode == 5:
            self.image.blit(b_gachaitem_img, (20, 20))
            self.image.blit(bag_gi_font_1,
                            (500-(bag_gi_font_1_w//2), 40))
            self.image.blit(bag_gi_font_2,
                            (20, 200))
            self.image.blit(bag_gi_font_3,
                            (20, 200+bag_gi_font_2_h+10))
        elif sprite.bag.itcode == 6:
            self.image.blit(b_magic_stone_img, (20, 20))
            self.image.blit(bag_mgs_font_1,
                            (500-(bag_mgs_font_1_w//2), 40))
            self.image.blit(bag_mgs_font_2,
                            (20, 200))
            self.image.blit(bag_mgs_font_3,
                            (20, 200+bag_mgs_font_2_h+10))
        self.change = True

# 武器介紹


class b_weapon_intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = b_introblock_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 400)
        self.change = True
        self.unknow = font_27_40_B.render('？？？', False, BLACK)
        self.alpha = pygame.surface.Surface((180, 180), pygame.SRCALPHA)
        self.alpha.fill(BLACK)
        self.alpha.set_alpha(159)
        self.equip = w_equip_img.copy()
        self.equiprect = self.equip.get_rect()
        self.equiprect.topleft = (700, 200)
        self.canequip = False

    def update(self):
        if mouse_one_press(0) or keyboard_one_press("any"):
            flag.in_wp_intro = False
            flag.sprite_need_change = True
            if self.canequip and self.equiprect.collidepoint(mouse_location):
                variable.equip_wp = sprite.weapon_bag.act
                variable.character_list[0].equip()

    def h_update(self):
        r, c = sprite.weapon_bag.act
        self.image = b_introblock_img.copy()
        self.image.blit(copy.copy(weapon_img[r][c]), (20, 20))
        self.namefont = font_27_60_B.render(weaponname[r][c], False, BLACK)
        self.namerect = self.namefont.get_rect()
        self.namerect.midtop = (500, 30)
        self.image.blit(self.namefont, self.namerect)
        self.equiprect.topleft = (700, 200)
        if not variable.weapon_list[r][c].has:
            self.image.blit(self.unknow, (20, 250))
            self.image.blit(self.alpha, (20, 20))
            self.canequip = False
        else:
            self.ATKfont = font_27_40_B.render(
                variable.weapon_list[r][c].ATKstr, False, BLACK)
            self.ATKrect = self.ATKfont.get_rect()
            self.ATKrect.topleft = (20, 230)
            self.image.blit(self.ATKfont, self.ATKrect)
            self.DEFfont = font_27_40_B.render(
                variable.weapon_list[r][c].DEFstr, False, BLACK)
            self.DEFrect = self.DEFfont.get_rect()
            self.DEFrect.topleft = (20, self.ATKrect.bottom+10)
            self.image.blit(self.DEFfont, self.DEFrect)
            self.typefont = font_27_40_B.render(
                '類型： '+weapontype[variable.weapon_list[r][c].type], False, BLACK)
            self.typerect = self.typefont.get_rect()
            self.typerect.topleft = (20, self.DEFrect.bottom+10)
            self.image.blit(self.typefont, self.typerect)
            self.norfont = font_27_30_B.render(
                variable.weapon_list[r][c].str, False, GRAY)
            self.norrect = self.norfont.get_rect()
            self.norrect.topleft = (20, self.typerect.bottom+10)
            self.image.blit(self.norfont, self.norrect)
            self.image.blit(self.equip, self.equiprect)
            self.canequip = True
        self.equiprect.topleft = (950, 300)


# 塔內的門（不同方向）
# 1:left 2:up 3:right 4:down


class tow_door_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.dirty = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = door1_img.copy()
        self.imgRect = self.img.get_rect()
        self.imgRect.center = (140, 400)
        self.image.blit(self.img, self.imgRect)
        self.mask = pygame.mask.from_surface(self.img)
        self.font = pygame.surface.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        pygame.Surface.blit(self.font, door_direction_font_l_1,
                            (self.fontRect.x, self.fontRect.y))
        pygame.Surface.blit(self.font, door_direction_font_2,
                            (self.fontRect.x, self.fontRect.y+door_direction_font_1_h))

    def update(self):
        if self.mask.overlap(sprite.manipulate_character.mask, (sprite.manipulate_character.maskRect.x-self.imgRect.x, sprite.manipulate_character.maskRect.y-self.imgRect.y)):
            self.image.blit(self.font, self.fontRect)
            self.dirty = True
            if keyboard_one_press(pygame.K_e):
                flag.room_change = True
                variable.direction = 1
        elif self.dirty:
            self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
            self.image.blit(self.img, self.imgRect)
            self.dirty = False


class tow_door_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.dirty = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = door2_img.copy()
        self.imgRect = self.img.get_rect()
        self.imgRect.center = (650, 80)
        self.image.blit(self.img, self.imgRect)
        self.mask = pygame.mask.from_surface(self.img)
        self.font = pygame.surface.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        pygame.Surface.blit(self.font, door_direction_font_2_1,
                            (self.fontRect.x, self.fontRect.y))
        pygame.Surface.blit(self.font, door_direction_font_2,
                            (self.fontRect.x, self.fontRect.y+door_direction_font_1_h))

    def update(self):
        if self.mask.overlap(sprite.manipulate_character.mask, ((sprite.manipulate_character.maskRect.x-self.imgRect.x), (sprite.manipulate_character.maskRect.y-self.imgRect.y))):
            self.image.blit(self.font, self.fontRect)
            self.dirty = True
            if keyboard_one_press(pygame.K_e):
                flag.room_change = True
                variable.direction = 2
        elif self.dirty:
            self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
            self.image.blit(self.img, self.imgRect)
            self.dirty = False


class tow_door_3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.dirty = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = door3_img.copy()
        self.imgRect = self.img.get_rect()
        self.imgRect.center = (1160, 400)
        self.image.blit(self.img, self.imgRect)
        self.mask = pygame.mask.from_surface(self.img)
        self.font = pygame.surface.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        pygame.Surface.blit(self.font, door_direction_font_3_1,
                            (self.fontRect.x, self.fontRect.y))
        pygame.Surface.blit(self.font, door_direction_font_2,
                            (self.fontRect.x, self.fontRect.y+door_direction_font_1_h))

    def update(self):
        if self.mask.overlap(sprite.manipulate_character.mask, ((sprite.manipulate_character.maskRect.x-self.imgRect.x), (sprite.manipulate_character.maskRect.y-self.imgRect.y))):
            self.image.blit(self.font, self.fontRect)
            self.dirty = True
            if keyboard_one_press(pygame.K_e):
                flag.room_change = True
                variable.direction = 3
        elif self.dirty:
            self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
            self.image.blit(self.img, self.imgRect)
            self.dirty = False


class tow_door_4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.dirty = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = door4_img.copy()
        self.imgRect = self.img.get_rect()
        self.imgRect.center = (650, 720)
        self.image.blit(self.img, self.imgRect)
        self.mask = pygame.mask.from_surface(self.img)
        self.font = pygame.surface.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        pygame.Surface.blit(self.font, door_direction_font_4_1,
                            (self.fontRect.x, self.fontRect.y))
        pygame.Surface.blit(self.font, door_direction_font_2,
                            (self.fontRect.x, self.fontRect.y+door_direction_font_1_h))

    def update(self):
        if self.mask.overlap(sprite.manipulate_character.mask, ((sprite.manipulate_character.maskRect.x-self.imgRect.x), (sprite.manipulate_character.maskRect.y-self.imgRect.y))):
            self.image.blit(self.font, self.fontRect)
            self.dirty = True
            if keyboard_one_press(pygame.K_e):
                flag.room_change = True
                variable.direction = 4
        elif self.dirty:
            self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
            self.image.blit(self.img, self.imgRect)
            self.dirty = False


# 塔的輪廓
class tow_out(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower_outline_img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not flag.in_tower:
            self.rect.center = (sprite.village_map.rect.centerx -
                                100, sprite.village_map.rect.top+105)


# 招募板
class ga_board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = gachaboard_img.copy()
        self.imgRect = self.img.get_rect()
        self.imgRect.center = (1000, 200)
        self.image.blit(self.img, self.imgRect)
        self.mask = pygame.mask.from_surface(self.image)
        self.maskRect = self.mask.get_rect()
        self.font = pygame.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        self.font.blit(gacha_font_1, (self.fontRect.x, self.fontRect.y))
        self.font.blit(gacha_font_2, (self.fontRect.x,
                       self.fontRect.y+gacha_font_1_h))

    def update(self):
        self.imgRect.center = (1000, sprite.village_map.rect.bottom-600)
        self.mask = pygame.mask.from_surface(self.img)
        self.maskRect = self.mask.get_rect()
        self.maskRect.center = self.imgRect.center
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.image.blit(self.img, self.imgRect)
        if sprite.manipulate_character.mask.overlap(self.mask, ((self.maskRect.x-sprite.manipulate_character.maskRect.x), (self.maskRect.y-sprite.manipulate_character.maskRect.y))):
            self.image.blit(self.font, self.fontRect)
            if keyboard_one_press(pygame.K_e):
                flag.sprite_need_change = True
                flag.in_gacha = True

# 招募介面

# 背景與退出


class gacha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gachaUI_img.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.cancel = cancel_img.copy()
        self.cancelrect = self.cancel.get_rect()
        self.cancelrect.topright = (1250, 30)
        self.image.blit(self.cancel, self.cancelrect)

    def update(self):
        self.image = gachaUI_img.copy()
        self.image.blit(self.cancel, self.cancelrect)
        if self.cancelrect.collidepoint(mouse_location) and mouse_one_press(0):
            flag.in_gacha = False
            flag.sprite_need_change = True

# 招募卷


class gahca_ticket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = g_gachaitem_img.copy()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (650, 780)
        self.in_control = False
        self.alpha = pygame.surface.Surface((150, 150), pygame.SRCALPHA)
        self.alpha.fill(BLACK)
        self.alpha.set_alpha(159)

    def update(self):
        if not self.in_control:
            self.image = g_gachaitem_img.copy()
            self.rect = self.image.get_rect()
            self.rect.midbottom = (650, 780)
        if variable.haveitem['gi'] == 0:
            self.image.blit(self.alpha, (0, 0))
        elif (mouse_one_press(2) or keyboard_one_press(pygame.K_c)) and self.in_control:
            self.in_control = False
        elif mouse_press[0] and self.in_control:
            self.rect.center = mouse_location
        elif not mouse_press[0] and self.in_control:
            self.in_control = False
            sprite.gachaUI.image.blit(b_gachaitem_img.copy(), self.rect)
            variable.haveitem['gi'] -= 1
            flag.in_gotcha = True
            flag.sprite_need_change = True
        elif mouse_one_press(0):
            self.in_control = True
            self.image = c_gachaitem_img.copy()
            self.rect = self.image.get_rect()


# 抽到的角色顯示


class gacha_got(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1300, 800), pygame.SRCALPHA)
        self.image.fill(BLACK)
        self.image.set_alpha(191)
        c = random.randint(1, len(variable.character_list)-1)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.cha = partner_l_img[c]
        self.charect = self.cha.get_rect()
        self.charect.midtop = (650, 250)
        self.image.blit(self.cha, self.charect)
        self.font = font_27_60_B.render(
            variable.character_list[c].name+' 加入隊伍', False, WHITE)
        self.fontrect = self.font.get_rect()
        self.fontrect.midtop = (650, 100)
        self.image.blit(self.font, self.fontrect)
        self.font2 = font_27_50_B.render('點擊左鍵或任意按鍵以確定', False, GRAY)
        self.font2rect = self.font2.get_rect()
        self.font2rect.midtop = (650, 600)
        self.image.blit(self.font2, self.font2rect)
        self.font3 = font_27_50_B.render('重複角色轉化為經驗', False, WHITE)
        self.font3rect = self.font3.get_rect()
        self.font3rect.midtop = (650, 500)
        if variable.character_list[c].level != 0:
            self.image.blit(self.font3, self.font3rect)
            variable.character_list[c].exp += 1
        else:
            variable.character_list[c].LVup()
            variable.character_list[c].SKCD = variable.character_list[c].oriSKCD

    def update(self):
        if mouse_one_press(0) or keyboard_one_press('any'):
            flag.sprite_need_change = True
            flag.in_gotcha = False


# 文字提示


class gacha_font(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1000, 80))
        self.image.fill(NAVAJO_WHITE)
        self.rect = self.image.get_rect()
        self.rect.midtop = (650, 0)

    def update(self):
        self.image = pygame.surface.Surface((1000, 80))
        self.image.fill(NAVAJO_WHITE)
        if variable.haveitem['gi'] == 0:
            self.image.blit(gacha_hasno_font, (100, 0))
        elif sprite.gachaticket.in_control:
            self.image.blit(gacha_cancel_font, (100, 0))
        else:
            self.image.blit(gacha_go_font, (100, 0))

# 村莊內的商店（輪廓）


class vil_shop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.img = shop_img
        self.imgRect = self.img.get_rect()
        self.imgRect.center = (300, 200)
        self.image.blit(self.img, self.imgRect)
        self.mask = pygame.mask.from_surface(self.image)
        self.maskRect = self.mask.get_rect()
        self.font = pygame.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.fontRect = self.font.get_rect()
        self.fontRect.midtop = (650, 0)
        self.font.blit(village_shop_font_1, (self.fontRect.x, self.fontRect.y))
        self.font.blit(village_shop_font_2, (self.fontRect.x,
                       self.fontRect.y+village_shop_font_1_h))

    def update(self):
        self.imgRect.center = (300, sprite.village_map.rect.bottom-600)
        self.mask = pygame.mask.from_surface(self.img)
        self.maskRect = self.mask.get_rect()
        self.maskRect.center = self.imgRect.center
        self.image = pygame.Surface((1300, 800), pygame.SRCALPHA)
        self.image.blit(self.img, self.imgRect)
        if abs(sprite.manipulate_character.maskRect.top-self.imgRect.bottom) <= 50:
            if sprite.manipulate_character.mask.overlap(self.mask, ((self.maskRect.x-sprite.manipulate_character.maskRect.x), (self.maskRect.y-sprite.manipulate_character.maskRect.y))):
                self.image.blit(self.font, self.fontRect)
                if keyboard_one_press(pygame.K_e):
                    flag.in_shop = True
                    flag.sprite_need_change = True


# 商店介面
class shop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shop_back_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.menu = shopmenu_img
        self.menuRect = self.image.get_rect()
        self.menuRect.topleft = (150, 200)
        self.image.blit(self.menu, self.menuRect)
        self.cancel = cancel_img
        self.cancelRect = self.cancel.get_rect()
        self.cancelRect.bottomright = (1150, 200)
        self.image.blit(self.cancel, self.cancelRect)
        self.giimg = gachaitem_img
        self.giRect = self.giimg.get_rect()
        self.giRect.topleft = (150, 200)
        self.gic = font_m_60.render("100", True, BLACK)
        self.giimg.blit(self.gic, (70, 310))
        self.image.blit(self.giimg, self.giRect)
        self.lpimg = life_potion_img
        self.lpRect = self.lpimg.get_rect()
        self.lpRect.topleft = (400, 200)
        self.lpc = font_m_60.render("50", True, BLACK)
        self.lpimg.blit(self.lpc, (70, 310))
        self.image.blit(self.lpimg, self.lpRect)
        self.epimg = exp_potion_img
        self.epRect = self.epimg.get_rect()
        self.epRect.topleft = (650, 200)
        self.epc = font_m_60.render("120", True, BLACK)
        self.epimg.blit(self.epc, (70, 310))
        self.image.blit(self.epimg, self.epRect)
        self.usimg = upstar_img
        self.usRect = self.usimg.get_rect()
        self.usRect.topleft = (900, 200)
        self.usc = font_m_60.render("500", True, BLACK)
        self.usimg.blit(self.usc, (70, 310))
        self.image.blit(self.usimg, self.usRect)
        self.items = il
        self.bt = -1

    def update(self):
        self.image = shop_back_img.copy()
        self.image.blit(self.menu, self.menuRect)
        self.image.blit(self.cancel, self.cancelRect)
        self.image.blit(self.giimg, self.giRect)
        self.image.blit(self.lpimg, self.lpRect)
        self.image.blit(self.epimg, self.epRect)
        self.image.blit(self.usimg, self.usRect)
        if self.cancelRect.collidepoint(mouse_location) and mouse_one_press(0):
            flag.in_shop = False
            flag.sprite_need_change = True
        if flag.in_key_in == False:
            if self.giRect.collidepoint(mouse_location) and mouse_one_press(0):
                flag.in_key_in = True
                self.bt = 0
            elif self.lpRect.collidepoint(mouse_location) and mouse_one_press(0):
                flag.in_key_in = True
                self.bt = 1
            elif self.epRect.collidepoint(mouse_location) and mouse_one_press(0):
                flag.in_key_in = True
                self.bt = 2
            elif self.usRect.collidepoint(mouse_location) and mouse_one_press(0):
                flag.in_key_in = True
                self.bt = 3
            if flag.in_key_in:
                all_sprite.add(sprite.inputbox)
                all_sprite.remove(self)
                background_sprite.add(self)


# 進塔時的文字顯示（可合併？）
class enter_tow_font(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 100))
        self.image.fill(NAVAJO_WHITE)
        self.rect = self.image.get_rect()
        self.rect.midtop = (650, 0)
        pygame.Surface.blit(self.image, enter_tower_font_1,
                            (self.rect.left, self.rect.top))
        pygame.Surface.blit(self.image, enter_tower_font_2,
                            (self.rect.left, self.rect.top+enter_tower_font_1_h))

    def update(self):
        if self.detect() and not flag.in_tower:
            self.rect.top = 0
        else:
            self.rect.bottom = 0

    def detect(self):
        if sprite.manipulate_character.rect.left >= 400 and sprite.manipulate_character.rect.right <= 900 and sprite.manipulate_character.mask.overlap(sprite.tower_outline.mask,
                                                                                                                                                       ((sprite.tower_outline.rect.x-sprite.manipulate_character.maskRect.x), (sprite.tower_outline.rect.y-sprite.manipulate_character.maskRect.y-50))):
            return True
        else:
            return False


# 塔內房間中央的物件
class tow_room_img(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 300), pygame.SRCALPHA)
        self.imageS = portal_img.copy()
        self.imageSR = self.imageS.get_rect()
        self.imageB = chest_img.copy()
        self.imageBR = self.imageB.get_rect()
        self.imageB2 = openedchest_img.copy()
        self.imageB2R = self.imageB.get_rect()
        self.imageM = Slime_l_img.copy()
        self.imageMR = self.imageM.get_rect()
        self.imageM2 = deadslime_img.copy()
        self.imageM2R = self.imageM2.get_rect()
        self.imageE = NPC_img.copy()
        self.imageER = self.imageE.get_rect()
        self.imageG = statue_img.copy()
        self.imageGR = self.imageG.get_rect()
        self.imageG2 = statue_2_img.copy()
        self.imageG2R = self.imageG2.get_rect()
        self.imageD = tomb_img.copy()
        self.imageDR = self.imageD.get_rect()
        self.imageP = knight_img.copy()
        self.imagePR = self.imageP.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.mask = pygame.mask.from_surface(self.image)
        self.maskRect = self.mask.get_rect()

    def h_update(self):
        if variable.room[variable.nowroom[1]][variable.nowroom[0]] == "S":
            self.image = self.imageS.copy()
            self.rect = self.imageSR
            self.rect.center = (650, 400)
        elif variable.room[variable.nowroom[1]][variable.nowroom[0]] == "B":
            if flag.roomgone[variable.nowroom[1]][variable.nowroom[0]]:
                self.image = self.imageB2.copy()
                self.rect = self.imageB2R
                self.rect.center = (650, 400)
            else:
                self.image = self.imageB.copy()
                self.rect = self.imageBR
                self.rect.center = (650, 400)
        elif variable.room[variable.nowroom[1]][variable.nowroom[0]] == "M":
            if flag.roomgone[variable.nowroom[1]][variable.nowroom[0]]:
                self.image = self.imageM2.copy()
                self.rect = self.imageM2R
                self.rect.center = (650, 400)
            else:
                self.image = self.imageM.copy()
                self.rect = self.imageMR
                self.rect.center = (650, 400)
        elif variable.room[variable.nowroom[1]][variable.nowroom[0]] == "E":
            self.image = self.imageE.copy()
            self.rect = self.imageER
            self.rect.center = (650, 400)
        elif variable.room[variable.nowroom[1]][variable.nowroom[0]] == "G":
            if not flag.roomgone[variable.nowroom[1]][variable.nowroom[0]]:
                self.image = self.imageG.copy()
                self.rect = self.imageGR
                self.rect.center = (650, 400)
            else:
                self.image = self.imageG2.copy()
                self.rect = self.imageG2R
                self.rect.center = (650, 400)
        elif variable.room[variable.nowroom[1]][variable.nowroom[0]] == "D":
            self.image = self.imageD.copy()
            self.rect = self.imageDR
            self.rect.center = (650, 400)
        elif variable.room[variable.nowroom[1]][variable.nowroom[0]] == "P":
            self.image = self.imageP.copy()
            self.rect = self.imagePR
            self.rect.center = (650, 400)

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.maskRect = self.mask.get_rect()
        self.maskRect.center = (650, 400)


# 塔內房間的部分物件互動、上方文字顯示
class tow_room_font_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 100), pygame.SRCALPHA)
        self.image.fill(NAVAJO_WHITE)
        self.rect = self.image.get_rect()
        self.rect.midtop = (650, 0)

    def update(self):
        try:
            nrt = variable.room[variable.nowroom[1]][variable.nowroom[0]]
        except:
            nrt = None
        if sprite.manipulate_character.mask.overlap(sprite.tower_room_image.mask, ((sprite.tower_room_image.maskRect.x-sprite.manipulate_character.maskRect.x), (sprite.tower_room_image.maskRect.y-sprite.manipulate_character.maskRect.y))):
            self.image = pygame.Surface((800, 100), pygame.SRCALPHA)
            self.image.fill(NAVAJO_WHITE)
            self.rect.midtop = (650, 0)
            if nrt == "S":
                self.image.blit(portal_font_1, (self.rect.x, self.rect.y))
                self.image.blit(portal_font_2, (self.rect.x,
                                self.rect.y+portal_font_1_h))
                if keyboard_one_press(pygame.K_e):
                    flag.out_tower = True
            elif nrt == "B":
                if flag.roomgone[variable.nowroom[1]][variable.nowroom[0]]:
                    self.image.blit(chest_font_1_2, (self.rect.x, self.rect.y))
                else:
                    self.image.blit(chest_font_1_1, (self.rect.x, self.rect.y))
                    self.image.blit(chest_font_2, (self.rect.x,
                                    self.rect.y+chest_font_1_h))
                    if keyboard_one_press(pygame.K_e):
                        flag.in_chest_gain = True
                        flag.sprite_need_change = True
                        sprite.chest.change = False
            elif nrt == 'G':
                self.image.blit(idol_font_1, (self.rect.x, self.rect.y))
                if flag.roomgone[variable.nowroom[1]][variable.nowroom[0]]:
                    self.image.blit(idol_font_2_2, (self.rect.x,
                                    self.rect.y+chest_font_1_h))
                else:
                    self.image.blit(idol_font_2_1, (self.rect.x,
                                    self.rect.y+chest_font_1_h))
                    if keyboard_one_press(pygame.K_e):
                        flag.in_pray = True
                        flag.sprite_need_change = True
                        sprite.idol.newgoal = True
            elif nrt == 'M':
                if flag.roomgone[variable.nowroom[1]][variable.nowroom[0]]:
                    self.image.blit(monster_font_2, (self.rect.x, self.rect.y))
                else:
                    self.rect.midbottom = (650, 0)
            elif nrt == 'E':
                self.image.blit(NPC_font_1, (self.rect.x, self.rect.y))
                self.image.blit(
                    NPC_font_2, (self.rect.x, self.rect.y+NPC_font_1_h))
            elif nrt == 'D':
                self.image.blit(tomb_font_1, (self.rect.x, self.rect.y))
                self.image.blit(tomb_font_2, (self.rect.x,
                                self.rect.y+tomb_font_1_h))
            elif nrt == 'P':
                self.image.blit(knight_font_1, (self.rect.x, self.rect.y))
                self.image.blit(knight_font_2, (self.rect.x,
                                self.rect.y+knight_font_1_h))
            else:
                self.rect.midbottom = (650, 0)

        else:
            self.rect.midbottom = (650, 0)


# 塔內房間的部分物件互動、中央文字顯示
class tow_room_font_mid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tow_midblock_img.copy()
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.display = False

    def update(self):
        try:
            nrt = variable.room[variable.nowroom[1]][variable.nowroom[0]]
        except:
            nrt = None
        if nrt == "M":
            if not flag.roomgone[variable.nowroom[1]][variable.nowroom[0]] and sprite.manipulate_character.walk:
                flag.sprite_need_change = True
                self.rect.center = (650, 400)
                self.image.blit(monster_font_1_1,
                                (500-(monster_font_1_1_w//2), 100))
                self.image.blit(
                    monster_font_1_2, (500-(monster_font_1_2_w//2), 200+monster_font_1_1_h))
                self.display = True
                variable.work = 200
                flag.roomgone[variable.nowroom[1]][variable.nowroom[0]] = True
                sprite.tower_room_image.h_update()
                flag.in_battle = True
                flag.battle_initial = True
                flag.sprite_need_change = True
                flag.new_round = True
            else:
                self.rect.bottom = 0
        else:
            self.rect.bottom = 0


# 塔內寶箱
class tow_chest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = chestgain_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.coin = c_coin_img.copy()
        self.change = True
        self.money_font = pygame.surface.Surface((80, 60), pygame.SRCALPHA)

    def openchest(self):
        item = random.randint(1, 1000) % 100
        r = 0
        m = random.randint(0, 40)
        if m >= 30:
            m -= random.randint(0, 10)
        elif m <= 10:
            m += random.randint(0, 10)
        m += (random.randint(0, (variable.floor-1)*5))
        self.money = self.money_font.copy()
        self.money.blit(font_m_100.render(str(m), False, BLACK), (0, 0))
        if item < 50:
            # 正常武器:1
            r = 1
        elif item < 55:
            # 高階武器:2
            r = 2
        elif item < 75:
            # 補血藥:6
            r = 6
        elif item < 86:
            # 經驗藥:7
            r = 7
        elif item < 94:
            # 招募卷:3
            r = 3
        elif item < 98:
            if Mainc.level >= 3:
                # 星星:4
                r = 4
            else:
                r = 1
        else:
            # 魔法石:5
            r = 5
        flag.roomgone[variable.nowroom[1]][variable.nowroom[0]] = True
        sprite.tower_room_image.h_update()
        return [r, m]

    def h_update(self):
        global background_sprite
        item, money = self.openchest()
        self.image = chestgain_img.copy()
        if item == 1:
            r = Mainc.level
            g = random.randint(0, len(variable.weapon_list[r])-1)
            self.image.blit(weapon_img[r][g], (250, 150))
            if variable.weapon_list[r][g].has:
                money += (10+(r-1)*5)
            else:
                variable.weapon_list[r][g].has = True
        elif item == 2:
            r = Mainc.level+1
            if Mainc.level >= 5:  # 5等以上資料庫尚未建立
                r = 4
            g = random.randint(0, len(variable.weapon_list[r])-1)
            self.image.blit(weapon_img[r][g], (250, 150))
            if variable.weapon_list[r][g].has:
                money += (10+(r-1)*5)
            else:
                variable.weapon_list[r][g].has = True
        elif item == 3:
            self.image.blit(c_gachaitem_img, (250, 150))
            variable.haveitem["gi"] += 1
        elif item == 4:
            self.image.blit(c_upstar_img, (250, 150))
            variable.haveitem["us"] += 1
        elif item == 5:
            self.image.blit(c_magic_stone_img, (250, 150))
            variable.haveitem["mgs"] += 1
        elif item == 6:
            self.image.blit(c_life_potion_img, (250, 150))
            variable.haveitem["lp"] += 1
        elif item == 7:
            self.image.blit(c_exp_potion_img, (250, 150))
            variable.haveitem["exp"] += 1
        self.change = True
        variable.coin += money
        self.coin = c_coin_img.copy()
        self.coin.blit(self.money, (120, 140))
        self.image.blit(self.coin, (550, 150))
        background_sprite = all_sprite.copy()

    def update(self):
        if mouse_one_press(0) or keyboard_one_press("any"):
            flag.in_chest_gain = False
            flag.sprite_need_change = True


# 塔內神像
class god_idol(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect = (0, 0)
        self.img = bigstatue_img
        self.imgrect = self.img.get_rect()
        self.imgrect.center = (650, 400)
        self.image.blit(self.img, self.imgrect)
        self.no = no_img
        self.norect = self.no.get_rect()
        self.norect.topleft = (850, 100)
        self.font = pygame.surface.Surface((800, 100))
        self.font.fill(NAVAJO_WHITE)
        self.font.blit(idol_font_3, (400-(idol_font_3_w//2), 10))
        self.image.blit(self.font, (250, 650))
        self.image.blit(self.no, self.norect)
        self.press = 0
        self.goal = 0
        self.light = 0
        self.lighting = False
        self.newgoal = False

    def update(self):
        if self.light > 0:
            self.light -= clock.get_rawtime()
        elif self.light < 0:
            self.light = 0
        if not self.lighting and self.light != 0:
            self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
            self.img = bigstatue_2_img
            self.imgrect = self.img.get_rect()
            self.imgrect.center = (650, 400)
            self.image.blit(self.img, self.imgrect)
            self.image.blit(self.font, (250, 650))
            self.image.blit(self.no, self.norect)
            self.lighting = True
        elif self.lighting and self.light == 0:
            self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
            self.img = bigstatue_img
            self.imgrect = self.img.get_rect()
            self.imgrect.center = (650, 400)
            self.image.blit(self.img, self.imgrect)
            self.image.blit(self.font, (250, 650))
            self.image.blit(self.no, self.norect)
            self.lighting = False
        if self.newgoal:
            self.goal = random.randint(variable.fr, variable.fr*3)
            self.press = 0
            self.newgoal = False
        if mouse_one_press(0) and self.norect.collidepoint(mouse_location):
            flag.in_pray = False
            flag.sprite_need_change = True
        elif mouse_one_press(0) and mouse_location[0] < 1300:
            self.press += 1
            self.light += 150
        if self.press == self.goal:
            flag.in_pray = False
            flag.sprite_need_change = True
            flag.roomgone[variable.nowroom[1]][variable.nowroom[0]] = True
            sprite.tower_room_image.h_update()
            for i in variable.usecha:
                tmp = variable.character_list[i]
                tmp.nHP += (tmp.HP[tmp.level]//5)
                tmp.nHP = min(tmp.nHP, tmp.HP[tmp.level])
            self.light = 0


# 以下皆為戰鬥介面的一堆東西
# 戰鬥場景
# 設定角色位置
chaloc = [(375, 450), (575, 450), (775, 450)]
eneloc = [(375, 50), (575, 50), (775, 50)]


# 戰鬥我方角色


class bat_cha(pygame.sprite.Sprite):
    def __init__(self, teamnum):
        pygame.sprite.Sprite.__init__(self)
        self.teamnum = teamnum
        self.image = pygame.surface.Surface((150, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = chaloc[teamnum]

    def update(self):
        self.image = partner_s_img[variable.usecha[self.teamnum]]
        if self.rect.collidepoint(mouse_location) and mouse_one_press(0):
            if not flag.attack_choose:
                sprite.act_information.act = self.teamnum
                # battle_large_image.h_update(照片)
            elif variable.character_list[variable.usecha[self.teamnum]].nHP == 0 and (variable.equip_wp != [4, 2] or sprite.act_information.act != 0):
                sprite.battle_font.situation = 2
                sprite.battle_font.display = True
                flag.attack_choose = False
                variable.work = 800
                sprite.battle_font.h_update()
                variable.myATKtype[sprite.act_information.act] = -1
            else:
                if len(variable.myATKobject[sprite.act_information.act]) == 0:
                    variable.myATKobject[sprite.act_information.act].append(
                        self.teamnum)
                else:
                    variable.myATKobject[sprite.act_information.act][0] = self.teamnum
                flag.attack_choose = False
                flag.sprite_need_change = True


# 戰鬥角色血條

class HPbar(pygame.sprite.Sprite):
    def __init__(self, num):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        self.image = s_HPbar_img.copy()
        self.rect = self.image.get_rect()

    def update(self):
        self.image = s_HPbar_img.copy()
        if self.num <= 2:
            self.rect.topleft = (
                chaloc[self.num][0]-1, chaloc[self.num][1]+159)
            size = (
                variable.character_list[variable.usecha[self.num]].HPpercentage(150), 11)
            self.green = pygame.surface.Surface(size)
            self.green.fill(HP_GREEN)
            self.image.blit(self.green, (1, 1))
        elif self.num <= 5:
            self.rect.topleft = (
                eneloc[self.num-3][0]-1, eneloc[self.num-3][1]+159)
            size = (variable.enemy[self.num-3].HPpercentage(150), 11)
            self.green = pygame.surface.Surface(size)
            self.green.fill(HP_GREEN)
            self.image.blit(self.green, (1, 1))


# 戰鬥敵方角色


class bat_ene(pygame.sprite.Sprite):
    def __init__(self, teamnum):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((150, 150))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.teamnum = teamnum
        self.rect.topleft = eneloc[self.teamnum]
        self.type_img = None

    def update(self):
        try:
            self.image = self.type_img[1].copy()
        except:
            pass
        if self.rect.collidepoint(mouse_location) and mouse_one_press(0):
            if not flag.attack_choose:
                sprite.act_information.act = self.teamnum+3
            elif variable.enemy[self.teamnum].nHP == 0:
                sprite.battle_font.situation = 2
                sprite.battle_font.display = True
                variable.work = 800
                flag.attack_choose = False
                sprite.battle_font.h_update()
                variable.myATKtype[sprite.act_information.act] = -1
            elif sprite.act_information.perform.ATKtype == 4:
                sprite.battle_font.situation = 5
                sprite.battle_font.display = True
                variable.work = 800
                flag.attack_choose = False
                sprite.battle_font.h_update()
                variable.myATKtype[sprite.act_information.act] = -1
            else:
                if len(variable.myATKobject[sprite.act_information.act]) == 0:
                    variable.myATKobject[sprite.act_information.act].append(
                        self.teamnum+3)
                else:
                    variable.myATKobject[sprite.act_information.act][0] = self.teamnum+3
                flag.attack_choose = False
                flag.sprite_need_change = True


# 選取角色放大圖


class bat_big_img(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((200, 200), pygame.SRCALPHA)
        self.image.fill(AMBER)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 600)

    def update(self):
        if sprite.act_information.act == -1:
            self.rect.top = 800
        elif sprite.act_information.act <= 2:
            self.image = partner_l_img[variable.usecha[sprite.act_information.act]].copy(
            )
            self.rect = self.image.get_rect()
            self.rect.topleft = (0, 600)
        else:
            self.image = sprite.battle_enemy_list[sprite.act_information.act -
                                                  3].type_img[0].copy()
            self.rect = self.image.get_rect()
            self.rect.topleft = (0, 600)


# 戰鬥行動與資訊欄

# 爆擊判定


def critical(character):
    rand = random.randint(1, 100)
    if character.nCR >= rand:
        return True
    return False


class a_inf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1300, 200))  # image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 0)
        self.act = 0
        self.HPimg_bottom = HPbar_img.copy()
        self.HPimg_bottom_rect = self.HPimg_bottom.get_rect()
        self.HPimg_bottom_rect.topleft = (427, 12)  # 邊框3像素
        self.HPimg_top = pygame.surface.Surface((400, 30))
        self.norbot = normalATK_botton_img.copy()
        self.norbotrect = self.norbot.get_rect()
        self.norbotrect.topleft = (400, 60)
        self.norbotmask = pygame.mask.from_surface(self.norbot)
        self.norbotmrect = self.norbotmask.get_rect()
        self.skibot = skillATK_botton_img.copy()
        self.skibotrect = self.skibot.get_rect()
        self.skibotrect.topleft = (560, 60)
        self.skibotmask = pygame.mask.from_surface(self.skibot)
        self.skibotmrect = self.skibotmask.get_rect()
        self.ultbot = ultraATK_botton_img.copy()
        self.ultbotrect = self.ultbot.get_rect()
        self.ultbotrect.topleft = (720, 60)
        self.ultbotmask = pygame.mask.from_surface(self.ultbot)
        self.ultbotmrect = self.ultbotmask.get_rect()
        self.healbot = healATK_botton_img.copy()
        self.healbotrect = self.healbot.get_rect()
        self.healbotrect.topleft = (880, 60)
        self.healbotmask = pygame.mask.from_surface(self.healbot)
        self.healbotmrect = self.healbotmask.get_rect()
        self.exebot = execute_botton_img.copy()
        self.exebotrect = self.exebot.get_rect()
        self.exebotrect.topleft = (1050, 5)
        self.exebotmask = pygame.mask.from_surface(self.exebot)
        self.exebotmrect = self.exebotmask.get_rect()
        self.detbot = detail_botton_img.copy()
        self.detbotrect = self.detbot.get_rect()
        self.detbotrect.topleft = (230, 60)
        self.detbotmask = pygame.mask.from_surface(self.detbot)
        self.detbotmrect = self.detbotmask.get_rect()
        self.ring = botton_ring_img.copy()
        self.ringrect = self.ring.get_rect()
        self.ringrect.top = 205
        self.CDalpha = circleSurface(BLACK, 55)
        self.CDalpha.set_alpha(159)
        self.CDalpharect = self.CDalpha.get_rect()
        self.havecalculate = False
        self.moreene = -1
        self.wpSK = 0
        self.o_is_monster = True

    def update(self):
        self.death_check()
        if self.act <= 2 and self.act >= 0:
            if keyboard_one_press(pygame.K_LEFT):
                self.act -= 1
                if self.act < 0:
                    self.act = len(variable.usecha)-1
            elif keyboard_one_press(pygame.K_RIGHT):
                self.act += 1
                if self.act > len(variable.usecha)-1:
                    self.act = 0
        self.w = variable.weapon_list[variable.equip_wp[0]
                                      ][variable.equip_wp[1]]
        self.str3 = ''
        if self.act == -1:
            self.rect.top = 801
        elif not flag.in_dmg_phrase:
            self.image = pygame.surface.Surface((1300, 200))
            self.image.fill(GRAY)
            self.rect.bottomleft = (0, 800)
            self.HPimg_bottom = HPbar_img.copy()
            self.detbotmrect.center = (
                self.detbotrect.centerx+self.rect.x, self.detbotrect.centery+self.rect.y)
            self.image.blit(self.detbot, self.detbotrect)
            if self.act <= 2 and variable.character_list[variable.usecha[self.act]].nHP != 0:
                self.image.blit(self.norbot, self.norbotrect)
                self.image.blit(self.skibot, self.skibotrect)
                self.image.blit(self.ultbot, self.ultbotrect)
                self.norbotmrect.center = (
                    self.norbotrect.centerx+self.rect.x, self.norbotrect.centery+self.rect.y)
                self.skibotmrect.center = (
                    self.skibotrect.centerx+self.rect.x, self.skibotrect.centery+self.rect.y)
                self.ultbotmrect.center = (
                    self.ultbotrect.centerx+self.rect.x, self.ultbotrect.centery+self.rect.y)
                self.image.blit(self.healbot, self.healbotrect)
                self.healbotmrect.center = (
                    self.healbotrect.centerx+self.rect.x, self.healbotrect.centery+self.rect.y)
                self.image.blit(self.exebot, self.exebotrect)
                self.exebotmrect.center = (
                    self.exebotrect.centerx+self.rect.x, self.exebotrect.centery+self.rect.y)
                self.perform = variable.character_list[variable.usecha[self.act]]
                size = (110, int(110*(self.perform.SKCD/self.perform.oriSKCD)))
                self.SKCDing = pygame.surface.Surface(size, pygame.SRCALPHA)
                self.SKCDingrect = self.SKCDing.get_rect()
                self.SKCDingrect.bottomleft = self.skibotrect.bottomleft
                self.CDalpharect.bottomright = size
                self.SKCDing.blit(self.CDalpha, self.CDalpharect)
                self.image.blit(self.SKCDing, self.SKCDingrect)
                size = (110, int(110*(self.perform.ULTCD/self.perform.oriULTCD)))
                self.ULTCDing = pygame.surface.Surface(size, pygame.SRCALPHA)
                self.ULTCDingrect = self.ULTCDing.get_rect()
                self.ULTCDingrect.bottomleft = self.ultbotrect.bottomleft
                self.CDalpharect.bottomright = size
                self.ULTCDing.blit(self.CDalpha, self.CDalpharect)
                self.image.blit(self.ULTCDing, self.ULTCDingrect)
                self.namefont = font_27_40_B.render(
                    self.perform.name, False, WHITE)
                if self.namefont.get_width() >= 240:
                    self.namefont = font_27_30_B.render(
                        self.perform.name, False, WHITE)
                self.image.blit(self.namefont, (230, 0))
                if (self.norbotmrect.collidepoint(mouse_location) and mouse_one_press(0)) or keyboard_one_press(pygame.K_a):
                    variable.myATKtype[self.act] = 0
                    if self.perform.nHP == 0:
                        sprite.battle_font.situation = 2
                        sprite.battle_font.display = True
                        variable.work = 800
                        sprite.battle_font.h_update()
                    else:
                        if self.w.code != (4, 1):
                            flag.attack_choose = True
                        if self.perform.name == '班長' and self.perform.skilling != 0:
                            flag.attack_choose = False
                elif (self.skibotmrect.collidepoint(mouse_location) and mouse_one_press(0)) or keyboard_one_press(pygame.K_q):
                    if self.perform.nHP == 0:
                        sprite.battle_font.situation = 2
                        sprite.battle_font.display = True
                        variable.work = 800
                        sprite.battle_font.h_update()
                    else:
                        if self.perform.SKCD == 0:
                            variable.myATKtype[self.act] = 1
                        else:
                            variable.work = 700
                            sprite.battle_font.display = True
                            sprite.battle_font.situation = 1
                            sprite.battle_font.h_update()
                elif (self.ultbotmrect.collidepoint(mouse_location) and mouse_one_press(0)) or keyboard_one_press(pygame.K_z):
                    if self.perform.nHP == 0:
                        sprite.battle_font.situation = 2
                        sprite.battle_font.display = True
                        variable.work = 800
                        sprite.battle_font.h_update()
                    else:
                        if self.perform.ULTCD == 0:
                            variable.myATKtype[self.act] = 2
                            flag.attack_choose = True
                            ultnc = [0, 2, 4]
                            for i in ultnc:
                                if variable.usecha[self.act] == i:
                                    flag.attack_choose = False
                                    break
                        else:
                            variable.work = 700
                            sprite.battle_font.display = True
                            sprite.battle_font.situation = 1
                            sprite.battle_font.h_update()
                elif (self.healbotmrect.collidepoint(mouse_location) and mouse_one_press(0)) or keyboard_one_press(pygame.K_h):
                    flag.heal_cha = True
                    flag.sprite_need_change = True
                elif (self.exebotmrect.collidepoint(mouse_location) and mouse_one_press(0)) or keyboard_one_press(pygame.K_RETURN):
                    for i in range(len(variable.usecha)):
                        if variable.myATKtype[i] == -1 and variable.character_list[variable.usecha[i]].dizz == 0 and variable.character_list[variable.usecha[i]].nHP != 0:
                            sprite.battle_font.display = True
                            sprite.battle_font.situation = 6
                            sprite.battle_font.h_update()
                            variable.work = 700
                            break
                    else:
                        flag.in_dmg_phrase = True
                        self.act = variable.act_order[0]
                if variable.myATKtype[self.act] == 0:
                    self.ringrect.center = self.norbotrect.center
                elif variable.myATKtype[self.act] == 1:
                    self.ringrect.center = self.skibotrect.center
                elif variable.myATKtype[self.act] == 2:
                    self.ringrect.center = self.ultbotrect.center
                else:
                    self.ringrect.top = 205
                self.image.blit(self.ring, self.ringrect)
            elif self.act <= 2:
                self.perform = variable.character_list[variable.usecha[self.act]]
                self.namefont = font_27_40_B.render(
                    self.perform.name, False, WHITE)
                if self.namefont.get_width() >= 240:
                    self.namefont = font_27_30_B.render(
                        self.perform.name, False, WHITE)
                self.image.blit(self.namefont, (230, 0))
            elif self.act <= 5:
                self.perform = variable.enemy[self.act-3]
                self.namefont = font_27_40_B.render(
                    self.perform.type, False, WHITE)
                if self.namefont.get_width() >= 240:
                    self.namefont = font_27_30_B.render(
                        self.perform.type, False, WHITE)
                self.image.blit(self.namefont, (230, 0))
            self.HPimg_top = pygame.surface.Surface(
                (self.perform.HPpercentage(400), 30))
            self.HPimg_top.fill(HP_GREEN)
            self.HPimg_bottom.blit(self.HPimg_top, (3, 3))
            self.image.blit(self.HPimg_bottom, self.HPimg_bottom_rect)
            self.HPfont = font_m_55.render(
                str(self.perform.nHP)+'/'+str(self.perform.HP[self.perform.level]), False, WHITE)
            self.image.blit(self.HPfont, (850, 14))
        else:
            if not self.havecalculate and not self.death_check():
                if self.act <= 2:  # 我方
                    self.perform = variable.character_list[variable.usecha[self.act]]
                    if self.perform.nHP != 0 and self.perform.dizz == 0:  # 還活著、沒暈眩
                        # 數據處理
                        if self.moreene == -1:
                            self.obj = variable.myATKobject[self.act]
                        if variable.myATKtype[self.act] == 0:  # 普攻
                            if self.wpSK == 10 and self.w.code == (3, 1) and self.act == 0:
                                self.perform.ATKtype = 3
                            self.str1 = self.perform.norfont
                            tmpATK = self.perform.nATK+self.perform.ATKlimit
                            if self.act == 0 and self.perform.skilling > 0:
                                if self.perform.skillup:
                                    tmpATK = int(tmpATK*1.5)
                                else:
                                    tmpATK = int(tmpATK*1.3)
                            if self.perform.ATKtype == 1:  # 物理
                                if (self.act == 0 and self.w.code == (2, 2) and self.moreene == -1):
                                    if random.randint(1, 100) <= 50:
                                        self.obj = []
                                        for i in range(len(variable.enemy)):
                                            if variable.enemy[i].nHP != 0:
                                                self.obj.append(i+3)
                                elif (variable.usecha[self.act] == 1 and self.perform.skilling == 1 and self.moreene == -1):
                                    variable.character_list[1].skilling = 0
                                    if self.perform.skillup:
                                        self.perform.ATKlimit += int(
                                            self.perform.ATK[self.perform.level]*1.5)
                                    if random.randint(1, 50) <= 100:
                                        self.obj = []
                                        for i in range(len(variable.enemy)):
                                            if variable.enemy[i].nHP != 0:
                                                self.obj.append(i+3)
                                elif self.act == 0 and self.w.code == (3, 0):
                                    self.obj = []
                                    tmpobj = []
                                    for i in range(len(variable.usecha)):
                                        if variable.character_list[variable.usecha[i]].nHP != 0:
                                            tmpobj.append(i)
                                    for i in range(len(variable.enemy)):
                                        if variable.enemy[i].nHP != 0:
                                            tmpobj.append(i+3)
                                    self.obj.append(random.choice(tmpobj))
                                if len(self.obj) == 1:  # 單一目標
                                    if self.act == 0 and self.perform.skilling > 0:
                                        if self.perform.skillup:
                                            tmpATK = int(tmpATK*1.5)
                                        else:
                                            tmpATK = int(tmpATK*1.3)
                                    o = self.obj[0]
                                    if o >= 3:
                                        self.o_is_monster = True
                                        o = variable.enemy[o-3]
                                        if self.moreene == -1:
                                            mockene = []
                                            # 判斷嘲諷
                                            for ene in variable.enemy:
                                                if ene.mock > 0:
                                                    mockene.append(ene)
                                            if len(mockene) != 0:
                                                o = random.choice(mockene)
                                        if o.type == '史萊姆':
                                            tmpATK //= 2
                                        self.str2 = '對 '+o.type+' 造成 '
                                    else:
                                        self.o_is_monster = False
                                        o = variable.character_list[variable.usecha[o]]
                                        self.str2 = '對 '+o.name+' 造成 '
                                    if critical(self.perform):
                                        tmpATK = int(tmpATK*1.5)
                                        self.str1 += '，造成暴擊'
                                    if self.act == 0 and self.w.code == (2, 2):
                                        if self.moreene != 0:
                                            tmpATK = int(tmpATK*1.5)
                                        else:
                                            tmpATK = int(tmpATK*0.75)
                                    self.moreene = -1
                                    tmpDEF = o.nDEF+o.DEFlimit
                                    if not self.o_is_monster:
                                        if o.name == '竹君' and o.skilling > 0:
                                            if self.perform.skillup:
                                                tmpDEF = int(tmpDEF*1.5)
                                            else:
                                                tmpDEF = int(tmpDEF*1.3)
                                    cause_dmg = tmpATK-tmpDEF
                                    if cause_dmg <= 0:
                                        cause_dmg = 1
                                    if self.act == 0 and self.w.code == (1, 1):
                                        cause_dmg *= 2
                                    elif self.act == 0 and self.w.code == (1, 2):
                                        if cause_dmg < 15:
                                            cause_dmg = 15
                                    elif self.act == 0 and self.w.code == (2, 1):
                                        tmpprob = random.randint(1, 100)
                                        if tmpprob >= 60:
                                            self.str2 = '麵掉在地上，miss'
                                            cause_dmg = 0
                                    elif self.act == 0 and self.w.code == (3, 2):
                                        tmpprob = random.randint(1, 100)
                                        tmpobj = []
                                        if tmpprob % 2:
                                            for i in variable.usecha:
                                                if variable.character_list[i].nHP != 0:
                                                    tmpobj.append(i)
                                            tmp = random.choice(tmpobj)
                                            variable.character_list[tmp].recover += 2
                                            self.str3 = '咖啡灑到隊友，使其獲得【恢復】效果。'
                                        else:
                                            for i in variable.enemy:
                                                if i.nHP != 0:
                                                    tmpobj.append(i)
                                            tmp = random.choice(tmpobj)
                                            i.poison += 2
                                            self.str3 = '咖啡（？灑到敵方，使其獲得【中毒】效果。'
                                    elif self.act == 0 and self.w.code == (4, 0):
                                        self.perform.nHP += int(cause_dmg*0.3)
                                        self.perform.nHP = min(
                                            self.perform.nHP, self.perform.HP[self.perform.level])
                                        self.str3 = "天秤回正，回復 " + \
                                            str(int(cause_dmg*0.3))+' 點HP'
                                    if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                        if not variable.character_list[3].skillup:
                                            cause_dmg = max(
                                                int(cause_dmg*1.3), cause_dmg+1)
                                        else:
                                            cause_dmg = max(
                                                int(cause_dmg*1.6), cause_dmg+1)

                                    if cause_dmg != 0:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點物理傷害'
                                        o.nHP = max(o.nHP, 0)
                                    if self.act == 0 and self.w.code == (1, 1):
                                        self.str2 += '，連擊！'
                                    elif self.act == 0 and self.w.code == (1, 2) and cause_dmg == 15:
                                        self.str2 += '，15公分！'
                                    elif self.act == 0 and self.w.code == (2, 0):
                                        another_ATK = (self.perform.nATK +
                                                       self.perform.ATKlimit)//5
                                        if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                            if not variable.character_list[3].skillup:
                                                cause_dmg = max(
                                                    int(cause_dmg*1.3), cause_dmg+1)
                                            else:
                                                cause_dmg = max(
                                                    int(cause_dmg*1.6), cause_dmg+1)
                                        o.nHP -= another_ATK
                                        o.nHP = max(o.nHP, 0)
                                        self.str2 += ('，追擊 ' +
                                                      str(another_ATK)+' 點真實傷害')
                                    if o.nHP == 0:
                                        self.str2 += '，使其死亡'
                                        o.mock = 0
                                    elif self.act == 0 and self.w.code == (2, 1) and cause_dmg != 0:
                                        self.str3 = '那個味道是真的...，對雙方造成【暈眩】效果'
                                        o.dizz = 2
                                        self.perform.dizz = 2
                                    if self.o_is_monster:
                                        if o.type == '奧利哈鋼魔像' and o.dizz == 0 and o.nHP != 0:
                                            antiatk = max(
                                                int(cause_dmg*0.1), 1)
                                            self.perform.nHP -= antiatk
                                            self.perform.nHP = max(
                                                self.perform.nHP, 0)
                                            self.str3 += '遭到魔像反擊，受到 ' + \
                                                str(antiatk)+' 點真實傷害'
                                else:   # 群體
                                    self.moreene = 0
                                    if self.moreene != len(self.obj):
                                        o = self.obj[0]
                                        self.obj.remove(o)
                                    if o >= 3:
                                        o = variable.enemy[o-3]
                                        if o.type == '史萊姆':
                                            tmpATK //= 2
                                        self.str2 = '對 '+o.type+' 造成 '
                                        self.o_is_monster = True
                                    else:
                                        self.o_is_monster = False
                                        o = variable.character_list[variable.usecha[o]]
                                        self.str2 = '對 '+o.name+' 造成 '
                                    if critical(self.perform):
                                        tmpATK = int(tmpATK*1.5)
                                        self.str1 += '，造成暴擊'
                                    if self.act == 0 and self.w.code == (2, 2):
                                        tmpATK = int(tmpATK*0.75)
                                    tmpDEF = o.nDEF+o.DEFlimit
                                    if not self.o_is_monster:
                                        if o.name == '竹君' and o.skilling > 0:
                                            if self.perform.skillup:
                                                tmpDEF = int(tmpDEF*1.5)
                                            else:
                                                tmpDEF = int(tmpDEF*1.3)
                                    cause_dmg = tmpATK-tmpDEF
                                    if cause_dmg <= 0:
                                        cause_dmg = 1
                                    if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                        if not variable.character_list[3].skillup:
                                            cause_dmg = max(
                                                int(cause_dmg*1.3), cause_dmg+1)
                                        else:
                                            cause_dmg = max(
                                                int(cause_dmg*1.6), cause_dmg+1)
                                    if cause_dmg != 0:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點物理傷害'
                                        o.nHP = max(o.nHP, 0)
                                    if o.nHP == 0:
                                        self.str2 += '，使其死亡'
                                        o.mock = 0
                                    if self.o_is_monster:
                                        if o.type == '奧利哈鋼魔像' and o.dizz == 0 and o.nHP != 0:
                                            antiatk = max(
                                                int(cause_dmg*0.1), 1)
                                            self.perform.nHP -= antiatk
                                            self.perform.nHP = max(
                                                self.perform.nHP, 0)
                                            self.str3 = '遭到反擊，受到 ' + \
                                                str(antiatk)+' 點真實傷害'
                            elif self.perform.ATKtype == 2:  # 魔法
                                if self.act == 0 and self.w.code == (4, 1) and self.moreene == -1:
                                    self.obj = []
                                    for i in range(len(variable.enemy)):
                                        if variable.enemy[i].nHP != 0:
                                            self.obj.append(i+3)
                                if len(self.obj) == 1:  # 單一目標
                                    o = self.obj[0]
                                    if o >= 3:
                                        self.o_is_monster = True
                                        o = variable.enemy[o-3]
                                        if self.moreene == -1:
                                            mockene = []
                                            # 判斷嘲諷
                                            for ene in variable.enemy:
                                                if ene.mock > 0:
                                                    mockene.append(ene)
                                            if len(mockene) != 0:
                                                o = random.choice(mockene)
                                        self.str2 = '對 '+o.type+' 造成 '
                                    else:
                                        o = variable.character_list[variable.usecha[o]]
                                        self.str2 = '對 '+o.name+' 造成 '
                                        self.o_is_monster = False
                                    self.moreene = -1
                                    if self.act == 0 and self.w.code == (4, 1):
                                        if o.burn != 0:
                                            tmpATK = int(tmpATK*1.5)
                                    if critical(self.perform):
                                        tmpATK = int(tmpATK*1.5)
                                        self.str1 += '，造成暴擊'
                                    tmpDEF = o.nDEF+o.DEFlimit
                                    if not self.o_is_monster:
                                        if o.name == '竹君' and o.skilling > 0:
                                            if self.perform.skillup:
                                                tmpDEF = int(tmpDEF*1.5)
                                            else:
                                                tmpDEF = int(tmpDEF*1.3)
                                    cause_dmg = tmpATK-tmpDEF
                                    if cause_dmg <= 0:
                                        cause_dmg = 1
                                    if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                        if not variable.character_list[3].skillup:
                                            cause_dmg = max(
                                                int(cause_dmg*1.3), cause_dmg+1)
                                        else:
                                            cause_dmg = max(
                                                int(cause_dmg*1.6), cause_dmg+1)
                                    if cause_dmg != 0:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點魔法傷害'
                                        o.nHP = max(o.nHP, 0)
                                    if o.nHP == 0:
                                        self.str2 += '，使其死亡'
                                        o.mock = 0
                                        if self.act == 0:
                                            self.str2 += '，但竹君也被辣暈了'
                                            self.perform.dizz += 3
                                    elif self.act == 0 and self.w.code == (4, 1):
                                        o.burn += 5
                                        self.str2 += '，使其食道灼傷，造成【燃燒】效果，但竹君也被辣暈了'
                                        self.perform.dizz += 2
                                    if self.o_is_monster:
                                        if o.type == '奧利哈鋼魔像' and o.dizz == 0 and o.nHP != 0:
                                            antiatk = max(
                                                int(cause_dmg*0.1), 1)
                                            self.perform.nHP -= antiatk
                                            self.perform.nHP = max(
                                                self.perform.nHP, 0)
                                            self.str3 = '遭到反擊，受到 ' + \
                                                str(antiatk)+' 點真實傷害'
                                else:   # 群體
                                    self.moreene = 0
                                    if self.moreene != len(self.obj):
                                        o = self.obj[0]
                                        self.obj.remove(o)
                                    if o >= 3:
                                        o = variable.enemy[o-3]
                                        self.str2 = '對 '+o.type+' 造成 '
                                        self.o_is_monster = True
                                    if self.act == 0 and self.w.code == (4, 1):
                                        if o.burn != 0:
                                            tmpATK = int(tmpATK*1.5)
                                    if critical(self.perform):
                                        tmpATK = int(tmpATK*1.5)
                                        self.str1 += '，造成暴擊'
                                    tmpDEF = o.nDEF+o.DEFlimit
                                    if not self.o_is_monster:
                                        if o.name == '竹君' and o.skilling > 0:
                                            if self.perform.skillup:
                                                tmpDEF = int(tmpDEF*1.5)
                                            else:
                                                tmpDEF = int(tmpDEF*1.3)
                                    cause_dmg = tmpATK-tmpDEF
                                    if cause_dmg <= 0:
                                        cause_dmg = 1
                                    if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                        if not variable.character_list[3].skillup:
                                            cause_dmg = max(
                                                int(cause_dmg*1.3), cause_dmg+1)
                                        else:
                                            cause_dmg = max(
                                                int(cause_dmg*1.6), cause_dmg+1)
                                    if cause_dmg != 0:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點魔法傷害'
                                        o.nHP = max(o.nHP, 0)
                                    if o.nHP == 0:
                                        self.str2 += '，使其死亡'
                                        o.mock = 0
                                    elif self.act == 0 and self.w.code == (4, 1):
                                        o.burn += 5
                                        self.str2 += '，使其食道灼傷，造成【燃燒】效果'
                                    if self.o_is_monster:
                                        if o.type == '奧利哈鋼魔像' and o.dizz == 0 and o.nHP != 0:
                                            antiatk = max(
                                                int(cause_dmg*0.1), 1)
                                            self.perform.nHP -= antiatk
                                            self.perform.nHP = max(
                                                self.perform.nHP, 0)
                                            self.str3 = '遭到反擊，受到 ' + \
                                                str(antiatk)+' 點真實傷害'
                            elif self.perform.ATKtype == 3:  # 真實
                                if len(self.obj) == 1:  # 單一目標
                                    o = self.obj[0]
                                    if o >= 3:
                                        o = variable.enemy[o-3]
                                        mockene = []
                                        # 判斷嘲諷
                                        for ene in variable.enemy:
                                            if ene.mock > 0:
                                                mockene.append(ene)
                                        if len(mockene) != 0:
                                            o = random.choice(mockene)
                                        self.str2 = '對 '+o.type+' 造成 '
                                        self.o_is_monster = True
                                    else:
                                        o = variable.character_list[variable.usecha[o]]
                                        self.o_is_monster = False
                                        self.str2 = '對 '+o.name+' 造成 '
                                    if critical(self.perform):
                                        tmpATK = int(tmpATK*1.5)
                                        self.str1 += '，造成暴擊'
                                    if self.act == 0 and self.w.code == (3, 1):
                                        tmpATK = max(int(tmpATK*0.25), 1)
                                        self.str1 = '竹君 使出 偽‧星爆氣流斬'
                                        self.str2 += (str(tmpATK) +
                                                      '點真實傷害 * 16 次')
                                        self.perform.ATKtype = 1
                                        cause_dmg = tmpATK*16
                                    if cause_dmg == 0:
                                        cause_dmg = 1
                                    if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                        if not variable.character_list[3].skillup:
                                            cause_dmg = max(
                                                int(cause_dmg*1.3), cause_dmg+1)
                                        else:
                                            cause_dmg = max(
                                                int(cause_dmg*1.6), cause_dmg+1)
                                    if cause_dmg != 0:
                                        o.nHP -= cause_dmg
                                        if self.act != 0 or self.w.code != (3, 1):
                                            self.str2 += str(cause_dmg) + \
                                                ' 點真實傷害'
                                        o.nHP = max(o.nHP, 0)
                                    if o.nHP == 0:
                                        self.str2 += '，使其死亡'
                                        o.mock = 0
                                    if self.o_is_monster:
                                        if o.type == '奧利哈鋼魔像' and o.dizz == 0 and o.nHP != 0:
                                            antiatk = max(
                                                int(cause_dmg*0.1), 1)
                                            self.perform.nHP -= antiatk
                                            self.perform.nHP = max(
                                                self.perform.nHP, 0)
                                            self.str3 = '遭到反擊，受到 ' + \
                                                str(antiatk)+' 點真實傷害'
                            elif self.perform.ATKtype == 4:  # 回復
                                if len(self.obj) == 1:  # 單一目標
                                    o = self.obj[0]
                                    self.str2 = ''
                                    if o >= 3:
                                        o = variable.enemy[o-3]
                                        self.str2 = '回復 '+o.type+' '
                                    else:
                                        o = variable.character_list[variable.usecha[o]]
                                        self.str2 = '回復 '+o.name+' '
                                        if o.nHP == 0:
                                            self.str2 = '復活，'
                                            cause_heal = int(o.HP[o.level]*0.2)
                                    if o.nHP != 0:
                                        cause_heal = tmpATK
                                    o.nHP += cause_heal
                                    self.str2 += str(cause_heal)+' 點生命'
                                    o.nHP = min(o.nHP, o.HP[o.level])
                        elif variable.myATKtype[self.act] == 1:  # 戰技
                            self.str1 = self.perform.skfont[0][0]
                            if variable.usecha[self.act] == 0:
                                self.str2 = self.perform.skfont[1][0]
                                self.perform.skilling = 3
                                if self.perform.skillup:
                                    self.perform.SKCD = self.perform.oriUPSKCD+1
                                else:
                                    self.perform.SKCD = self.perform.oriSKCD+1
                            elif variable.usecha[self.act] == 1:
                                self.str2 = self.perform.skfont[1][0]
                                self.perform.skilling = 1
                                if self.perform.skillup:
                                    self.perform.SKCD = self.perform.oriUPSKCD+1
                                else:
                                    self.perform.SKCD = self.perform.oriSKCD+1
                            elif variable.usecha[self.act] == 2:
                                self.str2 = self.perform.skfont[1][0]
                                self.perform.mock += 3
                                if self.perform.skillup:
                                    self.perform.SKCD = self.perform.oriUPSKCD+1
                                else:
                                    self.perform.SKCD = self.perform.oriSKCD+1
                                if self.perform.skillup:
                                    self.perform.DEFlimit += int(
                                        self.perform.nDEF*0.2)
                            elif variable.usecha[self.act] == 3:
                                self.str2 = self.perform.skfont[1][0]
                                self.perform.skilling = 2
                                if self.perform.skillup:
                                    self.perform.SKCD = self.perform.oriUPSKCD+1
                                else:
                                    self.perform.SKCD = self.perform.oriSKCD+1
                            elif variable.usecha[self.act] == 4:
                                tmplist = []
                                for i in variable.usecha:
                                    if variable.character_list[i].nDEF+variable.character_list[i].DEFlimit <= 7:
                                        tmplist.append(
                                            variable.character_list[i])
                                if len(tmplist) != 0:
                                    g = random.choice(tmplist)
                                    g.DEFlimit += self.perform.level
                                    self.str2 = g.name+' '
                                    self.str2 += self.perform.skfont[1][0]
                                else:
                                    self.str2 = '沒有合適對象，使用失敗'
                                if self.perform.skillup:
                                    self.perform.SKCD = self.perform.oriUPSKCD+1
                                else:
                                    self.perform.SKCD = self.perform.oriSKCD+1
                        elif variable.myATKtype[self.act] == 2:  # 奧義
                            self.str1 = self.perform.ultfont[0][0]
                            if variable.usecha[self.act] == 0:
                                self.str2 = self.perform.ultfont[1][0]
                                if self.perform.ultskilling < variable.floor:
                                    self.perform.ultskilling += 1
                                    self.perform.ULTCD = self.perform.oriULTCD+1
                                    self.perform.nHP += 5
                                    self.perform.ATKlimit += 3
                                    self.perform.DEFlimit += 3
                                else:
                                    self.str3 = '但是受到未知力量的阻撓而失敗，下一層再試試看吧'
                            elif variable.usecha[self.act] == 1:
                                self.str2 = self.perform.ultfont[1][0]
                                tmpATK = 2*(self.perform.nATK +
                                            self.perform.ATKlimit)
                                if critical(self.perform):
                                    tmpATK = int(tmpATK*1.5)
                                    self.str1 += '，造成暴擊'
                                o = variable.enemy[self.obj[0]-3]
                                mockene = []
                                # 判斷嘲諷
                                for ene in variable.enemy:
                                    if ene.mock > 0:
                                        mockene.append(ene)
                                if len(mockene) != 0:
                                    o = random.choice(mockene)
                                self.str2 += o.type+self.perform.ultfont[1][1]
                                cause_dmg = tmpATK
                                if o.type == '史萊姆':
                                    cause_dmg = int(cause_dmg/2)
                                self.str2 += str(cause_dmg) + \
                                    self.perform.ultfont[1][2]
                                o.nHP -= cause_dmg
                                o.nHP = max(o.nHP, 0)
                                if o.nHP == 0:
                                    self.str2 += '，使其死亡'
                                    o.mock = 0
                                else:
                                    self.perform.ultskilling = 2
                                    o.DEFlimit = -(o.nDEF)
                                self.perform.ULTCD = self.perform.oriULTCD+1
                            elif variable.usecha[self.act] == 2:
                                self.str2 = self.perform.ultfont[1][0]
                                self.perform.ultskilling = 3
                                self.perform.ULTCD = self.perform.oriULTCD+1
                            elif variable.usecha[self.act] == 3:
                                self.str2 = self.perform.ultfont[1][0]
                                tmpATK = 2*(self.perform.nATK +
                                            self.perform.ATKlimit)
                                if critical(self.perform):
                                    tmpATK = int(tmpATK*1.5)
                                    self.str1 += '，造成暴擊'
                                o = variable.enemy[self.obj[0]-3]
                                mockene = []
                                # 判斷嘲諷
                                for ene in variable.enemy:
                                    if ene.mock > 0:
                                        mockene.append(ene)
                                if len(mockene) != 0:
                                    o = random.choice(mockene)
                                self.str2 += o.type+self.perform.ultfont[1][1]
                                cause_dmg = tmpATK
                                self.str2 += str(cause_dmg) + \
                                    self.perform.ultfont[1][2]
                                o.nHP -= cause_dmg
                                o.nHP = max(o.nHP, 0)
                                if o.nHP == 0:
                                    self.str2 += '，使其死亡'
                                    o.mock = 0
                                else:
                                    o.burn = 5
                                self.perform.ULTCD = self.perform.oriULTCD+1
                            elif variable.usecha[self.act] == 4:
                                self.str2 = self.perform.ultfont[1][0]+str(
                                    int((self.perform.nATK+self.perform.ATKlimit)*1.25))+self.perform.ultfont[1][1]
                                for i in variable.usecha:
                                    g = variable.character_list[i]
                                    if g.nHP != 0:
                                        g.nHP += int((self.perform.nATK +
                                                     self.perform.ATKlimit)*1.25)
                                        g.recover = 3
                                        g.nHP = min(
                                            g.nHP, g.HP[g.level])
                                self.perform.ULTCD = self.perform.oriULTCD+1
                    elif self.perform.nHP == 0:
                        self.str1 = self.perform.name+' 已經掛了'
                        self.str2 = ''
                    else:
                        self.str1 = self.perform.name+' 暈眩中'
                        self.str2 = ''
                    self.havecalculate = True
                elif self.act <= 5:    # 敵方
                    self.o_is_monster = False
                    self.perform = variable.enemy[self.act-3]
                    self.str1 = self.perform.type+' 使出 普通攻擊'
                    if self.perform.nHP != 0 and self.perform.dizz == 0:  # 還活著、沒暈眩
                        self.obj = variable.eneATKobject[self.act-3]
                        if self.perform.ATKtype == 1:  # 物理
                            tmpATK = self.perform.nATK
                            o = variable.character_list[variable.usecha[self.obj]]
                            mockene = []
                            # 判斷嘲諷
                            for cha in variable.usecha:
                                if variable.character_list[cha].mock > 0:
                                    mockene.append(
                                        variable.character_list[cha])
                            if len(mockene) != 0:
                                o = random.choice(mockene)
                            self.str2 = '對 '+o.name+' 造成 '
                            if critical(self.perform):
                                tmpATK = int(tmpATK*1.5)
                                self.str1 += '，造成暴擊'
                            tmpDEF = o.nDEF+o.DEFlimit
                            if not self.o_is_monster:
                                if o.name == '竹君' and o.skilling > 0:
                                    if o.skillup:
                                        tmpDEF = int(tmpDEF*1.5)
                                    else:
                                        tmpDEF = int(tmpDEF*1.3)
                            cause_dmg = tmpATK-tmpDEF
                            if cause_dmg <= 0:
                                cause_dmg = 1
                            if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                if not variable.character_list[3].skillup:
                                    cause_dmg = int(cause_dmg*1.3)
                                else:
                                    cause_dmg = int(cause_dmg*1.6)
                            if cause_dmg != 0:
                                if not self.o_is_monster:
                                    if o.name == '副班長' and o.ultskilling > 0:
                                        for ene in variable.enemy:
                                            if ene.nHP != 0:
                                                ene.nHP -= cause_dmg
                                                ene.nHP = max(
                                                    ene.nHP, 0)
                                        self.str2 = '但被格擋，反擊全體敵方'+str(cause_dmg) + \
                                            ' 點傷害'
                                        o.ultskilling -= 1
                                    else:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點物理傷害'
                                        o.nHP = max(o.nHP, 0)
                                else:
                                    o.nHP -= cause_dmg
                                    self.str2 += str(cause_dmg) + \
                                        ' 點物理傷害'
                                    o.nHP = max(o.nHP, 0)
                            if o.nHP == 0:
                                self.str2 += '，使其死亡'
                                o.mock = 0
                            elif self.perform.type == '哥布林':
                                tmpprob = random.randint(1, 100)
                                if tmpprob % 10 == 3:
                                    o.poison += 2
                                    self.str3 = '受到【中毒】效果'
                            elif self.perform.type == '半獸人':
                                self.str3 = '攻擊過猛，自身受到【暈眩】效果'
                                self.perform.dizz += 2
                        elif self.perform.ATKtype == 2:  # 魔法
                            tmpATK = self.perform.nATK
                            o = variable.character_list[variable.usecha[self.obj]]
                            mockene = []
                            # 判斷嘲諷
                            for cha in variable.usecha:
                                if variable.character_list[cha].mock > 0:
                                    mockene.append(
                                        variable.character_list[cha])
                            if len(mockene) != 0:
                                o = random.choice(mockene)
                            self.str2 = '對 '+o.name+' 造成 '
                            if critical(self.perform):
                                tmpATK = int(tmpATK*1.5)
                                self.str1 += '，造成暴擊'
                            tmpDEF = o.nDEF+o.DEFlimit
                            if not self.o_is_monster:
                                if o.name == '竹君' and o.skilling > 0:
                                    if o.skillup:
                                        tmpDEF = int(tmpDEF*1.5)
                                    else:
                                        tmpDEF = int(tmpDEF*1.3)
                            if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                if not variable.character_list[3].skillup:
                                    cause_dmg = int(cause_dmg*1.3)
                                else:
                                    cause_dmg = int(cause_dmg*1.6)
                            cause_dmg = tmpATK-tmpDEF
                            if cause_dmg <= 0:
                                cause_dmg = 1
                            if cause_dmg != 0:
                                if not self.o_is_monster:
                                    if o.name == '副班長' and o.ultskilling > 0:
                                        for ene in variable.enemy:
                                            if ene.nHP != 0:
                                                ene.nHP -= cause_dmg
                                                ene.nHP = max(
                                                    ene.nHP, 0)
                                        self.str2 = '但被格擋，反擊全體敵方'+str(cause_dmg) + \
                                            ' 點傷害'
                                        o.ultskilling -= 1
                                    else:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點魔法傷害'
                                        o.nHP = max(o.nHP, 0)
                                else:
                                    o.nHP -= cause_dmg
                                    self.str2 += str(cause_dmg) + \
                                        ' 點魔法傷害'
                                    o.nHP = max(o.nHP, 0)
                            if o.nHP == 0:
                                self.str2 += '，使其死亡'
                                o.mock = 0
                            elif self.perform.type == '邪教祭司':
                                tmpprob = random.randint(1, 100)
                                if tmpprob <= 20:
                                    o.poison += 2
                                    self.str2 += '。給予我方目標【中毒】效果'
                                elif tmpprob <= 65:
                                    o.burn += 2
                                    self.str2 += '。給予我方目標【燃燒】效果'
                                else:
                                    o.dizz += 2
                                    self.str2 += '。給予我方目標【暈眩】效果'
                        elif self.perform.ATKtype == 3:  # 真實
                            tmpATK = self.perform.nATK
                            o = variable.character_list[variable.usecha[self.obj]]
                            mockene = []
                            # 判斷嘲諷
                            for cha in variable.usecha:
                                if variable.character_list[cha].mock > 0:
                                    mockene.append(
                                        variable.character_list[cha])
                            if len(mockene) != 0:
                                o = random.choice(mockene)
                            self.str2 = '對 '+o.name+' 造成 '
                            if critical(self.perform):
                                tmpATK = int(tmpATK*1.5)
                                self.str1 += '，造成暴擊'
                            if variable.character_list[3].skilling > 0 and self.o_is_monster:
                                if not variable.character_list[3].skillup:
                                    cause_dmg = int(cause_dmg*1.3)
                                else:
                                    cause_dmg = int(cause_dmg*1.6)
                            cause_dmg = tmpATK
                            if cause_dmg <= 0:
                                cause_dmg = 1
                            if cause_dmg != 0:
                                if not self.o_is_monster:
                                    if o.name == '副班長' and o.ultskilling > 0:
                                        for ene in variable.enemy:
                                            if ene.nHP != 0:
                                                ene.nHP -= cause_dmg
                                                ene.nHP = max(
                                                    ene.nHP, 0)
                                        self.str2 = '但被格擋，反擊全體敵方'+str(cause_dmg) + \
                                            ' 點傷害'
                                        o.ultskilling -= 1
                                    else:
                                        o.nHP -= cause_dmg
                                        self.str2 += str(cause_dmg) + \
                                            ' 點真實傷害'
                                        o.nHP = max(o.nHP, 0)
                                else:
                                    o.nHP -= cause_dmg
                                    self.str2 += str(cause_dmg) + \
                                        ' 點真實傷害'
                                    o.nHP = max(o.nHP, 0)
                            if o.nHP == 0:
                                self.str2 += '，使其死亡'
                                o.mock = 0
                        elif self.perform.ATKtype == 4:
                            HPnotfull = []
                            for ene in variable.enemy:
                                if ene.nHP != ene.HP[ene.level]:
                                    HPnotfull.append(ene)
                            o = random.choice(HPnotfull)
                            self.str2 = '回復 '+o.type+' '
                            cause_heal = self.perform.nATK
                            o.nHP += cause_heal
                            self.str2 += str(cause_heal)+' 點生命'
                            o.nHP = min(o.nHP, o.HP[o.level])
                        self.havecalculate = True
                    elif self.perform.nHP == 0:
                        self.str1 = self.perform.type+' 已經掛了'
                        self.str2 = ''
                    else:
                        self.str1 = self.perform.type+' 暈眩中'
                        self.str2 = ''
                    self.havecalculate = True
                # 圖片處理
                self.image = pygame.surface.Surface((1300, 200))
                self.image.fill(GRAY)
                self.rect.bottomleft = (0, 800)
                self.font1 = font_27_30_B.render(self.str1, False, WHITE)
                self.font2 = font_27_24_B.render(self.str2, False, WHITE)
                self.font3 = font_27_24_B.render(self.str3, False, WHITE)
                self.image.blit(self.font1, (350, 0))
                self.image.blit(self.font2, (350, 60))
                self.image.blit(self.font3, (350, 120))

    def death_check(self):
        # 死亡判定
        for i in variable.usecha:
            if variable.character_list[i].nHP != 0:
                break
        else:
            sprite.battle_font.situation = 3
            sprite.battle_font.display = True
            variable.work = 1000
            if variable.haveitem["mgs"] > 0:
                variable.haveitem["mgs"] -= 1
                sprite.battle_font.situation = 4
                variable.work = 800
                for i in variable.usecha:
                    tmp = variable.character_list[i]
                    tmp.nHP = tmp.HP[tmp.level]
                    tmp.SKCD = 0
                    tmp.ULTCD = 0
                sprite.battle_font.h_update()
                return False
            flag.lose_game = True
            sprite.battle_font.h_update()
            return True
        for i in variable.enemy:
            if i.nHP != 0:
                break
        else:
            flag.in_battle = False
            flag.win_battle = True
            flag.sprite_need_change = True
            self.moreene = -1
            sprite.battle_gain.h_update()
            return True
        return False

# 戰鬥特效

# 強制顯示文字欄


class b_font(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bat_font_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.display = False
        self.situation = 0    # 1：技能冷卻  2：角色死亡中 3：隊伍全滅  4：魔法石復活
        self.font1 = font_27_80_B.render("技能冷卻中", False, LIGHT_KHAKI)
        self.font1rect = self.font1.get_rect()
        self.font1rect.center = (500, 300)
        self.font2 = font_27_80_B.render("已經死了", False, STRONG_RED)
        self.font2rect = self.font2.get_rect()
        self.font2rect.center = (500, 300)
        self.font3 = font_27_100_B.render("隊伍全滅", False, STRONG_RED)
        self.font3rect = self.font3.get_rect()
        self.font3rect.center = (500, 300)
        self.font4_1 = font_27_80_B.render("一顆神秘的石頭粉碎", False, SUN_ORANGE)
        self.font4_1rect = self.font4_1.get_rect()
        self.font4_1rect.center = (500, 180)
        self.font4_2 = font_27_80_B.render("所有角色復活", False, HP_GREEN)
        self.font4_2rect = self.font4_2.get_rect()
        self.font4_2rect.center = (500, 360)
        self.font5 = font_27_80_B.render("請不要幫助敵人", False, STRONG_RED)
        self.font5rect = self.font2.get_rect()
        self.font5rect.center = (500, 300)
        self.font6 = font_27_80_B.render("請確保全員都有選取到行動", False, LIGHT_KHAKI)
        self.font6rect = self.font6.get_rect()
        self.font6rect.center = (500, 300)

    def h_update(self):
        global background_sprite, all_sprite
        if self.display:
            self.image = bat_font_img.copy()
            self.rect.center = (650, 400)
            background_sprite = sprite_group.battle_sprite.copy()
            background_sprite.remove(self)
            all_sprite.empty()
            all_sprite.add(self)
            if self.situation == 1:
                self.image.blit(self.font1, self.font1rect)
            elif self.situation == 2:
                self.image.blit(self.font2, self.font2rect)
            elif self.situation == 3:
                background_sprite.empty()
                self.image.blit(self.font3, self.font3rect)
                self.rect.center = (750, 400)
            elif self.situation == 4:
                self.image.blit(self.font4_1, self.font4_1rect)
                self.image.blit(self.font4_2, self.font4_2rect)
            elif self.situation == 5:
                self.image.blit(self.font5, self.font5rect)
            elif self.situation == 6:
                self.image.blit(self.font6, self.font6rect)
        else:
            self.rect.top = 800


# 使用藥水補血文字框
class bat_heal_font(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.image.blit(recover_font_img.copy(), (350, 220))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.yrect = yes_img.get_rect()
        self.yrect.topleft = (750, 600)
        self.nrect = no_img.get_rect()
        self.nrect.topleft = (400, 600)
        self.image.blit(yes_img.copy(), self.yrect)
        self.image.blit(no_img.copy(), self.nrect)

    def update(self):
        self.image = pygame.surface.Surface((1500, 800), pygame.SRCALPHA)
        self.image.blit(recover_font_img.copy(), (350, 220))
        self.image.blit(yes_img.copy(), self.yrect)
        self.image.blit(no_img.copy(), self.nrect)
        if self.yrect.collidepoint(mouse_location) and mouse_one_press(0):
            if variable.haveitem["lp"] > 0:
                variable.haveitem["lp"] -= 1
                sprite.act_information.perform.nHP += (
                    sprite.act_information.perform.HP[sprite.act_information.perform.level])//5
                sprite.act_information.perform.nHP = min(
                    sprite.act_information.perform.nHP, sprite.act_information.perform.HP[sprite.act_information.perform.level])
                flag.heal_cha = False
                flag.sprite_need_change = True
            else:
                self.image = pygame.surface.Surface(
                    (1500, 800), pygame.SRCALPHA)
                self.image.blit(recover_font2_img.copy(), (350, 220))
                variable.work = 700
        elif self.nrect.collidepoint(mouse_location) and mouse_one_press(0):
            flag.heal_cha = False
            flag.sprite_need_change = True

# 戰鬥獎勵


class bat_gain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = victory_gain_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (650, 400)
        self.coin = c_coin_img.copy()
        self.coinrect = self.coin.get_rect()
        self.coinrect.center = (500, 310)
        self.image.blit(self.coin, self.coinrect)

    def update(self):
        if mouse_one_press(0) or keyboard_one_press("any"):
            flag.win_battle = False
            flag.sprite_need_change = True

    def h_update(self):
        self.image = victory_gain_img.copy()
        self.image.blit(self.coin, self.coinrect)
        tmp = random.randint(15, 7*variable.fr)
        self.font = font_m_100.render(str(tmp), False, BLACK)
        self.fontrect = self.font.get_rect()
        self.fontrect.bottomright = (600, 420)
        self.image.blit(self.font, self.fontrect)
        variable.coin += tmp


# 出塔時做的事


def out_tower_init():
    if variable.nowroom[0] != 0:
        sprite_group.tower_sprite.remove(sprite.tower_door_left)
    if variable.nowroom[0] != variable.fr-1:
        sprite_group.tower_sprite.remove(sprite.tower_door_right)
    if variable.nowroom[1] != variable.fr-1:
        sprite_group.tower_sprite.remove(sprite.tower_door_down)
        if variable.nowroom[1] == 0:
            sprite_group.tower_sprite.add(sprite.tower_door_up)
    sprite.manipulate_character.rect.centerx = 650
    sprite.manipulate_character.rect.top = 200
    sprite.manipulate_character.background = sprite.village_map
    sprite_group.tower_sprite.remove(sprite.tower_room_image)
    sprite_group.tower_sprite.remove(sprite.tower_room_font_up)
    sprite_group.tower_sprite.remove(sprite.tower_room_font_middle)
    flag.in_tower = False
    flag.out_tower = False
    flag.sprite_need_change = True
    variable.floor += 1
    variable.fr += 1
    return

# 進塔時做的事


def enter_tower_init():
    flag.roomgone = []
    variable.room = []
    sprite.manipulate_character.background = sprite.tower_map
    flag.in_tower = True
    sprite.manipulate_character.rect.bottom = 600
    sprite.manipulate_character.rect.centerx = 650
    variable.room = shuffle_room()
    flag.roomgone = [[False for x in range(
        variable.fr)] for y in range(variable.fr)]
    variable.nowroom = [0, variable.fr]
    flag.enter_tower = False
    flag.sprite_need_change = True
    sprite.tower_room_image.image = pygame.Surface((300, 300), pygame.SRCALPHA)
    sprite_group.tower_sprite.add(sprite.tower_room_image)
    sprite_group.tower_sprite.add(sprite.tower_room_font_up)
    sprite_group.tower_sprite.add(sprite.tower_room_font_middle)
    return

# 房間變換時做的事


def room_change_init():
    # 房間代碼與場景處理
    if variable.direction == 2:
        if variable.nowroom[1] == variable.fr:
            sprite_group.tower_sprite.add(sprite.tower_door_right)
        if variable.nowroom[1] == variable.fr-1:
            sprite_group.tower_sprite.add(sprite.tower_door_down)
        variable.nowroom[1] -= 1
        if variable.nowroom[1] == 0:
            sprite_group.tower_sprite.remove(sprite.tower_door_up)
        sprite.manipulate_character.rect.center = (650, 650)
    elif variable.direction == 1:
        if variable.nowroom[0] == variable.fr-1:
            sprite_group.tower_sprite.add(sprite.tower_door_right)
        variable.nowroom[0] -= 1
        if variable.nowroom[0] == 0:
            sprite_group.tower_sprite.remove(sprite.tower_door_left)
        sprite.manipulate_character.rect.center = (1090, 400)
    elif variable.direction == 4:
        if variable.nowroom[1] == 0:
            sprite_group.tower_sprite.add(sprite.tower_door_up)
            for i in sprite.tower_door_list:
                if sprite_group.tower_sprite.has(i) and i != sprite.tower_door_up:
                    sprite_group.tower_sprite.remove(i)
                    sprite_group.tower_sprite.add(i)
            if sprite_group.tower_sprite.has(sprite.tower_room_font_up):
                sprite_group.tower_sprite.remove(sprite.tower_room_font_up)
                sprite_group.tower_sprite.add(sprite.tower_room_font_up)
        variable.nowroom[1] += 1
        if variable.nowroom[1] == variable.fr-1:
            sprite_group.tower_sprite.remove(sprite.tower_door_down)
        sprite.manipulate_character.rect.center = (650, 150)
    elif variable.direction == 3:
        if variable.nowroom[0] == 0:
            sprite_group.tower_sprite.add(sprite.tower_door_left)
        variable.nowroom[0] += 1
        if variable.nowroom[0] == variable.fr-1:
            sprite_group.tower_sprite.remove(sprite.tower_door_right)
        sprite.manipulate_character.rect.center = (210, 400)
    sprite.tower_room_image.h_update()
    flag.room_change = False
    flag.sprite_need_change = True
    variable.direction = 0
    return

# 所有的sprite


class sprites(object):
    def __init__(self):
        self.welcome_font = wel_font()
        self.quit_game = quit()
        self.start_game = play()
        self.inputbox = inpbox()
        self.alpha_background = Alpha_back()
        self.village_map = vil_map()
        self.tower_map = tow_map()
        self.manipulate_character = mani_cha()
        self.function_list = fn_list()
        self.bag = fn_bag()
        self.bag_item_intro = b_item_intro()
        self.weapon_bag = fn_wp()
        self.bag_weapon_intro = b_weapon_intro()
        self.partner_bag = fn_pn()
        self.partner_font = p_font()
        self.partner_up = p_up()
        self.nobgift = nobgift()
        self.giftgain = gift_gain()
        self.gachaUI = gacha()
        self.gachaticket = gahca_ticket()
        self.gacha_font = gacha_font()
        self.gacha_got = None
        self.tower_door_up = tow_door_2()
        self.tower_door_down = tow_door_4()
        self.tower_door_left = tow_door_1()
        self.tower_door_right = tow_door_3()
        self.tower_door_list = [
            self.tower_door_left, self.tower_door_up, self.tower_door_right, self.tower_door_down]
        self.tower_outline = tow_out()
        self.gachaboard = ga_board()
        self.village_shop = vil_shop()
        self.shopping = shop()
        self.enter_tower_font_sprite = enter_tow_font()
        self.tower_room_image = tow_room_img()
        self.tower_room_font_up = tow_room_font_up()
        self.tower_room_font_middle = tow_room_font_mid()
        self.chest = tow_chest()
        self.idol = god_idol()
        self.battle_character_0 = bat_cha(0)
        self.battle_character_1 = bat_cha(1)
        self.battle_character_2 = bat_cha(2)
        self.battle_character_list = [
            self.battle_character_0, self.battle_character_1, self.battle_character_2]
        self.battle_enemy_0 = bat_ene(0)
        self.battle_enemy_1 = bat_ene(1)
        self.battle_enemy_2 = bat_ene(2)
        self.battle_enemy_list = [self.battle_enemy_0,
                                  self.battle_enemy_1, self.battle_enemy_2]
        self.chaHP_0 = HPbar(0)
        self.chaHP_1 = HPbar(1)
        self.chaHP_2 = HPbar(2)
        self.chaHP_list = [self.chaHP_0, self.chaHP_1, self.chaHP_2]
        self.eneHP_0 = HPbar(3)
        self.eneHP_1 = HPbar(4)
        self.eneHP_2 = HPbar(5)
        self.eneHP_list = [self.eneHP_0, self.eneHP_1, self.eneHP_2]
        self.battle_large_image = bat_big_img()
        self.act_information = a_inf()
        self.battle_font = b_font()
        self.battle_heal_font = bat_heal_font()
        self.battle_gain = bat_gain()


sprite = sprites()

# 所有的group（sprite 的container）


class sprite_groups(object):
    def __init__(self):
        self.village_sprite = pygame.sprite.Group()
        self.tower_sprite = pygame.sprite.Group()
        self.bag_sprite = pygame.sprite.Group()
        self.weapon_sprite = pygame.sprite.Group()
        self.partner_sprite = pygame.sprite.Group()
        self.shop_sprite = pygame.sprite.Group()
        self.battle_sprite = pygame.sprite.Group()
        self.welcome_sprite = pygame.sprite.Group()
        self.gacha_sprite = pygame.sprite.Group()
        self.gacha_sprite.add(sprite.function_list)
        self.gacha_sprite.add(sprite.gachaUI)
        self.gacha_sprite.add(sprite.gachaticket)
        self.gacha_sprite.add(sprite.gacha_font)
        self.welcome_sprite.add(sprite.quit_game)
        self.welcome_sprite.add(sprite.start_game)
        self.welcome_sprite.add(sprite.welcome_font)
        self.bag_sprite.add(sprite.bag)
        self.bag_sprite.add(sprite.function_list)
        self.weapon_sprite.add(sprite.weapon_bag)
        self.weapon_sprite.add(sprite.function_list)
        self.partner_sprite.add(sprite.partner_bag)
        self.partner_sprite.add(sprite.function_list)
        self.village_sprite.add(sprite.village_map)
        self.village_sprite.add(sprite.tower_outline)
        self.village_sprite.add(sprite.village_shop)
        self.village_sprite.add(sprite.gachaboard)
        self.village_sprite.add(sprite.manipulate_character)
        self.village_sprite.add(sprite.enter_tower_font_sprite)
        self.village_sprite.add(sprite.nobgift)
        self.village_sprite.add(sprite.function_list)
        self.shop_sprite.add(sprite.shopping)
        self.shop_sprite.add(sprite.function_list)
        self.tower_sprite.add(sprite.tower_map)
        self.tower_sprite.add(sprite.function_list)
        self.tower_sprite.add(sprite.tower_door_up)
        self.tower_sprite.add(sprite.manipulate_character)
        self.battle_sprite.add(sprite.act_information)
        self.battle_sprite.add(sprite.battle_character_0)
        self.battle_sprite.add(sprite.function_list)
        self.battle_sprite.add(sprite.battle_large_image)
        self.battle_sprite.add(sprite.battle_font)


sprite_group = sprite_groups()

background_sprite = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()

# 遊戲主迴圈
flag.running = True  # flag：偵測是否要繼續遊戲


# 測試區
"""for i in range(1, 5):
    variable.character_list[i].LVup()
variable.usecha = [0]
sprite_group.battle_sprite.add(sprite.battle_character_1)
sprite_group.battle_sprite.add(sprite.battle_character_2)
variable.character_list[0].SKCD = 0
variable.haveitem['exp'] = 10"""

while flag.running:

    # 取得輸入

    clock.tick(FPS)
    events = pygame.event.get()
    mouse_press = pygame.mouse.get_pressed()
    mouse_location = pygame.mouse.get_pos()
    keyboard_press = pygame.key.get_pressed()

    # 更新遊戲

    for event in events:
        if event.type == pygame.QUIT:
            flag.running = False
            break
        if event.type == moving:
            sprite.manipulate_character.walkt += 1

    # 判斷是否位於強制對話中，以及是否於下次迴圈中退出對話
    if sprite.tower_room_font_middle.display:
        if mouse_one_press(0) or keyboard_one_press("any"):
            variable.work = 10
            sprite.tower_room_font_middle.display = False
            flag.sprite_need_change = True
        elif variable.work <= 200:
            variable.work += 200

    # 當場景變換時，正在使用的sprite（all_sprite）和背景（background_sprite）的變換
    if flag.sprite_need_change:
        if flag.in_welcome:
            all_sprite = sprite_group.welcome_sprite.copy()
            attack_str_set()
        elif flag.in_nobgift:
            all_sprite.empty()
            all_sprite.add(sprite.giftgain)
            background_sprite.empty()
            background_sprite = sprite_group.village_sprite.copy()
        elif flag.in_chest_gain:
            if not sprite.chest.change:
                sprite.chest.h_update()
            all_sprite.empty()
            all_sprite.add(sprite.chest)
        elif sprite.tower_room_font_middle.display:
            background_sprite.empty()
            background_sprite = sprite_group.tower_sprite.copy()
            background_sprite.remove(sprite.tower_room_font_middle)
            all_sprite.empty()
            all_sprite.add(sprite.tower_room_font_middle)
        elif flag.in_bag:
            if not flag.in_bag_intro:
                all_sprite = sprite_group.bag_sprite.copy()
                background_sprite.empty()
            else:
                all_sprite.empty()
                all_sprite.add(sprite.bag_item_intro)
                background_sprite = sprite_group.bag_sprite.copy()
                if not sprite.bag_item_intro.change:
                    sprite.bag_item_intro.h_update()
        elif flag.in_partner:
            sprite.partner_bag.h_update()
            all_sprite = sprite_group.partner_sprite.copy()
            if flag.partner_font:
                all_sprite.empty()
                all_sprite.add(sprite.partner_font)
                background_sprite = sprite_group.partner_sprite.copy()
            elif flag.partner_up:
                all_sprite.empty()
                all_sprite.add(sprite.partner_up)
                background_sprite = sprite_group.partner_sprite.copy()
        elif flag.in_weapon:
            if not flag.in_wp_intro:
                sprite.weapon_bag.h_update()
                all_sprite = sprite_group.weapon_sprite.copy()
            else:
                all_sprite.empty()
                background_sprite = sprite_group.weapon_sprite.copy()
                all_sprite.add(sprite.bag_weapon_intro)
        elif flag.in_battle:
            if flag.heal_cha:
                all_sprite.empty()
                all_sprite.add(sprite.battle_heal_font)
                background_sprite = sprite_group.battle_sprite.copy()
            else:
                all_sprite = sprite_group.battle_sprite.copy()
                background_sprite.empty()
        elif flag.win_battle:
            all_sprite.empty()
            all_sprite.add(sprite.battle_gain)
            background_sprite.empty()
            background_sprite = sprite_group.tower_sprite.copy()
        elif flag.in_pray:
            all_sprite.empty()
            background_sprite = sprite_group.tower_sprite.copy()
            background_sprite.remove(sprite.function_list)
            all_sprite.add(sprite.function_list)
            all_sprite.add(sprite.idol)
        elif flag.in_shop:
            all_sprite = sprite_group.shop_sprite.copy()
            flag.in_key_in = False
        elif flag.in_gacha:
            all_sprite = sprite_group.gacha_sprite.copy()
            if flag.in_gotcha:
                all_sprite.empty()
                sprite.gacha_got = gacha_got()
                all_sprite.add(sprite.gacha_got)
                background_sprite = sprite_group.gacha_sprite.copy()
        elif not flag.in_tower:
            all_sprite = sprite_group.village_sprite.copy()
        else:
            all_sprite = sprite_group.tower_sprite.copy()
        flag.sprite_need_change = False

    # 當work!=0時，不執行更新程式
    # 反之，執行all_sprite內的更新程式
    if variable.work == 0:
        if sprite.battle_font.display:
            sprite.battle_font.display = False
            flag.sprite_need_change = True
            sprite.battle_font.h_update()
            # 下場遊戲的初始化
            if flag.lose_game:
                flag.sprite_need_change = True
                flag.lose_game = False
                flag = flags()
                variable = variables()
                variable.character_init()
                sprite = sprites()
                sprite_group = sprite_groups()
                background_sprite.empty()
                all_sprite.empty()
        all_sprite.update()  # 執行all_sprite的update函式
        if background_sprite.has(sprite.alpha_background):
            background_sprite.remove(sprite.alpha_background)
        background_sprite.add(sprite.alpha_background)
        sprite.alpha_background.h_update()
        # 置頂圖層
        if all_sprite.has(sprite.manipulate_character):
            all_sprite.remove(sprite.manipulate_character)
            all_sprite.add(sprite.manipulate_character)

    else:
        variable.work -= clock.get_rawtime()
        if variable.work <= 0:
            if flag.heal_cha:
                flag.heal_cha = False
                flag.sprite_need_change = True
            if flag.partner_font:
                flag.partner_font = False
                flag.sprite_need_change = True
            variable.work = 0

    # 進塔的判斷與動作
    if not flag.in_tower:
        if sprite.enter_tower_font_sprite.detect():
            if keyboard_one_press(pygame.K_e):
                flag.enter_tower = True
                enter_tower_init()
    # 出塔與進房間的判斷與動作
    if flag.in_tower:
        if flag.room_change:
            room_change_init()
        if flag.out_tower:
            out_tower_init()

    # 買東西輸入
    if flag.in_key_in:
        tmp = sprite.inputbox.keyin()
        if type(tmp) == int:
            if tmp == -1:
                sprite.inputbox.image.blit(inp_error_img, (400, 350))
                variable.work = 500
            elif tmp == -2:
                pass
            elif tmp == 0:
                flag.in_key_in = False
            else:
                tmplist = sprite.shopping.items[sprite.shopping.bt].buy(tmp)
                if tmplist[0] == True:
                    variable.coin = tmplist[1]
                    sprite.shopping.image.blit(buy_suc_img, (400, 350))
                    variable.work = 500
                    if sprite.shopping.bt == 0:
                        variable.haveitem["gi"] += tmp
                    elif sprite.shopping.bt == 1:
                        variable.haveitem["lp"] += tmp
                    elif sprite.shopping.bt == 2:
                        variable.haveitem["exp"] += tmp
                    elif sprite.shopping.bt == 3:
                        variable.haveitem["us"] += tmp
                else:
                    sprite.shopping.image.blit(buy_fail_img, (400, 350))
                    variable.work = 500
                flag.in_key_in = False
        if not flag.in_key_in:
            background_sprite.remove(sprite.shopping)
            all_sprite.add(sprite.shopping)
            all_sprite.remove(sprite.inputbox)

    # 戰鬥中
    if flag.in_battle:
        if flag.battle_initial:
            enter_battle()
            all_sprite = sprite_group.battle_sprite.copy()
            flag.battle_initial = False
        if flag.new_round:
            round_start()
            sprite.act_information.wpSK += 1
            flag.new_round = False
        if flag.attack_choose:
            all_sprite.remove(sprite.act_information)
            all_sprite.remove(sprite.battle_large_image)
            all_sprite.remove(sprite.function_list)
            background_sprite.add(sprite.act_information)
            background_sprite.add(sprite.battle_large_image)
            background_sprite.add(sprite.function_list)
        if flag.in_dmg_phrase:
            if (mouse_one_press(0) or keyboard_one_press(pygame.K_SPACE)) and sprite.act_information.havecalculate:
                if sprite.act_information.moreene == -1:
                    variable.dmg_phrase_index += 1
                    if flag.lose_game:
                        flag.in_dmg_phrase = False
                        flag.in_battle = False
                    elif variable.dmg_phrase_index < len(variable.act_order):
                        sprite.act_information.act = variable.act_order[variable.dmg_phrase_index]
                        sprite.act_information.havecalculate = False
                    elif not sprite.act_information.death_check():
                        flag.in_dmg_phrase = False
                        flag.new_round = True
                else:
                    if flag.lose_game:
                        flag.in_dmg_phrase = False
                        flag.in_battle = False
                    else:
                        sprite.act_information.havecalculate = False

    # 畫面顯示

    if not flag.lose_game:
        screen.fill(WHITE)  # 重製畫面為白色（洗掉原本畫面上的圖案，不然會發生重疊）
        if flag.in_battle:
            screen.blit(bat_back_img, (0, 0))
        if flag.in_welcome:
            screen.blit(in_back_img, (0, 0))
    else:
        screen.fill(BLACK)
    background_sprite.draw(screen)  # 畫背景
    all_sprite.draw(screen)  # 畫主物件
    gc.collect()    # 聽說可以優化空間，所以就丟上來了
    pygame.display.update()  # 展示更新（把畫面丟上螢幕）


pygame.quit()  # 當不執行時，退出遊戲
