class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        n_devices = []
        for i in range(len(bank)):
            l_devices = list(bank[i])
            c_devices = l_devices.count('1')
            if c_devices!=0:
                n_devices.append(c_devices)
        
        output=0
        if len(n_devices)>1:
            for j in range(len(n_devices)-1):
                output = output + n_devices[j]*n_devices[j+1]
        return output
