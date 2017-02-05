package parrot;

public class Parrot {

    protected static final double BASE_SPEED = 12.0;
    protected static final double LOAD_FACTOR = 9.0;

    private ParrotTypeEnum type;
    private int numberOfCoconuts = 0;
    private double voltage;
    private boolean isNailed;


    public Parrot(ParrotTypeEnum _type, int numberOfCoconuts, double voltage, boolean isNailed) {
        this.type = _type;
        this.numberOfCoconuts = numberOfCoconuts;
        this.voltage = voltage;
        this.isNailed = isNailed;
    }

    public static Parrot europeanParrot() {
        return new EuropeanParrot();
    }

    public static Parrot africanParrot(int numberOfCoconuts) {
        return new AfricanParrot(numberOfCoconuts);
    }

    public double getSpeed() {
        switch(type) {
            case NORWEGIAN_BLUE:
                return norwegianBlueSpeed();
        }
        throw new RuntimeException("Should be unreachable");
    }

    private double norwegianBlueSpeed() {
        return (isNailed) ? 0 : getBaseSpeed(voltage);
    }

    private double getBaseSpeed(double voltage) {
        return Math.min(24.0, voltage * BASE_SPEED);
    }

}
