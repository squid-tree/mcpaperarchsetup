serviceinfo = """
[Unit]

Description=Minecraft Server

After=network.target

[Service]

User=minecraft

Nice=1

KillMode=none

SuccessExitStatus=0 1

ProtectHome=true

ProtectSystem=full

PrivateDevices=true

NoNewPrivileges=true

WorkingDirectory=/opt/minecraft/mcserver

ExecStart=java -Xmx%s%s -Xms%s%s -jar /opt/minecraft/mcserver/paperdirectory/%s nogui

ExecStop=mcrcon -H 127.0.0.1 -P 25575 -p %s stop

[Install]

WantedBy=multi-user.target"""
