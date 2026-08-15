import json
import os
import shutil
import socket
import subprocess


def get_server_info():

  cpu_val = round((os.getloadavg()[0] / (os.cpu_count() or 1)) * 100, 1)

  with open("/proc/meminfo") as f:
    m = f.readlines()
  mem_val = round(
      ((int(m[0].split()[1]) - int(m[2].split()[1])) / int(m[0].split()[1]))
      * 100,
      1,
  )

  st = os.statvfs("/")
  disk_val = round(((st.f_blocks - st.f_bavail) / st.f_blocks) * 100, 1)

  if cpu_val > 90 or mem_val > 90 or disk_val > 90:
    status = "Critical"
  elif cpu_val > 70 or mem_val > 70 or disk_val > 70:
    status = "Warning"
  else:
    status = "Healthy"

  ssh_status = "unknown"

  if shutil.which("systemctl"):
    try:
      res = subprocess.run(
          ["systemctl", "is-active", "ssh"], capture_output=True
      )
      ssh_status = "active" if res.returncode == 0 else "inactive"
    except Exception:
      ssh_status = "unknown"
  else:
    
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        ssh_status = (
            "active" if s.connect_ex(("127.0.0.1", 22)) == 0 else "inactive"
        )
    except Exception:
      ssh_status = "unavailable"

  uptime_seconds = float(open("/proc/uptime").read().split()[0])
  uptime_minutes = int(uptime_seconds // 60)
  uptime_seconds = int(uptime_seconds % 60)

  data = {
      "hostname": socket.gethostname(),
      "status": status,
      "cpu": f"{cpu_val}%",
      "memory": f"{mem_val}%",
      "disk": f"{disk_val}%",
      "uptime": f"Uptime: {uptime_minutes} minutes, {uptime_seconds} seconds",
      "processes": len([p for p in os.listdir("/proc") if p.isdigit()]),
      "services": {"ssh": ssh_status},
      "network": {"ip": socket.gethostbyname(socket.gethostname())},
  }

  return json.dumps(data, indent=4)


if __name__ == "__main__":
  print(get_server_info())
