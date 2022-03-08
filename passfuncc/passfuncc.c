#include <passfuncc.h>
double evaluate_and_add_in_c(double t,int N,double (**funcs)(double t)) {
    int ii;
    double out;
    double (*tfunc)(double t);
    out= 0.;
    for (ii=0; ii < N; ii++) {
        tfunc= (double (*)(double t)) *funcs;
        out+= (*tfunc)(t);
        funcs++;
    }
    return out;
}