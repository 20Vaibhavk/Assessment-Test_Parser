import re
import json

def parse_questions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into individual questions
    questions = re.split(r'\\section\*?\{Question\s+ID:\s+(\d+)\}', content.strip())

    parsed_questions = []

    for i in range(1, len(questions), 2):
        question_number = (i + 1) // 2
        question_id = int(questions[i])

        # Extract question body
        question_match = re.search(r'(?:Q(?:uestion)?\.?)\s*(.*?)(?=(?:A(?:nswer)?\.)|(?=Sol:)|\\section)', questions[i + 1], re.IGNORECASE | re.DOTALL)
        if question_match:
            question_text = question_match.group(1).strip().replace('\\', '\\\\').replace('\n', '\\n')
        else:
            question_text = ""

        # Extract options and correct option
        options_matches = re.findall(r'\(([A-D])\)\s*(.*?)\s*(?=\(|$)', questions[i + 1])
        options = []
        correct_option = None
        for letter, text in options_matches:
            options.append({"optionText": text.strip().replace('\\', '\\\\').replace('\n', '\\n'), "isCorrect": False})
            if letter == 'A':
                correct_option = len(options) - 1

        if correct_option is not None:
            options[correct_option]["isCorrect"] = True

        # Construct JSON object for the question
        question_obj = {
            "questionNumber": question_number,
            "questionId": question_id,
            "questionText": question_text,
            "options": options,
        }
        parsed_questions.append(question_obj)

    return parsed_questions

def main():
    file_path = 'D:\Saee\CSE\Sasuke\Text_Parser\Task.txt'  # Update with your file path
    parsed_questions = parse_questions(file_path)

    # Write JSON output to file
    with open('output.json', 'w') as json_file:
        json.dump(parsed_questions, json_file, indent=4)

if __name__ == "__main__":
    main()
