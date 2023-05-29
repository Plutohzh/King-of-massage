import random

names=["青眼白龙", "兰斯", "川普", "欧贝利斯克的巨神兵", "雄火龙", "威斯克", "沸羊羊", "田所浩二", "压缩毛巾", "初音未来", "小圆", "魔法少女奈叶", "有脸的西瓜", "博丽灵梦", "ChatGPT", "赛利亚", "叶赫那拉", "玛丽萝丝", "终结者", "霸天虎", "避难所小子", "司马睿", "施瓦辛格", "史蒂夫", "金闪闪", "凉宫春日", "成步堂龙一", "杀手皇后", "古达", "巨龙传说", "滴嘟侠", "天崎奈奈", "正交矩阵", "自由使徒", "莱拉", "在原七海", "虎式坦克"]

c_names=["富可敌国流浪汉","童心未泯中年大叔","身强体壮老爷子","捡垃圾吃的贵族","踩单车的资本家","商科专业的下头男","睡眼朦胧的大学生","转生的史莱姆","浑身喷香水的僵尸","喜欢打牌的法老王","正派人物哥布林","路过的冥王星人"]

class worker:
    def __init__(self, name, age, beauty, skill, spirit, traits, exp):
        self.name = name
        self.age = age
        self.beauty = beauty
        self.skill = skill
        self.spirit = spirit
        self.traits = traits
        self.exp = exp
    def reduce_spirit(self, amount):
        # 减少该技师的精神值（工作意愿）
        self.spirit -= amount
    def reduce_beauty(self, amount):
        self.beauty -= amount
    def add_exp(self, amount):
        self.exp += amount


    def __repr__(self):
        return f"{self.name}, 容貌:{self.beauty}, 技巧:{self.skill}, 精神:{self.spirit}, 特质:{self.traits}, 服务经验:{self.exp}"

class Customer:
    def __init__(self, name, money, preference):
        self.name = name
        self.money = money
        self.preference = preference

    def __repr__(self):
        return f"{self.name}, 持有金: {self.money}, 偏好: {self.preference}"


