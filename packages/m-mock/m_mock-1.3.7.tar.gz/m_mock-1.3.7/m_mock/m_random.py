import random
import re
import string
import uuid
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from m_mock.m_random_source import single_family_name, en_family_name, en_name


def inNone(obj):
    if isinstance(obj, (tuple, list)):
        # 都为空的就返回True
        boo = []
        for i in obj:
            boo.append(i in ('', None))
        return False if False in boo else True
    return obj in ('', None)


def tuple_to_str(objects) -> str:
    """
    :param objects: 被转换的元组/列表
    :return: 列表被转换后的字符串
    """
    return str(''.join(objects))


def shuffle_string(strings) -> str:
    """

    :param strings: 被打乱的字符(str/list/tuple)
    :return: 打乱的字符
    """
    if isinstance(strings, (list, tuple)):
        pass
    elif isinstance(strings, str):
        strings = list(strings)
    random.shuffle(strings)
    strings = ''.join(strings)
    return strings


class MockPyExpressionException(Exception):
    def __init__(self, exception='Incorrect mocker expression is used.', remark=None):
        super().__init__()
        if remark is None:
            remark = str(remark)
        self.exception = f'{exception}{remark}'

    def __str__(self):
        return self.exception

    @classmethod
    def min_max_value_exception(cls, min_value, max_value):
        if (max_value is None or min_value is None) is False:
            if min_value >= max_value:
                raise MockPyExpressionException('min_value cannot be greater than or equal to max_value.')


_mock_exception = MockPyExpressionException()

