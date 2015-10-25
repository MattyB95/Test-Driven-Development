/**
 * Created by Matthew on 19/10/2015.
 * Test-Drive Development By Example.
 */

public interface Expression {

    Money reduce(Bank bank, String to);

    Expression plus(Expression added);

}