class massage:
    def __init__(self, name, funds, workers, reputation):
        self.name = name
        self.funds = funds
        self.workers = workers
        self.reputation = reputation
    
    def check_info(self):
        print(f"按摩店名称:{self.name}")
        print(f"资金: {self.funds}")
        print(f"声誉: {self.reputation}")
        print("技师:")
        for worker in self.workers:
            print(f"\t姓名: {worker.name}")
            print(f"\t年龄: {worker.age}")
            print(f"\t容貌: {worker.beauty}")
            print(f"\t技巧: {worker.skill}")
            print(f"\t精神: {worker.spirit}")
            print(f"\t特质: {worker.traits}")
            print(f"\t经验: {worker.exp}")
            print("")
    
    def care_workers(self):
        cost = random.randint(500,1000)*len(self.workers)
        if self.funds < cost:
            print("钱不够！")
            return
        if self.workers == []:
            print("没有技师！")
            return
        for worker in self.workers:
            improvement1 = random.randint(1, 20)
            improvement2 = random.randint(1, 20)
            improvement3 = random.randint(1, 20)
            worker.beauty += improvement1
            worker.skill += improvement2
            worker.spirit += improvement3
        self.funds -= cost
        print("已经培训了技师们，狠狠地搞企业文化，带他们在操场上跑了一百圈，然后在大厅喊口号跺脚......")
    
    def fire_worker(self):
        fire_worker = input("输入你要解雇技师的姓名：")
        for worker in self.workers:
            if worker.name == fire_worker:
                lose_workers.append(worker)
                self.workers.remove(worker)
                print(f"{fire_worker} 被打晕，连带着他的桶一起被扔出窗外，有望引发三十年战争。")
                return
        print(f"没有{fire_worker}这个人。")
    
    def p_hire_worker(self):
        cost = random.randint(100,500)
        self.funds -= cost
        if self.funds < cost:
            print("你的HR把工资吹得太高，来面试的一问知道入职第一年没有工资，直接提桶跑路了。")
            return
        name = input("你的HR终于骗来一个冤种，现在你可以给这个技师取个名字：")
        age = random.randint(16, 30)
        beauty = random.randint(50, 90)
        skill = random.randint(50, 90)
        spirit = random.randint(50, 90)
        trait1, trait2, trait3 = random.sample(["大力王", "能唠嗑", "打拍子", "懂针灸", "会拔罐", "爱哼歌"], k=3)
        exp = 0
        new_worker = worker(name, age, beauty, skill, spirit, [trait1, trait2, trait3], exp)
        self.workers.append(new_worker)
        print(f"{name}被哄着骗着成为了按摩店的一份子，你准备让他体验体验社会的毒打。")

    def hire_worker(self):
        cost = random.randint(100,500)
        self.funds -= cost
        name = random.choice(names)
        age = random.randint(16, 30)
        beauty = random.randint(50, 90)
        skill = random.randint(50, 90)
        spirit = random.randint(50, 90)
        trait1, trait2, trait3 = random.sample(["大力王", "能唠嗑", "打拍子", "懂针灸", "会拔罐", "爱哼歌"], k=3)
        exp = 0
        new_worker = worker(name, age, beauty, skill, spirit, [trait1, trait2, trait3], exp)
        self.workers.append(new_worker)
        print(f"{name}成为了其它按摩店的一份子。")
    
    def steal_worker(self):
        other_massage_workers = massage1.workers+massage2.workers+massage3.workers
        if not other_massage_workers:
            print("其它按摩店没有人了。你的专业绑匪们扑了个空。")
            return
        stolen_worker = random.choice(other_massage_workers)
        if stolen_worker in massage1.workers:
            massage1.workers.remove(stolen_worker)
        if stolen_worker in massage2.workers:
            massage2.workers.remove(stolen_worker)
        if stolen_worker in massage3.workers:
            massage3.workers.remove(stolen_worker)

        self.workers.append(stolen_worker)
        self.reputation -= 10
        print(f"你挖角了一名其它按摩店的技师{stolen_worker.name}。那个按摩店暴跳如雷，现在逢人就骂你。")

    def o_steal_worker(self):
        if not massage0.workers:
            print(f"{massage0.name}现在一个人都没有。其他按摩店的绑匪抢了个寂寞。")
            return
        stolen_worker = random.choice(massage0.workers)
        massage0.workers.remove(stolen_worker)
        self.workers.append(stolen_worker)    
        print(f"该死的！{self.name}把我们的{stolen_worker.name}挖走了！")
    
    def add_funds(self, amount):
        """
        给massage增加资金
        """
        self.funds += amount
    
    def __repr__(self):
        return f"按摩店名称： {self.name}, 有{len(self.workers)}个技师, 资金{self.funds}，名誉{self.reputaion}"
    
# 实例化三个massage并添加技工 worker(name, age, beauty, skill, spirit, traits, exp),massage(name, funds, workers, reputation)
broname = input("输入你按摩店的名称:")
massage0 = massage(broname, 3000, [], 10)
massage1 = massage("正宗盲人推拿店", 30000, [worker("可达鸭", 21, 90, 60, 50, ["大力王","能唠嗑","懂针灸"], 0), worker("纳米机器", 20, 70, 60, 50, ["大力王","能唠嗑"], 0)], 500)
massage2 = massage("正经兽人按摩馆", 20000, [worker("胖虎", 19, 60, 80, 85, ["大力王","懂针灸"], 0), worker("季伯常", 24, 70, 80, 60, ["能唠嗑","懂针灸"], 0)],400)
massage3 = massage("霸道总裁按摩店", 10000, [worker("阎魔刀", 16, 85, 70, 60, ["大力王","懂针灸"], 0), worker("马骑马", 25, 80, 50, 60, ["能唠嗑","懂针灸"], 0)],300)
massages = [massage1, massage2, massage3]
lose_workers = []  # 用于储存临时失踪的技师
                                       
