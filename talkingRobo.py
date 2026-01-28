import os

if __name__ == "__main__" :
    print("welcome to robo :")
    x=1
    while x==1 :
        command = input("enter what you want to speak : ")
        if command == "q" :
            os.system("say bye bye")
            break
        os.system(f"say {command}")