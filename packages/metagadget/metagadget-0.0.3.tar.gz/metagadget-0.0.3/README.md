# MetaGadget
## はじめに
- Raspberry Pi Zero 2 W, Zero Wでの動作を想定しています。
- OSはRaspbian OS Lite を使用してください。 
## 環境構築
gitとエディタのインストール
```bash
sudo apt-get install git gitk vim
```
RPi.GPIO のインストールにpython3-devが必要
```bash
sudo apt-get install python3-dev
```
最近の Raspbian OS は仮想環境じゃないと pip が動かないので venv をインストール
```bash
python -m venv venv
```
仮想環境構築
```bash
. venv/bin/activate
```
pipで必要パッケージのインストール
```bash
pip install -U Flask ngrok RPi.GPIO
```
## 使い方
起動時に ngrok の TOKEN と DOMAIN 名を渡す
```bash
NGROK_DOMAIN="YOUR.ngrok-free.app" NGROK_AUTHTOKEN="YOUR TOKEN" python your_app.py
```