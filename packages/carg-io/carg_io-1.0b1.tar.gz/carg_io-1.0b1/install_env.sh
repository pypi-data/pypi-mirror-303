
source ~/.bashrc

conda create --prefix ./.venv -y python=3.11

conda activate ./.venv
conda install pip -y
pip install -e .[dev]


