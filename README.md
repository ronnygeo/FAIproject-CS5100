## Introduction

**Social Effects on People from Different Cultures**
This research is focused on finding out how a user's social circle might influence his preferences for users from different parts of the world or culture.

#### Previous Work:
An application uses KNN to create an artificial agent that can recommend eating places to a user. Our agent will parse through the user's information with an aim to understand different characteristics about the user. Then based on that we will provide different recommendations to the user. Additionally, through user’s feedback, the agent will evolve its preference model and recommendation function. 

### Initial Results
| user_id                | No of friends | Estimated User Location       | training factor | with friends  |     | without friends |     |
|------------------------|---------------|-------------------------------|-----------------|---------------|-----|-----------------|-----|
|                        |               |                               |                 | No of reviews | MAE | No of reviews   | MAE |
| 0tYlK-FieQXAdmTQ9DWTbA | 4             | Goodyear, Arizona, US         | 0.75            | 362           | 0.7 | 100             | 1.1 |
| PuTmcfPDLNUAKo68LmdZOA | 36            | Litchfield Park, Arizona, US  | 0.75            | 2977          | 1.3 | 99              | 1.3 |
| 22-6yC05pgWbLupHZTjQig | 38            | Montreal, Quebec, CA          | 0.75            | 448           | 1.5 | 100             | 0.7 |
| gUr8qs00wFAk851yHMlgRQ | 86            | Summerlin South, Nevada, US   | 0.75            | 8560          | 1.2 | 199             | 0.9 |
| 2l2lRFuHLdyGjAuusqPDag | 116           | Whitney, Nevada, US           | 0.75            | 10627         | 0.8 | 199             | 0.7 |
| 22glItKiH7hQRWszhmcohw | 124           | Spring Valley, Nevada, US     | 0.75            | 8905          | 0   | 100             | 1.1 |
| crHk39O5I5ZEpzNQz6XgAw | 159           | Summerlin South, Nevada, US   | 0.75            | 13761         | 0.7 | 99              | 0   |
| pEVf8GRshP9HUkSpizc9LA | 165           | Phoenix, Arizona, US          | 0.75            | 8549          | 1.1 | 682             | 0.7 |
| WdzFfqEoVWqh8bp9mkzPfA | 168           | Spring Valley, Nevada, US     | 0.75            | 14326         | 0.5 | 199             | 1   |
| Iu3Jo9ROp2IWC9FwtWOaUQ | 453           | Paradise, Nevada, US          | 0.75            | 37327         | 1.1 | 869             | 0   |
| 9A2-wSoBUxlMd3LwmlGrrQ | 618           | Spring Valley, Nevada, US     | 0.75            | 36245         | 0.9 | 988             | 0   |
| QlOc_cKy_7Fs-Pg0vi9NAg | 703           | Charlotte, North Carolina, US | 0.75            | 26382         | 0.7 | 199             | 1.1 |
| kGgAARL2UmvCcTRfiscjug | 2332          | Paradise Valley, Arizona, US  | 0.75            | 57798         | 1.1 | 783             | 0.5 |

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