# 定义夜晚事件
def night_event():
    print("夜幕降临，准备开工！\n")

    # 如果其它店没人了就各进一个。
    if massage1.workers==[] or massage2.workers==[] or massage3.workers==[]:
        massage1.hire_worker()
        massage2.hire_worker()
        massage3.hire_worker()


    ## 随机事件
    # 招工事件
    c = random.randint(0,20)
    if c==1:
        massage1.hire_worker()
    elif c==2:
        massage2.hire_worker()
    elif c==3:
        massage3.hire_worker()
        
    # 绑架事件
    c = random.randint(0,25)
    if c==1:
        massage1.o_steal_worker()
    elif c==2:
        massage2.o_steal_worker()
    elif c==3:
        massage3.o_steal_worker()
    # 盗窃事件
    c = random.randint(0,20)
    if c==1:
        print("有小偷！你柜台里的钱不见了！你发出了蟹老板的声音。")
        massage0.add_funds(int((-1)*massage0.funds/(random.randint(6,12))))
    # 袭击事件
    c = random.randint(0,15)
    if c==1:
        attacked_worker = random.choice(massage0.workers)
        print(f"{attacked_worker.name}被袭击了！他吓了一跳发动忍术，当场后空翻三圈，可惜脸部着地。")
        attacked_worker.reduce_spirit(random.randint(1,5))
        attacked_worker.reduce_beauty(random.randint(1,5))
    # 冲突事件
    c = random.randint(0,15)
    if c==1:
        print("楼上居民楼住着的人骂你们技师一边按摩一边唱歌声音太大，你骂他吼那么大声干什么，结果附近居民都打开窗户开始骂你，你的声誉降低了。")
        massage0.reputation -= random.randint(1,5)
    # 搬家事件
    c = random.randint(0,20)
    if c==1:
        print("你被举报没有营业执照，不得不拖家带口把按摩店换到街里另外一个巷子里，花了很多钱。")
        massage0.funds -= random.randint(100,500)*len(massage0.workers)
    # 白嫖事件
    c = random.randint(0,25)
    if c==1:
        print("该死！隔壁街臭名昭著的一伙白嫖怪来了！他们把五星上将保安大队长打晕，要挟技师们免费服务，还抢了钱走！")
        massage0.funds -= random.randint(300,1000)*len(massage0.workers)
        for worker in massage0.workers:
            worker.exp += random.randint(0,5)
    # 献祭事件
    c = random.randint(0,20)
    if c==1:
        num = random.randint(5,30)
        givemoney = num*random.randint(100,1000)
        print(f"今夜有一个网上订单：可以派遣一名技师上门服务{num}个人，有概率获得大量收入，但是风险不确定。")
        g = input("输入1同意，输入2不同意")
        if g == "1":
            h = eval(input("选择你要派遣的技师（按照加入按摩店的时间顺序输入整数，0代表倒数第一个）: "))-1
            try:
                given_worker = massage0.workers[h]
                print(f"你选择了{given_worker.name}")
                j = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
                if j == 1 or j == 5:
                    print(f"该死的！这帮人付了{givemoney}的定金之后就没影了，{given_worker.name}可能被带去缅北噶腰子了！")
                    given_worker.exp += random.randint(50,100)
                    given_worker.spirit *= 0
                    lose_workers.append(given_worker)
                    massage0.workers.remove(given_worker)
                    massage0.funds += givemoney
                elif j == 2:
                    print(f"该死的！这帮王八蛋不仅不付钱，竟敢把{given_worker.name}送去种植园摘棉花！")
                    massage0.workers.remove(given_worker)
                    massage0.reputation -= random.randint(3,8)
                elif j == 3 or j == 6:
                    print(f"{given_worker.name}给这群人按摩之后，居然变帅了许多？你不管这些，你把{givemoney}的钱收入口袋。")
                    massage0.funds += givemoney
                    given_worker.exp += random.randint(30,50)
                    given_worker.skill += 20
                    given_worker.beauty += 20
                else:
                    print(f"{given_worker.name}给{num}个人连续按摩之后差点累死，最终决定开始摆烂。但是你的腰包里多了{givemoney}。")
                    massage0.funds += givemoney
                    given_worker.exp += random.randint(30,50)
                    given_worker.spirit *= 0

            except:
                print("查无此人！视作放弃机会。")

        else:
            print("你无视了这次机会。")


    ## 上钟事件
    customer = Customer(random.choice(c_names), random.randint(50, 200), random.choice(["大力王", "能唠嗑", "打拍子", "懂针灸", "会拔罐", "爱哼歌"]))#改为列表，增加for循环可以生成多个
    print("\n今夜顾客:")
    print(customer)  # 如果生成多个，以下代码需要重复运行几次，并且考虑是否要避免重复派遣同一个人
    for massage in massages:
        try:
            worker = random.choice(massage.workers)
        except:
            print("某家按摩店没有人了")
        o_chosen_worker = []
        o_chosen_worker.append(worker)
        print(f"{massage.name} 派遣了 {worker.name}.")
    a = eval(input("选择你要派遣的技师（按照加入按摩店的时间顺序输入整数，0代表倒数第一个）: "))-1
    try:
        p_chosen_worker = massage0.workers[a]
        print(f"你选择了{p_chosen_worker.name}")
        o_chosen_worker.append(p_chosen_worker)
        max_beauty_worker = o_chosen_worker[0]
        for worker in o_chosen_worker[1:]:
            if worker.beauty > max_beauty_worker.beauty:
                max_beauty_worker = worker
    except:
        print("查无此人！视作不派遣。")
        max_beauty_worker = o_chosen_worker[0]
        for worker in o_chosen_worker[1:]:
            if worker.beauty > max_beauty_worker.beauty:
                max_beauty_worker = worker

    if max_beauty_worker in massage0.workers:
        massage0.add_funds(worker.skill + customer.money)
        worker.reduce_spirit(10)
        worker.reduce_beauty(10)
        worker.add_exp(1)
        print(f"{max_beauty_worker.name}被顾客选中了")
        if customer.preference in max_beauty_worker.traits:
            print(f"顾客很喜欢{max_beauty_worker.name}的{customer.preference},多给了一些小费。")
            massage0.add_funds(customer.money*2)
            massage0.reputation += 5
        massage0.reputation += 5
        income = customer.money*3 + worker.skill
        print(f"今日收入：{income}\n")
    elif max_beauty_worker in massage1.workers:
        massage1.add_funds(worker.skill + customer.money)
        worker.reduce_spirit(10)
        worker.reduce_beauty(10)
        worker.add_exp(1)
        print(f"{max_beauty_worker.name}被顾客选中了")
        if customer.preference in max_beauty_worker.traits:
            print(f"顾客很喜欢{max_beauty_worker.name}的{customer.preference},多给了一些小费。")
            massage1.add_funds(customer.money*2)
            massage1.reputation += 5
        massage1.reputation += 5
    elif max_beauty_worker in massage2.workers:
        massage2.add_funds(worker.skill + customer.money)
        worker.reduce_spirit(10)
        worker.reduce_beauty(10)
        worker.add_exp(1)
        print(f"{max_beauty_worker.name}被顾客选中了")
        if customer.preference in max_beauty_worker.traits:
            print(f"顾客很喜欢{max_beauty_worker.name}的{customer.preference},多给了一些小费。")
            massage2.add_funds(customer.money*2)
            massage2.reputation += 5
        massage2.reputation += 5
    elif max_beauty_worker in massage3.workers:
        massage3.add_funds(worker.skill + customer.money)
        worker.reduce_spirit(10)
        worker.reduce_beauty(10)
        worker.add_exp(1)
        print(f"{max_beauty_worker.name}被顾客选中了")
        if customer.preference in max_beauty_worker.traits:
            print(f"顾客很喜欢{max_beauty_worker.name}的{customer.preference},多给了一些小费。")
            massage3.add_funds(customer.money*2)
            massage3.reputation += 5
        massage3.reputation += 5
    e = random.choice([1,2,3,4,5,6])
    if e == 1:
        print(f"{max_beauty_worker.name}逮着客人的脑壳一阵猛晃，差点把脑浆都给干出来了。\n{customer.name}意识模糊地付了钱，然后一瘸一拐地走出了按摩店。")
    elif e == 2:
        print(f"{max_beauty_worker.name}把客人全身上下的骨头按得发响。\n{customer.name}当时觉得爽，结果发现发响是因为骨头被折断了。\n现在他床都下不了，你把他的钱包拿走，然后把他丢到街上。")
    elif e == 3:
        print(f"{customer.name}有点小紧张，{max_beauty_worker.name}说不怕不怕，\n叫店里的麻醉师泰森过来一拳直冲面门，把他干睡着了。紧张不了一点。")
    elif e == 4:
        print(f"{customer.name}这两天有点受凉，{max_beauty_worker.name}表示按两下就能给他按好。\n{max_beauty_worker.name}拿起店里的铁锤对着客人的屁股梆梆几锤，直接给消化道吓得半个月不敢蠕动。")
    elif e == 5:
        print(f"按着按着，{max_beauty_worker.name}发现{customer.name}脑子里长了块恶性肿瘤。\n还好{max_beauty_worker.name}技术高超，一发波动拳接升龙拳，把肿瘤打的稀碎。")
    elif e == 6 and (max_beauty_worker in massage0.workers):
        money = random.randint(1000,5000) + max_beauty_worker.skill + max_beauty_worker.beauty
        print(f"{customer.name}体验过{max_beauty_worker.name}的按摩之后，愿意花费{money}雇他当私人技师，每天都给自己按摩。你是否同意？")
        f = input("1.同意；2.不同意")
        if f == "1":
            print(f"你同意了{customer.name}的请求，将{max_beauty_worker.name}以{money}的价钱卖给了他。")
            massage0.add_funds(money)
            lose_workers.append(max_beauty_worker)
            massage0.workers.remove(max_beauty_worker)
        else:
            print(f"你没有同意{customer.name}的请求，他离开后称自己的性别是武装直升机旋翼上的沃尔玛购物袋，\n跟逼逼C和C嗯嗯记者说你们按摩店歧视他，你遭到了口诛笔伐。")
            massage0.reputation -= random.randint(1,5)
    else:
        print(f"{max_beauty_worker.name}手艺太好，直接把客人按爽死了。\n还好{customer.name}是体育生，一个鲤鱼打挺把孟婆汤打翻，然后一个滑铲撂倒黑白无常，返回阳间。")
            
    print("\n啊，又是激情的一夜！\n")

    # 精神过低
    for worker in (massage0.workers and massage1.workers and massage2.workers and massage3.workers):
        if worker.spirit <= 0:
            print(f"{worker.name}天天加班天天996，累个半死，现在他直接开摆，问啥都说啊对对对。")
            worker.beauty *= 0
            worker.skill *= 0
            worker.spirit *= 0
    # 交维护费
    print("\n街上的各家按摩店都需要缴纳保护费、租金、维护费，以及技师们的工资。")
    dcost0 = random.randint(50,100)*len(massage0.workers) + 200
    dcost1 = random.randint(50,100)*len(massage1.workers) + 200
    dcost2 = random.randint(50,100)*len(massage2.workers) + 200
    dcost3 = random.randint(50,100)*len(massage3.workers) + 200
    massage0.funds -= dcost0
    massage1.funds -= dcost1
    massage2.funds -= dcost2
    massage3.funds -= dcost3
    print(f"{massage0.name}花费了{dcost0}。")
    print(f"{massage1.name}花费了{dcost1}。")
    print(f"{massage2.name}花费了{dcost2}。")
    print(f"{massage3.name}花费了{dcost3}。")
    
    # 资金过少
    if massage0.funds < 0:
        print(f"{massage0.name}的资金不够了，付不起保护费与租金。在这条街上的名誉严重下降。")
        massage0.reputation -= random.randint(5,15)
    if massage1.funds < 0:
        print(f"{massage1.name}的资金不够了，付不起保护费与租金。在这条街上的名誉严重下降。")
        massage1.reputation -= random.randint(5,15)
    if massage2.funds < 0:
        print(f"{massage2.name}的资金不够了，付不起保护费与租金。在这条街上的名誉严重下降。")
        massage2.reputation -= random.randint(5,15)
    if massage3.funds < 0:
        print(f"{massage3.name}的资金不够了，付不起保护费与租金。在这条街上的名誉严重下降。")
        massage3.reputation -= random.randint(5,15)




