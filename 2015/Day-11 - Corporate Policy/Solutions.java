public class Solutions {

    private final String[] alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
    public static void main(String[] args) {
    }

    public static String generateNewPassword(String givenPassword) {
        boolean validPassword = false;

        String updatedAttempt = givenPassword;

        while(!validPassword) {
            updatedAttempt = incrementPassword(updatedAttempt);

            validPassword = checkPassword(updatedAttempt);
            
            if(validPassword) {
                return updatedAttempt;
            }
        }

        return null; //If for some reason the loop is broken, then return null.  but this should never be reached.
    }

    public static String bumpLastLetter(String givenPassword) {
        String beginningPortion = givenPassword.substring(0, givenPassword.length() - 1);
        String lastLetter = givenPassword.substring(givenPassword.length() - 1);

        //This is such a terrible way to do this, but I really can't remember how to convert a string to 
        // a char, and then a char back to a string.  This is in theory how I would want this to work:
        // char lastLetterChar = (char) lastLetter;
        // int asciiLastLetter = (int) lastLetterChar;
        // char newLastLetter = (char) (asciiLastLetter + 1);
        // String newLastLetterString = newLastLetter.toString();
        for(int i = 0; i < alphabet.length; i++) {

        }
    }
}
