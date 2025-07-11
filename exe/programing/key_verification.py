import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import sys
from pathlib import Path

class KeyVerificationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("密钥验证(Version 1.0.1)")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.option_add("*Font", "SimHei 10")

        # 密钥配置文件路径
        self.key_file_path = os.path.join(os.getcwd(), "resources", "keys.json")

        # 错误计数器
        self.error_attempt_count = 0
        self.max_attempts = 3

        # 创建UI
        self.create_ui()

        # 检查密钥状态
        self.check_key_status()

    def create_ui(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        ttk.Label(main_frame, text="Python 到 EXE 编译器(V1.0.1)\n\n获取密钥请加Q:1312914463", font=("SimHei", 16, "bold")).grid(row=0, column=0,
                                                                                             columnspan=2, pady=10)

        # 状态显示
        self.key_status = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.key_status).grid(row=1, column=0, columnspan=2, pady=10)

        # 密钥输入框
        ttk.Label(main_frame, text="密钥:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.key_input_entry = ttk.Entry(main_frame, show="*", width=30)
        self.key_input_entry.grid(row=2, column=1, sticky=tk.W, pady=10)

        # 验证结果显示
        self.verification_result = tk.StringVar()
        self.result_label = ttk.Label(main_frame, textvariable=self.verification_result, foreground="red")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

        # 验证按钮
        self.verify_button = ttk.Button(main_frame, text="验证", command=self.verify_key)
        self.verify_button.grid(row=4, column=0, columnspan=2, pady=15)

    def check_key_status(self):
        # 检查密钥文件是否存在
        if not os.path.exists(self.key_file_path):
            self.key_status.set("密钥文件不存在，请联系管理员")
            self.key_input_entry.configure(state=tk.DISABLED)
            self.verify_button.configure(state=tk.DISABLED)
            return

        # 检查是否已锁定
        try:
            with open(self.key_file_path, 'r', encoding='utf-8') as f:
                key_data = json.load(f)
                if key_data.get("locked", False):
                    self.key_status.set("密钥已被锁定，请联系管理员")
                    self.key_input_entry.configure(state=tk.DISABLED)
                    self.verify_button.configure(state=tk.DISABLED)
        except Exception as e:
            self.key_status.set(f"密钥文件损坏: {str(e)}")
            self.key_input_entry.configure(state=tk.DISABLED)
            self.verify_button.configure(state=tk.DISABLED)

    def verify_key(self):
        user_input_key = self.key_input_entry.get().strip()

        try:
            with open(self.key_file_path, 'r', encoding='utf-8') as f:
                key_data = json.load(f)
                predefined_keys = key_data.get("keys", [])

                if user_input_key in predefined_keys:
                    self.verification_result.set("验证成功，正在启动程序...")
                    self.result_label.configure(foreground="green")
                    self.root.after(1000, self.start_compiler)
                else:
                    self.error_attempt_count += 1
                    remaining_attempts = self.max_attempts - self.error_attempt_count

                    if remaining_attempts > 0:
                        self.verification_result.set(f"密钥错误！还剩{remaining_attempts}次尝试机会")
                    else:
                        # 锁定密钥文件
                        key_data["locked"] = True
                        with open(self.key_file_path, 'w', encoding='utf-8') as f:
                            json.dump(key_data, f, ensure_ascii=False, indent=4)

                        self.verification_result.set("错误次数超过限制，密钥已被锁定")
                        self.key_status.set("密钥已被锁定，请联系管理员")
                        self.verify_button.configure(state=tk.DISABLED)
        except Exception as e:
            self.verification_result.set(f"验证过程发生错误: {str(e)}")

    def start_compiler(self):
        self.root.destroy()
        import subprocess
        # 使用subprocess启动主程序，跳过密钥验证
        subprocess.Popen([sys.executable, "main.py", "--skip-key"])