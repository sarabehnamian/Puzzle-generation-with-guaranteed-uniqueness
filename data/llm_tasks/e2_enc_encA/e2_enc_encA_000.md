# Task: encode logic-grid puzzles as solver constraints

Translate each puzzle below into constraints in a small Python DSL. A program will check your
constraints with a SAT/SMT solver, so they must say exactly what each clue says - no more, no less.

The DSL:
- pos('value') is the house number (an integer from 1 to N) of the given value. Use the value names
  exactly as they appear in the puzzle header (case does not matter).
- The basic rules (every value is in exactly one house; values of the same category are in different
  houses) are added automatically. Do not encode them.
- Encode each numbered clue as ONE Python boolean expression using pos(...), integer constants,
  == != < <= > >= + -, and the functions Abs(x), And(a, b, ...), Or(a, b, ...), Not(a), Implies(a, b).
- Do not use Python's and/or/not/in, chained comparisons such as 1 < x < 3, or abs().

Examples (from other puzzles):
- "The baker keeps the parrot."            ->  pos('baker') == pos('parrot')
- "The violinist lives in the fourth house." ->  pos('violinist') == 4
- "The person who reads poetry lives next to the person who drinks lemonade."
                                            ->  Abs(pos('poetry') - pos('lemonade')) == 1

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encA/e2_enc_encA_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/1/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, David, Eve
- flower: rose, tulip, lily, daisy, orchid
- instrument: piano, violin, flute, drums, harp
- city: Paris, Rome, Oslo, Lima, Cairo

Clues:
1. Carol lives at one end of the row and Bob lives at the other end, with Carol to the left of Bob.
2. Eve lives directly right of Carol.
3. Alice lives in the middle house.
4. Carol grows daisies.
5. The rose grower lives directly right of the daisy grower.
6. The lily grower lives directly left of Bob.
7. Alice does not grow tulips.
8. The harpist lives in the daisy house.
9. The pianist lives directly right of the harpist.
10. The drummer grows orchids.
11. Bob does not play the flute.
12. The person from Lima plays the harp.
13. The person from Oslo plays the piano.
14. The person from Paris is Alice.
15. The person from Rome lives somewhere to the right of the person from Cairo.

## Puzzle zebra/1/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- person: Anna, Ben, Cleo, Dev, Finn
- sport: swimming, tennis, rowing, boxing, judo
- fruit: apple, banana, cherry, lemon, peach
- music: jazz, rock, folk, opera, techno

Clues:
1. There is exactly one house between Anna and Cleo.
2. Finn lives in the middle house.
3. Anna lives somewhere to the left of Cleo.
4. Dev lives somewhere to the left of Ben.
5. Finn plays tennis.
6. Ben is the swimmer.
7. The boxer lives directly left of the swimmer.
8. The rower does not live next to Finn.
9. The lemon lover is the rower.
10. The apple eater does judo.
11. The peach eater is the swimmer.
12. The cherry eater lives directly left of the banana eater.
13. The jazz fan eats cherries.
14. The opera fan is Dev.
15. The rock fan is Cleo.
16. The techno fan does judo.

## Puzzle zebra/3/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: pink, gray, black, orange, brown
- vehicle: tram, bike, van, bus, car
- fruit: mango, apple, cherry, grape, banana
- job: nurse, welder, baker, judge, tailor

Clues:
1. The pink house is at one end of the row.
2. The gray house is directly right of the pink house.
3. The black house is in the middle of the row.
4. The orange house is directly left of the brown house.
5. The baker lives in the black house.
6. The welder lives in the gray house.
7. The judge lives next to the baker.
8. The tailor lives somewhere right of the judge.
9. The person who rides the bus is the judge.
10. The van owner lives in the middle house.
11. The car owner lives directly right of the bus rider.
12. The bike rider is not the nurse.
13. The cherry eater lives in the middle house.
14. The banana eater owns the car.
15. The grape eater lives in the orange house.
16. The apple eater lives next to the cherry eater.

## Puzzle zebra/3/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- profession: actor, banker, clerk, diver, editor
- color: beige, cyan, gold, magenta, teal
- tree: birch, cedar, maple, oak, pine
- pet: crab, newt, owl, pig, yak

Clues:
1. The editor lives in the middle house.
2. The banker and the diver live at opposite ends of the row.
3. The diver lives somewhere left of the banker.
4. The clerk lives somewhere left of the actor.
5. The cyan house is at one end of the row, but it does not belong to the banker.
6. The magenta house belongs to the banker.
7. The gold house is directly right of the cyan house.
8. The teal house belongs to the actor.
9. The cedar grows at the teal house.
10. The birch grows in the banker's garden.
11. The maple grows in the editor's garden.
12. The pine grows somewhere left of the maple.
13. The oak is not in the gold house.
14. The crab lives with the actor.
15. The pig lives next to the crab.
16. The newt lives in the beige house.
17. The owl does not live in the gold house.

## Puzzle zebra/2/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: Green, Black, White, Red, Blue
- pet: Rabbit, Cat, Snake, Owl, Dog
- drink: Tea, Wine, Cola, Beer, Water
- sport: Rugby, Judo, Golf, Tennis, Boxing

