print("Generating Map \n");

from PIL import Image

from Map import *
from Generator import *
from Classes import *
from Vector import *

image = Image.new("RGB", (mapSize,mapSize))
targetGenerator = None

targetGenerator = MapGen_Main();

print("Generating... \n");

targetGenerator.GenerateFull();

print("\n\nGeneration finished. Saving output as Generated.png.");

for x in range(0, mapSize):
    for y in range(0, mapSize):
        image.putpixel((x,y), colorMap[x][y].GetTuple());

image.save("Generated.png");
image.show();
