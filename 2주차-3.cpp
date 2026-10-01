#include <stdio.h>
#include <math.h>

#define EPSILON 1e-9

int main(void)
{
    /*
        2x1 +  x2 =  3
        2x1 -  x2 =  1
         x1 - 2x2 = -1
    */

    double A[3][2] = {
        {2.0,  1.0},
        {2.0, -1.0},
        {1.0, -2.0}
    };

    double b[3] = {3.0, 1.0, -1.0};

    double determinant;
    double x1;
    double x2;
    int commonSolution = 1;

    /* 첫 번째와 두 번째 방정식의 행렬식 */
    determinant =
        A[0][0] * A[1][1]
        - A[0][1] * A[1][0];

    if (fabs(determinant) < EPSILON) {
        printf("첫 번째와 두 번째 방정식만으로는 ");
        printf("유일한 해를 구할 수 없습니다.\n");

        return 1;
    }

    /* 크래머 공식으로 해 계산 */
    x1 = (
        b[0] * A[1][1]
        - A[0][1] * b[1]
    ) / determinant;

    x2 = (
        A[0][0] * b[1]
        - b[0] * A[1][0]
    ) / determinant;

    printf("계산된 해\n");
    printf("x1 = %.6f\n", x1);
    printf("x2 = %.6f\n\n", x2);

    /* 계산된 해가 세 방정식을 모두 만족하는지 확인 */
    for (int i = 0; i < 3; i++) {
        double leftSide = A[i][0] * x1 + A[i][1] * x2;
        double error = leftSide - b[i];

        printf(
            "%d번 방정식: 좌변 = %.6f, 우변 = %.6f\n",
            i + 1,
            leftSide,
            b[i]
        );

        if (fabs(error) > EPSILON) {
            commonSolution = 0;
        }
    }

    if (commonSolution) {
        printf("\n세 방정식의 공통해가 존재합니다.\n");
        printf("공통해: (x1, x2) = (%.0f, %.0f)\n", x1, x2);
    } else {
        printf("\n세 방정식을 모두 만족하는 공통해가 없습니다.\n");
    }

    return 0;
}