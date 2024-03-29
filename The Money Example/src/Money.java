import org.jetbrains.annotations.Contract;

/**
 * Created by Matthew on 18/10/2015.
 * Test-Drive Development By Example.
 */

public class Money implements Expression {

    protected int amount;
    protected String currency;

    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    @Contract("_ -> !null")
    static Money dollar(int amount) {
        return new Money(amount, "USD");
    }

    @Contract("_ -> !null")
    static Money franc(int amount) {
        return new Money(amount, "CHF");
    }

    public Expression times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }

    @SuppressWarnings("EqualsWhichDoesntCheckParameterClass")
    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && currency().equals(money.currency());
    }

    String currency() {
        return currency;
    }

    public String toString() {
        return amount + " " + currency;
    }

    public Expression plus(Expression addend) {
        return new Sum(this, addend);
    }

    public Money reduce(Bank bank, String to) {
        int rate = bank.rate(currency, to);
        return new Money(amount / rate, to);
    }

}