'''
拥有礼物的标识
发礼物的方法
展示礼物的方法
'''
have_gift= False

def send():
    print("发礼物啦")
    global have_gift

def show():
    if have_gift == True:
        print("收到礼物，好开心")
    else:
        print("没有礼物")
if __name__ == '__main__':
    send()
    show()