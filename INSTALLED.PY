import subprocess

AUTHOR = "BLACK-HAT_NS"

def banner():
    print("=" * 65)
    print(" ANDROID INSTALLED APPS HISTORY ")
    print(f" Created by : {AUTHOR}")
    print("=" * 65)

def get_apps():
    try:
        result = subprocess.check_output(
            ["cmd", "package", "list", "packages", "-3"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.splitlines()
    except:
        print("❌ Permission denied or cmd not accessible")
        return []

def get_install_time(pkg):
    try:
        output = subprocess.check_output(
            ["cmd", "package", "dump", pkg],
            stderr=subprocess.DEVNULL,
            text=True
        )
        for line in output.splitlines():
            if "firstInstallTime" in line:
                return line.strip()
    except:
        return "Install time not accessible"
    return "Install time not found"

if __name__ == "__main__":
    banner()
    apps = get_apps()

    for i, app in enumerate(apps, 1):
        pkg = app.replace("package:", "")
        install_time = get_install_time(pkg)

        print(f"[{i:03}] {pkg}")
        print(f"      {install_time}")
        print("-" * 45)
