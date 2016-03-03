/**
 * Created by Matthew on 03/03/2016.
 * Test-Drive Development By Example.
 */

public class Fibonacci {

    int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        return fib(n - 1) + fib(n - 2);
    }

}