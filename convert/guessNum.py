import random
game_count = 0
all_count =[]
while True:
  game_count += 1
  guess_count = 0
  answer = random.randint(0, 99)
  while True:
    guess = int(input("请输入0-99任意一个数字："))
    guess_count += 1
    if guess == answer:
      print("恭喜你猜对了！")
      print("你一共猜了" + str(guess_count)+ "次")
      all_count.append(guess_count)
      break
    elif guess > answer:
      print('太大了')
    else:
      print('太小了')
  onemore = raw_input('one more(Y/N)?')
  if onemore != "Y" and onemore != "y":
    print (onemore)
    print ("舍不得你，下次再来哈")
    print ("您的成绩如下：")
    print(all_count)
    print ("平均拆中次数" + str(sum(all_count) / int(len(all_count))))
    break
  else: 
    print("coming")