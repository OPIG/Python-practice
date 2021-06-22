fb = open("./ancesor.txt", "r")
article = fb.read()
#此行可以设置flitter
new_article = article
#将数据换行划分，然后用空格连接起来（“ ”.join()），然后去首尾空格，然后分解
words = " ".join(new_article.split("\n")).strip().split(" ")
#创建一个字典
word_counts = {}
#实现单词的全部变大写
for word in words:
  upperWord = word.upper()
  if upperWord in  word_counts:
    word_counts[upperWord] = word_counts[upperWord] + 1
  else:
    word_counts[upperWord] = 1

key_list = list(word_counts.keys())
key_list.sort()
for key in key_list:
  #对计数大于0的进行打印
  if word_counts[key] > 0:
    print("{}:{}".format(key, word_counts[key]))
