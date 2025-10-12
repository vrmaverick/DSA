def find_subsets_bfs(nums):
    """
    Generates all subsets (the Power Set) of a given list of numbers 
    using the Breadth-First Search (iterative) pattern.

    Args:
        nums (list[int]): The input set represented as a list.

    Returns:
        list[list[int]]: A list containing all possible subsets.
    """
    # 1. Start with an empty list containing just the empty set [[]].
    # This list represents our queue/current collection of subsets.
    subsets = [[]]

    # 2. Iterate through each number in the input list.
    for number in nums:
        # Get the current number of subsets we have so far.
        n = len(subsets)
        
        # 3. Iterate through all EXISTING subsets.
        # We must use 'n' here because we'll be adding new subsets during this loop.
        for i in range(n):
            # Take a copy of the existing subset.
            # Using list slicing [:] ensures we get a shallow copy, so we don't modify the original subset in place.
            current_subset = list(subsets[i]) # list() or [:] creates a copy ########################################################### Important function to list(from list) converts to list or either use slicing, failing to use may cause list mai hii update
            
            # 4. Create a NEW subset by adding the 'number' to the copy.
            current_subset.append(number)
            
            # 5. Add this newly created subset to our main collection.
            subsets.append(current_subset)

    return subsets



def find_permutations(s: str) -> list[str]:
    """
    Finds all unique permutations of a string using recursion and backtracking.

    Args:
        s (str): The input string.

    Returns:
        list[str]: A list of all unique permutations.
    """
    results = []

    # Helper function to perform the backtracking search
    def backtrack(current_permutation, remaining_characters):
        # Base Case: If there are no characters left, a complete permutation is formed.
        if not remaining_characters:
            results.append("".join(current_permutation))
            return

        # Recursive Step: Try placing each remaining character next.
        for i in range(len(remaining_characters)):
            # 1. Choose: Select the current character.
            char = remaining_characters[i]
            
            # 2. Explore: 
            #   - Add the chosen character to the current permutation.
            current_permutation.append(char)
            
            #   - Recursively call backtrack with the remaining characters.
            #     (The new 'remaining_characters' is the list without the chosen character 'char'.)
            new_remaining = remaining_characters[:i] + remaining_characters[i+1:]
            
            backtrack(current_permutation, new_remaining)
            
            # 3. Backtrack: Undo the choice to explore other branches.
            #   - Remove the character from the current permutation.
            current_permutation.pop()

    # Start the recursion with an empty permutation and all characters from the input string.
    backtrack([], list(s))
    
    return results

# --- Example Usage ---
input_string = "abc"
permutations = find_permutations(input_string)

print(f"String: '{input_string}'")
print(f"Total Permutations: {len(permutations)}")
print(f"Permutations: {permutations}")

print("\n" + "-" * 30)

input_string_2 = "cat"
permutations_2 = find_permutations(input_string_2)
print(f"String: '{input_string_2}'")
print(f"Permutations: {permutations_2}")
