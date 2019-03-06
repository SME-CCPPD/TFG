import numpy as np
class Filter:
    def z_plane(self):
        pass

    def freq_resp(self):
        pass

    def imp_resp(self):
       pass

    def phase_resp(self):
        pass
        
    def display(self):
        self.z_plane()
        self.freq_resp()
        self.imp_resp()
        self.phase_resp()
        

    def zeros(self):
        return np.roots(self.fir_coefs)
        
    def poles(self):
        return np.roots(self.iir_coefs)

    def __init__(self, fc, ic):
        self.fir_coefs=fc if np.size(fc)>1  else np.append(fc,0)
        self.iir_coefs=ic if np.size(ic)>1  else np.append(ic,0)

    def create(zeros,poles):
        fc=np.poly(zeros)
        ic=np.poly(poles)
        return Filter(fc,ic)
    