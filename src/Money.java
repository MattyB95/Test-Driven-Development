/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */
public class Money {

    protected int amount;

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount;
    }

}
