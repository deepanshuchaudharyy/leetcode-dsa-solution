class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int cnt = 0;
        int element;

        // Applying the Boyer - Moore Voting Algorithm
        for(int i=0;i<n;i++){
            if(cnt==0){
                cnt=1;
                element=nums[i];
            }
            else if(element == nums[i]){
                cnt++;
            }
            else{
                cnt--;
            }
        }

        int count=0; //declaring the count variable

        // Iterating through the array
        for(int i = 0;i<n;i++){
            if(nums[i]==element) count ++; // check if array[i] == element
        }

        // checking the condition for majorityElement
        if(count > n/2){
            return element;
        } 

       return -1; 
    }
};