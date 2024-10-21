import psutil





def get_running_programs():
    program_list = []
    
    # 获取所有正在运行的进程
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'status']):
        try:
            # 获取进程信息
            pid = proc.info['pid']
            name = proc.info['name']
            exe_path = proc.info['exe']
            status = proc.info['status']
            
            # 将进程信息添加到列表中
            program_info = {
                'PID': pid,
                'Name': name,
                'Executable Path': exe_path,
                'Status': status
            }
            program_list.append(program_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # 处理访问某些系统进程时可能出现的异常
            pass
    
    return program_list

