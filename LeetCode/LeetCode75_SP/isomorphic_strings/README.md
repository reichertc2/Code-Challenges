# Isomorphic Strings

Given two strings ```s``` and ```t```, ***determine if they are isomorphic***.

Two strings ```s``` and ```t``` are isomorphic if the characters in ```s``` can be replaced to get ```t```.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Example 1

```PYTHON
Input: s = "egg", t = "add"
Output: true
```

## Example 2

```PYTHON
Input: s = "foo", t = "bar"
Output: false
```

## Example 3

```PYTHON
Input: s = "paper", t = "title"
Output: true
```

## Constraints

- ```1 <= s.length <= 5 * 104```
- ```t.length == s.length```
- ```s``` and ```t``` consist of any valid ascii character.

## Notes

Passed in pytest. Even LeetCode actual and expected match, still marked wrong.
