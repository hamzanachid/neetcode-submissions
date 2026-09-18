class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] nums2=Arrays.copyOf(nums, nums.length);
        int num1=0,num2=0;
        HashMap<Integer,Integer> index=new HashMap<Integer,Integer>();
        Arrays.sort(nums);
        int i =0;
        int j = nums.length-1;
        while(i!=j){
            int out=nums[i]+nums[j];
            if(out<target){
                i+=1;
            }
            else if(out>target){
                j-=1;
            }
            else{
                num1=nums[i];
                num2=nums[j];
                break;
            }
        } 
         int index1=0,index2=0;
        for(int f =0;f<nums2.length;f++){
            if(nums2[f]==num1){
                index1=f;
                break;
            }
        }
        for(int f =0;f<nums2.length;f++){
            if(nums2[f]==num2 && f!=index1){
                index2=f;
                break;
            }
        }
        if(index1<index2)  return  new int[]{index1, index2};
        else  return  new int[]{index2, index1};
       
    }
}
