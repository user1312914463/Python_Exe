import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from exe.exe.programing.compilation_engine import CompilationEngine
from config_manager import ConfigManager
import os


class PythonToExeCompilerApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Python 到 EXE 编译器(V1.0.1)")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        # 设置中文字体支持
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("SimHei", 10))
        self.style.configure("TButton", font=("SimHei", 10))
        self.style.configure("TCheckbutton", font=("SimHei", 10))
        self.style.configure("TCombobox", font=("SimHei", 10))

        # 初始化配置管理器
        self.config_manager = ConfigManager()

        # 初始化编译引擎
        self.compilation_engine = CompilationEngine()
        self.compilation_engine.set_log_callback(self.log_message)

        # 创建UI
        self.create_ui()

        # 加载保存的设置
        self.load_settings()

    def create_ui(self):
        # 创建主框架
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Python 文件选择
        ttk.Label(self.main_frame, text="Python 文件:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.python_file_path = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.python_file_path, width=50).grid(row=0, column=1, pady=5)
        ttk.Button(self.main_frame, text="浏览...", command=self.select_python_file).grid(row=0, column=2, padx=5,
                                                                                          pady=5)

        # 输出目录选择
        ttk.Label(self.main_frame, text="输出目录:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.output_directory = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.output_directory, width=50).grid(row=1, column=1, pady=5)
        ttk.Button(self.main_frame, text="浏览...", command=self.select_output_directory).grid(row=1, column=2, padx=5,
                                                                                               pady=5)

        # 图标文件选择（可选）
        ttk.Label(self.main_frame, text="图标文件 (可选):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.icon_file_path = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.icon_file_path, width=50).grid(row=2, column=1, pady=5)
        ttk.Button(self.main_frame, text="浏览...", command=self.select_icon_file).grid(row=2, column=2, padx=5, pady=5)

        # 编译选项
        ttk.Label(self.main_frame, text="编译选项:").grid(row=3, column=0, sticky=tk.W, pady=10)

        # 单文件模式
        self.is_onefile_mode = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.main_frame, text="单文件模式", variable=self.is_onefile_mode).grid(row=4, column=0,
                                                                                                sticky=tk.W, pady=2)

        # 窗口模式
        self.is_windowed_mode = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.main_frame, text="窗口模式 (无控制台)", variable=self.is_windowed_mode).grid(row=4,
                                                                                                          column=1,
                                                                                                          sticky=tk.W,
                                                                                                          pady=2)

        # 调试模式
        self.is_debug_mode = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.main_frame, text="调试模式", variable=self.is_debug_mode).grid(row=4, column=2,
                                                                                            sticky=tk.W, pady=2)

        # 清理临时文件
        self.is_clean_temp_files = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.main_frame, text="清理临时文件", variable=self.is_clean_temp_files).grid(row=5, column=0,
                                                                                                      sticky=tk.W,
                                                                                                      pady=2)

        # 控制台编码
        ttk.Label(self.main_frame, text="控制台编码:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.console_encoding = tk.StringVar(value="utf-8")
        ttk.Combobox(self.main_frame, textvariable=self.console_encoding, values=["utf-8", "gbk", "gb2312", "ascii"],
                     width=15).grid(row=6, column=1, sticky=tk.W, pady=5)

        # 保存/加载设置
        ttk.Button(self.main_frame, text="保存设置", command=self.save_settings).grid(row=7, column=0, padx=5, pady=10)
        ttk.Button(self.main_frame, text="加载设置", command=self.load_settings).grid(row=7, column=1, padx=5, pady=10)

        # 编译按钮
        self.compile_button = ttk.Button(self.main_frame, text="开始编译", command=self.start_compilation)
        self.compile_button.grid(row=7, column=2, padx=5, pady=10)

        # 进度条
        self.progress_value = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.main_frame, variable=self.progress_value, length=100,
                                            mode='indeterminate')
        self.progress_bar.grid(row=8, column=0, columnspan=3, sticky=tk.W + tk.E, pady=10)

        # 日志区域
        ttk.Label(self.main_frame, text="编译日志:").grid(row=9, column=0, sticky=tk.W, pady=5)
        self.compilation_log_text = tk.Text(self.main_frame, height=10, width=80)
        self.compilation_log_text.grid(row=10, column=0, columnspan=3, sticky=tk.W + tk.E + tk.N + tk.S, pady=5)
        scrollbar = ttk.Scrollbar(self.main_frame, command=self.compilation_log_text.yview)
        scrollbar.grid(row=10, column=3, sticky=tk.N + tk.S)
        self.compilation_log_text.config(yscrollcommand=scrollbar.set)

        # 设置网格权重，使日志区域可扩展
        self.main_frame.grid_rowconfigure(10, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

    def select_python_file(self):
        file_path = filedialog.askopenfilename(
            title="选择Python文件",
            filetypes=[("Python files", ["*.py", "*.python"]), ("All files", "*.*")]
        )
        if file_path:
            self.python_file_path.set(file_path)

    def select_output_directory(self):
        directory_path = filedialog.askdirectory(title="选择输出目录")
        if directory_path:
            self.output_directory.set(directory_path)

    def select_icon_file(self):
        file_path = filedialog.askopenfilename(
            title="选择图标文件",
            filetypes=[("Icon files", "*.ico"), ("All files", "*.*")]
        )
        if file_path:
            self.icon_file_path.set(file_path)

    def save_settings(self):
        settings = {
            "python_file": self.python_file_path.get(),
            "output_dir": self.output_directory.get(),
            "icon_file": self.icon_file_path.get(),
            "onefile": self.is_onefile_mode.get(),
            "windowed": self.is_windowed_mode.get(),
            "debug": self.is_debug_mode.get(),
            "clean": self.is_clean_temp_files.get(),
            "encoding": self.console_encoding.get()
        }

        self.config_manager.save_settings(settings)
        self.log_message("设置已保存")

    def load_settings(self):
        settings = self.config_manager.load_settings()

        self.python_file_path.set(settings.get("python_file", ""))
        self.output_directory.set(settings.get("output_dir", os.getcwd()))
        self.icon_file_path.set(settings.get("icon_file", ""))
        self.is_onefile_mode.set(settings.get("onefile", True))
        self.is_windowed_mode.set(settings.get("windowed", False))
        self.is_debug_mode.set(settings.get("debug", False))
        self.is_clean_temp_files.set(settings.get("clean", True))
        self.console_encoding.set(settings.get("encoding", "utf-8"))

        self.log_message("已加载保存的设置")

    def log_message(self, message):
        self.compilation_log_text.insert(tk.END, message + "\n")
        self.compilation_log_text.see(tk.END)

    def start_compilation(self):
        # 清空日志
        self.compilation_log_text.delete(1.0, tk.END)

        # 获取用户选择的文件和选项
        python_file = self.python_file_path.get()
        output_dir = self.output_directory.get()
        icon_file = self.icon_file_path.get() if self.icon_file_path.get() else None

        # 验证输入
        if not python_file:
            messagebox.showerror("错误", "请选择Python文件")
            return

        if not os.path.exists(python_file):
            messagebox.showerror("错误", f"Python文件不存在: {python_file}")
            return

        if not output_dir:
            messagebox.showerror("错误", "请选择输出目录")
            return

        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
                self.log_message(f"创建输出目录: {output_dir}")
            except Exception as e:
                messagebox.showerror("错误", f"无法创建输出目录: {str(e)}")
                return

        # 禁用编译按钮并启动进度条
        self.compile_button.config(state=tk.DISABLED)
        self.progress_bar.start()

        # 设置编译选项
        options = {
            "onefile": self.is_onefile_mode.get(),
            "windowed": self.is_windowed_mode.get(),
            "debug": self.is_debug_mode.get(),
            "clean": self.is_clean_temp_files.get(),
            "encoding": self.console_encoding.get()
        }

        # 在单独的线程中执行编译，避免阻塞UI
        threading.Thread(target=self.compilation_engine.compile, args=(python_file, output_dir, icon_file, options),
                         daemon=True).start()

    def compilation_complete(self, success, error_message=None):
        # 启用编译按钮并停止进度条
        self.compile_button.config(state=tk.NORMAL)
        self.progress_bar.stop()

        if success:
            self.log_message("\n编译成功!")
            messagebox.showinfo("成功", "编译完成!")
        else:
            self.log_message(f"\n编译失败: {error_message}")
            messagebox.showerror("错误", f"编译失败: {error_message}")