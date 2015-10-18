/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */

public class Dollar {

    int amount;

    Dollar(int amount) {
        this.amount = amount;
    }

    Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

}