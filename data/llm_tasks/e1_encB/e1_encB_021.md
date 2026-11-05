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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_021.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00110

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, golf, tennis
- pet: horse, rabbit, fish, bird, dog
- drink: milk, cocoa, tea, coffee, juice
- nationality: Dane, Swede, Spaniard, Norwegian, Brit

Clues:
1. Whoever drinks juice is a golf enthusiast.
2. The Brit and the rabbit keeper live two houses apart.
3. The cocoa drinker's house is immediately to the left of the Dane's house.
4. The horse belongs to the cooking enthusiast.
5. The rabbit is kept in house 5.
6. The coffee drinker lives somewhere to the right of the Dane.
7. The tennis enthusiast lives directly to the left of the chess enthusiast.
8. The dog owner drinks juice.
9. The hiking enthusiast lives directly to the left of the dog owner.
10. The Swede occupies the leftmost house.
11. The Norwegian lives immediately to the right of the golf enthusiast.
12. The fish owner and the milk drinker are next-door neighbours.

## Puzzle paraphrase:zebra-00144

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee
- pet: horse, fish, dog, rabbit, cat
- nationality: Spaniard, Dane, Norwegian, Swede, Brit
- color: green, purple, red, blue, yellow

Clues:
1. Water is drunk by the person in house 4.
2. The Dane is the water drinker.
3. The Spaniard lives in house 5.
4. The Brit and the yellow house's occupant are two houses apart.
5. The green house's occupant drinks water.
6. The rabbit owner and the tea drinker live two houses apart.
7. Juice is drunk in the yellow house.
8. The purple house and the water drinker are two houses apart.
9. The fish keeper lives in one of the two end houses.
10. One house separates the coffee drinker from the juice drinker.
11. The cat owner lives somewhere right of the fish keeper.
12. The blue house's occupant and the cat owner are not neighbours.
13. One end of the row is where the Norwegian lives.
14. The blue house's occupant keeps the horse.
15. The Spaniard is the person in the red house.

## Puzzle plain:zebra-00044

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- pet: cat, bird, dog, fish, horse
- drink: milk, cocoa, water, coffee, tea
- color: green, purple, blue, white, yellow

Clues:
1. The person who drinks coffee lives in the third house.
2. The Spaniard either keeps the fish or keeps the horse.
3. The person who keeps the dog and the person who drinks water live in adjacent houses.
4. The person who keeps the dog and the Swede are neighbours.
5. The occupant of the purple house either keeps the fish or keeps the horse.
6. The person in the white house keeps the horse.
7. There is exactly one house between the cocoa drinker and the Dane.
8. The person who keeps the fish lives in the house just left of the one where the cat owner lives.
9. The person who drinks tea lives in the second house.
10. The person in the yellow house lives immediately to the right of the person who keeps the bird.
11. The owner of the cat lives in house 5.
12. The Brit lives in the third house.
13. The owner of the fish lives directly to the left of the person in the green house.

## Puzzle paraphrase:zebra-00185

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, lawyer, pilot, doctor, farmer
- nationality: Norwegian, Brit, Swede, Spaniard, Dane
- hobby: chess, cooking, hiking, tennis, painting
- drink: tea, juice, water, milk, coffee

Clues:
1. The farmer and the milk drinker have exactly one house between them.
2. Water is drunk in the second house.
3. The doctor's drink is coffee.
4. The Brit lives immediately right of the tea drinker.
5. The pilot's hobby is hiking.
6. The Spaniard lives in one of the end houses.
7. The tennis player is either the baker or the pilot.
8. The baker lives immediately to the left of the Brit.
9. The painter is the Spaniard.
10. The Dane drinks either juice or tea.
11. The lawyer lives immediately to the left of the milk drinker.
12. The doctor's hobby is either cooking or hiking.
13. The cooking enthusiast lives next door to the Swede.

## Puzzle paraphrase:zebra-00179

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Swede, Spaniard, Brit
- color: yellow, blue, red, green, white
- drink: cocoa, tea, coffee, water, juice
- job: lawyer, doctor, baker, pilot, farmer

Clues:
1. The German does not live next door to the water drinker.
2. The red house is immediately to the right of the tea drinker.
3. The Dane lives in the first house.
4. The baker lives at one end of the row.
5. The farmer lives next door to the German.
6. The lawyer is the tea drinker.
7. The green house and the juice drinker are two houses apart.
8. The pilot lives in the blue house.
9. One house lies between the red house and the yellow house.
10. The farmer is the Brit.
11. The white house is immediately to the left of the Spaniard.
12. The Brit lives at one end of the row.
13. The Brit lives somewhere to the right of the cocoa drinker.
14. The red house's occupant drinks coffee.

## Puzzle hard:zebra_hard-00003

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, bird, cat
- color: green, white, red, purple, blue
- job: pilot, baker, farmer, teacher, lawyer
- hobby: painting, cooking, hiking, tennis, chess

