#run.py
import subprocess
import os

def run_app():
    # 获取当前脚本的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Current directory: {current_dir}")
    # 构建 app.py 的完整路径
    app_path = os.path.join(current_dir, 'app.py')
    
    # 确保 app.py 文件存在
    if not os.path.exists(app_path):
        print(f"Error: {app_path} does not exist.")
        return
    
    # 使用 subprocess.run 来运行 streamlit run app.py 命令
    subprocess.run(["streamlit", "run", app_path,"--server.enableXsrfProtection=false"])

if __name__ == "__main__":
    run_app()