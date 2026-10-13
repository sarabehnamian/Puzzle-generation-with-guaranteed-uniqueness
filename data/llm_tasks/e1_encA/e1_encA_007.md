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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_007.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00061

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, juice, water
- nationality: Norwegian, German, Swede, Spaniard, Dane
- job: baker, teacher, doctor, lawyer, pilot
- hobby: chess, hiking, golf, cooking, painting

Clues:
1. The doctor lives at one end of the row.
2. The juice drinker lives next to the Norwegian.
3. The teacher and the person who drinks water are neighbours.
4. The cocoa drinker lives directly to the left of the person who drinks juice.
5. The Dane and the lawyer live in adjacent houses.
6. The Dane lives directly to the left of the Swede.
7. The doctor lives somewhere to the left of the person who drinks water.
8. The person who enjoys golf and the person who drinks water live in adjacent houses.
9. The cocoa drinker either enjoys chess or enjoys hiking.
10. The Swede lives in the house just left of the one where the painting enthusiast lives.
11. The person who drinks tea either works as the doctor or works as the lawyer.
12. The German lives in a lower-numbered house than the juice drinker.
13. The German either enjoys hiking or enjoys painting.
14. The golf enthusiast and the Swede live two houses apart.
15. The baker lives somewhere to the right of the cocoa drinker.

## Puzzle plain:zebra-00071

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, purple, red, yellow, blue
- job: pilot, teacher, farmer, lawyer, baker
- nationality: Swede, Spaniard, Dane, Norwegian, German
- drink: water, cocoa, milk, juice, tea

Clues:
1. The Spaniard lives in the house just left of the one where the occupant of the red house lives.
2. Whoever lives in the white house drinks juice.
3. The person in the blue house lives somewhere to the right of the Dane.
4. The German lives in house 5.
5. The baker lives in the purple house.
6. The farmer lives directly to the left of the Spaniard.
7. The Spaniard lives in the middle house.
8. The person who drinks cocoa is the Swede.
9. The pilot and the Swede live in adjacent houses.
10. The person who drinks tea lives in the house just left of the one where the teacher lives.
11. The Dane either drinks cocoa or drinks milk.
12. The Norwegian lives in the house just left of the one where the baker lives.
13. The farmer either drinks cocoa or drinks juice.

## Puzzle plain:zebra-00056

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, horse, cat, fish
- color: blue, purple, red, green, white
- nationality: Dane, German, Norwegian, Swede, Brit
- job: teacher, baker, doctor, farmer, pilot

Clues:
1. There is exactly one house between the Dane and the occupant of the green house.
2. The horse owner lives directly to the left of whoever lives in the white house.
3. The Brit lives directly to the left of the baker.
4. The fish owner and the person in the green house are neighbours.
5. The Swede lives at one end of the row.
6. The German keeps the dog.
7. The fish owner lives next to the person in the red house.
8. The teacher lives in the house just left of the one where the person who keeps the horse lives.
9. The baker lives in the white house.
10. The German lives in the white house.
11. The pilot lives in house 2.
12. Whoever lives in the red house lives in house 2.
13. The fish owner and whoever lives in the purple house live two houses apart.
14. The owner of the cat lives next to the farmer.

## Puzzle hard:zebra_hard-00016

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, cat, fish, rabbit
- drink: milk, juice, water, tea, coffee
- hobby: painting, golf, tennis, cooking, hiking
- color: yellow, white, blue, purple, green

Clues:
1. One of the neighbours of the person in the purple house enjoys golf.
2. The right-hand neighbour of whoever lives in the purple house lives in the white house.
3. One of the neighbours of the person who keeps the dog lives in the yellow house.
4. The occupant of the blue house has only one neighbour.
5. If the owner of the fish does not enjoy cooking, then that person enjoys painting.
6. The person who enjoys tennis lives somewhere between the tea drinker and the person who drinks water.
7. One of the neighbours of the person who drinks water lives in the green house.
8. The milk drinker and the tennis enthusiast are one and the same person.
9. The cat owner and the cooking enthusiast are one and the same person.
10. One of the neighbours of the tea drinker keeps the cat.
11. Exactly 0 houses lie to the left of the home of the juice drinker.
12. Exactly 1 house lies to the left of the home of the person who keeps the horse.
13. One of the neighbours of the person who enjoys painting lives in the yellow house.
14. The person who enjoys cooking lives in the fifth house from the right.

