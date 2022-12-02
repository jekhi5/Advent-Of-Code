import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Solution extends Instruction{
    public static void main(String[] args) {

        ArrayList<Instruction> loInstructions = new ArrayList<Instruction>();

        boolean toggle = false;
        boolean on = false;

        String x1 = "";
        String y1 = "";

        String x2 = "";
        String y2 = "";

        Posn posn1;
        Posn posn2;

        boolean reachedComma = false;
        boolean finishedFirstPosn = false;
        
        Instruction givenInstruction;

        try {
            File myObj = new File("Input-File.txt");
            Scanner myReader = new Scanner(myObj);

            while(myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(data.charAt(2) == 'g') {
                    toggle = true;
                    for(int i = 7; i < data.length(); i++) {
                        if (!finishedFirstPosn) {
                            if(data.charAt(i) == ',') {
                                reachedComma = true;
                            } else if(data.charAt(i) == ' ') {
                                finishedFirstPosn = true;
                                reachedComma = false;
                                i += 8;
                            } else if(!reachedComma) {
                                x1 += data.charAt(i);
                            } else if(reachedComma) {
                                y1 += data.charAt(i);
                            }
                        } else {
                            if(data.charAt(i) == ',') {
                                reachedComma = true;
                            } else if(!reachedComma) {
                                x2 += data.charAt(i);
                            } else if(reachedComma) {
                                y2 += data.charAt(i);
                            }
                        }
                    }
                } else {
                    toggle = false;
                    if(data.charAt(6) == 'n') {
                        on = true;
                        for(int i = 8; i < data.length(); i++) {
                            if (!finishedFirstPosn) {
                                if(data.charAt(i) == ',') {
                                    reachedComma = true;
                                } else if(data.charAt(i) == ' ') {
                                    finishedFirstPosn = true;
                                    reachedComma = false;
                                    i += 8;
                                } else if(!reachedComma) {
                                    x1 += data.charAt(i);
                                } else if(reachedComma) {
                                    y1 += data.charAt(i);
                                }
                            } else {
                                if(data.charAt(i) == ',') {
                                    reachedComma = true;
                                } else if(!reachedComma) {
                                    x2 += data.charAt(i);
                                } else if(reachedComma) {
                                    y2 += data.charAt(i);
                                }
                            }
                        }
                    } else {
                        on = false;
                        for(int i = 9; i < data.length(); i++) {
                            if(!finishedFirstPosn) {
                                if(data.charAt(i) == ',') {
                                    reachedComma = true;
                                } else if(data.charAt(i) == ' ') {
                                    finishedFirstPosn = true;
                                    reachedComma = false;
                                    i += 8;
                                } else if(!reachedComma) {
                                    x1 += data.charAt(i);
                                } else if(reachedComma) {
                                    y1 += data.charAt(i);
                                }
                            } else {
                                if(data.charAt(i) == ',') {
                                    reachedComma = true;
                                } else if(!reachedComma) {
                                    x2 += data.charAt(i);
                                } else if(reachedComma) {
                                    y2 += data.charAt(i);
                                }
                            }
                        }
                    }
                }

                posn1 = new Posn (Integer.parseInt(x1), Integer.parseInt(y1));
                posn2 = new Posn (Integer.parseInt(x2), Integer.parseInt(y2));

                givenInstruction = new Instruction(toggle, on, posn1, posn2);

                loInstructions.add(givenInstruction);

                toggle = false;
                on = false;
                x1 = "";
                y1 = "";
                x2 = "";
                y2 = "";

                reachedComma = false;
                finishedFirstPosn = false;
            }
            
            myReader.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }


          int[][] v1 = new int[1000][1000];
          int[][] v2 = new int[1000][1000];

          v1 = buildGrid(v1);
          v2 = buildGrid(v2);

          v1 = runInstructions(v1, loInstructions, false);
          v2 = runInstructions(v2, loInstructions, true);

          int totalLightsOn = getTotalLightsOn(v1);
          int totalBrightness = countTotalBrightness(v2);

          System.out.println("Total lights on after instructions: " + totalLightsOn);
          System.out.println("Total brightness after instructions: " + totalBrightness);


          /*
          for(int row = 0; row < v1.length - 1; row++) {
              for(int col = 0; col < v1[0].length - 1; col++) {
                System.out.print(v1[row][col] + ", ");
              }
              System.out.print(v1[row][v1.length - 1] + "\n");
          }*/
    }

    public static int countTotalBrightness(int[][] grid) {
        int total = 0;
        
        for(int row = 0; row < grid.length; row++) {
            for(int col = 0; col < grid[0].length; col++) {
                total += grid[row][col];
            }
        }

        return total;

    }

    public static int getTotalLightsOn(int[][] grid) {
        
        int total = 0;

        for(int row = 0; row < grid.length; row++) {
            for(int col = 0; col < grid[0].length; col++) {
                if(grid[row][col] == 1) {
                    total++;
                }
            }
        }

        return total;
    }

    public static int[][] runInstructions(int[][] grid, ArrayList<Instruction> loInstructions, boolean runningLightsV2) {
        Instruction currentInstruction;

        int[][] result = grid;

        Posn from;
        Posn to;

        for(int i = 0; i < loInstructions.size(); i++) {
            currentInstruction = loInstructions.get(i);
            from = currentInstruction.getFrom();
            to = currentInstruction.getTo();

            for(int row = from.getY(); row <= to.getY(); row++) {
                for(int col = from.getX(); col <= to.getX(); col++) {
                    if(currentInstruction.isToggle()) {
                        if(runningLightsV2) {
                            result[row][col] += 2;
                        } else {
                            if(result[row][col] == 0) {
                                result[row][col] = 1;
                            } else {
                                result[row][col] = 0;
                            }
                        }
                    } else if(currentInstruction.isOn()) {
                        if(runningLightsV2) {
                            result[row][col] += 1;
                        } else {
                            result[row][col] = 1;
                        }
                    } else {
                        if(runningLightsV2) {
                            result[row][col] = Math.max((result[row][col] - 1), 0);
                        } else {
                            result[row][col] = 0;
                        }
                    }
                }
            }
            
        }

        return result;
        
    }

    public static int[][] buildGrid(int[][] grid) {
        int[][] result = new int[grid.length][grid[0].length];
        
        for(int row = 0; row < result.length; row++) {
            for(int col = 0; col < result[0].length; col++) {
                result[row][col] = 0;
            }
        }

        return result;
    }
}
