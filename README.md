Before running this program, ensure that the numpy and PIL packages are installed in your python interpreter.
If it is not, you may install them using the following commands from your command prompt:
python -m pip install numpy
python -m pip install PIL*

*If there is an error in installing PIL, try installing Pillow with 

This program accepts two arguments in the following order:
1) string <image_file> specifies the file name of the image being used
2) int <k> specifies the number of clusters of points being collected

This program takes the inputted image, finds k clusters of similar appoints and assigns their mean value as a group as their value, and outputs the new image. The integer k specifies the number of unique colors in the resulting image. 

Image 1:
First make sure the image shock.jpg is in the same directory as the python file 684HW3Group3.py
Then run the following command in the command prompt: 
python main.py shock.png 5

This should result in a compressed version of shock.jpg composed of 5 unique colors. 
In this command, the number 5 can be changed depending on the image quality you are looking for. 

Dataset 2:
First make sure the image surfs_up.jpg is in the same directory as the python file 684HW3Group3.py
Then run the following command in the command prompt: 
python main.py surfs_up.png 10

This should result in a compressed version of surfs_up.jpg composed of 10 unique colors. 

Dataset 3:
First make sure the image tub.jpg is in the same directory as the python file 684HW3Group3.py
Then run the following command in the command prompt: 
python main.py tub.png 15

This should result in a compressed version of tub.jpg composed of 15 unique colors. 
