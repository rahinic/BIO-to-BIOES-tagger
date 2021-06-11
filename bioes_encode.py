import argparse

parser = argparse.ArgumentParser(description='Change encoding from BIO to BIOES')
parser.add_argument('input', metavar='-i', type=str, help='The path to the original file with BIO encoding')
parser.add_argument('output', metavar='-o', type=str, help='The name of your BIOLU encoded file')
args = parser.parse_args()

input_file = args.input
output_file = args.output


def read_file(input_file):
    with open(input_file, 'rb') as f:
        return f.read().decode('ASCII').split('\n')


def write_line(new_label: str, prev_label: str, line_content: list, output_file):
    new_iob = new_label + prev_label
    if len(new_iob) == 2:
        new_iob = new_iob[0]
    line_content[2] = new_iob
    current_line = ' '.join(line_content)
    output_file.write(current_line + '\n')


def convert(input_file, output_path):
    output_file = open(output_path, 'w')

    for i in range(len(input_file) + 1):

        try:
            current_line = input_file[i]

            if '-DOCSTART-' in current_line:
                output_file.write(current_line + '\n')
            elif len(current_line) == 0:
                output_file.write(current_line + '\n')


            else:
                prev_iob = None
                next_iob = None
                prev_line = None
                next_line = None

                try:
                    prev_line = input_file[i - 1]
                    next_line = input_file[i + 1]

                    if len(prev_line) > 0:
                        prev_line_content = prev_line.split()
                        prev_iob = prev_line_content[2]
                        #print(f"Previous line content: {prev_line_content} and previous iob: {prev_iob}")

                    if len(next_line) > 0:
                        next_line_content = next_line.split()
                        next_iob = next_line_content[2]
                        #print(f"Next line content: {next_line_content} and previous iob: {next_iob}")

                except IndexError:
                    pass

                current_line_content = current_line.split()
                current_iob = current_line_content[2]

                
                #print(f"Current line content: {current_line_content} and previous iob: {current_iob}")
                


                # 00. End of line entities
                if (". . O O" in current_line):
                    output_file.write(current_line + '\n')

                # 01. Last(End) element entities
                elif(". . O O" not in prev_line or len(prev_line) != 0) and (". . O O" in next_line):
                    write_line('E-', current_iob[2:], current_line_content, output_file)

                # 02. First(Begin) element entities 
                elif (". . O O" in prev_line or len(prev_line) == 0 or str(current_iob)[0] == 'B') and (". . O O" not in next_line):
                    write_line('B-', current_iob[2:], current_line_content, output_file)

                # 03. Single entities
                elif (". . O O" in prev_line or len(prev_line) == 0) and (". . O O" in next_line):
                    write_line('S-', current_iob[2:], current_line_content, output_file)

                # 04. Intermediate element (1)
                elif (str(prev_iob)[0] == 'B' or str(prev_iob)[0] == 'O' or str(prev_iob)[0] == 'I') and prev_line != ". . O O" and (str(next_iob)[0] != 'E') and current_iob != 'O':
                    write_line('I-', current_iob[2:], current_line_content, output_file)

                # 05. Other entities 
                elif(". . O O" not in current_line and current_iob =='O' and str(prev_iob)[0] != 'B'):
                    write_line('O', current_iob[2:], current_line_content, output_file)

                # 06. Intermediate element (2)
                elif(". . O O" not in current_line and current_iob =='O' and str(prev_iob)[0] == 'B'):
                    write_line('I-', current_iob[2:], current_line_content, output_file)

        except IndexError:
            pass

bio = read_file(input_file)
convert(bio, output_file)
