package designCorner;

public class Rectangle
{
    protected double length;
    protected double width;

    /** The constructor initialize rectangle's
     *  length and width with default value */
    public Rectangle() {
        length = 0;
        width = 0;
    }

    /** The constructor accepts the rectangle's length and width. */
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public double getArea() {
        return length * width;
    }
}
