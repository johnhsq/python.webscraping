# https://www.jeddd.com/article/python-ngram-language-prediction.html
### 删除空白字符
content = content.replace(u'\t', '')      # 去除制表符
content = content.replace(u'\xa0', '')    # 去除全角空格
content = content.replace(u'\u3000', '')  # 去除不间断空白符

### 切割成句子
content = re.split('，|。|；|？|！|：|\n', content)
content = list(filter(None, content))  # 去除空句子

### 分词并去除停止词
# 结巴中文分词（jieba）的效果最好，而且分词速度足够快
# 中文停止词表可以在这个 GitHub 仓库找到
with open('stopwords/中文停用词表.txt') as f:
    stopwords = f.readlines()
stopwords = set(map(lambda x:x.strip(), stopwords))  # 去除末尾换行符

# 分词、去除停止词
sentence = jieba.cut(sentence)  # 分词
word_list = [word.strip() for word in sentence if word.strip() and word not in stopwords]  # 去除停止词
sentence = ' '.join(word_list)  # 用空格分隔分词结果

### 构建词表 word_table
for word in word_list:
    word = word.strip()
    word_table[word] = word_table.get(word, 0) + 1  # 频数加一
# 保存词表到文件
with open('wordtable2.txt', 'w', encoding='utf-8') as f:
    for i, word in enumerate(word_table):
        f.write(str(i) + ' ' + word + '\n')


##### n-gram model
### n=3 trigram
n = 3
ngrams_list = []  # n元组（分子）
prefix_list = []  # n-1元组（分母）

# 遍历所有预处理过的新闻文件
for i, datafile in enumerate(os.listdir(data_path)):
    with open(data_path + datafile, encoding='utf-8') as f:
        for line in f:
            # 在每个句子前后添加上 <BOS> 和 <EOS>
            sentence = ['<BOS>'] + line.split() + ['<EOS>']  # 列表，形如：['<BOS>', '显得', '十分', '明亮', '<EOS>']
            # 从中提取所有的 n-gram 元组（n=3 时就是三元组），保存在 ngrams_list 列表中；
            ngrams = list(zip(*[sentence[i:] for i in range(n)]))   # 一个句子中n-gram元组的列表
            prefix = list(zip(*[sentence[i:] for i in range(n-1)])) # 历史前缀元组的列表
            ngrams_list += ngrams
            prefix_list += prefix

ngrams_counter = Counter(ngrams_list)
prefix_counter = Counter(prefix_list)


##### 进行预测
# 挖去一个词的句子，我们要使用 n-gram 模型预测这个挖去的词是什么
# 思路是将词表中的所有词作为候选词，依次尝试将每个词填入空，然后计算句子的概率，
# 最终选取使得句子概率最大的那个词。由于每个待测句子都只有一个待预测词，所以实际上无需计算整个句子的概率，只需计算待预测词附近的概率即可
def probability(sentence):
    """
    计算一个句子的概率。
    Params:
        sentence: 由词构成的列表表示的句子。
    Returns:
        句子的概率。
    """
    prob = 1  # 初始化句子概率
    ngrams = list(zip(*[sentence[i:] for i in range(n)]))   # 将句子处理成n-gram的列表
    for ngram in ngrams:
        # 累乘每个n-gram的概率，并使用加一法进行数据平滑
        prob *= (1 + ngrams_counter[ngram]) / (len(prefix_counter) + prefix_counter[(ngram[0], ngram[1])])
    return prob
