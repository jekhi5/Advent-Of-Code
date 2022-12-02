public class Instruction extends Posn{
    boolean toggle;
    boolean on;
    Posn from;
    Posn to;
    
    public Instruction() {
        toggle = false;
        on = false;
        from = new Posn(-5, -5);
        to = new Posn(-5, -5);
    }
    
    public Instruction(Boolean toggle, boolean on, Posn from, Posn to) {
        this.toggle = toggle;
        this.on = on;
        this.from = from;
        this.to = to;
    }

    public Boolean isToggle() {
        return toggle;
    }

    public Boolean isOn() {
        return on;
    }

    public Posn getFrom() {
        return from;
    }

    public Posn getTo() {
        return to;
    }
}
