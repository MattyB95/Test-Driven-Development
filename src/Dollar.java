/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */

public class Dollar extends Money {

    Dollar(int amount, String currency) {
        super(amount, currency);
    }

    Money times(int multiplier) {
        return Money.dollar(amount * multiplier);
    }

}