
echo "installing virtual env"

pip3 install virtualenv

echo "activateing env"

powershell env\bin\activate.ps1

powershell pip3 install -r requirements.txt