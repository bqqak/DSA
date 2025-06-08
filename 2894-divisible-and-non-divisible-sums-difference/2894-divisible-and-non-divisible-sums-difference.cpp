class Solution {
public:
    int differenceOfSums(int n, int m) {
        // using maths, because maths is a power
        //using sum formula   (1, n) -> S = (1 + n) * n / 2;
        // S = num1 + num2,   so   num1 = S - num2,   we need find num1 - num2 = S - 2num2
        // k = n / m (number that divisible by m). For instance n = 17, m = 3 -> ans: 5   (3, 6, 9, 12, 15)
        // num2 = m + 2m + 3m + 4m + km = m(1 + 2 + 3 + 4 + k) = m * k(1+k) / 2
        int S = (1 + n) * n / 2;
        int k = n / m;
        int num2 = m * k * (1 + k) / 2;
        return S - 2 * num2;
    }
};