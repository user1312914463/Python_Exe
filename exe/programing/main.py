import sys
import tkinter as tk
from exe.exe.programing.key_verification import KeyVerificationGUI
from exe.exe.programing.compiler_gui import PythonToExeCompilerApp

def main():
    # 检查命令行参数
    if len(sys.argv) > 1 and sys.argv[1] == "--skip-key":
        # 用于开发测试，跳过密钥验证
        root = tk.Tk()
        app = PythonToExeCompilerApp(root)
        root.mainloop()
    else:
        # 正常启动流程，先验证密钥
        key_verification_window = tk.Tk()
        key_verification = KeyVerificationGUI(key_verification_window)
        key_verification_window.mainloop()

if __name__ == "__main__":
    main()    