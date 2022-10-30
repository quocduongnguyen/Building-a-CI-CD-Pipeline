ssh-keygen -t rsa
cat /home/nguyen/.ssh/id_rsa.pub
git clone git@github.com:quocduongnguyen/Building-a-CI-CD-Pipeline.git
cd Building-a-CI-CD-Pipeline/
python3 -m venv ~/.myrepo
source ~/.myrepo/bin/activate
make all
pip3 install locust
az webapp log tail -g duongnq9-project2-devops-rg --name duongnq9-project2-webapp
locust --headless --users 10 --spawn-rate 1 -H https://duongnq9-project2-webapp.azurewebsites.net
chmod +x  make_predict_azure_app.sh
./make_predict_azure_app.sh