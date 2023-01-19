import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/*
 * Contains Duplicate Problem
 * 
 * Brute Force Method:
 * 
 * Time: O(n^2)
 * Space: O(1)
 * Checking every single element of array by comparing each element with its
 * preceding elements
 * 
 * Sorting Solution:
 * 
 * Time: O(nlogn)
 * Space: O(1)
 * We sort the array first so that same elements are positioned adjacently
 * 
 * Hashset Solution:
 * 
 * Time: O(n)
 * Space: O(n)
 * We use a hashset to determine whether the set contains a duplicate or not
 * 
 */

public class contain_dup {

    public static void main(String[] args) {

        int[] arr = { 1, 2, 3, 4 };
        int[] brr = { 1, 2, 3, 1 };

        boolean result = containsDuplicate(arr); // validating the method, should print false and true
        boolean result2 = containsDuplicate(brr);
        System.out.println(result);
        System.out.println(result2);
    }

    public static boolean containsDuplicate(int[] nums) { // we create a method that accepts an int array

        Set<Integer> uniques = new HashSet<>(); // We then convert the array to a hashset

        for (int i = 0; i < nums.length; i++) { /*
                                                 * we loop through the array and if we find a duplicate then we print
                                                 * true if not loop all the way and print false
                                                 */
            if (uniques.contains(nums[i])) {
                return true;
            }
            uniques.add(nums[i]);

        }
        return false;
    }
}
