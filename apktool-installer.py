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
WSA='WsaClient.exe /launch wsa://com.android.documentsui'

def main():
    global PATH
    if '\\' in ADB_PATH:
        print("adb found at: " + ADB_PATH)
    else:  
        PATH=input('enter path to adb.exe ')
        exit()
    ipt,ip=input(f'default WSA IP is {DEFAULT_IP}, do you wish to change this? (y/n) ').lower(),DEFAULT_IP
    if ipt == 'y':
        ip=input('enter new IP: ')
    print('making apktool...')
    batch=f':start\n@echo off\necho installing apk...\nadb disconnect\ntasklist /fi "ImageName eq WsaClient.exe" /fo csv 2>NUL | find /I "WsaClient.exe">NUL\nIF "%ERRORLEVEL%"=="0" (\n{ADB_PATH} connect {ip}\n{ADB_PATH} install %1\n) ELSE (echo WSA is not running!\necho starting WSA...\nstart {WSA} & set /p g=press enter when WSA finishes loading...\ngoto start)'
    with open(f'{PATH}apktool.bat','w') as f:
        f.write(batch)
    # trying to set apktool.bat as the default app to open .apk files
    out=get_cmd_output('reg delete "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\.apk" /f')
    os.system(f'REG ADD HKCR\\Software\\Classes\\.apk\\shell\\open\\command /t REG_SZ /d "{PATH}apktool.bat" /f')
    os.system('assoc .apk=apkfile')
    os.system('ftype apkfile="'+PATH+'apktool.bat" "%1"')
    # it's worth a shot!
    print('you can run this installer again in case your WSA IP changes. press any key to exit.')
    if msvcrt.getch():
        exit()

if __name__ == '__main__':
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
