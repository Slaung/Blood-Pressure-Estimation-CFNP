# 使用 卷積模糊神經網路 對 ECG 與 PPG 信號進行血壓預測

目錄：
- 系統架構
- 資料集與預處理
- 方法:網路模型
- 成果展示

## 1. 系統架構
將感測器所收集到的PPG與ECG信號進行預處理，欲處理會對信號提取與血壓相關等特徵，最後將這些特徵輸入到卷積模糊神經網路，進行平均動脈壓(Mean Arterial Pressure)、收縮壓(Systolic Blood Pressure)和舒張壓(Diastolic Blood Pressure)之預測
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure1.png)
