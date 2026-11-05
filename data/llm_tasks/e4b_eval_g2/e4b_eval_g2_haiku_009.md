# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_009.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Clues:
1. The owner of the cat lives in the house just left of the one where the juice drinker lives.
2. The person who enjoys chess lives at one end of the row.
3. The person who keeps the horse lives in the yellow house.
4. The Spaniard lives in house 6.
5. The occupant of the green house lives immediately to the right of the baker.
6. The Brit lives next to the milk drinker.
7. The cocoa drinker lives in one of the two end houses.
8. The Dane enjoys chess.
9. The person who enjoys painting keeps the rabbit.
10. The person who enjoys golf lives in the fourth house.
11. The person who drinks tea works as the doctor.
12. The occupant of the blue house and the Norwegian live two houses apart.
13. The tennis enthusiast lives in one of the two end houses.
14. The bird owner lives in the house just left of the one where the person who keeps the horse lives.
15. The bird owner lives immediately to the right of the coffee drinker.
16. There is exactly one house between the person who keeps the dog and the person who drinks milk.
17. The occupant of the blue house lives in the sixth house.
18. The owner of the horse and the lawyer are neighbours.
19. The Swede and the Spaniard live in adjacent houses.
20. There is exactly one house between the person who enjoys golf and the person who enjoys tennis.
21. The teacher is the German.
22. The German keeps the fish.
23. The German and the person who enjoys tennis are different people.
24. The owner of the bird works as the farmer.
25. The person in the purple house is the Dane.
26. The person who enjoys hiking and the person in the white house are neighbours.
27. The tea drinker lives in a lower-numbered house than the pilot.
28. Whoever lives in the white house and the occupant of the blue house are not neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
