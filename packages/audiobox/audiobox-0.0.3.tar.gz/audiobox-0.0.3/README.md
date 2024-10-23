# AudioBox

AudioBox allows the user to play music and sound effects on any platform as long as you have the files.

## Latest Updates: 
* Made sfx play in a seperate thread like music

## Installation

Install via pip:

```bash
pip install audiobox
```

Example code: 

```py
from audiobox import *

generate_example_files() # Generates two audio clips for example use

sfx("example_sfx") # Handles .mp3 and .wav | Only use the file name and not extension
wait(5)
play_music("example_music") # Handles .mp3 and .wav | Only use the file name and not extension
wait(165)
```

## Links: 
### Website: https://tairerullc.vercel.app/


#### Contact 'tairerullc@gmail.com' for any inquires and we will get back at our latest expense. Thank you for using our product and happy coding!