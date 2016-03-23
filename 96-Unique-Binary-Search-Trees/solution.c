int numTrees(int n) {
    if (n==0) {
        return 0;
    }
    
    int T[n+1];
    T[0] = 1;
    T[1] = 1;
    for (int i=2; i<=n; i++) {
        int t=0;
        for (int j=0; j<i/2; j++) {
            t += T[i-1-j] * T[j] * 2;
        }
        if (i%2) {
            t += T[i/2]*T[i/2];
        }
        T[i] = t;
    }
    return T[n];
}