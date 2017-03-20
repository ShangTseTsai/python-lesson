a = input("你的名字？");
b = a[0];
if a == "許鈞傑":
    print ("許導好，恭迎許導蒞臨！！！");
if a == "蔡尚澤":
    print ("可恥！洗洗睡吧你！");
else:
    print ( b + "導好！");
    print ("要加入許導教嗎？（請輸入：好 / 不要）");
    c = input("");
    if c == "好":
        print (a + "已經加入許導教了～");
    else:
        print ("你終究要加入的");
