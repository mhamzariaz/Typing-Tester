from randomwordsapi import get_word_from_api
from scorecalculator import CalculateScores
from userinput import UserInput


def print_results(user_accuracy, user_time, total_score, word_definition, word_pronunciation):

    print('\nAccuracy score: ', user_accuracy)
    print('Time Score: ', user_time)
    print('\nTotal Score: ', total_score)
    print('\nDefinition: ', word_definition)
    print('Pronunciation: ', word_pronunciation)
    print('\n')


if __name__ == "__main__":

    word_dict = get_word_from_api()
    random_word = word_dict['word']
    print('Word:', random_word)
    print('No of letters: ', len(random_word))

    user_input = UserInput()
    calculations = CalculateScores()

    input_user = user_input.get_user_input()

    input_word = input_user['Input']
    back_spaces = input_user['Backspaces']
    total_time_taken = calculations.calculate_total_time_taken(input_user['Start Time'], input_user['End Time'])

    print('Time taken by the User: ', total_time_taken)

    results = calculations.calculate_total_score(len(random_word), back_spaces,
                                                 calculations.compare_words(random_word, input_word),
                                                 total_time_taken)

    time = results['Time Score']
    accuracy = results['Accuracy Score']
    total_score = results['Total Score']

    print_results(accuracy, time, total_score, word_dict['definition'], word_dict['pronunciation'])