chinese = "一乙二十丁厂七卜人入八九几儿了力乃刀又三于干亏士工土才寸下大丈与万上小口巾山千乞川亿个勺久凡及夕丸么" \
          "广亡门义之尸弓己已子卫也女飞刃习叉马乡丰王井开夫天无元专云扎艺木五支厅不太犬区历尤友匹车巨牙屯比互切" \
          "瓦止少日中冈贝内水见午牛手毛气升长仁什片仆化仇币仍仅斤爪反介父从今凶分乏公仓月氏勿欠风丹匀乌凤勾文六" \
          "方火为斗忆订计户认心尺引丑巴孔队办以允予劝双书幻玉刊示末未击打巧正扑扒功扔去甘世古节本术可丙左厉右石" \
          "布龙平灭轧东卡北占业旧帅归且旦目叶甲申叮电号田由史只央兄叼叫另叨叹四生失禾丘付仗代仙们仪白仔他斥瓜乎" \
          "丛令用甩印乐句匆册犯外处冬鸟务包饥主市立闪兰半汁汇头汉宁穴它讨写让礼训必议讯记永司尼民出辽奶奴加召皮" \
          "边发孕圣对台矛纠母幼丝式刑动扛寺吉扣考托老执巩圾扩扫地扬场耳共芒亚芝朽朴机权过臣再协西压厌在有百存而" \
          "页匠夸夺灰达列死成夹轨邪划迈毕至此贞师尘尖劣光当早吐吓虫曲团同吊吃因吸吗屿帆岁回岂刚则肉网年朱先丢舌" \
          "竹迁乔伟传乒乓休伍伏优伐延件任伤价份华仰仿伙伪自血向似后行舟全会杀合兆企众爷伞创肌朵杂危旬旨负各名多" \
          "争色壮冲冰庄庆亦刘齐交次衣产决充妄闭问闯羊并关米灯州汗污江池汤忙兴宇守宅字安讲军许论农讽设访寻那迅尽" \
          "导异孙阵阳收阶阴防奸如妇好她妈戏羽观欢买红纤级约纪驰巡寿弄麦形进戒吞远违运扶抚坛技坏扰拒找批扯址走抄" \
          "坝贡攻赤折抓扮抢孝均抛投坟抗坑坊抖护壳志扭块声把报却劫芽花芹芬苍芳严芦劳克苏杆杠杜材村杏极李杨求更束" \
          "豆两丽医辰励否还歼来连步坚旱盯呈时吴助县里呆园旷围呀吨足邮男困吵串员听吩吹呜吧吼别岗帐财针钉告我乱利" \
          "秃秀私每兵估体何但伸作伯伶佣低你住位伴身皂佛近彻役返余希坐谷妥含邻岔肝肚肠龟免狂犹角删条卵岛迎饭饮系" \
          "言冻状亩况床库疗应冷这序辛弃冶忘闲间闷判灶灿弟汪沙汽沃泛沟没沈沉怀忧快完宋宏牢究穷灾良证启评补初社识" \
          "诉诊词译君灵即层尿尾迟局改张忌际陆阿陈阻附妙妖妨努忍劲鸡驱纯纱纳纲驳纵纷纸纹纺驴纽奉玩环武青责现表规" \
          "抹拢拔拣担坦押抽拐拖拍者顶拆拥抵拘势抱垃拉拦拌幸招坡披拨择抬其取苦若茂苹苗英范直茄茎茅林枝杯柜析板松" \
          "枪构杰述枕丧或画卧事刺枣雨卖矿码厕奔奇奋态欧垄妻顷转斩轮软到非叔肯齿些虎虏肾贤尚旺具果味昆国昌畅明易" \
          "昂典固忠咐呼鸣咏呢岸岩帖罗帜岭凯败贩购图钓制知垂牧物乖刮秆和季委佳侍供使例版侄侦侧凭侨佩货依的迫质欣" \
          "征往爬彼径所舍金命斧爸采受乳贪念贫肤肺肢肿胀朋股肥服胁周昏鱼兔狐忽狗备饰饱饲变京享店夜庙府底剂郊废净" \
          "盲放刻育闸闹郑券卷单炒炊炕炎炉沫浅法泄河沾泪油泊沿泡注泻泳泥沸波泼泽治怖性怕怜怪学宝宗定宜审宙官空帘" \
          "实试郎诗肩房诚衬衫视话诞询该详建肃录隶居届刷屈弦承孟孤陕降限妹姑姐姓始驾参艰线练组细驶织终驻驼绍经贯" \
          "奏春帮珍玻毒型挂封持项垮挎城挠政赴赵挡挺括拴拾挑指垫挣挤拼挖按挥挪某甚革荐巷带草茧茶荒茫荡荣故胡南药" \
          "标枯柄栋相查柏柳柱柿栏树要咸威歪研砖厘厚砌砍面耐耍牵残殃轻鸦皆背战点临览竖省削尝是盼眨哄显哑冒映星昨" \
          "畏趴胃贵界虹虾蚁思蚂虽品咽骂哗咱响哈咬咳哪炭峡罚贱贴骨钞钟钢钥钩卸缸拜看矩怎牲选适秒香种秋科重复竿段" \
          "便俩贷顺修保促侮俭俗俘信皇泉鬼侵追俊盾待律很须叙剑逃食盆胆胜胞胖脉勉狭狮独狡狱狠贸怨急饶蚀饺饼弯将奖" \
          "哀亭亮度迹庭疮疯疫疤姿亲音帝施闻阀阁差养美姜叛送类迷前首逆总炼炸炮烂剃洁洪洒浇浊洞测洗活派洽染济洋洲" \
          "浑浓津恒恢恰恼恨举觉宣室宫宪突穿窃客冠语扁袄祖神祝误诱说诵垦退既屋昼费陡眉孩除险院娃姥姨姻娇怒架贺盈" \
          "勇怠柔垒绑绒结绕骄绘给络骆绝绞统耕耗艳泰珠班素蚕顽盏匪捞栽捕振载赶起盐捎捏埋捉捆捐损都哲逝捡换挽热恐" \
          "壶挨耻耽恭莲莫荷获晋恶真框桂档桐株桥桃格校核样根索哥速逗栗配翅辱唇夏础破原套逐烈殊顾轿较顿毙致柴桌虑" \
          "监紧党晒眠晓鸭晃晌晕蚊哨哭恩唤啊唉罢峰圆贼贿钱钳钻铁铃铅缺氧特牺造乘敌秤租积秧秩称秘透笔笑笋债借值倚" \
          "倾倒倘俱倡候俯倍倦健臭射躬息徒徐舰舱般航途拿爹爱颂翁脆脂胸胳脏胶脑狸狼逢留皱饿恋桨浆衰高席准座脊症病" \
          "疾疼疲效离唐资凉站剖竞部旁旅畜阅羞瓶兼烤烘烦烧烛烟递涛浙涝酒涉消浩海涂浴浮流润浪浸涨烫涌悟悄悔悦害宽" \
          "家宵宴宾窄容宰案请朗诸读扇袜袖袍被祥课谁调冤谅谈谊剥恳展弱陵陶陷陪娱娘通能难预桑绢绣验继球理捧堵描域" \
          "掩捷排掉堆推掀授教掏掠培接控探据掘职基著勒黄萌萝菌菜萄菊萍菠营械梦梢梅检梳梯副票戚爽聋袭盛雪辅辆虚雀" \
          "堂常匙晨睁眯眼悬野啦晚啄距跃略蛇累唱患唯崖崭崇圈铜铲银甜梨犁移笨笼笛符第敏做袋悠偿偶偷您售停偏假盘船" \
          "斜盒鸽悉欲彩领脚脖脸脱象够猜猪猎猫猛馅馆凑减毫麻痒痕廊康庸鹿盗章竟商族旋望率着盖粘粗粒断剪兽清添淋淹" \
          "渠渐混渔淘液淡深渗情惜惭悼惧惕惊惨惯寇寄宿窑密谋谎祸谜逮敢屠弹随蛋隆隐婚婶颈绩绪续骑绳维绵绸绿琴斑替" \
          "款堪搭塔越趁趋超提堤博揭喜插揪搜煮援搂搅握揉斯期欺联散惹葬葛董葡敬葱落朝辜葵棒棋植森椅椒棵棍棉棚棕惠" \
          "惑逼厨厦硬确雁殖裂雄暂雅辈悲紫辉敞赏掌晴暑最量喷晶喇遇喊跌跑遗蛙蛛蜓喝喂喘喉幅帽赌赔黑铸铺链销锁锄锅" \
          "锈锋锐短智毯鹅剩稍程稀税筐等筑策筛筒答筋筝傲傅牌堡集焦傍储奥街惩御循艇舒番释脾腔鲁猾猴然馋装蛮就痛童" \
          "阔善羡普粪尊道曾焰港湖渣湿温渴滑湾渡游滋溉愤慌惰愧愉慨割寒富窜窝窗遍裕裤裙谢谣谦属屡强粥疏隔隙絮缎缓" \
          "编骗缘瑞魂肆摄摸填搏塌鼓摆携搬摇搞塘摊蒜勤鹊蓝墓幕蓬蓄蒙蒸献禁楚想槐榆楼概赖酬感碍碑碎碰碗碌雷零雾雹" \
          "输督龄鉴睛睡睬鄙盟歇暗照跨跳跪路跟遣蛾蜂嗓置罪罩错锡锣锤锦键锯矮辞稠愁筹签简毁舅鼠催傻像躲微愈遥腰腥" \
          "腹腾腿触解酱痰廉新韵意粮数煎塑慈煤煌源滤滥滔溪溜滚滨粱滩慎誉塞谨福群殿辟障嫌嫁叠缝缠静碧璃墙撇嘉摧截" \
          "誓境摘摔聚蔽慕暮蔑模榴榜榨歌遭酷酿酸磁愿需弊裳颗嗽蜻蜡蝇锹锻舞稳算箩管僚鼻魄貌膜膊膀鲜疑馒裹敲豪膏遮" \
          "腐瘦辣竭端旗精歉熄熔漆漂漫滴演漏慢寨赛察蜜谱嫩翠熊凳骡缩慧撕撒趣趟撑播撞撤增蕉蔬横槽樱橡飘醋醉震霉瞒" \
          "题暴瞎影踢踏踩踪蝶蝴嘱墨镇靠稻黎稿稼箱箭篇僵躺僻德艘膝膛熟摩颜毅糊遵潜潮懂额慰劈操燕薯薪薄颠橘整餐嘴" \
          "蹄器赠默镜赞篮邀衡膨雕磨凝辨辩糖糕燃澡激懒壁避缴戴擦鞠藏霜霞瞧蹈螺穗繁辫赢糟糠燥臂翼骤鞭覆蹦镰翻鹰警" \
          "攀蹲颤瓣爆疆壤耀嚷籍魔灌蠢霸露料益拳粉剧屑桶救得衔婆梁裁搁景践禽腊嫂登愚暖满漠蜘赚聪鞋融醒躁嚼"
