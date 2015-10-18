/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */
public class Franc extends Money {

    Franc(int amount) {
        this.amount = amount;
    }

    Franc times(int multiplier) {
        return new Franc(amount * multiplier);
    }

}
