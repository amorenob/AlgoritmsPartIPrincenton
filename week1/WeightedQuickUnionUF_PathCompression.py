import sys
import os.path

class WeightedQuickUnionUF:
    """union-find data structure with n sites 0 through n-1.

    Args:
        n (int): n the number of sites.

    Attributes:
        parent (list): parent[i] = parent of i
        components (int): number of components.
        n (int): the number of sites.
        size(list): size[i] = weight of i
    """
    
    def __init__(self, n):
        """Initializes an empty union-find data structure with n sites
           0 through n-1. Each site is initially in its own component.
        """
        
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n
        self.n = n
        
    def __len__(self):
        return len(self.parent)
    
    def __str__(self):
        ids = '|'.join(map(str, range(self.n)))
        parents = '|'.join(map(str, self.parent))
        weights =  '|'.join(map(str, self.size))
        return 'id:     {0}\nparent: {1}\nweight: {2}'.format(ids, parents, weights)
         
    def find(self, p):
        """Returns the component identifier for the component containing site p
        
        Parameters:
            p (int): the integer representing one site
            
        Returns:
            int: the component identifier for the component containing site p
        """
        self.validate(p)
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]    #flat the tree
            p = self.parent[p]
        return p
    
    
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
        return self.find(p) == self.find(q)
    
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
        
        rootP = self.find(p)
        rootQ = self.find(q)
        
        # p and q are already in the same component
        if rootP == rootQ: return
        
        #make smaller root point to larger one
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
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
            uf = WeightedQuickUnionUF(n);
            for line in file:
                p, q = map(int, line.split())
                if uf.connected(p, q): next
                uf.union(p, q)
                print('{0} {1}'.format(p, q))

print(uf)

