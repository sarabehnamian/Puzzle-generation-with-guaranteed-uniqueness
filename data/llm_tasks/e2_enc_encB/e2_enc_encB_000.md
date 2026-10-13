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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encB/e2_enc_encB_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/3/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Gus, Hana, Ivan, Lena, Kai
- dance: tango, waltz, salsa, polka, swing
- gem: opal, ruby, topaz, onyx, pearl
- month: April, March, July, May, June

Clues:
1. Gus lives in the middle house.
2. Lena lives at one end of the row.
3. Ivan lives somewhere right of Gus.
4. Hana lives directly left of Ivan.
5. The waltz dancer lives next to Gus and is not Hana.
6. The polka dancer lives directly right of Gus.
7. The swing dancer lives at the far right end of the row.
8. Lena does not dance salsa.
9. The ruby is worn by the waltz dancer.
10. The topaz owner lives directly right of the ruby owner.
11. The pearl owner is the swing dancer.
12. The onyx owner does not live at either end of the row.
13. The person born in July owns the topaz.
14. The person born in June is the swing dancer.
15. The person born in March lives directly right of the person born in April.

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

## Puzzle zebra/1/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ana, Bo, Cy, Di, Ed
- fruit: apple, kiwi, lime, melon, fig
- sport: golf, judo, polo, yoga, darts
- city: Bern, Riga, Oslo, Rome, Kiev

Clues:
1. Ana lives in the middle house.
2. Ed and Di each live directly next to Ana, on opposite sides of her.
3. Ed lives to the left of Di.
4. Bo lives somewhere to the right of Cy.
5. Ana eats apples.
6. The fig eater lives directly left of Ana.
7. The kiwi eater lives next to the apple eater and is not the fig eater.
8. The lime eater lives somewhere to the right of the kiwi eater.
9. Bo does yoga.
10. The polo player eats melon.
11. The golfer lives directly left of the darts player.
12. Ed does not do judo.
13. The polo player lives in Rome.
14. The person from Riga does yoga.
15. The person from Bern plays golf.
16. The person from Oslo lives next to the person from Riga.

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

## Puzzle zebra/2/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- flower: Lily, Daisy, Tulip, Orchid, Rose
- bird: Swan, Robin, Finch, Owl, Crow
- tea: Oolong, Mint, Chai, Green tea, Earl Grey
- instrument: Cello, Tuba, Oboe, Lute, Banjo

Clues:
1. The lily is in the house at the far left.
2. The daisy is next to the lily.
3. The tulip is not in either end house.
4. The orchid is directly right of the tulip.
5. The rose is somewhere to the right of the orchid.
6. The crow lives in the house with the rose.
7. The finch lives in the tulip house.
8. The owl lives directly left of the crow.
9. The swan does not live next to the finch.
10. The green tea drinker keeps the owl.
11. Earl Grey is drunk directly right of the green tea.
12. The chai drinker keeps the finch.
13. The mint drinker lives directly left of the chai drinker.
14. The banjo player lives in the rose house.
15. The oboe player drinks chai.
16. The lute player lives directly right of the oboe player.
17. The tuba player drinks mint.
18. There is exactly one house between the swan and the finch.

## Puzzle zebra/1/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Italian, French, Greek, Polish, Dutch
- dish: soup, curry, salad, stew, noodles
- transport: bus, bike, tram, train, taxi
- door: red, blue, green, white, black

Clues:
1. The Dutch person lives in the middle house.
2. The Greek lives directly left of the Dutch person.
3. The French person lives next to the Italian.
4. The Italian lives somewhere to the right of the French person.
5. The Polish person eats curry.
6. The Dutch person eats soup.
7. The French person eats stew.
8. The Italian does not eat noodles.
9. The taxi passenger eats curry.
10. The bike rider eats noodles.
11. The bus rider is Dutch.
12. The tram rider lives somewhere to the right of the train rider.
13. The green door belongs to the bus rider.
14. The Polish person's door is white.
15. The black door is next to the white door.
16. The blue door is not the French person's.

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

## Puzzle zebra/3/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: amber, coral, indigo, olive, silver
- pet: ferret, gecko, goldfish, pony, spider
- drink: cider, lemonade, mead, smoothie, stout
- hobby: baking, chess, knitting, painting, hiking

Clues:
1. The amber house is in the middle of the row.
2. There is exactly one house between the olive house and the silver house.
3. The coral house is not next to the amber house.
4. The silver house is somewhere right of the olive house.
5. The indigo house is somewhere left of the olive house.
6. The goldfish lives in the coral house.
7. The spider lives in the silver house.
8. The pony lives in the olive house.
9. The gecko does not live in the amber house.
10. The mead drinker keeps the goldfish.
11. The lemonade drinker lives in the silver house.
12. The smoothie drinker keeps the ferret.
13. The cider drinker does not live in the indigo house.
14. The knitter drinks mead.
15. The painter drinks lemonade.
16. The chess player lives in the amber house.
17. The baker lives directly right of the hiker.

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
