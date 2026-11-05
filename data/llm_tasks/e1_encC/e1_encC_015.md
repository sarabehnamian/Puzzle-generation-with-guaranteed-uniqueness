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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_015.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00060

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, dog, cat, bird
- nationality: Brit, German, Spaniard, Swede, Norwegian
- hobby: tennis, hiking, painting, cooking, chess
- drink: coffee, juice, water, tea, cocoa

Clues:
1. The left-hand neighbour of the tennis enthusiast is the Swede.
2. The Norwegian and the rabbit owner are one and the same person.
3. The left-hand neighbour of the painting enthusiast drinks juice.
4. Exactly 0 houses lie to the left of the home of the Spaniard.
5. If the person who enjoys tennis is not the German, then that person is the Spaniard.
6. If the hiking enthusiast does not keep the bird, then that person keeps the dog.
7. The Brit and the person who keeps the horse are one and the same person.
8. If the person who keeps the cat does not enjoy chess, then that person enjoys painting.
9. The cat owner lives in the fourth house from the right.
10. The left-hand neighbour of the tea drinker drinks coffee.
11. The rabbit owner lives somewhere between the owner of the bird and the horse owner.
12. None of the neighbours of the chess enthusiast keeps the bird.
13. The person who keeps the bird and the water drinker are one and the same person.

## Puzzle paraphrase:zebra-00164

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, golf, tennis
- drink: coffee, milk, water, cocoa, tea
- nationality: Norwegian, Spaniard, Swede, Dane, Brit
- color: blue, purple, red, white, yellow

Clues:
1. The painter lives in the blue house.
2. Exactly one house lies between the milk drinker and the Norwegian.
3. The blue house's occupant and the water drinker live next door to each other.
4. The purple house's occupant drinks tea.
5. The hiker lives in a lower-numbered house than the Dane.
6. The Swede lives somewhere to the left of the red house.
7. The tennis enthusiast lives in house 4.
8. The Brit lives next door to the cocoa drinker.
9. The white house is the middle house.
10. The water drinker lives immediately to the left of the golfer.
11. The purple house's occupant lives next to the Swede.
12. The hiker lives immediately to the right of the Spaniard.

## Puzzle hard:zebra_hard-00029

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, chess, hiking, cooking
- color: purple, yellow, green, red, blue
- pet: dog, bird, fish, cat, horse
- nationality: Spaniard, Dane, Norwegian, Brit, German

Clues:
1. The cooking enthusiast and the owner of the dog are one and the same person.
2. One of the neighbours of the owner of the bird lives in the purple house.
3. If the person in the purple house does not keep the cat, then that person keeps the horse.
4. One of the neighbours of whoever lives in the yellow house keeps the bird.
5. The owner of the dog lives further to the right than the person who enjoys chess.
6. The painting enthusiast and the Spaniard are one and the same person.
7. Exactly one house separates the person who keeps the cat from the German.
8. If the occupant of the green house does not enjoy cooking, then that person enjoys golf.
9. Neither the hiking enthusiast nor the person in the purple house keeps the cat.
10. The hiking enthusiast lives in the second house from the right.
11. One of the neighbours of the person in the purple house lives in the blue house.
12. The person in the yellow house lives somewhere between the Dane and the owner of the fish.
13. One of the neighbours of the cat owner is the Spaniard.
14. At least one house separates the Norwegian from the person in the blue house.
15. The cat owner lives two doors away from the person who enjoys chess.

## Puzzle plain:zebra-00034

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, chess, hiking, golf, cooking
- nationality: Swede, Brit, German, Spaniard, Dane
- job: lawyer, baker, pilot, teacher, farmer
- color: green, red, purple, yellow, blue

Clues:
1. The German lives in the house just left of the one where the golf enthusiast lives.
2. The farmer either enjoys golf or enjoys hiking.
3. Whoever lives in the blue house lives in the second house.
4. The Brit lives in the fourth house.
5. The baker lives in house 1.
6. The Dane works as the farmer.
7. The German lives in the house just left of the one where the Swede lives.
8. The person who enjoys chess and the person who enjoys hiking are neighbours.
9. There is exactly one house between the German and the occupant of the yellow house.
10. The pilot and the person in the red house live in adjacent houses.
11. The painting enthusiast either is the Brit or is the Spaniard.
12. The teacher lives in one of the two end houses.
13. The person in the green house lives directly to the left of the golf enthusiast.

## Puzzle hard:zebra_hard-00084

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, teacher
- hobby: golf, chess, tennis, cooking, painting
- nationality: Spaniard, Dane, Swede, Norwegian, Brit
- pet: cat, dog, fish, bird, horse

Clues:
1. The left-hand neighbour of the farmer keeps the fish.
2. The right-hand neighbour of the person who enjoys painting keeps the bird.
3. The right-hand neighbour of the person who enjoys cooking works as the teacher.
4. The left-hand neighbour of the doctor is the Dane.
5. The left-hand neighbour of the golf enthusiast enjoys cooking.
6. One of the neighbours of the person who enjoys tennis works as the teacher.
7. The Brit lives two doors away from the person who keeps the cat.
8. The owner of the fish lives two doors away from the person who keeps the horse.
9. The left-hand neighbour of the dog owner is the Norwegian.
10. If the lawyer is not the Norwegian, then that person is the Swede.
11. The right-hand neighbour of the teacher is the Swede.
12. The left-hand neighbour of the person who keeps the fish keeps the cat.

