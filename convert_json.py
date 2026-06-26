import os
import json

# =======================================================
# 自動語法解法：以這個 Python 檔案所在的資料夾為基準路徑
# =======================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pos_dir = os.path.join(BASE_DIR, 'pos')
output_file = os.path.join(BASE_DIR, 'pos.txt')

print(f"目前偵測到的專案目錄為: {BASE_DIR}")
print(f"正在尋找的 pos 資料夾路徑: {pos_dir}")

if not os.path.exists(pos_dir):
    print("❌ 錯誤：在同一個目錄下找不到 'pos' 資料夾！請確認此 Python 檔案有跟 pos 資料夾放在一起。")
    exit()

count = 0
with open(output_file, 'w', encoding='utf-8') as f:
    for file in os.listdir(pos_dir):
        if file.endswith('.json'):
            json_path = os.path.join(pos_dir, file)
            
            # 偵測圖片副檔名
            img_name = None
            for ext in ['.jpg', '.jpeg', '.png', '.JPG', '.PNG']:
                test_name = file.replace('.json', ext)
                if os.path.exists(os.path.join(pos_dir, test_name)):
                    img_name = test_name
                    break
            
            if not img_name:
                continue
                
            img_path = f"pos/{img_name}"
            
            with open(json_path, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
            
            shapes = data.get('shapes', [])
            if not shapes: continue
                
            line = f"{img_path} {len(shapes)}"
            for shape in shapes:
                if shape['shape_type'] == 'rectangle':
                    points = shape['points']
                    x1, y1 = points[0]
                    x2, y2 = points[1]
                    
                    xmin = int(min(x1, x2))
                    ymin = int(min(y1, y2))
                    w = int(abs(x2 - x1))
                    h = int(abs(y2 - y1))
                    
                    line += f" {xmin} {ymin} {w} {h}"
            
            f.write(line + '\n')
            count += 1

print(f"🎉 成功！順利轉換 {count} 個標註檔案，已生成 {output_file}！")
