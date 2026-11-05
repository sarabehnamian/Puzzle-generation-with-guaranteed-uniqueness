# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 6-house logic-grid puzzle with a known unique solution. A language-model
solver attempted it; its mistakes are listed. Propose 2 variants of each puzzle that you expect to
be HARDER for a language-model solver, while staying solvable by pure step-by-step deduction.

You edit puzzles with operations on the formal clue list:
- {"op": "remove", "clue": <clue number>}
- {"op": "add", "clue": {"type": <type>, "args": [...]}}
- {"op": "replace", "clue": <clue number>, "with": {"type": <type>, "args": [...]}}
Use 1 to 4 operations per variant. Clue types (a, b, c are value names; k is a house number):
  same(a,b)        a and b belong to the same person
  not_same(a,b)    a and b belong to different people
  at(a,k)          a is in house k            not_at(a,k)     a is not in house k
  left_of(a,b)     a is directly left of b    next_to(a,b)    a and b are neighbours
  not_next_to(a,b) a and b are not neighbours (they may share a house)
  before(a,b)      a is somewhere left of b   gap2(a,b)       exactly one house between a and b
  end(a)           a is in house 1 or house 6
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_mut_g1\e4b_mut_g1_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4b-g1-11

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Formal clues (with their English text):
1. gap2(farmer, red)   "There is exactly one house between the farmer and the occupant of the red house."
2. not_next_to(bird, brit)   "The person who keeps the bird does not live next to the Brit."
3. or(dog, lawyer, teacher)   "The person who keeps the dog either works as the lawyer or works as the teacher."
4. same(tennis, white)   "The person who enjoys tennis lives in the white house."
5. or(cocoa, doctor, pilot)   "The cocoa drinker either works as the doctor or works as the pilot."
6. next_to(norwegian, yellow)   "The Norwegian and whoever lives in the yellow house live in adjacent houses."
7. or(baker, horse, rabbit)   "The baker either keeps the horse or keeps the rabbit."
8. gap2(cat, cocoa)   "The cat owner and the cocoa drinker live two houses apart."
9. next_to(golf, tea)   "The person who enjoys golf and the person who drinks tea are neighbours."
10. next_to(cat, purple)   "The cat owner lives next to the occupant of the purple house."
11. before(water, swede)   "The water drinker lives somewhere to the left of the Swede."
12. gap2(blue, doctor)   "There is exactly one house between the occupant of the blue house and the doctor."
13. same(cooking, fish)   "The person who enjoys cooking keeps the fish."
14. left_of(tea, green)   "The tea drinker lives in the house just left of the one where whoever lives in the green house lives."
15. not_same(coffee, purple)   "Whoever lives in the purple house and the coffee drinker are different people."
16. or(rabbit, dane, german)   "The owner of the rabbit either is the Dane or is the German."
17. left_of(rabbit, horse)   "The owner of the horse lives immediately to the right of the person who keeps the rabbit."
18. left_of(norwegian, german)   "The Norwegian lives in the house just left of the one where the German lives."
19. same(golf, lawyer)   "The golf enthusiast works as the lawyer."
20. at(german, 6)   "The German lives in the sixth house."
21. not_same(brit, red)   "The Brit does not live in the red house."
22. next_to(green, tennis)   "Whoever lives in the green house and the person who enjoys tennis are neighbours."
23. same(coffee, painting)   "The painting enthusiast drinks coffee."
24. same(bird, farmer)   "The bird owner works as the farmer."
25. gap2(chess, lawyer)   "The person who enjoys chess and the lawyer live two houses apart."
26. left_of(yellow, horse)   "Whoever lives in the yellow house lives directly to the left of the horse owner."
27. gap2(horse, purple)   "There is exactly one house between the owner of the horse and whoever lives in the purple house."
28. same(blue, juice)   "Whoever lives in the blue house drinks juice."

Solution: house 1: brit, dog, tea, teacher, tennis, white; house 2: cat, golf, green, lawyer, spaniard, water; house 3: bird, farmer, hiking, milk, purple, swede; house 4: chess, cocoa, dane, doctor, rabbit, yellow; house 5: baker, coffee, horse, norwegian, painting, red; house 6: blue, cooking, fish, german, juice, pilot
Solver mistakes: brit (put in house 2, correct 1); spaniard (put in house 1, correct 2)
Solver cell accuracy so far: 0.94

