Dungeons and Dragons Random Character Creator

Based on the site 'Who the Fuck is my DnD Character'


# character_gen functions #
**def introduction_scream()**
```
Retrieves all of the possible introductions that the program
can say, before randomly selecting one of them
```


**def character_scream()**
```
Retrieves all possible descriptors, classes, races, etc needed to
put together a random character from predetermined list
```


**def big_scream()**
```
Prints introduction_scream() and character_scream()
```


**def save_character()**
```
Saves the character to a json file
```


**def class_saving_throws()**
```
No function currently
```


**def c_page_assembly()**
```
Retrieves the modified stats for the generated character and
places them into a dictionary for later use
```


**def save_character()**
```
Saves the generated character and its stats into a json file
*Note that it saves the files in the 'saved characters' folder*
```


**def main()**
```
Main driver
```


# stat_gen functions #
**def race_check(race)**
```
Checks what race was rolled and logs it for later use
```


**def apply_racial_stat**
```
Applies the relevant stat increases based on what race was rolled
```


**def generate_ability_score(dice_type)**
```
Generates ability scores based on whichever type of dice
is selected, either a D20 or 4D6
```


**def stat_modifier()**
```
Eventually will calculate the stat modifier for each stat and
add them to the json
*Work in Progress*
```


**def pass_scores()**
```
Retrieves the dictionary containing the stats
```
