# KeyGen

KeyGen is a script that allows quick query by separating tasks
into multiple threads. The script assumes the case where an
web app needs to provide a query to users quickly.

With metadata such as keywords and title, it can be easily done.
But, in case where the documents lack the meta data, it raises
an issue: IT TAKES DAMN LONG.

KeyGen, however, can fix this issue by _populating keyword vector
for each document._ By running population and user UI in a parallel,
KeyGen need not to worry about a sad user experience. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install numpy.

```bash
pip install numpy
```

## Usage

```bash
make                # when you run the script first time
make input          # if you want to continue adding input
make restart        # delete previous pickle files and start again
```

## Little Math Behind the Scene
I questioned myself while I make KeyGen. What is a decision factor
of keywords?<br>
My quick answer to this was, WHY DO WE BOTHER?

People already know the keyword so let them type them.
So my better question after this was,<br>
If there is a keyword match for this document and that document,
_which one comes first?_

Solely on frequency of the keyword in the document couldn't be
accurate because this meant longer the document, it is more likely
to be more related document for more keywords. Which is not true.
So, I decided to _normalize the keyword vector_ and then call the
document that has highest value to the matching keyword to be
the most related document. Next document next most related and so on.

That's it! I hope I did not make you fall asleep.

## Contributing
Pull requests are welcome. For major changes, please open an
issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
