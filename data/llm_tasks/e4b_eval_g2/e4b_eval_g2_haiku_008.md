# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_008.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Clues:
1. The hiking enthusiast and the occupant of the white house live in adjacent houses.
2. Whoever lives in the yellow house keeps the horse.
3. The person in the white house lives in house 3.
4. The person who drinks coffee lives directly to the left of the owner of the bird.
5. The person who drinks tea works as the doctor.
6. The person who drinks juice lives immediately to the right of the cat owner.
7. There is exactly one house between the golf enthusiast and the person who enjoys tennis.
8. The golf enthusiast and the occupant of the white house are neighbours.
9. The chess enthusiast lives at one end of the row.
10. The farmer keeps the bird.
11. The person who keeps the horse and the lawyer live in adjacent houses.
12. The Spaniard lives in one of the two end houses.
13. The person in the green house lives immediately to the right of the baker.
14. The German works as the teacher.
15. The occupant of the blue house lives in the sixth house.
16. There is exactly one house between the occupant of the blue house and the Norwegian.
17. There is exactly one house between the person who keeps the dog and the person who drinks milk.
18. The tea drinker lives in a lower-numbered house than the pilot.
19. The cocoa drinker lives in one of the two end houses.
20. The owner of the fish is the German.
21. The Swede lives in house 5.
22. The person who enjoys painting keeps the rabbit.
23. The Dane lives in the purple house.
24. The horse owner lives immediately to the right of the bird owner.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
