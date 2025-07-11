import subprocess
import sys
import os


class CompilationEngine:
    def __init__(self):
        self.log_callback = None
        self.current_process = None

    def set_log_callback(self, callback):
        self.log_callback = callback

    def log(self, message):
        if self.log_callback:
            self.log_callback(message)

    def compile(self, python_file, output_dir, icon_file=None, options=None):
        try:
            self.log("开始编译...")
            self.log(f"Python 文件: {python_file}")
            self.log(f"输出目录: {output_dir}")
            if icon_file:
                self.log(f"图标文件: {icon_file}")

            # 构建PyInstaller命令
            command = [
                sys.executable,  # 使用当前Python解释器
                "-m", "PyInstaller",
                "--distpath", output_dir,
                "--workpath", os.path.join(output_dir, "build"),
            ]

            # 添加编译选项
            if options.get("onefile", False):
                command.append("--onefile")

            if options.get("windowed", False):
                command.append("--windowed")

            if options.get("debug", False):
                command.append("--debug")

            if options.get("clean", False):
                command.append("--clean")

            # 添加图标
            if icon_file:
                command.extend(["--icon", icon_file])

            # 添加Python文件
            command.append(python_file)

            self.log("\n执行命令: " + " ".join(command))
            self.log("\n编译过程可能需要几分钟时间，请耐心等待...\n")

            # 执行命令
            self.current_process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                encoding=options.get("encoding", "utf-8")
            )

            # 实时输出命令行信息
            for line in iter(self.current_process.stdout.readline, ''):
                self.log(line.strip())

            # 等待命令执行完成
            self.current_process.wait()

            if self.current_process.returncode == 0:
                self.log("\n编译成功!")
                self.log(f"可执行文件位于: {output_dir}")
                success = True
                error_message = None
            else:
                self.log(f"\n编译失败，返回代码: {self.current_process.returncode}")
                success = False
                error_message = f"返回代码: {self.current_process.returncode}"

        except Exception as e:
            self.log(f"\n发生错误: {str(e)}")
            success = False
            error_message = str(e)

        finally:
            self.current_process = None
            # 通知主界面编译完成
            import tkinter as tk
            if self.log_callback:
                # 使用after方法确保在主线程中执行
                root = tk._default_root
                if root:
                    root.after(0, lambda: self.log_callback(f"compilation_complete|{success}|{error_message}"))