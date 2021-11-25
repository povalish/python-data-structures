from structures.stack.stack import Stack


def match_delimiters(expression) -> bool:
  opening_delims = '({['
  closing_delims = ')}]'
  stack: Stack[str] = Stack()

  for symbol in expression:
    if symbol in opening_delims:
      stack.push(symbol)

    if symbol in closing_delims:
      if stack.is_empty():
        return False

      last_open_delim = stack.pop()
      if opening_delims.index(last_open_delim) != closing_delims.index(symbol):
        return False

  return stack.is_empty()



if __name__ == '__main__':
  print(f"Example 1: {match_delimiters('()(()){([()])}')}")
  print(f"Example 2: {match_delimiters('((()(()){([()])}))')}")
  print(f"Example 3: {match_delimiters(')(()){([()])}')}")
  print(f"Example 4: {match_delimiters(')')}")
