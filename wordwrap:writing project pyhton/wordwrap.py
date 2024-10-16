#Noah Taylor lab 5


#define the fucntion
def word_wrap(input_file, output_file, line_width): 
    with open(input_file, 'r') as file:
        words = file.read().split()
#reads the input file
    lines = []
    line = "" 
#variable initializing
    for word in words:
        if len(line) +len(word) + 1 > line_width:
            lines.append(line)
            line = word
        else:
            line += " " + word if line else word 
#processing the words
    if line:
        lines.append(line)

    with open(output_file, 'w') as file:
        for line in lines:
            file.write(line + '\n')
#writes output file
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
line_width = int(input("Enter the line width: "))

word_wrap(input_file, output_file, line_width)
#input & function calling
print("\nThank you for using the noah wordwrap code")
