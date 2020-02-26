from PIL import Image, ImageDraw, ImageFont, ImageTk
import pytesseract
import operator


def print_dict_of_lists(a):
    out_str = ''
    for i in a:
        out_str += i
        out_str += '\t'
    out_str += '\n'
    for j in range(len(a['conf'])):
        for i in a:
            out_str += str(a[i][j])
            out_str += '\t'
        out_str += '\n'
    print(out_str)


def conf_trim(a):
    a_process = {}
    for j in a:
        a_process[j] = []
        for i in range(len(a['conf'])):
            if int(a['conf'][i]) >= 0 and (a['text'][i] == '' or a['text'][i] == ' '):
                a_process[j].append(a[j][i])
    return a_process


def draw_line_boxes(a):
    n_boxes = len(a['conf'])
    img_list = []
    font = ImageFont.truetype("/Library/Fonts/arial.ttf", 20)

    for i in range(n_boxes):
        # Box Shape
        (x, y, w, h) = (a['left'][i], a['top'][i], a['width'][i], a['height'][i])
        # open copy of image
        image_copy = Image.open('SU-4719_P_H_copy.jpg')
        # Open Draw Object on image_copy
        img1 = ImageDraw.Draw(image_copy)
        # Draw our stuff
        img1.rectangle([(x, y), (x + w, y + h)], outline=(0, 255, 0), fill=None)
        img1.text((x, y), a['text'][i], font=font, fill=(0, 255, 0))
        img1.text((100, 100), str(i), font=font, fill=(0, 0, 255))

        # Build a list of images to animate later
        img_list.append(image_copy)
    return img_list


def draw_cells_numbers(grid, numbers):
    font = ImageFont.truetype("/Library/Fonts/arial.ttf", 40)
    # open copy of image
    image_copy = Image.open('SU-4719_P_H_copy.jpg')
    # Open Draw Object on image_copy
    img1 = ImageDraw.Draw(image_copy)
    for i in grid:
        # Box Shape
        (x, y, w, h) = grid[i]
        # Draw our stuff
        img1.rectangle([(x, y), (x + w, y + h)], outline=(0, 255, 0), fill=None)
        img1.text(grid[i], numbers[i], font=font, fill=(0, 0, 255))
    # image_copy.show()
    return image_copy


def find_cells(a):
    grid = {}
    n_lines = len(a['conf'])
    h_lines, v_lines = [], []
    for i in range(n_lines):
        if a['width'][i] > a['height'][i]:
            # (left, top, width, height) - Needed for PIL
            h_lines.append((a['left'][i], a['top'][i], a['width'][i], a['height'][i]))
        else:
            v_lines.append((a['left'][i], a['top'][i], a['width'][i], a['height'][i]))

    ih, iv = 0, 0
    for h in range(len(h_lines)-1):
        for v in range(len(v_lines)-1):

            x = v_lines[v][0] + v_lines[v][2]
            y = h_lines[h][1] + h_lines[h][3]
            cell_width = v_lines[v + 1][0] - x
            cell_height = h_lines[h + 1][1] - y
            # x, y, cell_width, cell_height
            grid[ih, iv] = (x, y, cell_width, cell_height)

            iv += 1
        iv = 0
        ih += 1
    return grid


def point_in_bbox(a, b, c):
    if b[0] < a[0] < c[0] and b[1] < a[1] < c[1]:
        return True
    return False


def near_other_item(i, iset):
    for j in iset:
        # is an item is within 5 (these are pixels) !after! another item in our list remove it
        if 0 < i-j < 5:
            return False
    return True


def identify_cells(grid, config, image):
    numbers_grid = {}
    for i in grid:
        # cropbox = (left, upper, right, lower)
        crop_box = (grid[i][0], grid[i][1], grid[i][0] + grid[i][2], grid[i][1] + grid[i][3])
        cropped = image.crop(crop_box)
        cropped.load()
        # cropped.show()
        digit = pytesseract.image_to_string(cropped, lang='eng', config=config)
        if digit == '' or digit == '-':
            digit = '0'
        print(digit)
        numbers_grid[i] = digit
    return numbers_grid


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
config_numbers = '--psm 10 digits tessedit_char_whitelist=123456789'
config_lines = '--psm 3'

img = Image.open('SU-4719_P_H_copy.jpg')
# text = pytesseract.image_to_string(img, lang='eng', config=config_numbers)
print('Finding Lines')
d = pytesseract.image_to_data(img, config=config_lines, output_type=pytesseract.Output.DICT)
# d_text = pytesseract.image_to_data(img, config=config_lines)
d_process = conf_trim(d)

print('Finding Cells')
cell_grid = find_cells(d_process)

print('Identifying Numbers in cells')
numbers_grid = identify_cells(cell_grid, config_numbers, img)

# print out the tesseract data in an excel pasteable format
# print_dict_of_lists(d_process)

print('Animating - Lines')
album = draw_line_boxes(d_process)
print('Animating - Numbers')

# cell_img = draw_cells(cell_grid)
cells_numbers_image = draw_cells_numbers(cell_grid, numbers_grid)

# album.append(cell_img)
# album.append(numbers_image)
album.append(cells_numbers_image)

album[0].save('out.gif', save_all=True, append_images=album, duration=100, loop=1)

with open('./input/file.txt', 'w') as f:
    out_string = ''
    for i in range(9):
        for j in range(9):
            out_string += str(numbers_grid[(i, j)])
        out_string += '\n'
    f.write(out_string)
    print(out_string)