## Puzzle e4b-g0-01

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Formal clues (with their English text):
1. next_to(green, norwegian)   "The person in the green house lives next to the Norwegian."
2. before(german, fish)   "The German lives somewhere to the left of the person who keeps the fish."
3. same(baker, dog)   "The person who keeps the dog works as the baker."
4. end(golf)   "The person who enjoys golf lives at one end of the row."
5. gap2(cocoa, milk)   "There is exactly one house between the person who drinks cocoa and the milk drinker."
6. left_of(doctor, hiking)   "The hiking enthusiast lives immediately to the right of the doctor."
7. same(green, lawyer)   "The person in the green house works as the lawyer."
8. not_next_to(green, tennis)   "Whoever lives in the green house and the person who enjoys tennis are not neighbours."
9. at(brit, 1)   "The Brit lives in the first house."
10. same(dog, water)   "The person who drinks water keeps the dog."
11. gap2(horse, milk)   "The owner of the horse and the milk drinker live two houses apart."
12. same(rabbit, swede)   "The Swede keeps the rabbit."
13. at(blue, 6)   "Whoever lives in the blue house lives in the last house."
14. next_to(cat, tea)   "The cat owner and the tea drinker live in adjacent houses."
15. left_of(golf, chess)   "The person who enjoys golf lives directly to the left of the person who enjoys chess."
16. left_of(cat, teacher)   "The teacher lives immediately to the right of the cat owner."
17. same(doctor, fish)   "The owner of the fish works as the doctor."
18. left_of(farmer, lawyer)   "The lawyer lives immediately to the right of the farmer."
19. next_to(dane, dog)   "The Dane lives next to the dog owner."
20. left_of(white, juice)   "Whoever lives in the white house lives in the house just left of the one where the person who drinks juice lives."
21. same(cat, red)   "The person in the red house keeps the cat."
22. at(yellow, 3)   "The person in the yellow house lives in house 3."
23. left_of(dog, doctor)   "The owner of the dog lives in the house just left of the one where the doctor lives."
24. gap2(cooking, white)   "There is exactly one house between the cooking enthusiast and the occupant of the white house."

Solution: house 1: bird, brit, coffee, farmer, golf, purple; house 2: chess, cocoa, german, green, horse, lawyer; house 3: baker, dog, norwegian, painting, water, yellow; house 4: dane, doctor, fish, milk, tennis, white; house 5: cat, hiking, juice, pilot, red, spaniard; house 6: blue, cooking, rabbit, swede, tea, teacher
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-03

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Formal clues (with their English text):
1. left_of(baker, milk)   "The milk drinker lives immediately to the right of the baker."
2. at(dane, 3)   "The Dane lives in the third house."
3. same(cooking, german)   "The person who enjoys cooking is the German."
4. same(brit, white)   "The occupant of the white house is the Brit."
5. same(dog, water)   "The owner of the dog drinks water."
6. next_to(fish, horse)   "The owner of the fish and the person who keeps the horse are neighbours."
7. at(cocoa, 5)   "The cocoa drinker lives in the fifth house."
8. next_to(chess, doctor)   "The chess enthusiast lives next to the doctor."
9. left_of(teacher, blue)   "Whoever lives in the blue house lives immediately to the right of the teacher."
10. or(lawyer, milk, water)   "The lawyer either drinks milk or drinks water."
11. or(juice, horse, rabbit)   "The person who drinks juice either keeps the horse or keeps the rabbit."
12. left_of(blue, brit)   "The Brit lives immediately to the right of the person in the blue house."
13. left_of(norwegian, fish)   "The owner of the fish lives immediately to the right of the Norwegian."
14. same(pilot, yellow)   "The pilot lives in the yellow house."
15. before(red, rabbit)   "The person in the red house lives in a lower-numbered house than the owner of the rabbit."
16. same(baker, tea)   "The baker drinks tea."
17. next_to(brit, purple)   "The Brit and the person in the purple house live in adjacent houses."
18. gap2(lawyer, milk)   "There is exactly one house between the lawyer and the milk drinker."
19. same(golf, spaniard)   "The Spaniard enjoys golf."
20. same(milk, tennis)   "The tennis enthusiast drinks milk."
21. same(coffee, golf)   "The golf enthusiast drinks coffee."
22. before(red, spaniard)   "The person in the red house lives in a lower-numbered house than the Spaniard."
23. same(painting, water)   "The person who drinks water enjoys painting."
24. same(cat, cooking)   "The owner of the cat enjoys cooking."

Solution: house 1: baker, cat, cooking, german, red, tea; house 2: bird, milk, pilot, swede, tennis, yellow; house 3: dane, green, hiking, juice, rabbit, teacher; house 4: blue, dog, lawyer, norwegian, painting, water; house 5: brit, chess, cocoa, farmer, fish, white; house 6: coffee, doctor, golf, horse, purple, spaniard
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
