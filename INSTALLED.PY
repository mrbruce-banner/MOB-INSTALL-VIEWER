import subprocess

#======================
AUTHOR = "BLACK-HAT_NS"
#======================
print("=" * 65)
print(" ANDROID INSTALLED APPS HISTORY ")
print(f" Created by : {AUTHOR}")
print("=" * 65)

result = subprocess.getoutput("pm list packages -3")
apps = result.splitlines()

for i, app in enumerate(apps, 1):
    pkg = app.replace("package:", "")
    info = subprocess.getoutput(
        f"dumpsys package {pkg} | grep firstInstallTime"
    )
    print(f"[{i:03}] {pkg}")
    print(f"      {info}")
    print("-" * 45)