def main():
    day = 0
    while True:
        print("")
        print(f"开业第{day}天")
        print("1. 确认信息")
        print("2. 培训技师")
        print("3. 解雇技师")
        print("4. 招募技师")
        print("5. 抢夺技师")
        print("其它 跳过白天")
        choice = input("请选择: ")
        if choice == "1":
            massage0.check_info()
            continue
        elif choice == "2":
            massage0.care_workers()
        elif choice == "3":
            massage0.fire_worker()
            continue
        elif choice == "4":
            massage0.p_hire_worker()
        elif choice == "5":
            massage0.steal_worker()
        else:
            print("今天白天无事发生。")

        if not massage0.workers:
            print("店里一个技师都没有！你无法营业！跳过今日。")
            day += 1
            continue
        # 夜晚事件
        night_event()
        # 次日与游戏结束
        day += 1
        if massage0.reputation <0:
            print("")
            print("你臭名昭著！有人向上头举报了你们，你被关进大牢，你的技师们纷纷跑路。")
            print("唉，资本！")
            for worker in massage0.workers:
                be = random.choice([1,2,3,4,5,6,7,8,9,10])
                if be == 1:
                    print(f"{worker.name}决定跑去当虚拟主播，平均一天咬三次打火机，四次把李宁踹开线，五次不要笑挑战......")
                if be == 2:
                    print(f"{worker.name}在获得哲学、生化环材等学位后转专业去了土木，现在在工地打灰，混得不错。")
                if be == 3:
                    print(f"{worker.name}靠着这段时间按摩的本事修机器，机魂大悦。智械危机爆发后，他成了机器人的御用按摩师。")
                if be == 4:
                    print(f"{worker.name}在核战争之后，化名推拿四郎，遇到敌人就会使用瞬间按摩，让对方五秒后活活爽死。")
                if be == 5:
                    print(f"{worker.name}踏上了寻找七颗龙珠的旅程，实现了成为木叶村海贼王的愿望，与夕立等舰娘并肩作战。")
                if be == 6:
                    print(f"{worker.name}考研失败，考公失败，考编失败，参军被刷，最后前往工地帮打灰的哥们搬砖。")
                if be == 7:
                    print(f"{worker.name}因为被鉴定为比较纯真，被拉去当电子烟代言人，与其他几位著名烟草代言人火爆全球。")
                if be == 8:
                    print(f"{worker.name}沉迷两款开放世界游戏，因为频繁歪，为了赚648成为了光荣的A股股民，蒸蒸日上。")
                if be == 9:
                    print(f"{worker.name}掌握始祖巨人之力之后试图召唤高达踏平世界，结果受开罗尔物质影响，引发了智械危机。")
                if be == 10:
                    print(f"{worker.name}先是考上了北京大学，然后升入中等技术学校，现在成为一名售货员，有着光明的未来。")
            print("")
            print("以下是你按摩店倒闭后的信息：")
            massage0.check_info()
            input("按回车键结束......")
            return
        if massage0.reputation > massage1.reputation and massage0.reputation > massage2.reputation and massage0.reputation > massage3.reputation:
            print("")
            print("你的{massage0.name}成为了这条街最著名的按摩店！你成为了推拿之王！你可以继续游戏，也可以关闭结束。")
            print("")
            input("按回车键继续......")
            
# 可该特质："大力王", "能唠嗑", "打拍子", "懂针灸", "会拔罐", "爱哼歌"
# 以下为主角的初始员工
gs=[worker("老王", 16, 90, 90, 90, ["大力王","能唠嗑","会拔罐"], 0),
worker("李华", 17, 90, 90, 90, ["会拔罐","爱哼歌","懂针灸"], 0)]
massage0.workers=massage0.workers+gs

# 游戏正式开始
main()
