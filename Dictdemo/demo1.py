#字典的创建
price={'鸡蛋':1,'耳机':200,'奶茶':8}
scores=dict(高数=100,英语='a')
print(price)
print(scores)
#字典元素的获取
print(price['耳机'])
print(scores.get('高数'))
'''
   使用[]获取不存在的键值会报错，
   而使用get()方法获取不存在的键值会返回none，
   如果get()里面带参数，则会返回默认值参数
'''
b=sorted(price.items(),key=lambda price:price[1])
print(b)