Clues:
1. The golf player lives in the middle house.
2. The white house belongs to the golf player.
3. The red house is directly right of the white house.
4. The blue house is next to the red house.
5. The green house is somewhere to the left of the black house.
6. The dog owner lives in the blue house.
7. The snake owner drinks cola.
8. The cola drinker is the golf player.
9. The owl owner lives directly right of the snake owner.
10. The cat owner lives in the black house.
11. The beer drinker lives directly right of the cola drinker.
12. The water drinker owns the dog.
13. The wine drinker lives next to the cola drinker.
14. The tennis player drinks beer.
15. The boxer owns the dog.
16. The judo player drinks wine.

## Puzzle zebra/1/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, blue, green, yellow, white
- pet: dog, cat, parrot, turtle, rabbit
- drink: tea, coffee, milk, juice, cider
- hobby: chess, painting, hiking, cooking, knitting

Clues:
1. The red house is the middle house.
2. The white house is directly right of the red house.
3. The green house is somewhere to the right of the white house.
4. The yellow house is not next to the red house.
5. The cat lives in the green house.
6. The parrot lives in the red house.
7. The rabbit lives directly right of the parrot.
8. The turtle does not live in the blue house.
9. The cider drinker owns the cat.
10. The coffee drinker lives in the white house.
11. The tea drinker lives directly right of the juice drinker.
12. The milk drinker owns the parrot.
13. The chess player drinks milk.
14. The painter lives directly right of the chess player.
15. The knitter owns the cat.
16. The cook drinks tea.

## Puzzle zebra/3/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- language: Greek, Hindi, Latin, Polish, Swahili
- dessert: cake, flan, pie, tart, trifle
- pet: snake, rabbit, parrot, turtle, hamster
- color: ivory, teal, maroon, navy, lime

Clues:
1. The Greek speaker lives in the middle house.
2. The Hindi speaker lives at one end of the row.
3. The Polish speaker does not live next to the Greek speaker.
4. The Latin speaker lives directly left of the Greek speaker.
5. The Polish speaker lives somewhere left of the Hindi speaker.
6. The Hindi speaker lives in the ivory house.
7. The Latin speaker lives in the lime house.
8. The maroon house is directly right of the navy house.
9. The turtle lives in the teal house.
10. The snake owner lives next to the turtle owner.
11. The hamster owner speaks Swahili.
12. The rabbit does not live in the ivory house.
13. The trifle eater keeps the parrot.
14. The rabbit owner eats cake.
15. The flan eater lives in the maroon house.
16. The snake owner does not eat tart.

## Puzzle zebra/2/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- country: Cuba, Spain, Iran, Chad, Italy
- vehicle: Taxi, Bus, Ferry, Tram, Bike
- dessert: Pie, Tart, Gelato, Cake, Flan
- hobby: Dance, Poetry, Hiking, Drawing, Baking

Clues:
1. The Cuban and the Italian live in the two end houses, one at each end.
2. The Spaniard lives directly right of the Cuban.
3. The Chadian lives directly left of the Italian.
4. The Iranian takes the ferry.
5. The Italian rides the bike.
6. The tram rider is either the Cuban or the Chadian.
7. The taxi passenger lives directly left of the bus rider.
8. The gelato eater takes the ferry.
9. The cake eater rides the tram.
10. The flan eater is the Italian.
11. The tart eater lives directly right of the pie eater.
12. The person who enjoys baking eats flan.
13. The hiking fan eats gelato.
14. The poetry lover rides the bus.
15. The drawing fan is the Chadian.

## Puzzle zebra/1/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Norwegian, Swede
- sport: tennis, golf, rugby, cricket, hockey
- car: Audi, Ford, Fiat, Volvo, Mazda
- fruit: apple, pear, plum, grape, mango

Clues:
1. The Norwegian lives in the first house.
2. The Swede lives next to the Norwegian.
3. The Brit lives directly right of the Swede.
4. The German lives somewhere to the left of the Dane.
5. The Norwegian plays hockey.
6. The tennis player lives directly right of the hockey player.
7. The cricket player is the Brit.
8. The golfer is not the Dane.
9. The hockey player drives the Fiat.
10. The Swede drives the Volvo.
11. The Audi owner lives directly left of the golfer.
12. The Dane drives the Ford.
13. The mango eater drives the Fiat.
14. The apple eater lives directly right of the mango eater.
15. The grape eater plays cricket.
16. The pear eater is not the Dane.

## Puzzle zebra/3/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- person: Mia, Noah, Olga, Pete, Quinn
- dish: curry, pasta, ramen, salad, tacos
- sport: judo, golf, polo, yoga, squash
- city: Paris, Rome, Oslo, Lima, Bern

Clues:
1. Quinn lives in the middle house.
2. Mia lives directly left of Quinn.
3. Olga lives directly right of Quinn.
4. Noah lives somewhere right of Olga.
5. The tacos eater lives at one end of the row.
6. Noah does not eat tacos.
7. The curry eater lives in the middle house.
8. The salad eater lives directly right of the curry eater.
9. Mia does not eat pasta.
10. The polo player eats tacos.
11. The judo player eats curry.
12. The golfer eats pasta.
13. The yoga fan is not Olga.
14. The Paris resident does judo.
15. The Oslo resident is the golfer.
16. The Lima resident eats salad.
17. The Bern resident does not play polo.