cn_punctuation = r"""。？！，、；：“”‘’『』「」（）[]〔〕【】——……·—-～《》〈〉___/"""


class BooleanM:
    @classmethod
    def boolean(cls, min_value=None, max_value=None, current=None):
        """
        生成一个布尔值。

        :param min_value: 最小值，默认为0。
        :param max_value: 最大值，默认为1。
        :param current: 当前值，默认为True。
        :return: 生成的布尔值。
        """
        _mock_exception.min_max_value_exception(min_value, max_value)
        if inNone((max_value, current)) and inNone(min_value) is False:
            # 如果只输入了min_value且max_value和current都为空，则返回True。
            return True
        min_value = 0 if inNone(min_value) else min_value
        max_value = 1 if inNone(max_value) else max_value
        current = True if inNone(current) else current
        luck_boolean_number = random.randint(min_value, max_value)
        if luck_boolean_number == min_value:
            return current
        else:
            return not current


m_boolean = BooleanM()


class NaturalM:
    @classmethod
    def natural(cls, min_value=None, max_value=None) -> int:
        """

        :param min_value: 最小值,默认值:0
        :param max_value: 最大值,默认值:9999999999999999
        :return: 自然数
        """
        if inNone(min_value):
            min_value = 0
        if inNone(max_value):
            max_value = 9999999999999999
        _mock_exception.min_max_value_exception(min_value, max_value)
        return random.randint(min_value, max_value)


