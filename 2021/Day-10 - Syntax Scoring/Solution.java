import java.util.Scanner;

public class Solution {

    public static final String[] closingValues = {")", "]", "}", ">"};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String ln = scanner.nextLine();
    }

    public static boolean isCorrupted(String input) {
        
        for(int i = 0; i < (input.length() - 1); i++) {
            boolean lookingForOpening = 
            boolean foundMatch = false;
            String searchingVal = input.substring(i - 1, i);

            for(int j = i; j < input.length(); j++) {
                String curVal = input.substring(j, (j + 1));
                if(curVal.equals(searchingVal)) {
                    foundMatch = true;
                    j = input.length();
                }
            }
            if(!foundMatch) {
                return true;
            }
        }
        return false;
    }
}