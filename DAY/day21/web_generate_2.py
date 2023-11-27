import requests
import io
if __name__ == '__main__':
	from PIL import Image, ImageSequence

	# 从网上获取图片
	url = 'https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg'
	response = requests.get(url)
	image_data = response.content

	# 创建BytesIO对象
	buffer = io.BytesIO(image_data)

	# 打开图片序列
	im = Image.open(buffer)

	# 获取图片序列
	frames = list(ImageSequence.Iterator(im))

	# 循环显示图片序列
	for frame in frames:
		frame.show()