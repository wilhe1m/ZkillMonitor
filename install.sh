echo "installing ZkillMonitor"

echo "doing pip"
pip3 install requirements.txt

echo "installing service (you may need to be root)"
cp ZkillMonitor.service /etc/systemd/system/ZkillMonitor.service

echo "starting service (you may need to be root)"
systemctl start ZkillMonitor.service

echo "done"
