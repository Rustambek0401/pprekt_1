from PSQL import DataBase
class betta:
    @staticmethod
    def select(tebel):
        query = f""" SELECT * FROM {tebel}; """
        return DataBase.datbase(query,'select')
    @staticmethod
    def delete(ustun,qator,teble):
        query = f"""DELETE FROM {teble} WHERE {ustun} = '{qator}';"""
        return DataBase.datbase(query,'delete')
    @staticmethod
    def delete_id(ustun,qator,teble):
        query = f"""DELETE FROM {teble} WHERE {ustun} = {qator};"""
        return DataBase.datbase(query,'delete')
    @staticmethod
    def updata(query):
        return DataBase.datbase(query,'updata')
class python(betta):
    def __init__(self, model_nomi:str ,necha_oy_otilishi:float ,necha_model:int ,narxi: str):
        self.model_nomi = model_nomi
        self.necha_oy_otilishi = necha_oy_otilishi
        self.necha_model = necha_model
        self.narxi = narxi
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(model_nomi, necha_oy_otilishi, nechta_model, narxi) VALUES ('{self.model_nomi}',{self.necha_oy_otilishi},{self.necha_model},'{self.narxi}');"""
        return DataBase.datbase(query, 'insert')
class java(python):
    def __init__(self,model_nomi: str ,necha_oy_otilishi: float ,necha_model:int ,narxi: str):
        super().__init__(self, model_nomi ,necha_oy_otilishi ,necha_model ,narxi)
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(model_nomi,necha_oy_otilishi,nechta_model,narxi) VALUES ('{self.model_nomi}',{self.necha_oy_otilishi},{self.necha_model},'{self.narxi}');"""
        return DataBase.datbase(query,'insert')

class c_pilus(python):
    def __init__(self, model_nomi: str, necha_oy_otilishi: float, necha_model: int, narxi: str):
        super().__init__(self, model_nomi, necha_oy_otilishi, necha_model, narxi)

    def insert(self, teble):
        query = f"""INSERT INTO {teble}(model_nomi,necha_oy_otilishi,nechta_model,narxi) VALUES ('{self.model_nomi}',{self.necha_oy_otilishi},{self.necha_model},'{self.narxi}');"""
        return DataBase.datbase(query, 'insert')
class c_shar(python):
    def __init__(self, model_nomi: str, necha_oy_otilishi: float, necha_model: int, narxi: str):
        super().__init__(self, model_nomi, necha_oy_otilishi, necha_model, narxi)

    def insert(self, teble):
        query = f"""INSERT INTO {teble}(model_nomi,necha_oy_otilishi,nechta_model,narxi) VALUES ('{self.model_nomi}',{self.necha_oy_otilishi},{self.necha_model},'{self.narxi}'):"""
        return DataBase.datbase(query, 'insert')
class bepul_kurs(betta):
    def __init__(self, nomi:str, izox:str, nechta_dars:int, darslar_soni:int):
        self.nomi = nomi
        self.izox = izox
        self.nechta_dars = nechta_dars
        self.darslar_soni =darslar_soni
    def insert(self,tebel):
        query = f"""INSERT INTO {tebel}( nomi, izox, nechta_dars, darslar_soni ) VALUES ('{self.nomi}','{self.izox}',{self.nechta_dars},{self.darslar_soni});"""
        return DataBase.datbase(query,'insert')
class kurslar(betta):
    def __init__(self,python_id:int,java_id:int,c_pilus_id:int,c_shar_id:int,bepul_kurs_id:int):
        self.python_id = python_id
        self.java_id = java_id
        self.c_pilus_id = c_pilus_id
        self.c_shar_id = c_shar_id
        self.bepul_kurslar_id = bepul_kurs_id
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(python_id,java_id,c_pilus_id,c_shar_id,bepul_kurs_id) VALUES ({self.python_id},{self.java_id},{self.c_pilus_id},{self.c_shar_id},{self.bepul_kurslar_id});"""
        return DataBase.datbase(query,'insert')
class royxatdan_otish():
    def __init__(self,ismi:str, familasi:str, nomer:str, password:str, adres:str,kusr_id:int):
        self.ismi = ismi
        self.familasi = familasi
        self.nomer = nomer
        self.password = password
        self.adres = adres
        self.kusr_id = kusr_id
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(ismi,familasi,nomer,password,adres,kusr_id) VALUES ('{self.ismi}','{self.familasi}','{self.nomer}','{self.password}','{self.adres}',{self.kusr_id});"""
        return DataBase.datbase(query,'insert')
