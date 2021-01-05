# Text Markovify

## Description
This repo is the assignment of the Reading and Writing Electronic Text course at ITP.  

The assignment was use predictive models to generate text: either a Markov chain or a neural network, or both.

I created a program that uses a Markov chain to combine **The Wonderful Wizard of Oz** and **Peter Pan**, and generate a new story out of it.

The program creates character-level models of each book's text with the n-gram length of 10 and combines the two models, equally weighted using `markovify.combine()`.

And lastly, the program generates sentences using `make_short_sentence()` until it finds 4 sentences starting with "Dorothy", and another 4 sentences starting with "Peter". 
The length of the characters in each sentence is limited to 100.

In the future, I would like to use [Markovify with SpaCy's part-of-speech](https://github.com/jsvine/markovify#extending-markovifytext) to generate a Markov model that obeys sentence structure better than a naive model.

## Example output
```
Dorothy was left of the forest, and then he'll get you.”

Peter struck true and deep.

Dorothy could see that you were crying,” she said, “I have come for her.

Peter cried.

Dorothy reached the nest fell into the smallest star of all called out:  “Don’t chase me!”

Peter was honest just now to lull Wendy's suspicion.

Dorothy said, with hesitation, “You are very kind to me.

Peter put the eggs into this hat and looked at her, and not far away she saw a Scarecrow!”
```

## How to use
1. Installation of python3 is required. Follow [this guide](https://realpython.com/installing-python/) to install it.
2. Run the following commands in the Terminal. (replace the path/to/file.txt)
```
git clone https://github.com/cuinjune/text-markovify.git
cd text-markovify
pip install -r requirements.txt
python main.py
```

## Author
* [Zack Lee](https://www.cuinjune.com/about): MPS Candidate at [NYU ITP](https://itp.nyu.edu).
