import pyqrcode


code = pyqrcode.create('Hello. Uhh, can we have your liver?')
code.svg('live-organ-transplants.svg', 3.6)
code.svg('live-organ-transplants.svg', scale=4, module_color='purple', background='white')
code.svg('organ-transplants.svg', scale=4, module_color='red', background='white')
code.svg('transplants.svg', scale=4, module_color='blue', background='white')