Clues:
1. Exactly 0 houses lie to the left of the home of the hiking enthusiast.
2. The pilot and the person in the white house are one and the same person.
3. One of the neighbours of the hiking enthusiast keeps the bird.
4. If the occupant of the green house is not the farmer, then that person works as the pilot.
5. The person who enjoys chess lives further to the right than whoever lives in the green house.
6. The person who keeps the cat lives somewhere between the baker and the fish owner.
7. None of the neighbours of the occupant of the white house lives in the red house.
8. The person who keeps the fish and the teacher are one and the same person.
9. The person who enjoys painting and the person in the white house are one and the same person.
10. One of the neighbours of the teacher keeps the dog.
11. The bird owner and the person in the green house are one and the same person.
12. If the occupant of the blue house is not the baker, then that person works as the farmer.
13. One of the neighbours of the cooking enthusiast keeps the dog.
14. The cooking enthusiast does not live in the second house from the right.

## Puzzle plain:zebra-00087

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, tea, cocoa
- hobby: cooking, tennis, hiking, chess, golf
- job: baker, pilot, lawyer, farmer, teacher
- pet: bird, cat, fish, horse, rabbit

Clues:
1. The person who drinks cocoa and the person who drinks water live in adjacent houses.
2. The chess enthusiast lives somewhere to the right of the tennis enthusiast.
3. The pilot keeps the rabbit.
4. The person who keeps the cat lives directly to the left of the owner of the fish.
5. The water drinker either keeps the fish or keeps the rabbit.
6. The cocoa drinker and the person who enjoys tennis are neighbours.
7. The rabbit owner enjoys chess.
8. The lawyer keeps the fish.
9. The coffee drinker either keeps the fish or keeps the horse.
10. The person who enjoys hiking does not keep the fish.
11. The baker and the person who drinks coffee are not neighbours.
12. The person who enjoys cooking lives in house 2.
13. The person who keeps the bird lives immediately to the right of the owner of the horse.
14. The farmer enjoys cooking.
15. The tennis enthusiast lives in a lower-numbered house than the milk drinker.
16. The tennis enthusiast drinks tea.

## Puzzle plain:zebra-00090

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Dane, Swede, Brit
- job: farmer, doctor, pilot, baker, teacher
- color: purple, red, white, yellow, green
- pet: bird, rabbit, horse, cat, fish

Clues:
1. There is exactly one house between the bird owner and the Swede.
2. The fish owner lives immediately to the right of the Brit.
3. The pilot lives in house 2.
4. The farmer lives in the house just left of the one where the Spaniard lives.
5. The doctor either is the Dane or is the Norwegian.
6. The Norwegian lives next to the occupant of the purple house.
7. The occupant of the purple house lives immediately to the right of the baker.
8. The person who keeps the fish and the owner of the horse live in adjacent houses.
9. The owner of the fish lives immediately to the right of the person in the yellow house.
10. The owner of the cat and the doctor live in adjacent houses.
11. The Spaniard lives directly to the left of the doctor.
12. The person in the green house either is the Dane or is the Spaniard.
13. Whoever lives in the green house and the occupant of the red house live two houses apart.

## Puzzle paraphrase:zebra-00155

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, painting, hiking, tennis
- drink: water, milk, coffee, juice, tea
- color: white, yellow, blue, green, purple
- pet: cat, bird, dog, horse, fish

Clues:
1. The hiker drinks coffee.
2. The juice drinker lives in house 4.
3. Exactly one house lies between the green house and the purple house.
4. The blue house's occupant and the tea drinker are neighbours.
5. The bird owner lives immediately to the left of the purple house's occupant.
6. The cooking enthusiast lives next door to the water drinker.
7. The golfer and the tennis player live next to each other.
8. The tennis player doesn't keep the dog.
9. One house sits between the bird's owner and the yellow house's occupant.
10. The juice drinker lives somewhere to the right of the yellow house.
11. The golfer and the horse keeper are not neighbours.
12. The fish owner lives immediately to the left of the cat owner.
13. The painter lives in a lower-numbered house than the hiker.
14. The milk drinker and the tennis player are not next-door neighbours.
15. The white house's occupant enjoys either cooking or painting.
16. The fish owner and the water drinker live next door to each other.
17. The tennis player lives in either the green house or the purple house.

## Puzzle paraphrase:zebra-00100

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, horse, cat, fish
- drink: tea, water, juice, coffee, milk
- hobby: chess, tennis, painting, cooking, hiking
- job: lawyer, pilot, doctor, baker, farmer

Clues:
1. The doctor and the farmer live next door to each other.
2. The milk drinker lives in house 3.
3. Somewhere to the left of the chess enthusiast lives the cat owner.
4. The juice drinker lives directly to the left of the cooking enthusiast.
5. One house separates the coffee drinker from the farmer.
6. The cooking enthusiast lives right next to the horse keeper, on the left side.
7. The doctor's house has a lower number than the lawyer's.
8. The dog owner lives immediately to the left of the tennis enthusiast.
9. The fish owner and the tea drinker are neighbours.
10. Two houses separate the cooking enthusiast's home from the hiker's... that is, they live two houses apart.
11. The doctor and the lawyer live two houses apart.
12. The baker occupies house 2.
13. The person who keeps the bird loves hiking.
