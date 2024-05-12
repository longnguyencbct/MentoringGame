import sys
import subprocess
import os

original_stdout = sys.stdout

with open('output checker\\expected_output.txt', 'w') as f:
    sys.stdout = f
    completed_process = subprocess.run(['python', 'output checker\\expected.py'], stdout=subprocess.PIPE, text=True)
    captured_output = completed_process.stdout
    sys.stdout = original_stdout
    f.write(captured_output)

with open('output checker\\real_output.txt', 'w') as f:
    sys.stdout = f
    completed_process = subprocess.run(['python', 'output checker\\workspace.py'], stdout=subprocess.PIPE, text=True)
    captured_output = completed_process.stdout
    sys.stdout = original_stdout
    f.write(captured_output)

def compare_txt_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            if content1 == content2:
                return "Passed all test cases"
            else:
                return "Failed some or all testcases"

    except FileNotFoundError:
        return "One or both files not found."

if __name__ == "__main__":
    currDir=os.getcwd()
    file1_path = currDir+"\output checker\expected_output.txt"
    file2_path = currDir+"\output checker\\real_output.txt"
    
    comparison_result = compare_txt_files(file1_path, file2_path)
    print(comparison_result)

