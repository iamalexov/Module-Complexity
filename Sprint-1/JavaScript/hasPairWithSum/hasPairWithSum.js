/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * Refactored using Set.
 * Original complexity was O(n²) due to nested loops.
 * Using a Set allows constant-time lookups and reduces
 * the overall complexity to O(n).
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const number of numbers) {
    const complement = target - number;

    if (seen.has(complement)) {
      return true;
    }

    seen.add(number);
  }

  return false;
}