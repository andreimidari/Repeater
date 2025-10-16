import sys
import os
import subprocess
import time
from threading import Thread

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lib")
if os.path.isdir(lib_path):
    sys.path.append(lib_path)

from flowlauncher import FlowLauncher

class Repeater(FlowLauncher):

    def query(self, query):
        if "::" in query:
            parts = query.split("::", 1)
            count_str = parts[0]
            command = parts[1].strip()

            if count_str.isdigit():
                count = int(count_str)
                if count > 0 and command:
                    return [{
                        "Title": f"Execute '{command}' {count} times",
                        "SubTitle": "This will run the command in sequence.",
                        "IcoPath": "Images/app.png",
                        "JsonRPCAction": {
                            "method": "repeat_command",
                            "parameters": [command, count]
                        }
                    }]
        return []

    def repeat_command(self, command, count):
        thread = Thread(target=self._execute_in_background, args=(command, count))
        thread.daemon = True
        thread.start()

    def _get_flow_executable_path(self):
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        plugins_dir = os.path.dirname(plugin_dir)
        app_root_dir = os.path.dirname(plugins_dir)
        
        expected_path = os.path.join(app_root_dir, "Flow.Launcher.exe")
        if os.path.exists(expected_path):
            return expected_path
        
        return None

    def _execute_in_background(self, command, count):
        flow_exe_path = self._get_flow_executable_path()

        if not flow_exe_path:
            return
            
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        for _ in range(count):
            try:
                subprocess.run(
                    [flow_exe_path, "-query", command],
                    check=True,
                    startupinfo=startupinfo
                )
                time.sleep(0.5)  # 0.5 seconds
            except (subprocess.CalledProcessError, FileNotFoundError):
                break

if __name__ == "__main__":
    Repeater()


