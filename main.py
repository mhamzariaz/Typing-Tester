from randomwordsapi import get_word_from_API
from scorecalculator import CalculateScores
from userinput import UserInput


def compare_words(original_word, input_word):
    error = 0
    for i in range(len(original_word)):
        if original_word[i] != input_word[i]:
            error = error + 1
    return error


if __name__ == "__main__":
    word_dict = get_word_from_API()
    random_word = word_dict['word']
    print('Word:', random_word)
    print('No of letters: ', len(random_word))

    user_input = UserInput()

    input_user = user_input.get_user_input()

    input_word = input_user[0]
    total_time_taken = input_user[1]
    back_spaces = input_user[2]

    print('Time taken by the User: ', total_time_taken)

    calculations = CalculateScores()
    results = calculations.calculate_total_score(len(random_word), back_spaces,
                                                 compare_words(random_word, input_word),
                                                 total_time_taken)

    accuracy = results[1]
    time = results[2]
    total = results[0]

    print('\nAccuracy score: ', accuracy)
    print('Time Score: ', time)
    print('\nTotal Score: ', total)
    print('\nDefinition: ', word_dict['definition'])
    print('Pronunciation: ', word_dict['pronunciation'])
