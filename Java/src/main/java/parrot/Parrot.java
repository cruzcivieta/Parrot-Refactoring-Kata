package parrot;

abstract public class Parrot {

    protected static final double BASE_SPEED = 12.0;

    public static Parrot europeanParrot() {
        return new EuropeanParrot();
    }

    public static Parrot africanParrot(int numberOfCoconuts) {
        return new AfricanParrot(numberOfCoconuts);
    }

    public static Parrot norwegianBlue(double voltage, boolean isNailed) {
        return new NorwegianBlue(voltage, isNailed);
    }

    abstract public double getSpeed();

}
