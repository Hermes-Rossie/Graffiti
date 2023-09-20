def create_dropdown_lists(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        indent_level = 0  # Keep track of the current indentation level
        previous_indent_level = 0  # Keep track of the previous indentation level

        for line in input_file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line:
                # Calculate the current indentation level
                indent_level = len(line) - len(line.lstrip())

                # Close dropdown lists for decreased indentation
                while previous_indent_level > indent_level:
                    output_file.write('  ' * previous_indent_level + '</details>\n')
                    previous_indent_level -= 1

                # Create a dropdown list for increased indentation
                if indent_level > previous_indent_level:
                    output_file.write('  ' * previous_indent_level + '<details>\n')
                    output_file.write('  ' * indent_level + '<summary>' + line + '</summary>\n')
                else:
                    output_file.write('  ' * indent_level + '- ' + line + '\n')

                previous_indent_level = indent_level

        # Close any remaining dropdown lists
        while previous_indent_level > 0:
            output_file.write('  ' * previous_indent_level + '</details>\n')
            previous_indent_level -= 1

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.md"
    create_dropdown_lists(input_file, output_file)