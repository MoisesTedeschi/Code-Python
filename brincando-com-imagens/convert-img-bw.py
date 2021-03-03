from PIL import Image
'''
pip install Pillow
'''


img = Image.open('img/kakashi.jpeg')
black_and_white = img.convert('L')
black_and_white.save('img/bw_kakashi.jpeg')

black_and_white.show()
