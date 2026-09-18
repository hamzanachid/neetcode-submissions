class Solution {
    public boolean isPalindrome(String s) {
        String sregex=s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int i =0;
        int j=sregex.length()-1;
        while(i<=j){
            if(sregex.charAt(i)!=sregex.charAt(j)){
                return false;
            }
            i+=1;
            j-=1;
            System.out.println(i);
            System.out.println(j);
            System.out.println(i!=j); 
        }
        return true;
    }
}
