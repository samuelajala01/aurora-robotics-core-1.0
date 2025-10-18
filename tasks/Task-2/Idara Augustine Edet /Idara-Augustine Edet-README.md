## First, I went through the code line-by-line writing comments on my understanding of the codes
## In this README file, I will explain the extra details and uses of the lines of code that I understood when I did research about them. Any extra details about the lines of code that were too long to be included in the main code are talked about here 

## NumPy is a library used for numerical operations such as the trigonometry i.e cosine and sine, theta, etc., linear algebra, matrices and much more. There are trigonometric variables that we have present in the code. It makes thing easier as we don't have to predefine what these variables are in the code, reducing the workload. In computation heavy code, you need to create maximum performance and Numpy is much faster than normal python math operations. The line "Import numpy as np" is used to import the library as well as assign another name to numpy i.e. np, that is easier to use in code

## Matplotlib.pyplot is a library used for plotting and creating useful visualizations. It is useful in this code beavue ut enables us to visulaize how the changung of angles actually affects the end-effector's coordinates in space. This is the essence of forward kinematics. It also works great with numerical computing libraries like numpy which is useful in this code.  There are widgets also included in a library called matplotlib.widgets which includes the graphical user interface that make the plots interactive and easier to use. The slider is imported to make the visualizing the change of angles easier

## Since we are designing the arm ourselves, we always know the length of the links. They remain constant and aren't toggled like the angles because it creates a predictable movement which allows for precise calculations.

## The function fk used in lines 10 - 16 is used instead of a loop for various reasons. A function runs a specific block of code and can be called numerous times within the code which makes the code more organized and easy to maintain. The function fk takes in parameters, which in this case are theta1 and theta2. When the function is called later in the code, the values they take are called arguments. The function returns three things as tuples

## I noticed that a function to convert from degrees to radians was used in lines 28 and 29. This is because numpy functions work in radians and not degrees. Therefore, the conversion is necessary. Later on, the function rad2deg is used to convert back to degrees in line 44 and 45 so it can be used for the initial values of the slider.

## The next section of the code defines how the plot will look. It ensures that irrespective of the length of the links that the entire arm can be displayed. It sets the scale of the plot, sets whether on not to include gridlines as well as defines the style and width of the gridlines. 

## The next section calls the function fk and assigns its return values to the base, the link and the end-effector. The base is usually found at the origin, hence being assigned to (0,0). The link is found at the first set of x and y coordinates i.e. (x1,y1) and the end-effector is found at the second set of coordinates i.e. (x2,y2). These three values are tuples, which is why indexing is used in line 33 to 35 to plot the arm.

## As an addition, I will be adding a 3rd link to the code and plotting it.
## This is done by adding the forward kinematics equation to the function fk and adding theta3 as a parameter. 
