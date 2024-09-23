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
7. Womersley數（血液動力學中的一個無量綱數, alpha）
8. 收縮期上升時間(Systolic Upstroke Time, SUT)
9. 舒張期時間(Diastolic Time, DT)
10. 收縮期寬度在10%, 25%, 33%, 50% 處(Systolic Width at 10%, 25%, 33% ,50%)
11. 收縮期寬度在10%, 25%, 33%, 50%, 66%, 75%處 + 舒張期寬度在10%, 25%, 33%, 50%, 66%, 75%處(Systolic Width at 10%, 25%, 33%, 50%+ Diastolic Width at 10%, 25%, 33%, 50%, 66%, 75%)
12. 舒張期寬度在10%, 25%, 33%, 50%處 / 收縮期寬度在10%, 25%, 33%, 50%處(Diastolic Width at 10%, 25%, 33%, 50% / Systolic Width at 10%, 25%, 33%, 50%)

## 3. 網路模型
網路模型包含：輸入層(共23個特徵)、2層卷積層、特徵融合層、模糊神經網路層，輸出層(預測血壓值)
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure2.png)

網路模型參數設定如下圖，並針對不同特徵融合層做比較：
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure7.png)

## 4. 成果展示
用測試集資料所預測之Bland-Altman統計數據：
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure4.png)
在95%預測值中，接落在+20~-20的預測誤差。

每個特徵對於模型之貢獻度分析：
![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure8.png)
- SHAP正值代表該特徵對於血壓預測的正貢獻，負值代表負貢獻。

![image](https://github.com/Slaung/Blood-Pressure-Estimation-CFNP/blob/main/Figure9.png)
- 後續可以將貢獻度較小的特徵剔除掉，例如alpha。
