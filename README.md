# 翻译窗口
利用google翻译做的一个翻译窗口，自动监视粘贴板。当粘贴板发生变化时，自动翻译粘贴板内容。默认自动检测语言，翻译至中文。其他语言可自行向translate方法传递参数
# 依赖
- python2.7
- pyperclip
  可以使用pip install pyperclip安装
# 使用方法
```
python main.py
```
*在window系统中，也可以直接双击trans.bat*

然后会弹出一个translation窗口
- 点击run按钮，会自动监视粘贴板。当粘贴板发生变化时，自动翻译粘贴板内容
- 点击stop按钮，会暂停监视粘贴板（防止有时候粘贴板上的内容不方便上传）