m_natural = NaturalM()


class NumberM:
    number_str_max_length = None

    @classmethod
    def number_str(cls, min_length=None, max_length=number_str_max_length) -> str:
        """

        :param min_length:
        :param max_length:
        :return: 随机长度的数字字符
        """
        _mock_exception.min_max_value_exception(max_length, min_length)
        if inNone(min_length):
            min_length = random.randint(0, 15)
        if inNone(max_length):
            max_length = random.randint(min_length, 16)
        number_string_list = []
        range_size = cls.number_not_start_with_zero(min_length, max_length)
        for kk in range(range_size):
            number_string_list.append(str(random.randint(0, 9)))
        number_str = ''.join(number_string_list)
        return number_str

    @classmethod
    def number_not_start_with_zero(cls, start_number: int, end_number: int) -> int:
        """

        :param end_number: 随机数的最大值,包含
        :param start_number: 随机数的最小值,包含,默认=1
        :return: 从1开始的整数类型的随机数;[start_number,end_number] 取值范围为闭区间
        """
        return random.randint(start_number if start_number != 0 else 1, end_number if end_number != 1 else 2)


m_number = NumberM()


class IntegerM:
    @classmethod
    def integer(cls, min_value=None, max_value=None) -> int:
        """

        :param min_value: 最小值,默认值:0
        :param max_value: 最大值,默认值:9999999999999999
        :return: 自然数[min_value,max_value]
        """
        _mock_exception.min_max_value_exception(min_value, max_value)
        if inNone(min_value):
            min_value = -9999999999999999
        if inNone(max_value):
            max_value = 9999999999999999
        if min_value > max_value:
            raise MockPyExpressionException()
        return random.randint(min_value, max_value)


m_integer = IntegerM()


class CharacterM:
    @classmethod
    def character(cls, character_type=None):
        """
        生成一个随机字符

        :param character_type: 字符类型，默认为None
        :return: 生成的随机字符
        """
        character_type = random.choice(
            ('lower', 'upper', 'number', 'symbol')) if character_type is None else character_type
        return StringM.string(character_type, 1)


m_character = CharacterM()


class FloatM:
    @classmethod
    def float(cls, min_value=None, max_value=None, d_min_value=None,
              d_max_value=None):
        """
        生成一个随机浮点数。如果指定范围，将在该范围内生成。

        :param min_value: 整数部分最小值，如果未提供则不设置下限。
        :param max_value: 整数部分最大值，如果未提供则不设置上限。
        :param d_min_value: 小数部分最小位数，如果未提供，则随机选择0或2到5之间的一个数。
        :param d_max_value: 小数部分最大位数，如果未提供，则根据d_min_value随机确定上限。

        使用示例:
        - @float(95,100,12,19): 在95到100之间生成一个浮点数，小数部分位数在12到19之间。
        - @float(1,2): 在1到2之间生成一个浮点数，小数部分位数随机确定。
        - @float(952): 不小于952的浮点数，小数部分位数随机确定。
        - @float(): 完全随机生成一个浮点数。
        - @float: 与@float()相同，完全随机生成一个浮点数。

        :return: 生成的随机浮点数。
        """

        def __luck():
            # 随机决定是否执行某操作（3/4的概率为True）
            return random.randint(1, 4) in (1, 2, 3)

        # 校验最小值和最大值，抛出异常如果有必要（这里假设这个函数是已经实现的）
        _mock_exception.min_max_value_exception(min_value, max_value)

        # 设置默认整数部分最小值和最大值
        if inNone(min_value):
            min_value = -9999999999999999
        if inNone(max_value):
            max_value = 9999999999999999

        # 设置默认小数部分最小长度
        if inNone(d_min_value):
            d_min_value = random.randint(2, 5) if __luck() else 0

        # 设置默认小数部分最大长度
        if inNone(d_max_value):
            min_d_max_value = d_min_value if 14 > d_min_value > 0 else d_min_value + 1
            d_max_value = random.randint(min_d_max_value + 1, 16)

        # 生成随机小数部分字符串
        decimals = StringM.string_number(d_min_value, d_max_value)

        # 以3/4的概率执行以下代码块
        if __luck():
            while True:
                # 生成满足最小值和最大值的浮点数
                random_float = random.uniform(min_value, max_value)
                val = str(random_float)
                if '.' in val:
                    break
            int_part = val.split(".")[0]

            # 确保整数部分加上小数部分的长度不超过15位
            int_part = int_part if len(int_part) + len(decimals) <= 15 else int_part[:15 - len(decimals)]
            val = f'{int_part}.{decimals}'
            random_float = float(val)
        else:
            random_float = random.uniform(min_value, max_value)
            # 再次以3/4的概率执行以下代码块
            if __luck():
                # 保留随机浮点数的除最后一位外的所有数，并在最后追加一个新的随机整数(1-9)
                random_float = float(f'{str(random_float)[:-1]}{random.randint(1, 9)}')

        # 随机确定四舍五入的小数位数
        round_num = random.randint(d_min_value, d_max_value)
        return float(round(random_float, round_num))


