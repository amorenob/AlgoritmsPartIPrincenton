import sys
import os.path

class QuickFindUF:
    """union-find data structure with n sites 0 through n-1.

    Args:
        n (int): n the number of sites.

    Attributes:
        id (list): id[i] = component identifier of i
        components (int): number of components.
        n (int): the number of sites.

    """
    
    def __init__(self, n):
        """Initializes an empty union-find data structure with n sites
           0 through n-1. Each site is initially in its own component.
        """
        
        self.id = [i for i in range(n)]
        self.components = n
        self.n = n
        
    def __len__(self):
        return len(self.id)
    
    def __str__(self):
        ids = '|'.join(map(str, range(self.n)))
        values = '|'.join(map(str, self.id))
        return 'id:        {0}\ncomponent: {1}'.format(ids, values)
         
    def find(self, p):
        """Returns the component identifier for the component containing site p
        
        Parameters:
            p (int): the integer representing one site
            
        Returns:
            int: the component identifier for the component containing site p
        """
        self.validate(p)
        return self.id[p]
    
    
    def validate(self, p):
        """Validate that p is a valid index
        """
        n = self.n
        if p < 0 or p >= n:
            raise ValueError("index {0} is not between 0 and {1}".format(p, n-1))
            
    def connected(self, p, q):
        """Returns true if the the two sites are in the same component.
        Parameters:
            p (int): the integer representing one site
            q (int): the integer representing the other site
            
        Returns:
            bool: True if the two sites (p and q) are in the same component, False otherwise
            
        Raises:
            ValueError: unless 0 <= p < n and  0 <= q < n
        """
        self.validate(p)
        self.validate(q)
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        """Merges the component containing site p with the component containing site q.
        
        Parameters:
            p (int): the integer representing one site
            q (int): the integer representing the other site
            
        Raises:
            ValueError: unless 0 <= p < n and  0 <= q < n
        """
        self.validate(p)
        self.validate(q)
        
        pId = self.id[p]
        qId = self.id[q]
        
        # p and q are already in the same component
        if pId == qId: return
    
        # Rename p's component to q's name
        for i in range(self.n):
            if self.id[i] == pId: self.id[i] = qId
        
        # update number of components
        self.components -= 1

if __name__ == "__main__":
    """
     * Reads in a sequence of pairs of integers (between 0 and n-1) from standard input, 
     * where each integer represents some site;
     * if the sites are in different components, merge the two components
     * and print the pair to standard output.
     *
     * @param args the command-line arguments
    """
    filename = ''
    if len(sys.argv) > 1: filename = sys.argv[1]
    if os.path.isfile(filename):
        with open(filename,'r') as file:
            n = int(file.readline())
            uf = QuickFindUF(n);
            for line in file:
                p, q = map(int, line.split())
                if uf.connected(p, q): next
                uf.union(p, q)
                print('{0} {1}'.format(p, q))

print(uf)

