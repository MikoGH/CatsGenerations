from PIL import Image

def to_rgb(hex):
    return (int(hex[1:3], 16),int(hex[3:5], 16),int(hex[5:7], 16))

''' Изображение кота '''
class Cat_Image():
    def set_image(color, moons_name):
        zoom = 10
        real = 17
        size = real * zoom
        image = Image.new(mode="RGBA", size=(size, size))
        if moons_name == 'old' or moons_name == 'young':
            moons_name = 'adult'
        folder = f'patterns/{moons_name}/'

        bg_color = (150,150,150)
        matrix = [[bg_color for i in range(real)] for j in range(real)]
        matrix = Cat_Image.draw(matrix, folder, "shillouette.png", color.primary.color)
        matrix = Cat_Image.draw(matrix, folder, "eyes.png", color.eyes.color)
        for pattern in color.patterns:
            matrix = Cat_Image.draw(matrix, folder, pattern+".png", color.secondary.color)

        for i in range(size):
            for j in range(size):
                image.putpixel((i, j),matrix[i//zoom][j//zoom])  

        return image
    
    def draw(matrix, folder, image_name, color):
        image_shillouette = Image.open(folder + image_name)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if image_shillouette.getpixel((i,j)) == (0, 0, 0, 255): 
                    matrix[i][j] = to_rgb(color)        
        return matrix
        