class tolov_t(betta):
    def __init__(self, pyme:str, cilik:str, paynet:str ,hisob_raqam_orqali:str ):
        self.pyme = pyme
        self.cilik = cilik
        self.paynet = paynet
        self.hisob_raqam_orqali = hisob_raqam_orqali
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(pyme, cilik, paynet, hisob_raqam_orqali) VALUES ('{self.pyme}','{self.cilik}','{self.paynet}','{self.hisob_raqam_orqali}');"""
        return DataBase.datbase(query,'insert')
class tolov_u(betta):
    def __init__(self, oy_ma_oy_tolash: str, hammasini_birdan_tolash: str):
        self.oy_ma_oy_tolash = oy_ma_oy_tolash
        self.hammasini_birdan_tolash = hammasini_birdan_tolash
    def insert(self, teble):
        query = f"""INSERT INTO {teble}(oy_ma_oy_tolash, hammasini_birdan_tolash) VALUES ('{self.oy_ma_oy_tolash}','{self.hammasini_birdan_tolash}');"""
        return DataBase.datbase(query, 'insert')
class bitirganlar(betta):
    def __init__(self,ismi:str, familasi:str, qayda_ishlashi:str, lavozimi:str, maoshi:str ):
        self.ismi = ismi
        self.familasi = familasi
        self.qayda_ishlashi = qayda_ishlashi
        self.lavozimi = lavozimi
        self.maoshi = maoshi
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(ismi,familasi,qayda_ishlashi,lavozimi,maoshi) VALUES ('{self.ismi}','{self.familasi}','{self.qayda_ishlashi}','{self.lavozimi}','{self.maoshi}');"""
        return DataBase.datbase(query,'insert')
class oqituvchi(betta):
    def __init__(self, ismi: str, familasi: str, mutaxasisligi: str, tajribasi: str, strj:str):
        self.ismi = ismi
        self.familasi = familasi
        self.mutaxasisligi = mutaxasisligi
        self.tajribasi = tajribasi
        self.strj = strj
    def insert(self,teble):
        query = f"""INSERT INTO {teble}(ismi,familasi,mutaxasisligi,tajribasi,stj) VALUES ('{self.ismi}','{self.familasi}','{self.mutaxasisligi}','{self.tajribasi}','{self.strj}');"""
        return DataBase.datbase(query, 'insert')

class oquvchi():
    def __init__(self, ismi: str, familasi: str, qaysi_kursdaligi: str):
        self.ismi = ismi
        self.familasi = familasi
        self.qaysi_kursdaligi = qaysi_kursdaligi

    def insert(self, teble):
        query = f"""INSERT INTO {teble}(ismi,familasi,qaysi_kursdaligi) VALUES ('{self.ismi}','{self.familasi}','{self.qaysi_kursdaligi}');"""
        return DataBase.datbase(query, 'insert')
class kirish(betta):
    def __init__(self,onlayin_kurslar:str,talimturi:str,oquvchilar_natijasi:str, kamment:str,izox:str,users_id:int,oquvchi_id:int,oqituvchi_id:int,bitirgan_id:int,tolov_id:int):
        self.onlayin_kurslar = onlayin_kurslar
        self.talimturi = talimturi
        self.oquvchilar_natijasi = oquvchilar_natijasi
        self.kamment = kamment
        self.izox = izox
        self.users_id = users_id
        self.oquvchi_id = oquvchi_id
        self.oqituvchi_id = oqituvchi_id
        self.bitirgan_id = bitirgan_id
        self.tolov_id = tolov_id
    def insert(self,tebel):
        query = f"""INSERT INTO {tebel}(onlayin_kurslar,talimturi,oquvchilar_natijasi,kamment,izox,users_id,oquvchi_id,oqituvchi_id,bitirgan_id,tolov_id)
        VALUES ('{self.onlayin_kurslar}','{self.talimturi}','{self.oquvchilar_natijasi}','{self.kamment}','{self.izox}',{self.users_id},{self.oquvchi_id},{self.oqituvchi_id},{self.bitirgan_id},{self.tolov_id});
        """
        return DataBase.datbase(query,'insert')
