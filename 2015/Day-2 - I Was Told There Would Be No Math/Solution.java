import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Solution {
    
    public Solution() {
        super();
    }
    public static void main(String[] args) {
        ArrayList<Integer> lengths = new ArrayList<Integer>();
        ArrayList<Integer> widths = new ArrayList<Integer>();
        ArrayList<Integer> heights = new ArrayList<Integer>();
        try {
            File myObj = new File("Input-File.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
              String data = myReader.nextLine();

              int firstX = ordinalIndexOf(data, "x", 0);
              int secondX = ordinalIndexOf(data, "x", 1);

              String strLength = data.substring(0, firstX);
              String strWidth = data.substring((firstX + 1), secondX);
              String strHeight = data.substring((secondX + 1), data.length());

              Integer length = Integer.parseInt(strLength);
              Integer width = Integer.parseInt(strWidth);
              Integer height = Integer.parseInt(strHeight);

              lengths.add(length);
              widths.add(width);
              heights.add(height);
            }
            myReader.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

          ArrayList<Integer> test1 = new ArrayList<Integer>();
          ArrayList<Integer> test2 = new ArrayList<Integer>();
          ArrayList<Integer> test3 = new ArrayList<Integer>();
          
          test1.add(2);
          test2.add(3);
          test3.add(4);

          int totalSurfaceAreas = getTotalSA(lengths, widths, heights);
          int totalRibbonLength = getTotalRibbonLength(lengths, widths, heights);

          System.out.println("The total surface-area of all presents is: " + totalSurfaceAreas + ".\nThe total ribbon-length is: " + totalRibbonLength + ".");
    }

    public static int getTotalRibbonLength(ArrayList<Integer> lengths, ArrayList<Integer> widths, ArrayList<Integer> heights) {
        int total = 0;
        if((lengths.size() != widths.size()) || (lengths.size() != heights.size()) || (widths.size() != heights.size())) {
            System.out.println("Error.  The given ArrayList of lengths, widths, and heights are not the same size.");
            return -1;
        } else {
            for(int i = 0; i < lengths.size(); i++) {
                int givenLength = lengths.get(i);
                int givenWidth = widths.get(i);
                int givenHeight = heights.get(i);

                int smallestSideLength = Math.min(Math.min(givenLength, givenWidth), givenHeight);
                int middleSideLength = 0;
                if(givenLength == smallestSideLength) {
                    middleSideLength = Math.min(givenWidth, givenHeight);
                } else if(givenWidth == smallestSideLength) {
                    middleSideLength = Math.min(givenLength, givenHeight);
                } else if(givenHeight == smallestSideLength) {
                    middleSideLength = Math.min(givenLength, givenWidth);
                }

                int smallestPerimeter = ((2 * smallestSideLength) + (2 * middleSideLength));
                int volume = givenLength * givenWidth * givenHeight;

                total += smallestPerimeter + volume;
            }
        }
        return total;
    }

    public static int getTotalSA(ArrayList<Integer> lengths, ArrayList<Integer> widths, ArrayList<Integer> heights) {
        int total = 0;
        if((lengths.size() != widths.size()) || (lengths.size() != heights.size()) || (widths.size() != heights.size())) {
            System.out.println("Error.  The given ArrayList of lengths, widths, and heights are not the same size.");
            return -1;
        } else {
            for(int i = 0; i < lengths.size(); i++) {
                int givenLength = lengths.get(i);
                int givenWidth = widths.get(i);
                int givenHeight = heights.get(i);

                int side1 = (givenLength * givenWidth);
                int side2 = (givenLength * givenHeight);
                int side3 = (givenWidth * givenHeight);

                int givenSA = getSurfaceArea(givenLength, givenWidth, givenHeight);
                givenSA += Math.min(Math.min(side1,side2), side3);

                total += givenSA;
            }
        }
        return total;
    }

    public static int getSurfaceArea(int length, int width, int height) {
        return ((2 * length * width) + (2 * length * height) + (2 * width * height));
    }

    public static int ordinalIndexOf(String str, String substr, int n) {
        int pos = -1;
        do {
            pos = str.indexOf(substr, pos + 1);
        } while (n-- > 0 && pos != -1);
        return pos;
    }
}