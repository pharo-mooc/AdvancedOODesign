package designCorner;

public class Box extends Rectangle {
    protected double height;

    /** The constructor initialize box's
     *  length, width and height with default value. */
    public Box()
    {
        // Call the superclass default constructor to
        // initialize length and width.
        super();
        height = 0;
    }
    /** specific initialization */
    public Box(double length, double width, double height) {
        // Call the superclass constructor to
        // initialize length and width.
        super(length, width);
        // Initialize height.
        this.height = height;
    }

    public double getVolume() {
        return getArea() * height;
    }
}
