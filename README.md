# What can this program do?
It grabs every definition of a certain term from urbandictionary.com. It uses the module BeautifulSoup to extract the data
from the page's html.\
The main function ```define(word)``` takes a string as an argument and returns a list of dictionaries, each one containing
a definition and its example.

## Terms that have only one page.
```
print(define('Rio de Janeiro'))
```
The program will return:
```
[{'def': 'The best city EVER! IT HAS HOT WOMEN, GOOD WEATHER, AND HOT WOMEN!!!', 'ex': "Don't need an example. Nothing compares to Rio."}, {'def': '1.) A good city with HOT WOMEN, but a very LARGE crime rate. They were thinking about putting up a wall to trap escaping bullets from the downtown area of the city, but instead lifted all speed limits so that travelers could go faster without being shot.', 'ex': "Brazilian A: Let's do a driveby!\r\nBrazilian B: We can't since the speed limit was lifted. People drive way to fast, and I can't even hit them\r\nBrazilian A: Fuck you, man"}]
```
Since this function returns a list, you can choose elements from it.
```
print(define('Rio de Janeiro')[1])
```
```
{'def': '1.) A good city with HOT WOMEN, but a very LARGE crime rate. They were thinking about putting up a wall to trap escaping bullets from the downtown area of the city, but instead lifted all speed limits so that travelers could go faster without being shot.', 'ex': "Brazilian A: Let's do a driveby!\r\nBrazilian B: We can't since the speed limit was lifted. People drive way to fast, and I can't even hit them\r\nBrazilian A: Fuck you, man"}
```
If your goal is to only select a definition or an example, you may run ```define('Rio de Janeiro')[1]['def']``` or
```define('Rio de Janeiro')[1]['ex']```.


## Terms that have more than one page
```
print(define('botswana')
```
The program will return:
```
[{'def': "the BIGGEST diamond producer in the world. the most politically stable country in the world. the only country which had its first 2 presidents with the title 'SIR'.", 'ex': 'wer r u from? ans: Africa. Botswana'}, {'def': 'African slang meaning " Bitch, I swear. "', 'ex': 'A bushman returns home after a long day of unsuccessful hunting only to discover his wife has burnt the last of the goat meat. He angrily exclaims " Botswana! "'}, {'def': 'to hit the bots so hard that the bots make you wana', 'ex': 'Jesse- "Dude lets go to Botswana tonight go pick up a bot"\r\nShiva "I got the bot but I killed the bot I\'m already at Botswana. Swana swana?"'}, {'def': 'This is when the nipple resides on the boob in relation to where Botswana sits on the globeVery far south', 'ex': 'Those nipples about to fall off the map on those Botswana boobs'}, {'def': 'A white chick lost in the ghetto.', 'ex': 'Check out the botswana bambi, damn she must be far from the comforts of home.'}, {'def': 'A large parcel of cocaine, disguised in baby clothes, in order to smuggle it through border security. Often accompanied by a falsified record of adoption of a child, being taken out of a third world country.', 'ex': '"that bitch be bringin\' us a Botswana baby"'}
```
```
{'def': 'what your stomach feels like when eating things your Mom warned you not to- like : afterbirth, vietnamese whores, anti-freeze, pickled polish sausage, ATMs...', 'ex': "'I shouldn't have done that last ATM with that homeless dude' said the porno queen, ' it gave me botswana tummy'"}, {'def': 'The country that yakko likes for some reason', 'ex': 'Tunisia, Morocco, Uganda, Angola, Zimbabwe, Djibouti, BOTSWANAAAAAAA'}, {'def': 'Anal leakage', 'ex': 'One of the drug warnings was botswana, and I got it, and it burned'}, {'def': "Expertise in something obscure because there's less competition", 'ex': 'I learnt to play jazz double bass because of the Botswana principle'}]
```
The same operations done in the first example can be apllied on searches with multiple pages.
