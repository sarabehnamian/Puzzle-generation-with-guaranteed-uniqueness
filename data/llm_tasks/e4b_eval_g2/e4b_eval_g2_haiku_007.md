# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_007.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-09

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The person in the white house lives somewhere to the right of the person in the yellow house.
2. The juice drinker lives immediately to the right of whoever lives in the white house.
3. The water drinker keeps the dog.
4. The Swede keeps the rabbit.
5. The German lives in a lower-numbered house than the person who keeps the fish.
6. The person who keeps the dog lives directly to the left of the doctor.
7. The Brit lives in a lower-numbered house than the water drinker.
8. There is exactly one house between the owner of the horse and the person who drinks milk.
9. The doctor keeps the fish.
10. Whoever lives in the blue house and the Brit are not neighbours.
11. The person in the purple house lives in the house just left of the one where the German lives.
12. The person who enjoys golf lives directly to the left of the person who enjoys chess.
13. The owner of the cat and the tea drinker live in adjacent houses.
14. The cat owner lives directly to the left of the teacher.
15. The baker keeps the dog.
16. The lawyer lives immediately to the right of the farmer.
17. The occupant of the green house does not live next to the person who enjoys tennis.
18. Whoever lives in the green house lives next to the Norwegian.
19. The person in the red house keeps the cat.
20. The horse owner lives somewhere to the left of the person who keeps the fish.
21. The hiking enthusiast lives immediately to the right of the doctor.
22. The German keeps the horse.
23. The occupant of the green house works as the lawyer.
24. The cocoa drinker and the milk drinker live two houses apart.
25. The Dane lives next to the dog owner.
26. The Brit lives at one end of the row.
27. There is exactly one house between the person who enjoys cooking and the occupant of the white house.
28. The golf enthusiast lives at one end of the row.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
