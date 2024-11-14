sentence=list(input('enter a sentences'))
my_dic={}
for i in sentence:
    a=sentence.count(i)
    my_dic[i]=a
print(my_dic)