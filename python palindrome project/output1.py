#Noah Taylor lab 4 from arraystack
import ArrayStack def
reverse_string(string): stack =
ArrayStack() for char in string:
stack.push(char) reversed_string = ""
while not stack.isEmpty():
reversed_string += stack.pop() return
reversed_string def
is_palindrome(string): return string ==
reverse_string(string) def
reverse_number(number): return
int(reverse_string(str(number))) def
main(): while True: user_input =
input("Enter a string,number, or press
return to quit: ") if not user_input:
print("Thank you for using the noah
code") break if user_input.isdigit():
number = int(user_input)
print(f"Reversed, your number or phrase
is... {reverse_number(number)}") if
is_palindrome(user_input): print("Its a
palindrome") else: print("Its not a
palindrome") if __name__ == '__main__':
main()
