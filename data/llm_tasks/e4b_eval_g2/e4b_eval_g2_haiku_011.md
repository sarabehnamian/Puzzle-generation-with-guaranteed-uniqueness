# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_011.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The coffee drinker and the owner of the dog are not neighbours.
2. Whoever lives in the white house is the Brit.
3. The owner of the fish and the horse owner live in adjacent houses.
4. The person in the red house lives in a lower-numbered house than the owner of the rabbit.
5. The Spaniard enjoys golf.
6. The baker lives directly to the left of the milk drinker.
7. The occupant of the green house is the Dane.
8. The occupant of the red house lives in a lower-numbered house than the Spaniard.
9. The Brit lives immediately to the right of the Norwegian.
10. The pilot enjoys tennis.
11. The person who enjoys painting drinks water.
12. The Brit lives next to whoever lives in the purple house.
13. The tennis enthusiast drinks milk.
14. The occupant of the blue house lives directly to the left of the Brit.
15. The Norwegian lives in the house just left of the one where the person who keeps the fish lives.
16. The person who keeps the cat enjoys cooking.
17. The lawyer either drinks milk or drinks water.
18. The person who drinks juice either keeps the horse or keeps the rabbit.
19. The golf enthusiast drinks coffee.
20. The cocoa drinker lives next to the coffee drinker.
21. The person who enjoys chess and the doctor live in adjacent houses.
22. The German enjoys cooking.
23. The occupant of the blue house lives in the fourth house.
24. The teacher lives directly to the left of whoever lives in the blue house.
25. The tea drinker works as the baker.
26. The lawyer and the milk drinker live two houses apart.
27. The person who drinks water keeps the dog.
28. The occupant of the yellow house works as the pilot.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
