var1 = 5       ## 全域變數

def test():
    var1 = 10  ##區域變數
    
def test1():
    global var1  ##透過"global"來告訴Python這個變數是全域變數。
    var1 = 10

test()
#test1()
print(var1)
 
## output:
# 5