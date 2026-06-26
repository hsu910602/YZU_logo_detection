# YZU_logo_detection

訓練資料集https://drive.google.com/file/d/1Wdyui1YJNJuI1Um1VOT5-pqZ2QFhcXPF/view?usp=drive_link

本專案為元智大學「電腦視覺」課程之期末專題。專案內已包含校徽核心權重檔cascade.xml
下載後，無需重新訓練，即可直接對新照片進行校徽偵測！

下載專案後請確保或手動在根目錄下建立以下兩個資料夾：
1. `test` ： 放入你想要讓電腦辨識的原始照片（支援 `.jpg`, `.png`, `.jpeg`），或是可用test.zip裡面的照片
2. `op` ： 程式執行完畢後，會自動將畫好藍色辨識框的結果圖存在這裡。
3. 配置好資料夾並將測試照片丟入 `test` 之後，執行main.py就可以在OP資料夾察看結果

