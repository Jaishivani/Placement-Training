
#include <stdio.h>

int main() {
    int score;
    char grade;
    printf("Enter the student's score (0-100): ");
    scanf("%d", &score);
    if (score >= 90 && score <= 100) {
        grade = 'A';
    } else if (score >= 80 && score < 90) {
        grade = 'B';
    } else if (score >= 70 && score < 80) {
        grade = 'C';
    } else if (score >= 60 && score < 70) {
        grade = 'D';
    } else if (score >= 0 && score < 60) {
        grade = 'F';
    } else {
        printf("Invalid score\n");
        return 0;
    }

    printf("The grade for a score of %d is %c.\n", score, grade);

    return 0;
}