## Puzzle paraphrase:zebra-00167

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, baker
- drink: juice, coffee, tea, cocoa, milk
- color: red, green, purple, yellow, white
- pet: fish, cat, horse, dog, bird

Clues:
1. The fish owner and the lawyer live two doors apart.
2. The purple house is immediately to the left of the tea drinker's house.
3. The coffee drinker lives next door to the dog owner.
4. The juice drinker and the white house's occupant live in neighbouring houses.
5. Milk is drunk by someone living in one of the two end houses.
6. The purple house is directly to the right of the white house.
7. The bird belongs to the coffee drinker.
8. The purple house is where the dog owner lives.
9. The cat is owned by the baker.
10. The doctor lives right beside the dog owner.
11. The green house and the red house have exactly one house between them.
12. The farmer lives immediately to the left of the purple house's occupant.
13. The green house is the middle one.
14. The green house's occupant and the horse owner are two houses apart.

## Puzzle plain:zebra-00064

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Brit, Spaniard, Dane
- job: lawyer, baker, farmer, doctor, pilot
- color: green, purple, yellow, white, blue
- drink: coffee, cocoa, juice, milk, water

Clues:
1. The Dane and the milk drinker live in adjacent houses.
2. The occupant of the yellow house either is the Brit or is the Norwegian.
3. The occupant of the blue house and the farmer live two houses apart.
4. There is exactly one house between whoever lives in the purple house and the person who drinks water.
5. The person who drinks cocoa and the milk drinker live in adjacent houses.
6. The doctor drinks juice.
7. The Spaniard lives in house 4.
8. The baker is the German.
9. The baker and the Dane live two houses apart.
10. The person who drinks juice and the Norwegian live in adjacent houses.
11. The pilot lives in a lower-numbered house than the farmer.
12. The juice drinker lives somewhere to the right of the person in the green house.
13. The farmer and the pilot live two houses apart.
14. The Dane lives in the house just left of the one where the person who drinks coffee lives.

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

## Puzzle hard:zebra_hard-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, red, blue, white, purple
- job: pilot, doctor, farmer, baker, lawyer
- hobby: hiking, cooking, chess, tennis, golf
- nationality: Dane, Swede, Norwegian, Brit, German

Clues:
1. Neither the person who enjoys chess nor the cooking enthusiast is the Brit.
2. One of the neighbours of the person who enjoys cooking works as the pilot.
3. The Swede does not live to the right of the Norwegian.
4. The left-hand neighbour of the occupant of the purple house is the Dane.
5. The left-hand neighbour of the lawyer enjoys hiking.
6. The lawyer lives further to the right than the Dane.
7. If the German is not the baker, then that person works as the farmer.
8. The person who enjoys chess and the person in the green house are one and the same person.
9. Whoever lives in the green house lives somewhere between whoever lives in the purple house and the tennis enthusiast.
10. One of the neighbours of the baker is the Brit.
11. The German lives somewhere between the Dane and whoever lives in the white house.
12. The right-hand neighbour of the pilot works as the lawyer.
13. The left-hand neighbour of the person who enjoys golf lives in the blue house.
14. One of the neighbours of the Swede lives in the blue house.
15. One of the neighbours of the German enjoys chess.

## Puzzle paraphrase:zebra-00126

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, coffee
- job: pilot, baker, teacher, lawyer, doctor
- nationality: Spaniard, Norwegian, Dane, German, Swede
- color: blue, white, green, yellow, red

Clues:
1. The yellow house is the first house.
2. The occupant of the blue house does not drink tea.
3. The cocoa drinker and the Norwegian do not live next door to each other.
4. The water drinker and the white house have exactly one house between them.
5. The blue house's occupant and the cocoa drinker are not the same person.
6. The doctor and the water drinker live two houses apart.
7. The blue house stands directly to the left of the Dane's house.
8. The red house is not next door to the teacher.
9. The lawyer and the Spaniard live two houses apart.
10. The pilot and the tea drinker live next door to each other.
11. One house separates the cocoa drinker from the Spaniard.
12. The German lives right beside the white house.
13. The green house stands directly to the left of the cocoa drinker's house.
14. The coffee drinker lives in the white house.
