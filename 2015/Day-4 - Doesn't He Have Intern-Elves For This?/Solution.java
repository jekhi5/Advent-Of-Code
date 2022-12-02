import java.util.Scanner;
import java.util.regex.Pattern;
import java.io.File;
import java.io.FileNotFoundException;

public class Solution {
    public static void main(String[] args) {

        Pattern p1_p1 = Pattern.compile("ab|cd|pq|xy");
        Pattern p1_p2 = Pattern.compile("(.*[aeiou]){3}");
        Pattern p1_p3 = Pattern.compile("(.)\\1");
        Pattern p2_p1 = Pattern.compile("(..).*\\1");
        Pattern p2_p2 = Pattern.compile("(.).\\1");

        int p1_count = 0;
        int p2_count = 0;

        try {
            File myObj = new File("Input-File.txt");
            Scanner scanner = new Scanner(myObj);
            String data = scanner.nextLine();
            
            while(scanner.hasNextLine()) {
                String input = scanner.nextLine();
                if(!p1_p1.matcher(input).find() &&
                    p1_p2.matcher(input).find() &&
                    p1_p3.matcher(input).find()) {
                    p1_count++;
                }

                if(p2_p1.matcher(input).find() &&
                p2_p2.matcher(input).find()) {
                    p2_count++;
                }  
            }
            
            scanner.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

        System.out.println(p1_count);
        System.out.println(p2_count);
    }
}

/*

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {
    
    public static void main(String[] args) {
        int totalNiceWords = 0;
        boolean niceWord = false;


    try {
        File myObj = new File("Input-File.txt");
        Scanner myReader = new Scanner(myObj);
        String data = myReader.nextLine();
        
        while(myReader.hasNextLine()) {
            niceWord = checkNiceWord(data);

            if(niceWord) {
                totalNiceWords++;
            }    
        }
        
        myReader.close();
      } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
      }

      System.out.println("There are " + totalNiceWords + " nice words.");
    }

    public static boolean checkNiceWord(String input) {
        if(hasThreeVowels(input) && hasLegalDouble(input)) {
            return true;
        }
        return false;
    }

    public static boolean hasLegalDouble(String input) {
        boolean doubleLetter = false;
        boolean illegalPair = false;

        for(int i = 0; i < input.length() - 1; i++) {
            String first = "" + input.charAt(i);
            String second = "" + input.charAt(i + 1);

            if(first.equalsIgnoreCase(second)) {
                doubleLetter = true;
            }

            if((first + second).equalsIgnoreCase("ab") || (first + second).equalsIgnoreCase("cd") || (first + second).equalsIgnoreCase("pq") || (first + second).equalsIgnoreCase("xy")) {
                illegalPair = true;
            }

            if(illegalPair) {
                return false;
            }
        }

        if(doubleLetter) {
            return true;
        }

        return false;
    }

    public static boolean hasThreeVowels(String input) {
        int totalVowels = 0;

        for(int i = 0; i < input.length(); i++) {
            if(input.charAt(i) == 'a' || input.charAt(i) == 'b' || input.charAt(i) == 'i' || input.charAt(i) == 'o' || input.charAt(i) == 'u') {
                totalVowels++;
                if(totalVowels >= 3) {
                    return true;
                }
            }
        }
        return false;
    }

}
*/