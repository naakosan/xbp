ok = 0
ng = 0
print("君は日本の歴史どのくらい理解しているのか❓")
a = input("江戸幕府を開いた人物は誰？")
b = input("土偶が多く出土するのは何時代の遺跡？")
c = input("銀閣寺を建てたのは誰？")
d = input("武士で初めて太政大臣になった人物は誰？")
if a == "徳川家康":
    print("正解")
    ok = ok + 1
else:
    print("不正解")
    ng = ng + 1
if b == "縄文時代" or b == "縄文" or b == "じょうもん" :
    print("正解")
    ok = ok + 1
else:
    print("不正解")
    ng = ng + 1
if c == "足利義政" or c == "あしかがよしまさ" in c:
    print("正解")
    ok = ok + 1
else:
    print("不正解")
    ng = ng + 1
if d == "平清盛" or d == "たいらのきよもり":
    print("正解")
    ok = ok + 1
else:
    print("不正解")
    ng = ng + 1
print("問題終了！！　あなたの正解数は", ok, "正解率は", ok/(ok+ng)*100, "％だよ！　解いてくれてありがとう😊💗")
