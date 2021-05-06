"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
示例:

输入: a = 1, b = 1
输出: 2

提示：

    a, b 均可能是负数或 0
    结果不会溢出 32 位整数
"""

"""
Java 
public class Solution {
    public int Add(int num1,int num2) {
        while(num2!=0){
            int c = (num1&num2) << 1;
            num1 ^= num2;
            num2 = c;
        }
        return num1;

    }
}
"""
