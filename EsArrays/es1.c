// -------------------------
void somma_armonica(int n, double * h) {
    *(h + n - 1) = 1.0 / n;
    if (n > 1) somma_armonica(n - 1, h);
}

// -------------------------

double media(int * a, int l) {
    double s = 0;
    for (int i = 0; i < l; i++) {
        s += *(a+i);
    }
    return s / l;
}

double pow2(double n) {
    return n*n;
}

double var(int * a, int l) {
    double av = media(a, l);

    double s = 0;
    for (int i = 0; i < l; i++) {
        s += pow2(*(a+i) - av);
    }

    return s / l;
}

// ------------------------

int F1(int a[], int n, int x) {
    int IsMin = 0;
    while (n >= 0 && !IsMin) {
        //if (a[n] >= 0)
    }
}