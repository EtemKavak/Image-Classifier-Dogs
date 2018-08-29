
# Image-Classifier-Dogs


### Principle Objectives

- Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
 
- Correctly classify the breed of dog, for the images that are of dogs.
 
- Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives _1_ and _2_.
 
- Consider the time resources required to best achieve objectives _1_ and _2_, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.


### Program Outline

Repeat below for all three image classification algorithms (e.g. input algorithm as command line argument):

#### Time the program
- Use Time Module to compute program runtime

#### Get program Inputs from the user
- Use command line arguments to get user inputs

#### Create Pet Images Labels
- Use the pet images filenames to create labels
_ Store the pet image labels in a data structure (e.g. dictionary)

#### Create Classifier Labels and Compare Labels
- Use the Classifier function classify the images and create the classifier labels
- Compare Classifier Labels to Pet Image Labels
- Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)

#### Classifying Labels as "Dogs" or "Not Dogs"
- Classify all Labels (Pet & Classifier) as "Dogs" or "Not Dogs" using dognames.txt file
- Store new classifications in the complex data structure (e.g. dictionary of lists)

#### Calculate the Results
- Use Labels and their classifications to determine how well the algorithm worked on classifying images.

#### Print the Results


### Programming Concepts and Skills Covered by this Project

##### Use of functions for:
- Task isolation
- Testing code
- Code reuse

##### Timing runtime of a program to understand algorithm complexity-timing trade-off.

##### Use of command line arguments for increased functionality of the program.

##### Checking your program and it's functions as you code (Unit Testing).

##### Complex Data Structures:
- Usage of a dictionary of lists
- Selecting appropriate data structure for data storage
- Appropriate usage of dictionaries (mutable objects) within functions

##### Use of pre-trained Convolutional Neural Network (CNN) model architectures to classify images.

##### Retrieving information from a file, where that information will be used within the program.

##### Comparing different algorithms' results in accuracy and timing.

##### Use of batch files to run multiple programs sequentially.
