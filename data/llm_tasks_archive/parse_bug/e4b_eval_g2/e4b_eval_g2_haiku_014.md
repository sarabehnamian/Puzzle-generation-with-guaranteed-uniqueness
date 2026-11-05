# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_014.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The farmer lives in the fifth house.
2. The teacher lives immediately to the right of the person in the green house.
3. The teacher either is the Brit or is the German.
4. The farmer lives immediately to the right of the Dane.
5. The golf enthusiast either works as the farmer or works as the pilot.
6. The painting enthusiast lives somewhere to the right of the teacher.
7. The doctor and the person who enjoys tennis are neighbours.
8. The person in the purple house keeps the horse.
9. There is exactly one house between the person who enjoys cooking and whoever lives in the yellow house.
10. The bird owner and the fish owner are not neighbours.
11. The Brit lives in the white house.
12. The doctor either lives in the red house or lives in the blue house.
13. The baker lives in the green house.
14. There is exactly one house between the cocoa drinker and the Spaniard.
15. The Spaniard enjoys tennis.
16. Whoever lives in the blue house lives immediately to the right of the Brit.
17. The Swede enjoys golf.
18. The milk drinker and the Dane are different people.
19. The person who drinks juice lives in the white house.
20. The occupant of the white house lives immediately to the right of the person who drinks water.
21. The person who keeps the rabbit lives directly to the left of the tennis enthusiast.
22. The person who drinks coffee and the Norwegian live in adjacent houses.
23. The person who enjoys cooking lives immediately to the right of the person who enjoys tennis.
24. The German keeps the dog.
25. The bird owner lives in the second house.
26. The person who enjoys chess does not live in the first house.
27. The person who enjoys golf lives somewhere to the left of the tennis enthusiast.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
