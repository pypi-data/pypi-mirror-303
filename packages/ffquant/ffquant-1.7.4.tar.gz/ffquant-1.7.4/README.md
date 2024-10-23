# Install JupyterHub

```SHELL
curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin tljhadmin --version 1.0.0b1
```

Edit ~/.profile, add the following to the end

```SHELL
export PATH=/opt/tljh/user/bin/:$PATH
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
nvm install 20.17.0
nvm alias default 20.17.0
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt install -y nodejs
wget https://github.com/apache/rocketmq-client-cpp/releases/download/2.0.0/rocketmq-client-cpp-2.0.0.amd64.deb
sudo dpkg -i rocketmq-client-cpp-2.0.0.amd64.deb
sudo -E /opt/tljh/user/bin/python3 -m pip install backtrader matplotlib dash pandas psutil ffquant numpy rocketmq-client-python
sudo -E /opt/tljh/user/bin/python -m pip install jupyterlab-git==0.44.0
sudo -E /opt/tljh/user/bin/jupyter lab build
sudo systemctl restart jupyterhub jupyter-tljhadmin
```

Visit http://192.168.25.144 in your browser

Log in as tljhadmin and set your password


# Let new user register with username and password
```SHELL
sudo tljh-config set auth.type nativeauthenticator.NativeAuthenticator
sudo tljh-config reload
```

BE CAREFULL!!! When this feature is enabled, the admin user has to go through the sign-up process. Username must be the same with the one used in the installation command.

Admin user authorizes user registration at http://192.168.25.144/hub/authorize

# Disable Terminal
Log in as admin. Open the terminal and execute commands:

```SHELL
jupyter notebook --generate-config
sudo mv /home/jupyter-tljhadmin/.jupyter/jupyter_notebook_config.py /opt/tljh/user/etc/jupyter/
```

Edit /opt/tljh/user/etc/jupyter/jupyter_notebook_config.py and change c.NotebookApp.terminals_enabled to False.

```SHELL
sudo systemctl restart jupyterhub jupyter-tljhadmin
```

# Disable Culling Idle Servers
```SHELL
sudo tljh-config set services.cull.max_age 0
sudo tljh-config set services.cull.timeout 31536000
sudo systemctl restart jupyterhub jupyter-tljhadmin
```

# Compile ffquant and upload to PyPi
python -m pip install setuptools wheel twine

Increase version number in setup.py

python setup.py sdist bdist_wheel

python -m twine upload dist/*

Ask Joanthan for PyPi API token.