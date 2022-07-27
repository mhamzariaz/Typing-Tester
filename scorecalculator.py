class CalculateScores:

    @staticmethod
    def calculate_accuracy(no_of_letters, back_spaces, wrong_letters):
        score_of_one_letter = 100 / no_of_letters
        total_score = 100 - (score_of_one_letter * (back_spaces + wrong_letters))
        return float(total_score)

    @staticmethod
    def calculate_time_score(time_taken, no_of_letters):
        raw_score = time_taken / (0.4 + (0.28 * (no_of_letters + 1)))
        final_score = 0

        if raw_score < 1:
            final_score = 100

        elif raw_score > 1:
            final_score = 100 / raw_score
            if final_score < 0:
                final_score = 0

        return float(final_score)

    def calculate_total_score(self, no_of_letters, backspaces, wrong_input, time_taken):
        accuracy_score = self.calculate_accuracy(no_of_letters, backspaces, wrong_input)
        time_score = self.calculate_time_score(time_taken, no_of_letters)

        total_score = (accuracy_score * 0.5) + (time_score * 0.5)
        return float(total_score), accuracy_score, time_score
