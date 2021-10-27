# wsa-apktool
creates a batch file that uses adb to auto-install apks into the Windows Subsystem for Android and registers it as the default application to open apks.
<br><br>
Simply run this script and let it do its thing.

The file association will not work if you have already associated .apk files with another application, wether manually or through an application. In case the "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.apk\" exists, you will need to delete this key. (oh wait, can't i delete it? - didn't think about that, actually. I'll add it later, that should save you from accidentally messing up the registry)
