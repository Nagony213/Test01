mkdir -p portainer/data
mkdir django
sudo apt update && sudo apt upgrade -y
sudo apt-get install -y net-tools vim make binutils
sudo apt-get install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o \
        /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo apt-get install -y docker-compose
sudo systemctl enable docker
sudo systemctl start docker
sudo docker network create web-server
git clone https://github.com/aws/efs-utils
cd efs-utils
./build-deb.sh
sudo apt install -y ./build/amazon-efs-utils*deb
cd ..
