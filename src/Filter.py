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
        return []
        
    def poles(self):
        return []
