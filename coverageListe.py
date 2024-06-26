import os

current_path = os.getcwd()
print(current_path)

folder_path = current_path

folder_path = folder_path.replace('\\', '/')

file_names = os.listdir(folder_path)

for file_name in file_names:
    #print(file_name)
    coverage_files = [file_name for file_name in file_names if file_name.endswith('.coverage')]

#print(coverage_files)

    
for coverage_file in coverage_files:
    with open(os.path.join(folder_path, coverage_file), 'r') as file:
        data = file.read()
        print(coverage_file[:6] + ": " + data)

        with open('output2.txt', 'w') as output_file:
            for coverage_file in coverage_files:
                with open(os.path.join(folder_path, coverage_file), 'r') as file:
                    data = file.read()
                    output_file.write(coverage_file[:6] + " " + data )
