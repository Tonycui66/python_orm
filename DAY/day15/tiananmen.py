from PIL import Image, ImageDraw

# 创建一个大小为300x300像素的黑色图像
image = Image.new('RGB', (300, 300), (0, 0, 0))

# 创建一个白色的画笔
draw = ImageDraw.Draw(image)

# 绘制一个矩形来表示天安门
draw.rectangle((50, 50, 250, 250), fill=(255, 255, 255))

# 绘制天安门的门环
draw.ellipse((150, 150, 160, 160), fill=(255, 255, 255))

# 保存图像到文件
image.save('tiananmen.png')