## Puzzle plain:zebra-00050

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, bird, fish, cat
- drink: tea, water, cocoa, juice, milk
- job: pilot, baker, farmer, doctor, teacher
- hobby: cooking, painting, golf, hiking, tennis

Clues:
1. The pilot lives in the house just left of the one where the juice drinker lives.
2. The doctor lives somewhere to the right of the person who enjoys tennis.
3. The hiking enthusiast lives at one end of the row.
4. The milk drinker lives directly to the left of the baker.
5. The horse owner lives in house 2.
6. The cocoa drinker and the juice drinker are neighbours.
7. The hiking enthusiast lives somewhere to the left of the cooking enthusiast.
8. The painting enthusiast lives in the house just left of the one where the baker lives.
9. The farmer lives directly to the left of the person who enjoys golf.
10. The farmer and the person who drinks water live two houses apart.
11. The bird owner either works as the pilot or works as the teacher.
12. There is exactly one house between the person who keeps the cat and the person who keeps the dog.
13. There is exactly one house between the person who keeps the cat and the pilot.

## Puzzle hard:zebra_hard-00027

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- color: green, blue, purple, yellow, white
- drink: coffee, milk, cocoa, water, juice
- pet: dog, horse, fish, cat, bird

Clues:
1. The person who keeps the fish and the Spaniard are one and the same person.
2. If the Dane does not keep the fish, then that person keeps the horse.
3. The person who keeps the fish lives two doors away from the person who drinks milk.
4. One of the neighbours of the dog owner drinks cocoa.
5. The Swede lives somewhere between the person who drinks cocoa and the person in the yellow house.
6. The right-hand neighbour of the Dane lives in the green house.
7. The right-hand neighbour of the cat owner lives in the purple house.
8. Exactly one house separates the juice drinker from the Swede.
9. The person who drinks coffee lives two doors away from the Dane.
10. Whoever lives in the yellow house lives somewhere between the cat owner and the person who keeps the fish.
11. The Brit and whoever lives in the white house are one and the same person.
12. The cat owner and the person who drinks coffee are one and the same person.

## Puzzle paraphrase:zebra-00108

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, German, Spaniard, Dane, Swede
- hobby: hiking, chess, golf, painting, tennis
- job: farmer, teacher, pilot, doctor, lawyer
- pet: rabbit, horse, cat, bird, dog

Clues:
1. The rabbit owner lives in house 3.
2. One house lies between the golf enthusiast and the hiker.
3. The Spaniard lives immediately to the left of the dog owner.
4. The Swede lives in house 2.
5. One house separates the lawyer from the tennis enthusiast.
6. The Dane does not live next to the painting enthusiast.
7. The Dane and the teacher live in adjacent houses.
8. The golf enthusiast and the pilot live next door to each other.
9. The hiker is the lawyer.
10. The doctor lives in house 5.
11. The cat owner lives immediately to the left of the bird owner.
12. The Dane and the Norwegian are neighbours.
13. The horse owner lives in house 1.

## Puzzle paraphrase:zebra-00103

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, coffee, juice, water
- nationality: Spaniard, German, Brit, Swede, Norwegian
- hobby: hiking, golf, painting, cooking, chess
- color: red, purple, blue, green, white

Clues:
1. The coffee drinker's hobby is cooking.
2. The Brit lives in the purple house.
3. The cocoa drinker lives right next door to the hiker, on the hiker's right.
4. One house separates the blue house's occupant from the Norwegian.
5. The juice drinker lives in house 2.
6. The cocoa drinker lives somewhere to the right of the Swede.
7. One house lies between the German and the purple house's occupant.
8. The painting enthusiast lives immediately to the left of the Brit.
9. The white house's occupant enjoys hiking.
10. The Norwegian doesn't drink tea.
11. The blue house is house 3.
12. The red house's occupant enjoys golf.
13. The coffee drinker lives in the leftmost house.

## Puzzle hard:zebra_hard-00001

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, baker, farmer, lawyer, teacher
- nationality: Brit, Swede, Spaniard, German, Dane
- drink: milk, juice, water, tea, cocoa
- pet: bird, horse, rabbit, dog, cat

Clues:
1. Neither the cat owner nor the milk drinker works as the doctor.
2. The right-hand neighbour of the German is the Brit.
3. The left-hand neighbour of the baker keeps the horse.
4. The person who drinks cocoa and the doctor are one and the same person.
5. The person who keeps the rabbit lives somewhere between the bird owner and the farmer.
6. The owner of the bird and the teacher are one and the same person.
7. The left-hand neighbour of the Spaniard drinks tea.
8. One of the neighbours of the person who drinks juice keeps the cat.
9. The Dane lives in the fifth house from the right.
10. One of the neighbours of the person who drinks water keeps the bird.
11. The right-hand neighbour of the person who keeps the cat drinks tea.
12. The baker and the water drinker are one and the same person.
