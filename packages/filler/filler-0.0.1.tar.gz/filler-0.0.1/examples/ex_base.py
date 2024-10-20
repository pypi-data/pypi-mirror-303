import pandas as pd
from pathlib import Path
from filler import Filler

def main():
    
    cur_pth = Path(__file__).resolve().parent
    data = pd.read_excel(cur_pth /'data/获奖学生清单.xlsx')
    tpl = cur_pth / 'data/template.docx'
    output_path = cur_pth / 'data/output'
    output_name_pat ='{学号}_{姓名}_获奖证书.docx'

    filler = Filler(tpl, data, output_path=output_path, output_name_pat=output_name_pat)
    filler.fill()

if __name__ == '__main__':
    main()