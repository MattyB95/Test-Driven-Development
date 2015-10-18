/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DollarTest {

    @Test
    public void testMultiplication() {
        Dollar five = new Dollar(5);
        five.times(2);
        assertEquals(10, five.amount);
    }

}