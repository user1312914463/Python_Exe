import json
import os


class ConfigManager:
    def __init__(self):
        self.config_file = os.path.join(os.getcwd(), "py_to_exe_config.json")

    def save_settings(self, settings):
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
            return True, "设置已保存"
        except Exception as e:
            return False, f"保存设置失败: {str(e)}"

    def load_settings(self):
        default_settings = {
            "python_file": "",
            "output_dir": os.getcwd(),
            "icon_file": "",
            "onefile": True,
            "windowed": False,
            "debug": False,
            "clean": True,
            "encoding": "utf-8"
        }

        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    # 合并默认设置和保存的设置
                    return {**default_settings, **settings}
            except Exception as e:
                print(f"加载设置失败: {str(e)}")
                return default_settings
        else:
            return default_settings