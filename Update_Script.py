import zipfile
import cloudshell.api.cloudshell_api as api


NameOfDriver = 'VmwareConsole'
ZipAddress = NameOfDriver + '.zip'
z = zipfile.ZipFile(ZipAddress, "w")
# z.write("drivermetadata.xml")
z.write("requirements.txt")
z.write("vmwareConsole.py")
z.write("__main__.py")
z.close()

ss = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')
ss.UpdateScript(NameOfDriver, ZipAddress)