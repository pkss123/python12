user = {"kim1234":"kkk1234",
        "lee4567":"lll4567",
        "park9876":"ppp9876"}

print("\n아이디와 비밀번호를 입력하세요")
id = input("아이디:")
pw = input("비밀번호:")

if id in user:
    if pw == user[id]:
        print(id + "님 로그인을 환영합니다")
    else:
        print("비밀번호를 틀렸습니다")
else:
    print("존재하지않는 회원입니다")