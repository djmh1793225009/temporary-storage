import os
import sys
import time
import google.generativeai as genai

API_KEY = "AIzaSyAX9WKmoNTNhhKkn3WJPzsBq0Rkz5U9MrA"
genai.configure(api_key=API_KEY)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadingAnimation():
    for i in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\n')

def printHelp():
    helpText = """
    /help - 显示帮助信息
    /end - 结束当前对话并重新开始
    /exit - 退出脚本并询问是否保存对话
    """
    print(helpText)

def saveConversation(conversation):
    filename = "conversation.txt"
    try:
        with open(filename, "w", encoding='utf-8') as file:
            file.writelines(conversation)
        print(f"对话已保存到 {filename}")
    except Exception as e:
        print(f"保存对话失败: {e}")

def main():
    conversation = []
    clearScreen()
    
    while True:
        print("请选择要使用的模型：")
        print("1. gemini-1.0-pro")
        print("2. gemini-1.5-flash (默认)")
        print("3. gemini-1.5-pro")
        modelChoice = input("> ").strip()
        
        modelName = {
            "1": "gemini-1.0-pro",
            "3": "gemini-1.5-pro"
        }.get(modelChoice, "gemini-1.5-flash")
        
        try:
            model = genai.GenerativeModel(modelName)
        except Exception as e:
            print(f"模型加载失败: {e}")
            continue  # Continue to model selection if loading fails
            
        clearScreen()
        
        while True:
            try:
                userInput = input("\033[1;32m>\033[0m ").strip()
                if userInput.startswith('/'):
                    if userInput == "/end":
                        conversation.clear()
                        clearScreen()
                        break
                    elif userInput == "/help":
                        printHelp()
                    elif userInput == "/exit":
                        saveOption = input("是否保存对话？(y/n) ").strip().lower()
                        if saveOption == 'y':
                            saveConversation(conversation)
                        sys.exit(0)
                    else:
                        print("未知命令。输入 /help 查看帮助。")
                else:
                    conversation.append(f"用户: {userInput}\n")
                    print("生成中", end="")
                    loadingAnimation()
                    
                    try:
                        response = model.generate_content(userInput)
                        answer = response.text.strip()
                    except Exception as e:
                        print(f"AI 生成回复出错: {e}")
                        continue  # Continue to next user input if generation fails

                    conversation.append(f"AI: {answer}\n")
                    print(answer)
            except KeyboardInterrupt:
                print("\n强制退出。")
                sys.exit(0)

if __name__ == "__main__":
    main()