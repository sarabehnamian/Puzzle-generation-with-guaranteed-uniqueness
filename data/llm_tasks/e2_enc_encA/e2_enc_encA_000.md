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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encA\e2_enc_encA_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/1/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Italian, Japanese, Kenyan, Mexican, Polish
- drink: tea, coffee, juice, milk, soda
- car: Audi, Fiat, Ford, Mini, Volvo
- music: jazz, rock, folk, opera, blues

Clues:
1. The Mexican lives in the middle house.
2. There is exactly one house between the Kenyan and the Italian.
3. The Kenyan lives somewhere to the left of the Italian.
4. The Japanese lives next to the Italian.
5. The Mexican drinks coffee.
6. The tea drinker lives next to the Polish.
7. The Italian drinks soda.
8. The Japanese does not drink juice.
9. The Audi owner drinks soda.
10. The Mini owner drinks coffee.
11. The Fiat is directly left of the Mini.
12. The Ford owner lives next to the Audi owner.
13. The jazz fan lives directly right of the Polish.
14. The opera fan drinks milk.
15. The rock fan drives the Mini.
16. The blues fan lives somewhere to the right of the folk fan.

## Puzzle zebra/1/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- shop: bakery, bookshop, cafe, florist, pharmacy
- owner: Ann, Ben, Cy, Di, Ed
- door: red, blue, green, white, black
- pet: cat, dog, fish, owl, rabbit

Clues:
1. Cy lives in the middle house.
2. The cafe has the green door.
3. The cafe is run by Cy.
4. The bakery is directly left of the cafe.
5. The florist is directly right of the cafe.
6. The bookshop is somewhere to the right of the pharmacy.
7. Ann runs the bakery.
8. Ed lives next to Ann.
9. Ben does not run the florist.
10. The red door is directly left of the green door.
11. The bookshop has the black door.
12. The white door is at one end of the row.
13. The cat lives in the green-door house.
14. The owl owner lives next to Ann.
15. The fish is kept behind the red door.
16. Di does not own the dog.

## Puzzle zebra/3/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: green, red, white, blue, black
- pet: fish, cat, dog, bird, horse
- drink: tea, juice, milk, coffee, water
- sport: tennis, golf, rowing, cycling, boxing

Clues:
1. The milk drinker lives in the middle house.
2. The coffee drinker lives in the blue house.
3. The blue house is directly right of the white house.
4. The dog owner lives in the white house.
5. The dog owner drinks milk.
6. The black house is at one of the ends of the row.
7. The red house is somewhere to the left of the black house.
8. The green house is somewhere to the left of the red house.
9. The tea drinker lives in the green house.
10. The horse owner lives in the black house.
11. The juice drinker lives next to the milk drinker.
12. The bird owner drinks coffee.
13. The cat owner lives directly right of the fish owner.
14. The cyclist drinks coffee.
15. The rower owns the dog.
16. The golfer lives next to the rower.
17. The tennis player lives somewhere to the left of the boxer.

## Puzzle zebra/3/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: maroon, navy, ivory, olive, coral
- pet: snake, ferret, hamster, turtle, parrot
- drink: tea, cider, wine, beer, cola
- hobby: fishing, chess, gardening, knitting, diving

Clues:
1. The navy house is next to the ivory house.
2. The olive house is directly right of the ivory house.
3. The coral house is at the right-hand end.
4. The maroon house is not next to the olive house.
5. The wine drinker lives in the ivory house.
6. The tea drinker lives in the maroon house.
7. The cider drinker lives in the navy house.
8. The beer drinker lives next to the wine drinker.
9. The hamster owner drinks wine.
10. The parrot owner drinks cola.
11. The snake owner drinks tea.
12. The turtle owner lives somewhere to the right of the ferret owner.
13. The fisher drinks tea.
14. The diver lives in the coral house.
15. The chess player drinks cider.
16. The knitter keeps the turtle.

## Puzzle zebra/2/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: green, white, red, blue, yellow
- country: Kenya, Peru, Japan, Spain, Brazil
- instrument: drums, piano, violin, flute, guitar
- snack: cheese, apple, bread, nuts, cake

Clues:
1. The drummer lives in house 1.
2. The Kenyan plays the drums.
3. The Peruvian lives directly right of the Kenyan.
4. The Peruvian lives in the white house.
5. The apple eater lives in the white house.
6. The pianist lives next to the drummer.
7. The Kenyan lives in the green house.
8. The Japanese lives in the red house, which is somewhere to the right of the white house.
9. The violinist lives in the red house.
10. The blue house is directly right of the red house.
11. The Spaniard lives in the blue house.
12. The Brazilian does not live next to the Japanese.
13. The cheese eater plays the drums.
14. The bread eater lives in the red house.
15. The flute player eats nuts.
16. The nuts eater lives in the blue house.

