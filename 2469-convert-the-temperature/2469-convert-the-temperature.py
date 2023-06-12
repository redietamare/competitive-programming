class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kel=celsius+273.15
        far=(celsius*1.80)+32.00
        dpfar=float(f"{far:.5f}")
        dpkel=float(f"{kel:.5f}")
        ans=[dpkel,dpfar]
        return(ans)