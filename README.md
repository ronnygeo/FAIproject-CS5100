## Introduction

**Social Effects on People from Different Cultures**
This research is focused on finding out how a user's social circle might influence his preferences for users from different parts of the world or culture.

#### Previous Work:
An application uses KNN to create an artificial agent that can recommend eating places to a user. Our agent will parse through the user's information with an aim to understand different characteristics about the user. Then based on that we will provide different recommendations to the user. Additionally, through user’s feedback, the agent will evolve its preference model and recommendation function. 

#### Research Professor
* Yakov, Bart [Northeastern]

#### Research Assistant
* [Ronny Mathew](http://github.com/ronnygeo)


## Packages Used

`pymongo >= 3.1.1`

`plotly`

`reverse-geocoder`

`numpy`

`scipy`


To install all packages `cd` to the working directory and run, 

`pip install -e .`

## How to run

1. Clone this repo to your local machine using `git clone <repo link>`
2. `cd` to the root of the directory
3. Download all the required packages using the command `pip install -e`
4. Run `app.py`. That's it!

## File Structure
    
- `helpers:`
    Contains all the helper files.

- `util:`
    This folder contains all the utility functions.
    File Operations
    Dictionary Operations
    
- `static:`
    - csv
    - json
    
- 'lib:'
    This folder contains the codes for manipulating data, database and algorithms.

- `algorithm:`
    This folder contains the actual KNN algo.

- `docs:`
    Contains all the docs related to the project
    
- `models:`
    Contains the model data classes

- `plots`
    Contains the code for the graphs

- `tests`
    Testing

- `app.py` main file to run the program

- `settings.py` contains all the predefined settings

- `setup.py` to setup the project

## Graphs

The following graph shows the location of the user, the number of businesses in the area and the predicted businesses.
It takes `time` and `location` restrictions into consideration.

![Graph showing all the information](https://github.com/rohitbegani/FAIproject-CS5100/blob/master/docs/images/full-better-image.png)

## Performance

Our algorithm gives an MAE (Mean Absolute Error) of:

- Without any restrictions on the database: `-`
- With time and location restrictions on the database: `-`

The fact that we already have a restricted database gives us a MAE of `-` but restricting it further changes our MAE value by a factor of `-`. With a deeper dataset our algorithm would give an even better MAE value. 

## License

The MIT License (MIT)

Copyright (c) 2015-2017

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
