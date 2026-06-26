# blocking.py
import time

def cook_ramen():
    print('라면 물 끓이기')

    time.sleep(3) # 3초 동안 쓰레드 정지

    print("보글 보글")

if __name__ == '__main__':
    print('요리시작')

    cook_ramen()

    print('다음 작업 수행')