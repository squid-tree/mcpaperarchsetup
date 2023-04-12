serviceinfo = """
[Unit]

Description=Minecraft Server

After=systemd-user-sessions.service plymouth-quit-wait.service

After=rc-local.service

Before=getty.target

IgnoreOnIsolate=yes

[Service]

User=minecraft

Nice=1

KillMode=none

SuccessExitStatus=0 1

ProtectHome=true

ProtectSystem=full

PrivateDevices=true

NoNewPrivileges=true

WorkingDirectory=/opt/minecraft

ExecStart=java -Xmx%sG -Xms%sG -jar /opt/minecraft/mcserver/paperdirectory/%s --nogui

[Install]

WantedBy=multi-user.target"""
