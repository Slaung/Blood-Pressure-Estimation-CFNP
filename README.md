# 使用 卷積模糊神經網路 對 ECG 與 PPG 信號進行血壓預測

目錄：
- 系統架構
- 資料集與預處理
- 方法:網路模型
- 成果展示

## 1. 系統架構
將感測器所收集到的PPG與ECG信號進行預處理，提取與血壓相關等特徵，最後將這些特徵輸入到卷積模糊神經網路，進行平均動脈壓(Mean Arterial Pressure, MAP)、收縮壓(Systolic Blood Pressure, SBP)和舒張壓(Diastolic Blood Pressure, DBP)之預測
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure1.png)

## 2. 資料集與預處理
資料集有12000組實體數據，每組包含125Hz採樣率的PPG(光體積描記圖)、ABP(真實動脈信號)以及ECG信號。
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure3.png)

接著，對ECG和PPG波提取有關血壓等特徵，包含：
1. 脈搏傳輸時間(Pulse transmission time, PTT)
2. 心率(Heart rate)
3. PPG最高強度(Highest intensity of PPG)
4. PPG最低強度(Lowest intensity of PPG)
5. 光體積描記圖強度比(Photoplethysmogram intensity ratio)
6. PPG之AC分量的最大幅度(AC component max Amplitude of PPG)
7. Womersley數（血液動力學中的一個無量綱數）
8. 收縮期上升時間(Systolic Upstroke Time, SUT)
9. 舒張期時間(Diastolic Time, DT)
10. 收縮期寬度在10%, 25%, 33%, 50% 處(Systolic Width at 10%, 25%, 33% ,50%)
11. 收縮期寬度在10%, 25%, 33%, 50%, 66%, 75%處 + 舒張期寬度在10%, 25%, 33%, 50%, 66%, 75%處(Systolic Width at 10%, 25%, 33%, 50%+ Diastolic Width at 10%, 25%, 33%, 50%, 66%, 75%)
12. 舒張期寬度在10%, 25%, 33%, 50%處 / 收縮期寬度在10%, 25%, 33%, 50%處(Diastolic Width at 10%, 25%, 33%, 50% / Systolic Width at 10%, 25%, 33%, 50%)
