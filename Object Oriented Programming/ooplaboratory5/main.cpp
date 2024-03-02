#include "BigInteger.h"
#include "BigIntegerTest.h"

#include <iomanip>
#include <iostream>
#include <cassert>
using namespace std;


BigInteger computeNthFibonacci(unsigned int n) {
    BigInteger a("1");
    BigInteger b("1");
    BigInteger c("1");
    if (n == 0)
        return c;
    n--;
    while (n != 0) {
        c = a + b;
        b = a;
        a = c;
        n--;
    }
    return b;
}

void testFunction() {
    //test the Fibonacci sequence
    assert(computeNthFibonacci(0) == BigInteger("1"));
    assert(computeNthFibonacci(1) == BigInteger("1"));
    assert(computeNthFibonacci(2) == BigInteger("2"));
    assert(computeNthFibonacci(3) == BigInteger("3"));
    assert(computeNthFibonacci(4) == BigInteger("5"));
    assert(computeNthFibonacci(5) == BigInteger("8"));
    assert(computeNthFibonacci(10) == BigInteger("89"));
    assert(computeNthFibonacci(20) == BigInteger("10946"));
    assert(computeNthFibonacci(50) == BigInteger("20365011074"));
    assert(computeNthFibonacci(100) == BigInteger("354224848179261915075"));
    cout << "All tests passed! <3" << endl;
}

int main() {
#if ENABLE_TESTS > 0
    run_bigint_tests(true);
#endif

    BigInteger crt("- 1");
    BigInteger prev("- 1");
    bool isOverflow = false;
    for (int n = 0; n < 100; n += 10) {
        prev = crt;
        crt = computeNthFibonacci(n);
        if (crt < prev)
            isOverflow = true;
        cout << setw(5) << n << "\t" << setw(30) << crt.to_string() << "\t" << (isOverflow ? string(RED) + string("OVERFLOW !!!! ") + string(NC) : "") << endl;
    }
    testFunction();
    return 0;
}