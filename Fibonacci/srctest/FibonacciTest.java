/**
 * Created by Matthew on 03/03/2016.
 * Test-Drive Development By Example.
 */

import org.junit.Test;

import static org.testng.AssertJUnit.assertEquals;

public class FibonacciTest {

    Fibonacci fibonacci = new Fibonacci();

    @Test
    public void testFibonacci() {
        int cases[][] = {{0, 0}, {1, 1}, {2, 1}, {3, 2}};
        for (int[] aCase : cases) {
            assertEquals(aCase[1], fibonacci.fib(aCase[0]));
        }
    }

}