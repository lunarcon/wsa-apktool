import os,subprocess,sys,ctypes,msvcrt

def get_cmd_output(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out.decode("utf-8")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False  
    
ADB_PATH = get_cmd_output("where adb").strip()
DEFAULT_IP='127.0.0.1:58526'
PATH=os.getenv('SYSTEMROOT')+'\\'

def main():
    if not 'not' in ADB_PATH:
        print("adb found at: " + ADB_PATH)
    else:
        print("adb not found, please install it and/or add it to your PATH")  
        exit()
    ipt,ip=input(f'default WSA IP is {DEFAULT_IP}, do you wish to change this? (y/n)').lower(),DEFAULT_IP
    if ipt == 'y':
        ip=input('enter new IP: ')
    print('making apktool...')
    batch=f'{ADB_PATH} connect {ip}\n{ADB_PATH} install %1'
    with open(f'{PATH}apktool.bat','w') as f:
        f.write(batch)
    print('registering .apk extension to run apktool')
    os.system("assoc .apk=\""+PATH+"apktool.bat\"")
    print(f'done!\n(if that didn\'t work, please manually set .apk file association to {PATH}apktool.bat)')
    print('you can run this installer again in case your WSA IP changes. press any key to exit.')
    if msvcrt.getch():
        exit()

if __name__ == '__main__':
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
