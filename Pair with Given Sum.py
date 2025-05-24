class Solution:
    def twoSum(self, arr, target):
        # Ek set banate hain jo dekhega ki kaunse numbers humne pehle dekhe hain
        seen = set()

        for num in arr:
            complement = target - num
            # Agar complement pehle se set me hai, matlab dono ka sum target ke barabar hai
            if complement in seen:
                return True
            # Nahi mila toh current number ko set me daal do
            seen.add(num)

        # Agar pura array dekhne ke baad bhi pair nahi mila toh False return karo
        return False
