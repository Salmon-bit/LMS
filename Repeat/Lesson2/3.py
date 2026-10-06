import PIL

n = int(input())
img = Image.new("RGB", (n, n), "red")
draw = ImageDraw.Draw(img)
