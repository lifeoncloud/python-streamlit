from rembg import remove
from PIL import Image

# install rembg(https://github.com/danielgatis/rembg)
# pip3 install "rembg[cpu,cli]"

input_path = './간장계란밥.png'
output_path = './간장계란밥_output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
