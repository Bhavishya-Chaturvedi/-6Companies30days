class Solution:
    def linkdelete(self, head, m, n):
        current = head
        
        while current:
            for i in range(m-1):
                if not current:
                    break
                current = current.next
                
            if not current:
                break
                
            temp = current
            current = current.next
            
            for i in range(n):
                if not current:
                    break
                current = current.next
                
            temp.next = current
    