## Puzzle zebra/1/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, Dave, Eve
- fruit: apple, banana, cherry, grape, mango
- city: Paris, Rome, Oslo, Lima, Cairo
- sport: tennis, rowing, golf, boxing, skiing

Clues:
1. Alice eats grapes.
2. The grape eater lives in the middle house.
3. Eve lives directly right of Carol.
4. Bob lives somewhere to the right of Dave.
5. Dave lives next to Alice.
6. Dave eats mango.
7. Bob eats bananas.
8. Carol does not eat apples.
9. Alice is from Paris.
10. Dave is from Cairo.
11. The person from Lima lives directly right of the person from Rome.
12. The golfer eats grapes.
13. Bob goes skiing.
14. The tennis player lives next to the golfer and is from Lima.
15. Dave is not the rower.

## Puzzle zebra/3/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- country: Kenya, Peru, Nepal, Cuba, Chile
- door: purple, green, yellow, red, blue
- drink: cocoa, tea, juice, milk, coffee
- job: nurse, baker, farmer, lawyer, tailor

Clues:
1. There is exactly one house between the Peruvian and the Cuban.
2. The Kenyan lives in an end house.
3. The Chilean lives in an end house.
4. The Kenyan lives somewhere to the left of the Chilean.
5. The Peruvian lives somewhere to the left of the Cuban.
6. The Nepali has the yellow door.
7. The Cuban has the red door.
8. The Chilean has the blue door.
9. The purple door is somewhere to the left of the green door.
10. The Chilean drinks coffee.
11. The tea drinker lives behind the green door.
12. The Nepali drinks juice.
13. The cocoa drinker lives next to the tea drinker.
14. The baker drinks tea.
15. The nurse has the purple door.
16. The farmer drinks juice.
17. The lawyer lives somewhere to the left of the tailor.

## Puzzle zebra/2/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Abe, Bea, Cal, Dot, Eli
- shirt: lime, navy, coral, ochre, silver
- pet: pig, hen, cow, sheep, mule
- crop: corn, wheat, rye, oats, beans

Clues:
1. The cow owner lives in the middle house.
2. The cow owner grows beans.
3. Eli grows beans.
4. Eli wears silver.
5. The navy shirt is directly right of the silver shirt.
6. Dot lives in one of the end houses.
7. Abe lives directly right of Dot.
8. Cal does not live next to Eli.
9. Cal wears ochre.
10. The lime shirt is somewhere to the left of the coral shirt.
11. The wheat grower wears navy.
12. The rye grower wears lime.
13. The oats grower lives next to the wheat grower.
14. The hen lives directly right of the cow.
15. The mule owner grows corn.
16. Cal does not own the pig.

## Puzzle zebra/1/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, blue, green, yellow, purple
- job: doctor, chef, pilot, teacher, artist
- pet: dog, cat, rabbit, parrot, turtle
- hobby: chess, golf, painting, reading, cycling

Clues:
1. The red house is in the middle.
2. The pilot lives in the red house.
3. The chef lives directly left of the doctor.
4. The teacher lives somewhere to the right of the pilot.
5. The artist does not live next to the pilot.
6. The chef lives in the yellow house.
7. The purple house is directly right of the yellow house.
8. The artist does not live in the blue house.
9. The dog lives directly left of the red house.
10. The parrot lives in the green house.
11. The cat owner lives next to the parrot owner.
12. The turtle is not in an end house.
13. The artist's hobby is painting.
14. The golfer lives in the red house.
15. The reader keeps the cat.
16. The chess player lives somewhere to the left of the cyclist.

## Puzzle zebra/3/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: white, green, red, yellow, blue
- pet: rabbit, cat, dog, fish, bird
- drink: juice, tea, coffee, water, milk
- hobby: yoga, chess, baking, golf, tennis

Clues:
1. The green house is directly left of the red house.
2. The yellow house is directly right of the red house.
3. The blue house is at the right-hand end.
4. The white house is next to the green house.
5. The coffee drinker lives in the red house.
6. The tea drinker lives in the green house.
7. The water drinker lives in the yellow house.
8. The juice drinker lives next to the tea drinker.
9. The cat owner drinks tea.
10. The fish owner lives directly right of the dog owner.
11. The bird owner drinks milk.
12. The chess player owns the cat.
13. The tennis player drinks milk.
14. The golfer lives directly right of the baker.
