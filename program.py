class Solution:
    inputStr = input("Give a sring: ")
    def toLowerCase(self):
        self.lowercasedStr = self.inputStr.lower()
        return self.lowercasedStr


##     ##     ##     ##     ##     ##     ##     ##     ##     ##     
myMessage = Solution()
print(myMessage.toLowerCase())
