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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encB\e2_enc_encB_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/3/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Kara, Jack, Liam, Hugo, Iris
- sport: rugby, judo, archery, swimming, tennis
- meal: salad, pizza, soup, curry, pasta
- scarf: teal, orange, pink, gray, brown

Clues:
1. Hugo lives directly right of Liam.
2. Jack lives directly left of Liam.
3. Kara lives somewhere to the left of Jack.
4. Iris lives somewhere to the right of Hugo.
5. Iris plays tennis.
6. Hugo is the swimmer.
7. The rugby player lives in an end house.
8. The judo player lives directly left of the archer.
9. The soup eater lives in the middle house.
10. The curry eater is the swimmer.
11. The pizza eater lives next to the rugby player.
12. The salad eater lives somewhere to the left of the pasta eater.
13. The orange scarf belongs to the judo player.
14. The gray scarf is directly right of the pink scarf.
15. The curry eater wears the gray scarf.
16. The pasta eater wears the brown scarf.

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

## Puzzle zebra/1/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: cream, lilac, maroon, navy, orange
- job: baker, clerk, judge, nurse, pilot
- pet: ferret, gecko, koi, pigeon, tortoise
- drink: ale, cola, juice, tea, wine

Clues:
1. The clerk and the nurse live at opposite ends of the row.
2. The baker lives next to the judge.
3. The pilot lives somewhere to the right of the baker.
4. The nurse lives next to the pilot.
5. The judge lives in the cream house.
6. The baker lives in the orange house.
7. The cream house is directly right of the orange house.
8. The pilot lives in the lilac house.
9. The nurse does not live in the navy house.
10. The baker keeps the koi.
11. The tortoise owner lives next to the nurse.
12. The ferret owner lives in the cream house.
13. The pigeon owner is not the clerk.
14. The tea drinker keeps the koi.
15. The wine drinker lives in the lilac house.
16. The cola drinker lives in the middle house.
17. The clerk drinks ale.

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

## Puzzle zebra/2/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ann, Ben, Cy, Di, Ed
- car: Audi, BMW, Fiat, Ford, Kia
- city: Rome, Oslo, Lima, Bern, Cairo
- pet: cat, dog, owl, frog, hamster

Clues:
1. Ann lives in the middle house.
2. Di lives directly left of Ben.
3. Cy lives in one of the two end houses.
4. Ed lives somewhere to the left of Ann.
5. Ann drives the Kia.
6. The BMW driver lives next to Ann.
7. The Audi driver lives directly left of the Kia driver.
8. Cy drives the Ford.
9. The Audi driver is from Rome.
10. The Kia driver is from Cairo.
11. The person from Lima lives directly right of the person from Cairo.
12. Ben is not from Oslo.
13. The owl owner is from Oslo.
14. The dog owner drives the BMW.
15. The frog owner lives next to the dog owner.
16. The cat owner lives directly right of the owl owner.
17. Ann owns the hamster.

## Puzzle zebra/1/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Irish, Greek, Thai, Peruvian, Swiss
- drink: beer, cocoa, juice, tea, water
- pet: hamster, horse, lizard, mouse, snail
- hobby: knitting, sailing, baking, diving, yoga

Clues:
1. The Swiss lives in the middle house.
2. The Swiss drinks water.
3. The Thai lives next to the Swiss.
4. The beer drinker lives directly right of the water drinker.
5. The Irish drinks beer.
6. The Greek lives next to the Thai.
7. The Thai drinks juice.
8. The Peruvian does not drink tea.
9. The snail owner drinks water.
10. The mouse owner drinks tea.
11. The hamster owner is Irish.
12. The horse owner lives next to the Swiss.
13. The knitter keeps the snail.
14. The sailor keeps the horse.
15. The diver lives directly left of the baker.

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

## Puzzle zebra/3/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Thai, Mexican, Italian, Dane, Kenyan
- instrument: drums, piano, harp, cello, flute
- dessert: flan, cake, mousse, gelato, pie
- transport: tram, bike, ferry, scooter, bus

Clues:
1. The Mexican lives next to the Thai.
2. The Italian lives directly right of the Mexican.
3. The Kenyan lives in an end house.
4. The Dane lives somewhere to the right of the Italian.
5. The Dane does not live in an end house.
6. The Mexican plays the piano.
7. The cellist lives next to the Italian.
8. The flute player is Kenyan.
9. The drummer lives somewhere to the left of the harpist.
10. The cake lover plays the piano.
11. The mousse eater plays the harp.
12. The pie eater lives directly right of the gelato eater.
13. The bike rider eats cake.
14. The Dane rides the scooter.
15. The ferry passenger does not live in an end house.
16. The tram rider eats flan.

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