m_float = FloatM()


class StringM:
    @classmethod
    def string_lower(cls, min_value=None, max_value=None) -> str:
        """
        :return: 随机小写英文字符
        """
        return cls.get_random_string_by_source(string.ascii_lowercase, min_value, max_value)

    @classmethod
    def get_random_string_by_source(cls, source=None, min_value: int = None, max_value: int = None) -> str:
        """
        获取随机字符串 根据给定的字符集
        :param source:
        :param min_value: 最小值（包含）
        :param max_value: 最大值（包含）
        :return:
        """
        _mock_exception.min_max_value_exception(min_value, max_value)
        if inNone(min_value):
            length = random.randint(1, 9)
        elif inNone(max_value):
            length = min_value
        else:
            length = random.randint(min_value, max_value)
        str_list = []
        for i in range(length):
            str_list.append(random.choice(source))
        random.shuffle(str_list)
        return tuple_to_str(str_list)

    @classmethod
    def string_upper(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机大写英文字符
        """
        return cls.get_random_string_by_source(string.ascii_uppercase, min_value, max_value)

    @classmethod
    def string_number(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机长度数字字符
        """
        return cls.get_random_string_by_source(string.digits, min_value, max_value)

    @classmethod
    def string_symbol(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机标点符号字符
        """
        return cls.get_random_string_by_source(string.punctuation, min_value, max_value)

    @classmethod
    def strings(cls, min_value=None, max_value=None) -> str:
        """

        :return: 包含(英文/英文标点/数字)的随机长度的字符
        """
        source = string.ascii_letters + string.digits + string.punctuation
        return cls.get_random_string_by_source(source, min_value, max_value)

    @classmethod
    def chinese(cls, min_value=None, max_value=None) -> str:
        """

        :return: 纯中文随机字符
        """
        if inNone(min_value):
            min_value = 1
        return cls.get_random_string_by_source(chinese, min_value, max_value)

    @classmethod
    def english(cls, min_value=None, max_value=None) -> str:
        """

        :return: 纯英文随机字符
        """
        if inNone(min_value):
            min_value = 1
        source = string.ascii_letters
        return cls.get_random_string_by_source(source, min_value, max_value)

    @classmethod
    def cn_symbol(cls, min_value=None, max_value=None) -> str:
        """

        :return: 随机中文标点符号
        """
        return cls.get_random_string_by_source(cn_punctuation, min_value, max_value)

    @classmethod
    def cn_string(cls, min_value=None, max_value=None) -> str:
        """
        生成随机的中文标点符号字符

        :param min_value: 最小值，默认为None
        :param max_value: 最大值，默认为None
        :return: 随机标点符号字符
        """

        def __cn_sting():
            """
            生成随机的中文字符和标点符号字符的组合

            :return: 随机标点符号字符
            """
            cn_min_value = random.randint(1, max_value - 1)
            cn_str = cls.get_random_string_by_source(chinese, cn_min_value)
            cn_symbol = cls.cn_symbol(max_value - cn_min_value)
            cn_strings = list(cn_str + cn_symbol)
            random.shuffle(cn_strings)
            return tuple_to_str(cn_strings)

        if min_value >= 2 and inNone(max_value):
            max_value = min_value
            return __cn_sting()
        elif inNone(max_value) or min_value == 1:
            return cls.get_random_string_by_source(cn_punctuation + chinese, min_value, max_value)
        else:
            return __cn_sting()

    @classmethod
    def string(cls, *args) -> str:
        """

        :param args: 参数,例如:返回字符的长度
        :return: 随机长度的英/数/英文标点符号的混合字符
        """
        if len(args) <= 1 or isinstance(args[0], int):
            return cls.strings(*args)
        elif 3 >= len(args) >= 2:
            string_type = args[0]
            new_args = args[1:]
            if string_type == 'lower':
                return cls.string_lower(*new_args)
            elif string_type == 'upper':
                return cls.string_upper(*new_args)
            elif string_type == 'number':
                return cls.string_number(*new_args)
            elif string_type == 'symbol':
                return cls.string_symbol(*new_args)
            elif string_type == 'string':
                return cls.strings(*new_args)
            elif string_type == 'chinese':
                return cls.chinese(*new_args)
            elif string_type == 'english':
                return cls.english(*new_args)
            elif string_type == 'cn_symbol':
                return cls.cn_symbol(*new_args)
            elif string_type == 'cn_string':
                return cls.cn_string(*new_args)
            else:
                return cls.get_random_string_by_source(string_type, *new_args)
        elif len(args) > 3:
            raise MockPyExpressionException('only 3 parameters are allowed.')


m_string = StringM()


class DateM:
    @classmethod
    def datetime_calculate(cls, date_time, time_interval, format_str=None):
        """

        :param date_time: 需要计算的日期时间
        :param time_interval: 时间的计算量,例如:'+1min'
        :param format_str: 时间的格式
        :return:
        """
        # 定义初始化变量
        days = 0
        seconds = 0
        microseconds = 0
        milliseconds = 0
        minutes = 0
        hours = 0
        calculate = time_interval[:1]
        # 正则获取时间单位
        regular = '[a-zA-Z]+'  # 正则匹配英文
        match = re.search(regular, time_interval)
        group = match.group(0)
        # 时间的单位:天/月/年
        unit = group
        # 时间的计算量
        amount = int(time_interval[1:-len(unit)])
        # 处理时间的量
        if 'hours'.startswith(unit):
            hours = amount
        elif 'minutes'.startswith(unit):
            minutes = amount
        elif 'milliseconds'.startswith(unit):
            milliseconds = amount
        elif 'microseconds'.startswith(unit):
            microseconds = amount
        elif 'seconds'.startswith(unit):
            seconds = amount
        elif 'days'.startswith(unit):
            days = amount
        elif 'month'.startswith(unit):
            month = amount
            data_result = (date_time + relativedelta(months=month)).strftime(format_str)
            return data_result
        elif 'week'.startswith(unit):
            data_result = (date_time + relativedelta(weeks=amount)).strftime(format_str)
            return data_result
        timedelta_value = timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                    milliseconds=milliseconds, minutes=minutes, hours=hours)
        if calculate == '+':
            data_result = (date_time + timedelta_value).strftime(format_str)
            return data_result
        elif calculate == '-':
            data_result = (date_time - timedelta_value).strftime(format_str)
            return data_result

    @classmethod
    def datetime(cls, format_str=None, time_interval: str = None):
        """
        日期时间的装饰器函数，用于生成指定格式的日期时间字符串。

        Args:
            format_str (str, optional): 指定日期时间的格式，默认为 '%Y-%m-%d %H:%M:%S'。
            time_interval (str, optional): 时间间隔的表达式，默认为 None。可以是正数或负数，如 '+1min' 或 '-1mil'。

        Returns:
            str: 生成的日期时间字符串。

        Raises:
            MockPyExpressionException: 如果 time_interval 不满足表达式要求，抛出异常。

        Examples:
            @date('%Y-%m-%d %H:%M:%S')  2022-12-09 16:50:00
            @date('%Y-%m-%d %H:%M:%S','-1')  2022-12-08 16:50:00
            @date('%Y-%m-%d %H-%M-%S')
            @date()
        """
        # 判断是否满足表达式
        if not inNone(time_interval) and (len(time_interval) <= 1 or time_interval[:1] not in ('+', '-')):
            raise MockPyExpressionException(remark="The correct expression for time:'+1h' or '-1h'.")
        # 当前时间
        curr_time = datetime.now()
        today = curr_time.strftime(format_str)
        # 处理时间的计算
        if not inNone(time_interval):
            return cls.datetime_calculate(curr_time, time_interval, format_str)
        else:
            return today

    @classmethod
    def date(cls, format_str=None, time_interval: str = None):
        """
        example:
        @date('%Y-%m-%d')  2022-12-09
        @date('%Y-%m-%d','-1')  2022-12-08
        @date()
        可以传参'%Y-%m-%d %H:%M:%S'
        :param format_str:'%Y-%m-%d';'%Y:%m:%d'/'%Y-%m-%d %H:%M:%S'
        :param time_interval: 加或减
        :return: 随机日期(年月日/年月日时分秒),默认:2023-02-27
        """
        format_str = '%Y-%m-%d' if inNone(format_str) else format_str
        return cls.datetime(format_str, time_interval)

    @classmethod
    def timestamp(cls):
        """
        生成当前时间戳。

        该方法返回一个表示当前时间的UNIX时间戳。
        返回的时间戳是一个整数，代表自1970年1月1日（UTC）以来经过的毫秒数。

        :return: 当前时间的UNIX时间戳（毫秒级整数形式）。
        """
        # 获取当前时间
        now = datetime.now()
        # 将当前时间转换为毫秒级的时间戳，并转换为整数后返回
        return int(now.timestamp() * 1000)

    @classmethod
    def time(cls, format_str=None, time_interval: str = None):
        """
        example:
        @time('%Y-%m-%d')  15:03:49
        @time('%Y-%m-%d','-1')  2022-12-08
        @time()
        可以传参'%Y-%m-%d %H:%M:%S'
        :param time_interval: 加或减
        :param format_str:'%H:%M:%S'/'%Y:%m:%d';'%Y-%m-%d %H:%M:%S'
        :return: 随机日期(时分秒/年月日时分秒),默认:21:43:47
        """
        format_str = '%H:%M:%S' if inNone(format_str) else format_str
        return cls.datetime(format_str, time_interval=time_interval)

    @staticmethod
    def get_current_week(date=None, format_str='%Y-%m-%d'):
        """

        :param format_str:
        :param date: "2023-02-19",默认当前日期
        :return: 指定日期所在周的的元祖:(周一的日期,周日的日期)
        """
        if date:
            duty_date = datetime.strptime(str(date), format_str)
            monday, sunday = duty_date, duty_date
        else:
            monday, sunday = datetime.today(), datetime.today()
        one_day = timedelta(days=1)
        while monday.weekday() != 0:
            monday -= one_day
        while sunday.weekday() != 6:
            sunday += one_day
        # return monday, sunday
        # 返回时间字符串
        return datetime.strftime(monday, format_str), datetime.strftime(sunday, format_str)

    @classmethod
    def now(cls, unit: str = None, format_str='%Y-%m-%d %H:%M:%S'):
        """

        :param unit: 日期单位
        :param format_str: 
        :return: 当前时间:2023-02-27 21:43:47
        """
        default_format_str = '%Y-%m-%d %H:%M:%S'
        now = cls.date(format_str='%Y') + '-01-01 00:00:00'
        if unit == 'year':
            return datetime.strptime(now, default_format_str).strftime(format_str)
        elif unit == 'month':
            return datetime.strptime(cls.date(format_str='%Y-%m') + '-01 00:00:00', default_format_str).strftime(
                format_str)
        elif unit == 'week':
            # 当前日期的周日所在的日期
            return datetime.strptime(cls.get_current_week()[1] + ' 00:00:00', default_format_str).strftime(format_str)
        elif unit == 'day':
            return datetime.strptime(cls.date(format_str='%Y-%m-%d') + ' 00:00:00', default_format_str).strftime(
                format_str)
        elif unit == 'hour':
            return datetime.strptime(cls.date(format_str='%Y-%m-%d  %H') + ':00:00', default_format_str).strftime(
                format_str)
        elif unit == 'minute':
            return datetime.strptime(cls.date(format_str='%Y-%m-%d  %H:%M') + ':00', default_format_str).strftime(
                format_str)
        elif unit == 'second':
            return cls.datetime(format_str=format_str)
        elif unit is None:
            return cls.datetime(format_str=format_str)


m_date = DateM()


class HelperM:

    @classmethod
    def pick(cls, pick_list):
        """
        选择集合数据中的一个
        :param pick_list: 字符串/列表/元祖
        :return: 选择的元素
        """
        if inNone(pick_list):
            raise MockPyExpressionException('pick_list cannot be empty.')
        assert isinstance(pick_list, (str, list, tuple))
        if isinstance(pick_list, str):
            pick_list = eval(pick_list)
        return random.choice(pick_list)


m_helper = HelperM()


class NameM:
    """
    生成随机姓名
    """

    @classmethod
    def first(cls):
        """

        :return: 获取英文名的第一个单词-姓
        """
        return random.choice(en_family_name)

    @classmethod
    def last(cls):
        """

        :return: 获取英文名的最后一个单词-名
        """
        return random.choice(en_name)

    @classmethod
    def name(cls, middle=None):
        """
        返回英文名

        :param middle: 是否包含中间名（exp:Thomas Mary Martin），默认为None
        :return: 英文名
        """
        if middle is not None and middle in ('true', 'True', True, '1', 1):
            a = cls.first()  # 获取姓氏
            c = cls.last()  # 获取姓氏
            b = None
            for i in range(20):
                b = cls.first()  # 获取中间名
                if cls.first() != a:
                    break
            return f'{a} {b} {c}'  # 返回姓氏、中间名和姓氏
        return f'{cls.first()} {cls.last()}'

    @classmethod
    def cfirst(cls, length=None):
        """

        :return: 随机生成一个常见的中文名
        """
        length = random.randint(1, 3) if length is None else length
        if 3 <= length <= 1:
            raise MockPyExpressionException(length)
        return m_string.chinese(length, length + 1)[:length]

    @classmethod
    def clast(cls):
        """

        :return: 随机生成一个常见的中文姓
        """
        return random.choice(single_family_name)

    @classmethod
    def cname(cls, length=None):
        """
        生成中文姓氏

        :param length: 姓氏长度，可选参数，默认为None
        :return: 中文姓氏
        """
        length = random.randint(2, 3) if length is None else length
        if 3 <= length <= 2:
            raise MockPyExpressionException(length)
        cname = cls.clast() + cls.cfirst(length - 1)
        # assert not '\n' in cname
        return cname


m_name = NameM()


class MiscellaneousM:
    """
    杂项
    """

    @classmethod
    def uuid(cls):
        """
        生成随机的UUID
        :return: UUID
        """
        return str(uuid.uuid4())

    @classmethod
    def id(cls):
        """
        生成随机的身份证号
        :return: 身份证号
        """
        return cls.generate_random_id()

    increment_start = 0

    @classmethod
    def increment(cls, step=None):
        """
        自增函数,默认自增起始值为0
        :param step: 步长
        :return: 自增后的值
        """
        if step is None:
            step = 1
        cls.increment_start += step
        return f"{cls.increment_start}"

    @classmethod
    def get_random_date(cls, start_year=1960, end_year=2020):
        """生成随机出生日期"""
        import datetime
        start = datetime.date(start_year, 1, 1)
        end = datetime.date(end_year, 12, 31)
        days_between = (end - start).days
        random_days = random.randrange(days_between)
        birth_date = start + datetime.timedelta(days=random_days)
        return birth_date.strftime("%Y%m%d")

    @classmethod
    def calculate_checksum(cls, id17):
        """计算身份证最后的校验码"""
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        checksums = '10X98765432'
        sum_product = sum(int(id17[i]) * weights[i] for i in range(17))
        return checksums[sum_product % 11]

    @classmethod
    def generate_random_id(cls):
        """生成随机的中国身份证号码"""
        # 随机地址码（简化处理，实际应为有效地址码）
        region_code = str(random.randint(100000, 699999))
        # 随机生成出生日期码
        birth_date = cls.get_random_date()
        # 随机生成顺序码（性别码偶数女，奇数男）
        sequence_code = str(random.randint(000, 999)).zfill(3)
        # 组成前17位
        id17 = region_code + birth_date + sequence_code
        # 计算校验码
        checksum = cls.calculate_checksum(id17)
        # 完整的身份证号码
        return f"{id17}{checksum}"


m_miscellaneous = MiscellaneousM()


class TextM:
    """
    文本相关
    """

    @classmethod
    def paragraph(cls, min_sentences=3, max_sentences=10):
        """
        生成一段随机的英文文本，默认3-10句
        :param min_sentences: 最小句数
        :param max_sentences: 最大句数
        :return: 英文文本
        """
        num = random.randint(min_sentences, max_sentences)
        pick_list = [',', '!', '?']
        result = f"{''.join([f'{m_string.english(1, 10)[:-1]}{m_helper.pick(pick_list)}' for _ in range(num)])}"
        return f"{result[:-1]}."

    @classmethod
    def cparagraph(cls, min_sentences=3, max_sentences=10):
        """
        :param min_sentences: 最小句数
        :param max_sentences: 最大句数
        :return: 中文文本
        """
        num = random.randint(min_sentences, max_sentences)
        pick_list = ['，', '！', '？']
        result = f"{''.join([f'{m_string.chinese(1, 10)[:-1]}{m_helper.pick(pick_list)}' for _ in range(num)])}"
        return f"{result[:-1]}。"

    @classmethod
    def sentence(cls, min_words=3, max_words=10):
        """
        生成一句随机的英文文本，默认3-10个词
        :param min_words: 最小词数
        :param max_words: 最大词数
        :return: 英文文本
        """
        return m_string.english(min_words, max_words) + '.'

    @classmethod
    def csentence(cls, min_words=3, max_words=10):
        """
        生成一句随机的中文文本，默认3-10个词
        :param min_words: 最小词数
        :param max_words: 最大词数
        :return: 中文文本
        """
        return m_string.chinese(min_words, max_words) + '。'

    @classmethod
    def mix_sentence(cls, min_words=1, max_words=10):
        """
        生成一句随机的英文和中文文本和数组混合的文本，默认3-10个词
        :param min_words: 最小词数   英文文本
        :param max_words: 最大词数   英文文本
        :return: 英文/中文文本
        """
        result = (f"{cls.sentence(min_words, max_words)}{cls.csentence(min_words, max_words)}"
                  f"{m_string.string_number(min_words, max_words)}")
        return shuffle_string(result)


m_text = TextM()
