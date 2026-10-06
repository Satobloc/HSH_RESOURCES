
import os, hashlib, csv, psutil, win32security

OUTPUT_ROOT = r"D:\SYSTEM_SCAN"

def ensure_output():
    if not os.path.exists(OUTPUT_ROOT):
        os.makedirs(OUTPUT_ROOT, exist_ok=True)

def sha256(path):
    try:
        with open(path, "rb") as f:
            h = hashlib.sha256()
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
            return h.hexdigest()
    except:
        return None

def get_owner(path):
    try:
        sd = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, _ = win32security.LookupAccountSid(None, owner_sid)
        return f"{domain}\\{name}"
    except:
        return None

def scan_drive(root):
    ensure_output()
    drive_label = root.replace(":", "")
    outdir = os.path.join(OUTPUT_ROOT, f"Drive_{drive_label}")
    os.makedirs(outdir, exist_ok=True)
    csvpath = os.path.join(outdir, "filetree.csv")

    with open(csvpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["FullPath","Name","Ext","Size","Created","Modified","Accessed","Owner","SHA256"])

        for top, _, files in os.walk(root):
            for file in files:
                full = os.path.join(top, file)
                try:
                    stat = os.stat(full)
                    owner = get_owner(full)
                    hashv = sha256(full)
                except:
                    continue

                writer.writerow([
                    full,
                    file,
                    os.path.splitext(file)[1].lower(),
                    stat.st_size,
                    stat.st_ctime,
                    stat.st_mtime,
                    stat.st_atime,
                    owner,
                    hashv
                ])

def scan_all_drives():
    drives = [d.device for d in psutil.disk_partitions() if "fixed" in d.opts.lower()]
    for d in drives:
        scan_drive(d)
