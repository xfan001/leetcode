class Solution {
public:
    int integerBreak(int n) {
        if (n==2){
            return 1;
        }else if (n==3){
            return 2;
        }
        int T[n+1];
        T[1] = 1;
        T[2] = 2;
        T[3] = 3;
        for (int j=4; j<=n; j++){
            int max = 1;
            for (int i=1; i<j; i++){
                int tmp = (j-i) * T[i];
                max = tmp>max ? tmp : max;
            }
            T[j] = max;
        }
        return T[n];
    }
};