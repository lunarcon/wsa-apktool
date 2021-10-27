# wsa-apktool
creates a batch file that uses adb to auto-install apks into the Windows Subsystem for Android and registers it as the default application to open apks.
<br><br>
Simply run this script and let it do its thing.

The file association will not work if you have already associated .apk files with another application, wether manually or through an application. In case the <b>"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\\.apk\\"</b> key exists, the installiation script will delete this key. Run at your own risk, of course. Always keep backups of your registry!
<br><br>
Remember, WSA needs to be running when you want to install apks through adb. After apktool is installed, you can simply double-click on the apk file to install it into WSA.

## common errors
- adb refused to connect - this indicates that you need to use the ip found in WSA settings, which seems to be different every time. You can re-run the installer to do this
- failed streamed install - should be fixed by the same method as above
- WSA is not running - the tool will start WSA for you, after which you'll need to close the tool double-click the apk file again to reopen the tool.
- tool closed after 'Performing Streamed Install' - This (usually) means that the apk has been installed successfully.
