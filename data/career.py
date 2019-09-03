from .data_manager import Dataset

class Career:
    def __init__(self, date:str, text:str):
        self.date = date
        self.text = text

careers_dataset = Dataset()
careers_dataset.set_data_list([

    Career(date="2012年4月",
           text="近畿大学附属高校 特進一類 入学"),
    
    Career(date="2015年3月",
           text="近畿大学附属高校 特進一類 卒業"),

    Career(date="2015年4月",
           text="大阪市立大学 工学部 電気情報工学科 入学"),

    Career(date="2015年10月",
           text="アプリ開発団体ADOCUS 設立"),

    Career(date="2018年3月8,9日",
           text="さくらインターネットTrunckハッカソン 準優勝"),
    
    Career(date="2019年3月",
           text="大阪市立大学 工学部 電気情報工学科 卒業"),

    Career(date="2019年4月",
           text="神戸大学大学院 システム情報学研究科 入学"),
    
    Career(date="2019年8月",
           text="クックパッドインターン"),
    
    Career(date="2019年9月",
           text="チームラボインターン"),
    
    Career(date="2021年3月",
           text="神戸大学大学院 システム情報学研究科 卒業予定"),

])