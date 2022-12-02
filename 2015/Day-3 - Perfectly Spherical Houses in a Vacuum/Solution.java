import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        String input = "";
        try {
            File myObj = new File("Input-File.txt");
            Scanner myReader = new Scanner(myObj);
            String data = myReader.nextLine();
            input += data;
            myReader.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
          String[] arr = input.split("");
          String[] evenArr = new String[arr.length / 2];
          String[] oddArr = new String[arr.length / 2];
          for(int i = 0; i < arr.length; i++) {
              if(i % 2 == 0) {
                evenArr[i/2] = arr[i];
              } else {
                  oddArr[(int)(i / 2)] = arr[i];
              }
          }

          int evenLowest = getVertVal(evenArr, false);
          int evenHighest = getVertVal(evenArr, true);
          int evenLeftMost = getHorizVal(evenArr, true);
          int evenRightMost = getHorizVal(evenArr, false);

          int oddLowest = getVertVal(oddArr, false);
          int oddHighest = getVertVal(oddArr, true);
          int oddLeftMost = getHorizVal(oddArr, true);
          int oddRightMost = getHorizVal(oddArr, false);

          int robotLowest = Math.min(evenLowest, oddLowest);
          int robotHighest = Math.max(evenHighest, oddHighest);
          int robotLeftMost = Math.min(evenLeftMost, oddLeftMost);
          int robotRightMost = Math.max(evenRightMost, oddRightMost);

          int[][] robotGrid = new int[(Math.abs(robotLowest) + robotHighest + 1)][(Math.abs(robotLeftMost) + robotRightMost + 1)]; // The +1 is to account for the center location 0 square


          int lowest = getVertVal(arr, false);
          int highest = getVertVal(arr, true);
          int leftMost = getHorizVal(arr, true);
          int rightMost = getHorizVal(arr, false);
          int[][] grid = new int[(Math.abs(lowest) + highest + 1)][(Math.abs(leftMost) + rightMost + 1)]; // The +1 is to account for the center location 0 square

          grid = buildGrid(grid);
          robotGrid = buildGrid(robotGrid);

          int soloTotal = housesDelivered(grid, arr, (Math.abs(lowest) + 70), (Math.abs(leftMost)), false);
          System.out.println("Total houses delivered (alone): " + soloTotal + ".");

          int robotTotal = housesDelivered(robotGrid, arr, (Math.abs(robotLowest) + 38), (Math.abs(robotLeftMost)), true);
          System.out.println("Total houses delivered (with roboSanta): " + robotTotal + ".");
    }

    public static int housesDelivered(int[][] grid, String[] arr, int lowest, int leftMost, boolean hasRobotSanta) {
        int currentSantaRow = Math.abs(lowest);
        int currentSantaCol = Math.abs(leftMost);

        int currentRobotRow = currentSantaRow;
        int currentRobotCol = currentSantaCol;

        int totalHousesDelivered = 0;

        if(!hasRobotSanta) {
            grid[currentSantaRow][currentSantaCol] = 1; // Initial house gets a present

            for(int i = 0; i < arr.length; i++) {
                if(arr[i].equals("<")) {
                    currentSantaCol--;
                    grid[currentSantaRow][currentSantaCol]++;
                } else if(arr[i].equals(">")) {
                    currentSantaCol++;
                    grid[currentSantaRow][currentSantaCol]++;
                } else if(arr[i].equals("v")) {
                    currentSantaRow++;
                    grid[currentSantaRow][currentSantaCol]++;
                } else if(arr[i].equals("^")) {
                    currentSantaRow--;
                    grid[currentSantaRow][currentSantaCol]++;
                } else {
                    System.out.println("Error.  Illegal instruction given: " + arr[i]);
                }
            }

            for(int row = 0; row < grid.length; row++) {
                for(int col = 0; col < grid[0].length; col++) {
                    if(grid[row][col] > 0) {
                        totalHousesDelivered++;
                    }
                }
            }
        } else {
            grid[currentRobotRow][currentRobotCol] = 2; // Initial house gets two presents

            for(int i = 0; i < arr.length; i++) {
                if(i % 2 == 0) {
                    if(arr[i].equals("<")) {
                        currentSantaCol--;
                        grid[currentSantaRow][currentSantaCol]++;
                    } else if(arr[i].equals(">")) {
                        currentSantaCol++;
                        grid[currentSantaRow][currentSantaCol]++;
                    } else if(arr[i].equals("v")) {
                        currentSantaRow++;
                        grid[currentSantaRow][currentSantaCol]++;
                    } else if(arr[i].equals("^")) {
                        currentSantaRow--;
                        if(currentSantaRow == -1) {
                            System.out.println(i);
                            System.out.println(arr.length);
                        }
                        grid[currentSantaRow][currentSantaCol]++;
                    } else {
                        System.out.println("Error.  Illegal instruction given: " + arr[i]);
                    }
                } else {
                    if(arr[i].equals("<")) {
                        currentRobotCol--;
                        grid[currentRobotRow][currentRobotCol]++;
                    } else if(arr[i].equals(">")) {
                        currentRobotCol++;
                        grid[currentRobotRow][currentRobotCol]++;
                    } else if(arr[i].equals("v")) {
                        currentRobotRow++;
                        grid[currentRobotRow][currentRobotCol]++;
                    } else if(arr[i].equals("^")) {
                        currentRobotRow--;
                        grid[currentRobotRow][currentRobotCol]++;
                    } else {
                        System.out.println("Error.  Illegal instruction given: " + arr[i]);
                    }
                }
            }

            for(int row = 0; row < grid.length; row++) {
                for(int col = 0; col < grid[0].length; col++) {
                    if(grid[row][col] > 0) {
                        totalHousesDelivered++;
                    }
                }
            }
        }

        return totalHousesDelivered;
    }

    // Loads the entire grid with 0s
    public static int[][] buildGrid(int[][] grid) {
        int[][] result = new int[grid.length][grid[0].length];
        
        for(int row = 0; row < result.length; row++) {
            for(int col = 0; col < result[0].length; col++) {
                result[row][col] = 0;
            }
        }

        return result;
    }

    public static int getVertVal(String[] arr, boolean high) {
        String[] upAndDown = Arrays.stream(arr).filter(x -> (x.equals("^") || x.equals("v"))).toArray(String[]::new);

        int lowHeight = 0;
        int highHeight = 0;
        int currentHeight = 0;

        for(int i = 0; i < upAndDown.length; i++) {
            if(upAndDown[i].equals("v")) {
                currentHeight--;
                if(currentHeight < lowHeight) {
                    lowHeight = currentHeight;
                }
            } else {
                currentHeight++;
                if(currentHeight > highHeight) {
                    highHeight = currentHeight;
                }
            }
        }

        if(high) {
            return highHeight;
        }

        return lowHeight;
    }

    public static int getHorizVal(String[] arr, boolean left) {
        String[] leftAndRight = Arrays.stream(arr).filter(x -> (x.equals("<") || x.equals(">"))).toArray(String[]::new);

        int leftMost = 0;
        int rightMost = 0;
        int currentVal = 0;

        for(int i = 0; i < leftAndRight.length; i++) {
            if(leftAndRight[i].equals("<")) {
                currentVal--;
                if(currentVal < leftMost) {
                    leftMost = currentVal;
                }
            } else {
                currentVal++;
                if(currentVal > rightMost) {
                    rightMost = currentVal;
                }
            }
        }

        if(left) {
            return leftMost;
        }

        return rightMost;
    }
}
