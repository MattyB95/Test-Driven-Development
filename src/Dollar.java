/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */

public class Dollar {

    private int amount;

    Dollar(int amount) {
        this.amount = amount;
    }

    Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    public boolean equals(Object object) {
        Dollar dollar = (Dollar) object;
        return amount == dollar.amount;
    }

}